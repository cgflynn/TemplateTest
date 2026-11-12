# AGENTS.md: Rules for AI agents in this repository

These rules apply to Codex, Claude Code, and any other AI coding agent. If a request conflicts with them, stop and explain the conflict to the user.

## First action in every session
1. If `docs/PROJECT-SCOPE.md` contains `NOT YET SCOPED`, run the `start-here` skill before anything else.
2. Otherwise, read `docs/PROJECT-SCOPE.md` and the latest file in `docs/ai-log/` so you understand the project and where work left off.
3. Start or continue today's session log using the `session-log` skill.

## Hard rules
1. Never commit or push to `main`. Work on branches named `feat/*`, `fix/*`, `docs/*`, or `chore/*`.
2. Never merge, approve, or review pull requests. Approval is a human responsibility.
3. Never edit `.github/`, `AGENTS.md`, `CLAUDE.md`, `.agents/`, or `.claude/` unless the user explicitly asks; call it out in the session log if you do.
4. Never write secrets (keys, passwords, tokens, connection strings) into any file. Use environment variables and document names only in `.env.example`.
5. Use only data in `sample_data/` that is listed as approved in `docs/PROJECT-SCOPE.md`. Never use client, project, controlled, or personal data.
6. Never modify or overwrite input data. Write outputs to a separate folder.
7. Never delete or rewrite entries in `docs/ai-log/`. Append only.
8. Never disable, skip, or weaken tests or checks to make something pass.
9. Ask before adding any new package or dependency, and record why in `docs/DECISIONS.md`.

## Skills: when to use them
| Situation | Skill |
|---|---|
| New project, or user says "start here" | `start-here` |
| Start and end of every session; any significant action | `session-log` |
| Before writing or changing code | `plan-before-code` |
| Choosing script vs. desktop app vs. web page vs. GIS tool | `solution-shape` |
| Writing or changing code | `test-first` |
| Before every commit | `commit-discipline` |
| User asks "is this ready?" or wants a pull request | `ready-for-review` |
| User asks what something does, or seems unsure | `explain-to-me` |

## Working style
- Assume the user has no software development background. Explain in plain language, one step at a time.
- Prefer the simplest approach that meets the stated purpose.
- Make small changes. One logical change per commit.
- When requirements are unclear, ask rather than guess.

## Accountability
- Every commit made with AI help includes the trailer `AI-Assisted: <tool>`.
- The human user is the author of record and must review every change before it is committed.
- Merging to `main` requires a different person's pull request approval with the responsibility statement.
