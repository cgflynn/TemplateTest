---
name: dependency-check
description: Use before requesting approval, when a package is added or changed, or when the user says "check the dependencies". Confirms each third-party package is needed, maintained, free of known vulnerabilities, and suitably licensed, and saves a report in docs/reviews/.
---
# Dependency check

Purpose: every add-on package is code written by someone outside Dewberry. Confirm each one is necessary and trustworthy.

## Steps
1. **List dependencies** from `requirements.txt`, `pyproject.toml`, `package.json`, or equivalent. Include versions. If versions are not pinned, flag it.
2. **For each package, record:**
   - Purpose in this project (one line). If the Python or JavaScript standard library can do the job, flag it as removable.
   - Whether it is well known and actively maintained (recent releases, more than one maintainer where visible). Flag packages that look abandoned or have very few users.
   - Exact name check: confirm the name is spelled correctly and matches the official project (watch for look-alike names).
   - License. Flag anything that is not a common permissive license (MIT, BSD, Apache-2.0) for human review, especially copyleft (GPL, AGPL) or "no license".
3. **Scan for known vulnerabilities:**
   - Python: `pip install pip-audit` then `pip-audit -r requirements.txt`
   - JavaScript: `npm audit`
   Paste the summary. If a tool cannot run (no internet on the VM, for example), mark **Not checked** and say why.
4. **Check install-time behavior:** note any package that runs scripts on install or downloads extra files.
5. **Confirm decisions**: every package should appear in `docs/DECISIONS.md` with the reason it was added.

## Report
Save as `docs/reviews/YYYY-MM-DD_<branch-name>_dependencies.md`:
```
# Dependency check: <branch>
Date / tool / commit:
Overall: OK | Concerns | Not ready

| Package | Version | Purpose | Maintained? | License | Known vulnerabilities | Notes |
|---|---|---|---|---|---|---|

## Scan output summary
## Packages recommended for removal
## Items needing human decision (licenses, unmaintained packages)
```
Overall is **Not ready** if any package has an unresolved high or critical known vulnerability. Log the check and commit the report on the branch.
