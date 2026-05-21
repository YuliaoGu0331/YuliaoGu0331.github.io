# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Jekyll-based academic homepage built with the AcadHomepage template. It is deployed via GitHub Pages and includes an automated Google Scholar citation crawler.

## Common Commands

- **Start local development server** (with live reload):
  - Unix: `bash run_server.sh`
  - Windows: `run_server.bat`
  - Direct: `bundle exec jekyll serve --livereload`
- **Install dependencies**: `bundle install`
- **Build site**: `bundle exec jekyll build`

## Architecture

### Jekyll Structure

- **`_config.yml`**: Site configuration. Key fields include `title`, `description`, `repository`, `author`, and `google_scholar_stats_use_cdn`.
- **`_pages/`**: Site content pages (`about.md` is the homepage via `permalink: /`). Other pages include `research.md`, `publications.md`, `awards.md`, `experience.md`, `comments.md`.
- **`_layouts/default.html`**: Base layout wrapping all pages. Includes `head.html`, `masthead.html`, `sidebar.html`, and `scripts.html`.
- **`_includes/`**: Reusable templates. Notable includes:
  - `fetch_google_scholar_stats.html`: Client-side JS that fetches `gs_data.json` from the `google-scholar-stats` branch and injects citation counts.
  - `author-profile.html`: Renders the left sidebar author info card.
- **`_data/navigation.yml`**: Top navigation menu definition.
- **`assets/`**: CSS (`main.scss`, `academicons.css`), JS (`main.min.js`, `collapse.js`), and fonts.
- **`images/`**: Site images, favicons, and avatar.

### Google Scholar Citation Automation

- **Crawler**: `google_scholar_crawler/main.py` uses the `scholarly` Python library to fetch author data and publication citations.
- **Workflow**: `.github/workflows/google_scholar_crawler.yaml` runs the crawler on every `page_build` event, daily at 08:00 UTC, and on manual dispatch.
- **Output**: The workflow pushes `gs_data.json` and `gs_data_shieldsio.json` to the `google-scholar-stats` orphan branch.
- **Configuration**: The crawler requires a `GOOGLE_SCHOLAR_ID` repository secret. Set `google_scholar_stats_use_cdn: true` in `_config.yml` to fetch stats via jsDelivr CDN (helps with access from mainland China, but introduces cache delay).

### GitHub Pages Deployment

- The site is built and deployed automatically by GitHub Pages from the default branch.
- The `github-pages` gem pins Jekyll and plugins to GitHub Pages-compatible versions.
