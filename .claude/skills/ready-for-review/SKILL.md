---
name: ready-for-review
description: Use when the user asks "is this ready?", wants to open a pull request, or wants to request approval. Runs checks, summarizes the work in plain language, and prepares the pull request for a human approver.
---
# Ready for review

1. Confirm all work is on a branch and tests pass.
2. Confirm `docs/PROJECT-SCOPE.md` and today's session log are up to date.
3. Review the full change (`git diff main...HEAD`) and prepare, in plain language:
   - What changed and why
   - Which "done looks like" checks are now met, and how we know
   - What was not tested and any known limitations
   - New packages, if any
   - Links to the relevant `docs/ai-log/` files
4. If available, run the tool's built-in review (`/review` in Codex; `/code-review` or `/security-review` in Claude Code) and summarize findings. AI review supports human review; it never replaces it.
5. Fill in `.github/pull_request_template.md` with the above.
6. Tell the user:
   > "A different person must review and approve this pull request. Their approval must include: *I have reviewed this change, I understand what it does, and I accept responsibility for approving it.* Neither you nor I can approve it."
7. Never approve or merge the pull request.
