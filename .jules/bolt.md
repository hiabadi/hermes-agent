## 2024-05-18 - Avoid mutating lockfiles during routines
**Learning:** Running `uv sync` or `pnpm i` can unexpectedly update lockfiles (`uv.lock`, `web/pnpm-lock.yaml`). Committing these alongside minor performance fixes can severely pollute PRs and violate boundaries regarding not adding dependencies or making architectural changes.
**Action:** Always verify `git status` carefully before committing, and use `git restore --staged <file>` to remove automatically generated lockfile updates from the staging area if no new dependencies were actually intended to be added.
