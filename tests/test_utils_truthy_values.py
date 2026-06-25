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


def test_env_bool_returns_true_for_truthy_values(monkeypatch):
    monkeypatch.setenv("TEST_BOOL", "true")
    assert env_bool("TEST_BOOL") is True
    monkeypatch.setenv("TEST_BOOL", "1")
    assert env_bool("TEST_BOOL") is True
    monkeypatch.setenv("TEST_BOOL", "yes")
    assert env_bool("TEST_BOOL") is True


def test_env_bool_returns_false_for_falsey_values(monkeypatch):
    monkeypatch.setenv("TEST_BOOL", "false")
    assert env_bool("TEST_BOOL") is False
    monkeypatch.setenv("TEST_BOOL", "0")
    assert env_bool("TEST_BOOL") is False
    monkeypatch.setenv("TEST_BOOL", "no")
    assert env_bool("TEST_BOOL") is False


def test_env_bool_returns_default_when_missing():
    assert env_bool("MISSING_BOOL", default=True) is True
    assert env_bool("MISSING_BOOL", default=False) is False
