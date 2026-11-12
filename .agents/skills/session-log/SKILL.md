---
name: session-log
description: Use at the start and end of every working session and after any significant action. Maintains an append-only audit trail of what the user asked, what the agent did, and what changed, in docs/ai-log/.
---
# Session log (audit trail)

## File
`docs/ai-log/YYYY-MM-DD_<github-username>.md` (one file per person per day). Get the username with `git config user.name` or ask once.
Create from `docs/ai-log/_TEMPLATE.md` if it does not exist. **Append only. Never edit or delete earlier entries.**

## At the start of a session
Add a session header: time, tool (Codex or Claude Code), branch, and the user's goal for the session in one sentence.

## For each meaningful request (not every chat message)
Append an entry:
```
### HH:MM  Request
**Asked:** <the user's request, summarized faithfully; quote short requests exactly>
**Did:** <what the agent actually did, in plain language>
**Files changed:** <list, or "none">
**Commands run:** <tests, installs, scripts; or "none">
**Result:** <worked / failed / partial, and how we know>
**Decisions or assumptions:** <anything the agent assumed or the user decided>
**Follow-ups:** <open items>
```
Rules:
- Record what actually happened, including failures and abandoned attempts.
- If the agent declined something or a rule in AGENTS.md applied, record it.
- Do not paste secrets, personal data, or large data excerpts into the log.

## At the end of a session
Add a short summary: what was accomplished, what is still open, and what the next session should start with. Commit the log with the session's work (`docs:` commit if nothing else changed).

## Note
In Claude Code, a hook also records each prompt automatically in `docs/ai-log/prompts/`. That raw record does not replace this summary; the summary explains what was done and why.
