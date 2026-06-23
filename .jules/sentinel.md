## 2025-02-23 — Fix Command Injection Sink in Gateway Shell.Exec
**Class:** CWE-78 (Command Injection)
**Finding:** The `/shell.exec` remote RPC endpoint in `tui_gateway/server.py` passed untrusted remote inputs directly to `subprocess.run(cmd, shell=True)`, allowing trivial shell metacharacter injection.
**Why it existed:** The gateway uses shell execution for several built-in administrative / diagnostic actions, relying on a lightweight `detect_dangerous_command` deny-list which is easily bypassed by command injection primitives (`&&`, `;`, `|`).
**Action:** fixed
**Lesson:** The `shell.exec` endpoint must execute single commands safely via `shlex.split()` and `shell=False`. If pipelines are required in the future, they should be implemented via explicit orchestration rather than implicitly trusting the shell.
