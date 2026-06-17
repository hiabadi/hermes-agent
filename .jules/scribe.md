## 2025-06-18 — Fish shell completion

**Surface:** CLI documentation (`website/docs/reference/cli-commands.md`, `website/docs/user-guide/profiles.md`)
**Insight:** The completion script generator (`hermes_cli/completion.py`) supports `fish` shell, but the documentation only mentioned `bash` and `zsh`.
**Constraint / convention:** The fish completion script relies on `hermes completion fish | source`, whereas bash and zsh examples redirect output to their respective `rc` files (e.g. `hermes completion bash >> ~/.bashrc`).
**Next time:** Always check the underlying implementation or CLI output (like `--help`) when updating command documentation to ensure all supported options are listed.
