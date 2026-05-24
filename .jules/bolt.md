## 2024-05-24 - SQLite Variable Limits
**Learning:** SQLite has a hard limit on the number of variable placeholders (typically 999), meaning large batch queries using `IN (...)` can fail if not chunked. There was a latent bug in the unchunked batch UPDATE during prune_sessions.
**Action:** When creating batch operations (especially IN clauses) for potentially unbounded lists, ALWAYS chunk the list into smaller batches (e.g. 500) to safely operate within SQLite's parameters limits.
