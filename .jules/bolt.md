## 2024-06-25 - SQLite IN Clause Parameter Limits
**Learning:** SQLite has a parameter limit (MAX_VARIABLE_NUMBER) which defaults to 999. In `hermes_state.py`, applying a loop logic was correctly replaced with an `IN (...)` clause for `prune_sessions`, but chunking (size 500) was required to avoid crashing the queries when pruning thousands of sessions.
**Action:** When constructing SQLite queries with `IN (...)` for potentially large lists of IDs, always chunk the parameters.
