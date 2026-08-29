---
permalink: /experience/ai-tools
title: "AI Tools"
date: 2026-05-21
last_modified_at: 2026-08-29
author_profile: true
---

# AI Tools: A short introduction

{% include published-date.html date=page.date updated=page.last_modified_at %}

My daily research workflow runs on more than one AI agent: two terminal coding agents do the heavy lifting, while a self-improving personal assistant, a lightweight harness, and a handful of editor-side helpers rotate around them. This page organizes the setup agent by agent — what each one is good at, and, for the two workhorses, the skills and MCP servers they are equipped with.

<hr />

## Claude Code

### Overview

**Claude Code** is my primary terminal coding agent. Its strength is the harness around the model: a rich set of built-in tools covering the full software development lifecycle, three extension layers (MCP servers for context, plugins and skills for expertise, and hooks for guardrails), and fine-grained session customization such as a custom status line. A `PreToolUse` hook audits every shell command before it runs.

### Built-in Tools

Claude Code ships with a rich set of built-in tools that cover the full software development lifecycle. These include:

1. **File System Tools**: `Read`, `Write`, and `Edit` for manipulating source code and configuration files directly.
2. **Search Tools**: `Grep` and `Glob` for finding symbols, keywords, and file patterns across large codebases.
3. **Shell Execution**: `Bash` for running commands, installing dependencies, or executing build scripts.
4. **Web Access**: `WebSearch` and `WebFetch` for retrieving documentation, checking current events, or verifying API references.
5. **Agent Delegation**: `Agent` for spawning sub-agents to handle complex multi-step research or implementation tasks in parallel.
6. **Planning**: `EnterPlanMode` and `ExitPlanMode` for designing implementation strategies before writing code.
7. **Task Management**: `TodoWrite` for tracking progress on multi-step tasks.
8. **Scheduling**: `CronCreate`, `CronDelete`, and `ScheduleWakeup` for recurring or delayed automation.
9. **Notebook Support**: `NotebookEdit` for working with Jupyter notebooks.
10. **Git Workflow**: `EnterWorktree` and `ExitWorktree` for isolated branch experiments.

### MCP Servers

**MCP (Model Context Protocol)** servers act as bridges between an agent and external data sources or tools. They allow the AI to securely access local files, query databases, browse the web, and interact with development environments in real time, standardizing how context is exchanged without complex integration code. The following servers are configured:

1. **filesystem**: granular file access to approved folders (`Documents`, `Projects`, `Desktop`, `Downloads`), so the agent can read and write outside the current project directory.
2. **github**: repository operations through the GitHub API — issues, pull requests, and code search without leaving the terminal.
3. **context7**: injects up-to-date library documentation and API references into context, reducing hallucinated API calls.
4. **officecli**: exposes the officecli document suite over MCP, letting the agent create, proofread, and edit Word, PowerPoint, and Excel files programmatically.
5. **playwright**: browser automation using Playwright. It enables interaction with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models.
6. **matlab**: a project-scoped server connecting the agent to a live MATLAB session in a designated working folder — used for numerical experiments and plotting.

### Skills

**Skills** provide domain-specific expertise and pre-packaged workflows. They have some functions like MCP servers but provide lots of pre-prompts at the same time. Key skills in my Claude Code include:

**User-level skills**:

1. **Document suite (`docx`, `pdf`, `pptx`, `xlsx`)**: create and edit Word documents, PDFs, slide decks, and spreadsheets — the standard formats an academic workflow accumulates.
2. **Office automation (`officecli`)**: drive the officecli CLI, with its `officecli-docx`, `officecli-pptx`, and `officecli-xlsx` companions, for scripted proofreading, formatting, and batch modification of Office files.
3. **Browser control (`ego-browser`)**: operate an agent-friendly Chromium browser that reuses my login state in an isolated space instead of competing for the browser.

**Plugin skills**:

4. **Video production (`watch`)**: the claude-video plugin creates HTML-based video compositions — animations, captions, voiceovers, audio-reactive visuals, and scene transitions — with TTS and transcription for asset preprocessing.
5. **Engineering workflows (`mattpocock-skills`)**: a curated library of engineering practices covering code review, test-driven development, bug diagnosis, spec writing, and writing documentation for agents.
6. **Terse mode (`caveman`)**: a communication style that strips filler while preserving technical substance and exact code.
7. **Diagram design (`diagram-design`)**: turns ideas into clean architecture and flow diagrams.

**Built-in harness skills**:

8. **Verification (`verify`)**: run the application and manually observe behavior to confirm fixes or features work in production.
9. **Refinement (`simplify`)**: review changed code for reuse, quality, and efficiency issues.
10. **Configuration (`update-config`)**: modify harness settings, permissions, environment variables, and hooks.
11. **Automation (`loop`)**: set up recurring tasks or polling intervals.
12. **App launching (`run`)**: start the project application to see changes working live.
13. **Code review (`review`, `security-review`)**: review pull requests and perform security audits on pending changes.
14. **Claude API development (`claude-api`)**: build, debug, and optimize applications using the Anthropic SDK, including prompt caching and model migration.
15. **Project scaffolding (`init`)**: initialize project documentation such as `CLAUDE.md` files.

### A Typical Workflow

A common workflow involves reading existing code, planning changes, delegating implementation, and verifying results. For example, when adding a new feature:

1. Use `Grep` and `Read` to locate relevant files and understand current logic.
2. Enter `Plan` mode to design the implementation strategy and identify critical files.
3. Use `Edit` or `Write` to apply the changes, or spawn an `Agent` to handle refactoring across multiple files.
4. Run `Bash` commands to execute tests or build the project.
5. Invoke the `verify` skill to launch the app and visually confirm the feature works.
6. Use `TodoWrite` to mark tasks complete as you progress.

Below is a conceptual snippet showing how a developer might invoke a skill within Claude Code:

<div class="custom-code-box">
# ----------------- CONCEPTUAL CLAUDE CODE WORKFLOW -----------------
# 1. Search for all occurrences of a legacy API endpoint
Grep pattern="/api/v1/old-endpoint" glob="**/*.ts"

# 2. Plan the migration strategy before editing
EnterPlanMode
# ...design plan...
ExitPlanMode

# 3. Delegate multi-file refactoring to a sub-agent
Agent subagent_type="general-purpose" prompt="Migrate all v1 endpoints to v2"

# 4. Run the test suite to catch regressions
Bash command="npm test"

# 5. Verify the running application looks correct
Skill skill="verify"
</div>

<hr />

## Codex

### Overview

**Codex** is OpenAI's coding agent, and the second workhorse in my setup. It runs as a desktop app with a CLI companion, and its distinguishing strength is tight application integration: it can drive its own in-app browser, control Chrome, and operate macOS desktop applications directly, backed by a marketplace of plugins tuned for academic work.

### MCP Servers

1. **matlab**: the same MATLAB bridge used by Claude Code, connecting the agent to a live MATLAB session for numerical experiments and plotting.
2. **node_repl**: a bundled Node.js REPL that pairs with the browser, chrome, and computer-use plugins to script browser and desktop control flows.

### Plugins

Marketplace plugins extend Codex with ready-made capabilities:

1. **Academic**: `latex` for typesetting and compiling LaTeX documents, and `zotero` for searching and managing my reference library.
2. **Office documents**: `documents`, `pdf`, `spreadsheets`, and `presentations` read, generate, and edit the standard file formats, while `template-creator` turns recurring formats into reusable templates.
3. **Automation**: `browser` and `chrome` drive web pages, `computer-use` controls desktop applications, `build-macos-apps` packages native macOS apps, `github` handles repositories and pull requests, and `codex-app-tools` wires up ChatGPT-app integrations.
4. **Media**: `visualize` renders charts and interactive visualizations, and `sites` scaffolds and publishes small websites.

### Skills

Local skills cover knowledge management and content work:

1. **Obsidian suite (`obsidian-markdown`, `obsidian-cli`, `obsidian-bases`)**: author Obsidian-flavored markdown, control the vault from the command line, and build Bases database views.
2. **Canvas (`json-canvas`)**: create and edit JSON Canvas files, the format behind Obsidian's visual boards.
3. **Web extraction (`defuddle`)**: pull the main content out of cluttered web pages for clean archiving into notes.
4. **Image styles (`gpt-image-2-style-library`)**: reusable style presets for consistent image generation.
5. **Terse mode (`caveman`)**: the same shared communication style used by Claude Code.

<hr />

## Other agents in rotation

The rest of the fleet stays intentionally light, without custom MCP servers or skill lists to maintain:

1. **Hermes**: an open-source, self-improving agent by Nous Research. It turns experience into skills, keeps agent-curated memory, and runs as a single gateway process reachable from Telegram, Discord, Slack, WhatsApp, Signal, QQ, WeChat, Tencent Yuanbao, and the terminal — with cron-scheduled automations and a kanban board for long-running work.
2. **dsh**: DeepSeek's official harness (`@deepseek-ai/dsh`), a profile launcher that stacks plugin bundles and user patch layers. It boots interactive, `headless` one-shot, and `web` UI modes on demand.
3. **Gemini CLI**: Google's terminal agent, kept near-stock with personal OAuth and no MCP servers — a sandbox for quick experiments with Gemini models.
4. **Cursor**: the editor-based agent, configured only with a shared communication rule so its tone matches the terminal agents.
5. **ZCode**: the runtime that builds and maintains this very site, extended with official plugins for browser automation, desktop control, and document handling.
6. **Grok CLI**: xAI's terminal agent in a light configuration, slotted in for quick model comparisons.

GitHub Copilot, OpenCode, and Windsurf sit alongside these in near-default form.

<hr />

## One shared skill library

Beyond agent-specific setups, most of the fleet draws on one version-controlled library of engineering skills — code review, test-driven development, bug diagnosis, domain modeling, writing for agents — kept in a shared folder that any agent can load. The `ego-browser` skill, for instance, is installed simultaneously for Claude Code, Hermes, and Grok; an improvement to a single workflow benefits every agent that shares it.

By combining MCP-powered context access with built-in tools and specialized skills, this fleet of agents enables end-to-end AI-assisted research and software engineering — from literature and notes to code and deployment.
