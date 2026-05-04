## 2024-05-04 - SQLite Indexing
**Learning:** Adding indexes specifically matching querying queries with `IS NULL` on an indexed field combined with another field drastically reduces SQLite's need for temporary B-Trees when sorting, resulting in query times that are orders of magnitude faster when the DB grows.
**Action:** Be sure to always check the output of `EXPLAIN QUERY PLAN` in SQLite queries on hot paths to confirm `USE TEMP B-TREE FOR ORDER BY` is not unexpectedly being used.
