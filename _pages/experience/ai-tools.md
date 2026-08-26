---
permalink: /experience/ai-tools
title: "AI Tools"
date: 2026-05-21
author_profile: true
---

# AI Tools: A short introduction

{% include published-date.html date=page.date %}

## MCP Servers

**MCP (Model Context Protocol)** servers act as bridges between Claude Code and external data sources or tools. They allow the AI to securely access local files, query databases, browse the web, and interact with development environments in real time. MCP servers standardize how context is exchanged, making it easier to connect Claude Code to custom internal tools or third-party APIs without writing complex integration code. The following are the servers included:

1. **Playwright**: a MCP server that provides browser automation capabilities using Playwright. It enables interaction with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models.

<hr />

## Tools

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

<hr />

## Skills

**Skills** provide domain-specific expertise and pre-packaged workflows. They have some functions like MCP servers but provide lots of pre-prompts at the same time. Key skills in my claude code include:

1. **Video Production (`hyperframes`, `hyperframes-cli`, `hyperframes-media`, `hyperframes-registry`)**: Create HTML-based video compositions, animations, captions, voiceovers, audio-reactive visuals, and scene transitions. Also covers asset preprocessing like TTS and transcription.
2. **Claude API Development (`claude-api`)**: Build, debug, and optimize applications using the Anthropic SDK, including prompt caching and model migration.
3. **Project Scaffolding (`init`)**: Initialize project documentation such as `CLAUDE.md` files.
4. **Code Review (`review`, `security-review`)**: Review pull requests and perform security audits on pending changes.
5. **Verification (`verify`)**: Run the application and manually observe behavior to confirm fixes or features work in production.
6. **Refinement (`simplify`)**: Review changed code for reuse, quality, and efficiency issues.
7. **Configuration (`update-config`)**: Modify Claude Code harness settings, permissions, environment variables, and hooks.
8. **Automation (`loop`)**: Set up recurring tasks or polling intervals.
9. **App Launching (`run`)**: Start the project application to see changes working live.

<hr />

## Tools workflow

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

By combining MCP-powered context access with built-in tools and specialized skills, Claude Code enables end-to-end AI-assisted software engineering from research to deployment.
