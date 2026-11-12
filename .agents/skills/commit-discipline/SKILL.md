---
name: commit-discipline
description: Use before every commit. Checks branch, staged files, and secrets, writes a clear message with the AI-Assisted trailer, and updates the session log.
---
# Commit discipline

1. `git branch --show-current`. If it is `main`, STOP, create a branch, and move the changes.
2. `git status` and `git diff --staged`: confirm only intended files. Never stage outputs, `.env`, large data, or binaries.
3. Check the staged changes for anything that looks like a password, key, token, or internal server path. Remove it.
4. Run the tests if any exist.
5. Update today's session log.
6. Message format:
```
<type>: <short summary>

<what changed and why, 1-3 lines>
AI-Assisted: Codex | Claude Code
```
   Types: feat, fix, docs, test, refactor, chore.
7. Show the message to the user. The user confirms the commit; they are the author of record.
8. Push the branch only: `git push -u origin <branch>`. Never push to `main`.
