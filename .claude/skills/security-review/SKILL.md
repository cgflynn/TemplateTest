---
name: security-review
description: Use before requesting approval, when the user says "run a security review", or when ready-for-review finds no current security report. Reviews the branch for security weaknesses relevant to internal engineering tools, verifies each finding, and saves a report in docs/reviews/.
---
# Security review

Purpose: find realistic ways the tool could leak data, damage files, run unintended commands, or be misused, and confirm each finding is real before reporting it.

## Approach
1. **Understand first.** Read `docs/PROJECT-SCOPE.md` and the code. Write down, in 3-5 lines:
   - What goes in (files, user-typed values, network data) and where it comes from.
   - What comes out and where it is written.
   - What the tool can touch (folders, network, other programs, credentials).
   Anything coming from a user, a file, or the network is **untrusted input**.
2. **Check each category below** against the changed code (`git diff main...HEAD`) and the code it calls.
3. **Verify before reporting.** For each suspected issue, trace a concrete path from an untrusted input to a harmful action (source to sink). If you cannot show the path, mark it **Unconfirmed** rather than reporting it as a vulnerability. Do not pad the report with generic advice.
4. If available, also run the tool's built-in security review (`/security-review` in Claude Code; `/review` in Codex, asking it to focus on security) and include its findings after verifying them the same way.

## Categories

### A. Secrets and credentials
- Passwords, API keys, tokens, connection strings, or private keys anywhere in code, configs, notebooks, tests, logs, or git history (`git log -p` on the branch).
- Secrets printed to the screen or written to logs or output files.

### B. Files and paths
- User-supplied paths used without checking they stay inside the intended folder (e.g., `..\..\` path traversal).
- Writing to, deleting, or overwriting files outside the output folder.
- Following links or shortcuts to unexpected locations.
- Opening archives (zip) without checking where contents will be extracted.
- File type decided only by extension rather than by actually reading and validating the content.

### C. Running commands and code
- Building shell or system commands from user input (`os.system`, `subprocess` with `shell=True`, PowerShell strings).
- `eval`, `exec`, or dynamic imports driven by input.
- Loading untrusted data with unsafe loaders (Python `pickle`, `yaml.load` without a safe loader, `marshal`).

### D. Input validation
- Numbers, dates, and options checked for type and allowed range before use.
- Lists of allowed values used instead of trying to block bad values.
- Size limits on files and inputs that could exhaust memory or disk.

### E. Web pages and apps (if applicable)
- User or file content inserted into HTML without escaping (cross-site scripting).
- Database queries built by joining strings instead of parameters (SQL injection).
- Any network listener, open port, or hosted page: who can reach it and whether it requires sign-in.
- Third-party scripts loaded from the internet at run time.

### F. Network and data leaving the tool
- Any outbound network call: where it goes, what is sent, and whether the scope allows it.
- Data sent to external AI services or APIs.
- Telemetry or analytics in included libraries.

### G. Insecure defaults and failure behavior
- Debug modes, verbose errors, or test settings left on.
- Errors that are silently ignored (bare `except: pass`) and let the tool continue with bad data.
- Errors that "fail open" (skip a check and continue) instead of stopping safely.
- Error messages that reveal full internal paths, server names, or data contents.

### H. Agent and repository hygiene
- Changes on this branch to `.github/`, `AGENTS.md`, `.agents/`, `.claude/`, or CI workflows. These must be called out for the human approver.
- New scripts that run automatically (git hooks, install scripts, scheduled tasks).

## Severity
| Level | Meaning | Example |
|---|---|---|
| High | Confirmed path to data exposure, file damage outside the output folder, or running unintended commands | Output folder from user input allows writing to `C:\Windows` |
| Medium | Confirmed weakness that needs an unusual input or setup to cause harm | Large file crashes the tool and leaves partial output |
| Low | Hardening or hygiene improvement with no confirmed harmful path | Error message shows the full local path |

## Report
Save as `docs/reviews/YYYY-MM-DD_<branch-name>_security.md`:
```
# Security review: <branch>
Date / reviewer tool / commit: <date> / <tool> / <short SHA>
Overall: No confirmed issues | Issues to fix | Not ready

## What the tool touches (inputs, outputs, network, files)
## Findings
| # | Category | Severity | Location (file:line) | Confirmed path (source to sink) | Suggested fix |
|---|---|---|---|---|---|
## Unconfirmed items (could not demonstrate a path)
## Categories checked with no issues
## Changes to governance files (section H)
```
Then summarize for the user in plain language, log it in the session log, and commit the report on the branch.

Overall is **Not ready** if any High finding is open. AI security review is a support to, not a substitute for, IT and Cyber Security review at release.
