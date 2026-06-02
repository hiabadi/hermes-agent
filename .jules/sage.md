## 2025-06-02 — Stabilize test_counters_initialized_in_init
**Surface:** tests/run_agent/test_run_agent.py
**Insight:** test_counters_initialized_in_init was failing because it didn't mock out the LLM provider resolution, and when testing in a pristine environment without OPENROUTER_API_KEY, it failed fast with a RuntimeError.
**Pattern / anti-pattern:** Tests that instantiate AIAgent without properly mocking `agent.auxiliary_client.resolve_provider_client` are flaky depending on environment variables.
**Next time:** Mock `resolve_provider_client` when instantiating `AIAgent` in unit tests.
