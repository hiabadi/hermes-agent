## 2024-06-18 — Native Windows Support Docs
**Surface:** README, FAQ, Installation Guide, Contributing Docs
**Insight:** The memory states: "The Hermes Agent officially supports Linux, macOS, and WSL2. Native Windows is not officially supported; do not claim native Windows support in documentation, although the codebase includes defensive coding patterns (like installers and conditionals) for edge cases."
**Constraint / convention:** We must remove claims of native Windows being "fully supported" or "officially supported", and instead steer users towards WSL2 or acknowledge the scripts are there for edge cases but native windows is unsupported.
**Next time:** Remove all claims of native windows support in documentation.
