## 2025-06-08 — Fix CWE-78 (Command Injection) in local STT command execution
**Class:** CWE-78 Command Injection
**Finding:** `_transcribe_local_command` evaluated user-provided templates and file paths using `subprocess.run(..., shell=True)` after naive string interpolation.
**Why it existed:** The `command_template` parameter is a configurable string via `LOCAL_STT_COMMAND_ENV` that required interpolation of dynamic runtime paths (e.g. `{input_path}`). The developer used string formatting + `shlex.quote` + `shell=True` to run the configurable command.
**Action:** fixed
**Lesson:** Fixed by pre-tokenizing the command template via `shlex.split(command_template)` *before* variable interpolation to create a list. Removed `shlex.quote` from the interpolated variables to allow `subprocess.run(..., shell=False)` to interpret paths safely without extra quoting characters. Always pass dynamic command templates as lists when using `subprocess`.
