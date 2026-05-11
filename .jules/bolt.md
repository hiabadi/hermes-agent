## 2024-05-18 - Logs parsing string comparison performance
**Learning:** Calling `line.toUpperCase()` and then performing multiple `includes()` checks creates new string allocations for every log line, which is slow for large log files (like 10000+ lines).
**Action:** Use pre-compiled case-insensitive regular expressions (e.g. `const ERROR_RE = /ERROR|CRITICAL/i`) and `RE.test(line)`. It avoids intermediate string allocations and is over 2x faster for bulk log parsing.
