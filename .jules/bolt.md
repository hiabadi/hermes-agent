## 2024-05-18 - Missing SQLite Composite Index on Sessions Table
**Learning:** The `list_sessions_rich` query frequently filtered by `parent_session_id IS NULL` and ordered by `started_at DESC`. Without a composite index covering both `parent_session_id` and `started_at DESC`, SQLite resorted to slower query plans and temp B-Trees for sorting.
**Action:** Always look for composite indexes matching the `WHERE` clauses combined with `ORDER BY` clauses when analyzing slow SQLite queries with sub-queries and limits.
