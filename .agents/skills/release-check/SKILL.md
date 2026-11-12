---
name: release-check
description: Use before anything built in this repository is used on Dewberry machines, applied to real work files, shared beyond the builder, or delivered externally. Assembles the release record for the subject matter expert, IT, and Cyber Security.
---
# Release check (end gate)

Purpose: collect the evidence that people outside the project need to decide whether this tool can be used for real work. The agent assembles; people decide.

## Preconditions
- Work is merged to `main` through an approved pull request.
- Current quality, security, and dependency reports exist for the commit being released. If not, run them first.

## Checklist
| # | Item | Owner | Evidence |
|---|---|---|---|
| 1 | Scope still accurate; intended users and internal/external use confirmed | Builder | `docs/PROJECT-SCOPE.md` |
| 2 | Quality review: no Fails; Concerns accepted in writing | Builder + approver | Report link |
| 3 | Security review: no open High or Medium findings | IT reviewer | Report link |
| 4 | Dependency check: no unresolved high/critical vulnerabilities; licenses acceptable | IT reviewer | Report link |
| 5 | Validation on reference data by the subject matter expert, with results and tolerance recorded | SME | Signed entry below |
| 6 | Full automated scans run on `main` (e.g., CodeQL, secret scanning, dependency audit) | IT reviewer | Scan links |
| 7 | List of components (packages and versions) included | Agent | Section below |
| 8 | Version number and change notes | Builder | Section below |
| 9 | Run instructions and known limitations documented | Builder | README |
| 10 | Rollback plan: how users go back to the previous method | Builder | Section below |
| 11 | Desktop app (exe)? IT code signing and deployment arranged | IT | Ticket |
| 12 | External, client, or wide internal use? Third-party or Cyber Security review completed | Cyber Security | Record |
| 13 | Data: confirmed approved for the real data the tool will process, including client contract terms on AI-developed tools if applicable | Project manager | Record |

## Steps
1. Fill in the checklist with evidence links. Mark anything missing as **Open**. Never mark an item complete without evidence.
2. Generate the component list from the dependency files with exact versions.
3. Draft change notes from the merged pull requests since the last release.
4. Save as `docs/reviews/YYYY-MM-DD_release_v<version>.md` using the format below.
5. Tell the user which items are Open and who owns each.
6. Do not create release tags, builds for distribution, or installers unless the user confirms all items are complete; tag creation may be restricted to IT or Cyber Security.

## Release record format
```
# Release record: <project> v<version>
Commit: <SHA>    Date:
Recommendation from evidence: Ready | Not ready (open items listed)

## Checklist
<table above, completed>

## Components
## Change notes
## Known limitations
## Rollback plan

## Sign-off (completed by people, not the agent)
| Role | Name | Decision | Date |
|---|---|---|---|
| Subject matter expert | | | |
| IT reviewer | | | |
| Cyber Security (if required) | | | |
```
