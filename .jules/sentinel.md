## 2026-05-25 - SQLite Parameter Limit DoS
**Vulnerability:** Denial of Service risk due to unchunked IN (...) clauses in SQLite queries with potentially thousands of parameters.
**Learning:** SQLite has a hardcoded limit on the number of parameters per query (default 999). Exceeding this via user input or bulk operations throws an OperationalError and can crash the application.
**Prevention:** Always chunk list-based inputs for SQL IN clauses using a batch size (e.g. 500) within the allowed limit.
