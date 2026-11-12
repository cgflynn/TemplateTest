---
name: solution-shape
description: Use when deciding what form the solution should take (script, GIS tool, desktop app, web page, notebook). Recommends the simplest fit and records the decision.
---
# Solution shape

Prefer the first option that fits:
| If... | Recommend | Notes |
|---|---|---|
| One person or small team runs it on files | **Script** (usually Python) | Easiest to test and review |
| Users work inside ArcGIS Pro, QGIS, Civil 3D, etc. | **Plug-in or toolbox script** for that software | Fits existing workflow |
| Users cannot install anything and need a button | **Desktop app (exe)**, later | Build the script first; IT must sign and deploy |
| Many users in a browser; small data | **Web page or web app** | Needs hosting and a security review |
| Exploring an idea | **Notebook** | Not for production use |

Large local files (LiDAR, rasters, models) are usually a poor fit for browser-only HTML pages.

Steps:
1. Recommend one option with a one-sentence reason, and name the language.
2. List the minimum packages needed and why.
3. Record in `docs/DECISIONS.md`: chosen form, language, packages, alternatives considered.
