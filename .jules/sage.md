## 2025-01-16 — `env_bool` ignored default when empty
**Surface:** `utils.env_bool`
**Insight:** `os.getenv(key, "")` passed an empty string instead of `None` to `is_truthy_value`, which evaluated `""` as explicitly falsy and returned `False`, completely ignoring the requested `default=True`.
**Pattern / anti-pattern:** Bypassing default values by coercing missing values to empty strings before checking defaults.
**Next time:** Watch out for `os.getenv(key, "")` when the downstream parser relies on `None` to trigger default logic.
