## 2023-10-27 - SessionDB N+1 Queries
**Learning:** SQLite query loops (N+1) are significantly slow in Python when retrieving large numbers of records. The N+1 pattern of fetching records then fetching their associated relationships one-by-one is highly inefficient.
**Action:** Always prefer `JOIN` or `IN` statements for retrieving related entities over making iterative DB calls in a Python loop.
