## 2024-05-18 - Missing SQLite Compound Index for Session List
**Learning:** In the `list_sessions_rich` query in `hermes_state.py`, the lack of a compound index for filtering `parent_session_id IS NULL` and ordering by `started_at DESC` caused a significant performance bottleneck because SQLite resorted to a B-Tree sort or a full index scan.
**Action:** Always create compound indices spanning both the `WHERE` filters (like `parent_session_id` and `source`) and `ORDER BY` columns in frequently queried tables.
