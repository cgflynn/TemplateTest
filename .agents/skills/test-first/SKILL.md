---
name: test-first
description: Use whenever writing or changing code. Adds checks that prove the code works on approved sample data, and runs them.
---
# Test first

1. For each plan step, write an automated test that would fail before the change:
   - Python: `tests/test_*.py` with pytest.
   - JavaScript/HTML: `tests/*.test.js` (ask before adding a test framework).
   - Other: agree a repeatable check with the user and document it in `docs/DECISIONS.md`.
2. Use only files in `sample_data/`. Keep them small. Compare to known-good results with a stated tolerance where possible.
3. Write the minimum code to make the test pass. Run the tests and explain the result in plain language.
4. Add at least one test for bad input (missing file, wrong format) and confirm a clear error message, not a crash.
5. Confirm the code never writes into the input folder.
6. Never skip, delete, or loosen a failing test to make it pass. Report the failure and log it.
