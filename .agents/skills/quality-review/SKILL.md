---
name: quality-review
description: Use before requesting approval, when the user says "run a quality review", or when ready-for-review finds no current quality report. Works through a fixed quality checklist with evidence and saves a report in docs/reviews/.
---
# Quality review

Purpose: give the builder and the human approver an honest, evidence-based picture of whether the work does what the scope says, handles problems gracefully, and can be understood by the next person.

## Rules
- Every item gets a status: **Pass**, **Concern**, **Fail**, or **N/A**, plus **evidence** (test name, command output, file and line, or measured value).
- "Looks fine" is not evidence. If you cannot check an item, mark it **Not checked** and say why.
- Report what you find. Do not fix code during the review; list fixes as follow-ups and ask the user whether to address them.
- Review the changes on this branch (`git diff main...HEAD`) and anything they touch.

## Checklist

### 1. Correctness (against the scope)
- 1.1 Each "done looks like" check in `docs/PROJECT-SCOPE.md` has a test or recorded comparison that shows it is met.
- 1.2 Results on approved sample data match known-good results within the stated tolerance. Record the measured difference.
- 1.3 Units, coordinate systems, datums, and rounding are handled explicitly and documented where relevant.

### 2. Tests
- 2.1 All tests run and pass. Paste the summary line.
- 2.2 Tests check real results, not just "it ran without crashing".
- 2.3 No tests were skipped, deleted, or loosened on this branch.

### 3. Bad and unusual input
Run or test each that applies and record the behavior:
- 3.1 Missing or misspelled input file.
- 3.2 Empty file.
- 3.3 Wrong file type or corrupted file.
- 3.4 Unexpected values (negative, zero, missing, very large, non-numeric).
- 3.5 File names or paths with spaces or unusual characters.
- 3.6 Output folder already exists or already contains files.
Expected: a clear, plain-language error message and no partial or corrupted output left behind.

### 4. Data safety
- 4.1 Input files are never modified (confirm with a before/after file hash or timestamp on sample data).
- 4.2 Outputs go to a separate folder and do not silently overwrite earlier outputs.
- 4.3 Only approved sample data was used.

### 5. Performance
- 5.1 Time one run on the largest approved sample file. Record the time and file size.
- 5.2 Estimate behavior at realistic production size; flag if memory or time could become a problem.

### 6. Readability and maintainability
- 6.1 Names of files, functions, and variables describe what they do.
- 6.2 No dead code, commented-out blocks, or leftover experiments.
- 6.3 No copy-pasted duplicate logic that should be a single function.
- 6.4 Comments explain *why* where the logic is not obvious.
- 6.5 Settings that users may change (tolerances, paths, options) are in one place, not scattered as hard-coded values.
- 6.6 Linter runs clean (e.g., `ruff check .` for Python). Paste the result.

### 7. Usability and documentation
- 7.1 README "How to run" lets a new user run the tool from scratch. Follow it literally and record any step that fails.
- 7.2 Required inputs, outputs, and options are documented.
- 7.3 Known limitations are written down.

### 8. Traceability
- 8.1 Session logs in `docs/ai-log/` cover the work on this branch.
- 8.2 Significant choices are recorded in `docs/DECISIONS.md`.
- 8.3 Commits carry the `AI-Assisted:` trailer where AI was used.

## Report
Save as `docs/reviews/YYYY-MM-DD_<branch-name>_quality.md` (replace `/` in branch names with `-`):
```
# Quality review: <branch>
Date / reviewer tool / commit: <date> / <Codex|Claude Code> / <short SHA>
Overall: Ready | Ready with concerns | Not ready

| # | Item | Status | Evidence |
|---|---|---|---|

## Fails and concerns (with suggested fix)
## Not checked (and why)
```
Then:
1. Summarize the result for the user in 3-5 plain sentences.
2. Log the review in the session log.
3. Commit the report on the branch (`docs: add quality review`).

Overall is **Not ready** if any item is Fail. A human decides whether Concerns are acceptable.
