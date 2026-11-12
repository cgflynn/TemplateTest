---
name: plan-before-code
description: Use before writing or changing any code. Produces a short plan tied to the project scope and gets the user's agreement.
---
# Plan before code

1. Restate the request in one or two sentences.
2. Connect it to the purpose and "done looks like" checks in `docs/PROJECT-SCOPE.md`. If it does not fit, ask whether the scope should change.
3. Write a plan of 3-7 numbered steps. For each: files that will change and how we will check it works.
4. Note risks in plain language: wrong results, lost data, slow on large files, security.
5. Show the plan and wait for the user to say yes.
6. Make sure you are not on `main` (`git branch --show-current`). Create `feat/<short-name>` or `fix/<short-name>`.
7. Record the plan in the session log. Record significant choices in `docs/DECISIONS.md`.
