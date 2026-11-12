---
name: reviewer-assist
description: Use when preparing a pull request for approval, or when the person approving asks "brief me" or "what should I check?". Produces a short, plain-language briefing so the human approver can make an informed decision.
---
# Reviewer assist

Purpose: the approver signs a statement that they understand the change and accept responsibility. Give them what they need to do that honestly in about 15 minutes.

## Rules
- Be neutral. Do not argue for approval. Present concerns as prominently as successes.
- Do not restate the whole diff. Point the reviewer to the few places that matter most.
- Never approve on the reviewer's behalf.

## Briefing
Save as `docs/reviews/YYYY-MM-DD_<branch-name>_reviewer-brief.md` and link it in the pull request:
```
# Reviewer briefing: <branch>
Commit: <short SHA>

## In one paragraph
What this change does, for whom, and why, in plain language.

## Risk level: Low | Medium | High
Why (data handled, who will use it, what it can write or change).

## Review results
| Review | Overall | Open items |
|---|---|---|
| Quality | | |
| Security | | |
| Dependencies | | |

## Look at these first (max 5)
| File:lines | Why it matters |
|---|---|

## Questions to ask the builder (3-5)
Questions that test understanding, e.g. "What happens if the input file has no header?" or "How did you confirm the results against the manual method?"

## Things the AI could not verify
List anything that needs a person: technical correctness against engineering judgment, real-world data behavior, licensing decisions.

## Before you approve
- [ ] I read the briefing and the open items
- [ ] I looked at the files listed above
- [ ] The builder answered my questions satisfactorily
- [ ] I am comfortable with the open concerns, or they are fixed
```
Commit the briefing on the branch and log it in the session log.
