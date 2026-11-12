---
name: start-here
description: Use when the user says "start here", "start a new project", or when docs/PROJECT-SCOPE.md contains NOT YET SCOPED. Runs a short, friendly scoping interview and records a mini project scope.
---
# Start here: project scoping

Purpose: understand the project well enough to choose the right tools and checks, and keep a short record of what was intended.

## Tone
Be welcoming and practical. Open with:
> "To give you the best tools and set this project up well, I'd like to ask a few quick questions about what you're building and who it's for. It takes about five minutes, and your answers are saved in `docs/PROJECT-SCOPE.md` so we both have a reference."

Ask **one or two questions at a time**. Accept short or uncertain answers; "not sure yet" is fine. Offer examples when helpful.

## Questions
1. **Project**: In a sentence or two, what do you want to build?
2. **Purpose**: What problem does it solve? How is this done today, and roughly how long does it take?
3. **Users**: Who will use it: just you, your team, other Dewberry staff, or people outside Dewberry (clients, public)?
4. **Use**: Internal only, or could it ever be delivered to or used by a client?
5. **Inputs and outputs**: What goes in (file types, rough size) and what should come out?
6. **Data**: What data will you test with? Does any of it come from a client project, contain personal information, or carry contract restrictions?
   - If yes or unsure: tell the user to confirm with their project manager and Cyber Security before using it, and record "Pending approval".
7. **Done looks like**: How will you know it works? Help them state 1-3 checks (e.g., "results match the manual method within 0.05 m").
8. **Expert check**: Who can confirm the results are technically correct?
9. **Must never**: Anything the tool must never do (e.g., overwrite original files)?

## After the questions
1. Fill in `docs/PROJECT-SCOPE.md`. Replace `NOT YET SCOPED` with today's date. Use the user's words where possible.
2. Recommend a starting form using the `solution-shape` skill, briefly.
3. Read the scope back in 4-6 plain sentences and ask the user to confirm or correct it.
4. Flag any of these clearly:
   - External or client use → final review will need extra steps.
   - Client or restricted data → stop until approval is confirmed.
5. Log the interview with the `session-log` skill.
6. Create branch `docs/project-scope`, commit using `commit-discipline`, and suggest the user open a pull request so the scope is on record.

## Do not
- Write any code during this skill.
- Pressure the user for detail they don't have; mark it "To be determined".
