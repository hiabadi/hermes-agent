"""Tests for shared truthy-value helpers."""

from utils import env_bool, env_var_enabled, is_truthy_value


def test_is_truthy_value_accepts_common_truthy_strings():
    assert is_truthy_value("true") is True
    assert is_truthy_value(" YES ") is True
    assert is_truthy_value("on") is True
    assert is_truthy_value("1") is True


def test_is_truthy_value_respects_default_for_none():
    assert is_truthy_value(None, default=True) is True
    assert is_truthy_value(None, default=False) is False


def test_is_truthy_value_rejects_falsey_strings():
    assert is_truthy_value("false") is False
    assert is_truthy_value("0") is False
    assert is_truthy_value("off") is False


def test_env_var_enabled_uses_shared_truthy_rules(monkeypatch):
    monkeypatch.setenv("HERMES_TEST_BOOL", "YeS")
    assert env_var_enabled("HERMES_TEST_BOOL") is True

    monkeypatch.setenv("HERMES_TEST_BOOL", "no")
    assert env_var_enabled("HERMES_TEST_BOOL") is False


def test_env_bool_default_fallback(monkeypatch):
    monkeypatch.delenv("MISSING_VAR", raising=False)
    assert env_bool("MISSING_VAR", default=True) is True
    assert env_bool("MISSING_VAR", default=False) is False


def test_env_bool_with_explicit_value(monkeypatch):
    monkeypatch.setenv("PRESENT_VAR", "yes")
    assert env_bool("PRESENT_VAR", default=False) is True

    monkeypatch.setenv("PRESENT_VAR_2", "0")
    assert env_bool("PRESENT_VAR_2", default=True) is False
