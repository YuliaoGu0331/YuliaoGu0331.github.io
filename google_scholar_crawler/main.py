"""Google Scholar citation crawler.

Fetches author data from Google Scholar via the `scholarly` library and writes
JSON to results/. Designed to fail fast and loudly instead of hanging forever:
every network call is bounded by a socket timeout, and the whole fetch is
retried with exponential backoff up to MAX_ATTEMPTS times. On final failure the
script exits non-zero so the workflow fails visibly (and skips the push step)
rather than appearing to run forever.
"""

import json
import logging
import os
import socket
import sys
import time
from datetime import datetime

from scholarly import scholarly

socket.setdefaulttimeout(20)  # bound every socket op; prevents indefinite hangs

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("gs_crawler")

AUTHOR_ID = os.environ["GOOGLE_SCHOLAR_ID"]
MAX_ATTEMPTS = 5
BACKOFF_SECONDS = 15  # doubled after each failed attempt


def fetch_author(author_id):
    """Fetch + fill author data, retrying with backoff on failure."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            log.info("fetching author %s (attempt %d/%d)", author_id, attempt, MAX_ATTEMPTS)
            author = scholarly.search_author_id(author_id)
            scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
            log.info("fetched author %s", author.get("name"))
            return author
        except Exception as exc:  # noqa: BLE001 - any failure should be retried
            wait = BACKOFF_SECONDS * (2 ** (attempt - 1))
            log.warning("attempt %d failed: %s", attempt, exc)
            if attempt == MAX_ATTEMPTS:
                raise
            log.info("retrying in %ds", wait)
            time.sleep(wait)


def main():
    try:
        author = fetch_author(AUTHOR_ID)
    except Exception as exc:  # noqa: BLE001 - report and fail loudly
        log.error("crawler failed after %d attempts: %s", MAX_ATTEMPTS, exc)
        sys.exit(1)

    author["updated"] = str(datetime.now())
    author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}
    print(json.dumps(author, indent=2))

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open("results/gs_data_shieldsio.json", "w") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

    log.info("done: %s", author["name"])


if __name__ == "__main__":
    main()
