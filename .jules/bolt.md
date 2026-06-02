## 2025-06-03 — Optimize prune_sessions
**Where:** `hermes_state.py` (`SessionDB.prune_sessions`)
**Symptom:** N+1 queries when pruning a large number of sessions.
**Root cause:** The method iterated over `session_ids` and executed a `DELETE` for each message and session individually. Additionally, the `UPDATE` statement lacked batching, which could cause a `sqlite3.OperationalError: too many SQL variables` for large sets.
**Resolution:** Replaced the loop with chunked `IN` clauses (batches of 500) for both `UPDATE` and `DELETE` operations.
**Next time:** Watch out for similar loop-based `DELETE` or `UPDATE` operations that can be batched using chunked `IN` clauses in SQLite.
