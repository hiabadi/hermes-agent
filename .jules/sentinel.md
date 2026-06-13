## 2024-06-13 — Fixed local STT command injection
**Class:** CWE-78 (OS Command Injection)
**Finding:** Unsafe interpolation of file paths into `subprocess.run(..., shell=True)` for local transcription.
**Why it existed:** The code relied on `shlex.quote` inside a formatted string (`shell=True`), which can fail depending on template quoting logic.
**Action:** fixed
**Lesson:** Always use `shlex.split` on configuration templates *before* parameter injection, and execute as lists with `shell=False`. Ensure mocks in `tests/tools/test_transcription_tools.py` can distinguish binaries by checking `cmd[0]` when converted to list formatting.
