## 2026-06-11 — Unused f-strings
**Candidate:** unused f-strings
**Reality:** alive
**Why it deceived analysis:** Unused f-strings are not dead code to be deleted but rather strings without variable interpolation to be replaced with standard strings.
**Constraint for future runs:** None
