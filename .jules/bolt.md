## 2024-06-25 - SQLite N+1 Queries in Context Fetching
**Learning:** In SQLite/WAL mode with Python threads, repeated small sequential queries (N+1) within an un-batched loop cause significant lock contention and execution overhead. For instance, fetching surrounding messages one-by-one inside a loop can be optimized greatly.
**Action:** Always batch related lookups into a single `IN (...)` query and chunk it (e.g., max 900) to respect older SQLite host parameter limits.
