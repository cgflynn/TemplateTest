# START HERE

Welcome to an AI-assisted development project at Dewberry. Read this page first.

## 1. Open the project with your AI agent
1. On the pilot VM, clone this repository (GitHub Desktop: *File > Clone repository*).
2. Open the folder in **Codex** or **Claude Code**.
3. Type: **"Start here."**

The agent will ask you a few short questions about your project (what it is, why, who it is for). Your answers are saved in `docs/PROJECT-SCOPE.md` so that the right tools and checks can be chosen and so there is a record of what was intended.

## 2. How work is recorded
Every working session is logged in `docs/ai-log/`: what you asked the agent, what it did, and which files changed. The agent keeps this log for you; please do not delete it. This is the project's audit trail.

## 3. Ground rules (pilot)
1. Work only on the pilot VM and in this GitHub repository. Do not move code out by any other route.
2. Use synthetic or approved sample data only (`sample_data/`). No client, project, controlled, or personal data without approval.
3. Nothing you build runs on a Dewberry machine or touches real work files until it passes the final review.
4. Never put passwords, keys, or connection strings in the code.
5. Never overwrite source data. Write outputs to a new folder.
6. You must be able to explain what your code does. If you cannot, it is not ready.

## 4. Getting your work into `main`
- Work on a branch. Ask the agent: **"Is this ready for review?"**
- Open a pull request. A different person must review it and approve it with this statement:

  > I have reviewed this change, I understand what it does, and I accept responsibility for approving it.

- The pull request cannot merge without that approval.

## 5. Useful things to say to the agent
| Say | What happens |
|---|---|
| "Start here." | Project scoping interview |
| "Plan this change." | Written plan before any code |
| "Explain this to me." | Plain-language walkthrough of the code |
| "Log this session." | Writes or updates today's audit log entry |
| "Is this ready for review?" | Checks, summary, and pull request description |
