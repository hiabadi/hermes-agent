"""Tests for environment and JSON parsing utility functions."""

from utils import env_int, env_bool, safe_json_loads

# --- env_int tests ---


def test_env_int_valid_integer(monkeypatch):
    monkeypatch.setenv("TEST_INT", "42")
    assert env_int("TEST_INT") == 42


def test_env_int_whitespace_trimmed(monkeypatch):
    monkeypatch.setenv("TEST_INT", "  100  ")
    assert env_int("TEST_INT") == 100


def test_env_int_missing_uses_default():
    assert env_int("MISSING_VAR") == 0
    assert env_int("MISSING_VAR", default=99) == 99


def test_env_int_empty_string_uses_default(monkeypatch):
    monkeypatch.setenv("TEST_INT", "")
    assert env_int("TEST_INT") == 0
    assert env_int("TEST_INT", default=5) == 5


def test_env_int_whitespace_string_uses_default(monkeypatch):
    monkeypatch.setenv("TEST_INT", "   ")
    assert env_int("TEST_INT") == 0


def test_env_int_invalid_string_uses_default(monkeypatch):
    monkeypatch.setenv("TEST_INT", "abc")
    assert env_int("TEST_INT") == 0
    monkeypatch.setenv("TEST_INT", "1.5")
    assert env_int("TEST_INT") == 0


# --- env_bool tests ---


def test_env_bool_truthy_values(monkeypatch):
    for val in ("1", "true", "yes", "on"):
        monkeypatch.setenv("TEST_BOOL", val)
        assert env_bool("TEST_BOOL") is True

    # test case insensitivity
    monkeypatch.setenv("TEST_BOOL", "TRUE")
    assert env_bool("TEST_BOOL") is True
    monkeypatch.setenv("TEST_BOOL", "  On  ")
    assert env_bool("TEST_BOOL") is True


def test_env_bool_falsy_values(monkeypatch):
    for val in ("0", "false", "no", "off"):
        monkeypatch.setenv("TEST_BOOL", val)
        assert env_bool("TEST_BOOL") is False


def test_env_bool_missing_uses_default():
    assert env_bool("MISSING_VAR") is False
    assert env_bool("MISSING_VAR", default=True) is True


def test_env_bool_empty_string_uses_default(monkeypatch):
    monkeypatch.setenv("TEST_BOOL", "")
    assert env_bool("TEST_BOOL") is False
    assert env_bool("TEST_BOOL", default=True) is True


# --- safe_json_loads tests ---


def test_safe_json_loads_valid():
    assert safe_json_loads('{"a": 1}') == {"a": 1}
    assert safe_json_loads("[1, 2, 3]") == [1, 2, 3]
    assert safe_json_loads('"string"') == "string"
    assert safe_json_loads("123") == 123
    assert safe_json_loads("true") is True
    assert safe_json_loads("null") is None


def test_safe_json_loads_invalid_syntax():
    assert safe_json_loads("{invalid}") is None
    assert safe_json_loads("{invalid}", default={}) == {}


def test_safe_json_loads_type_error():
    assert safe_json_loads(None) is None
    assert safe_json_loads(None, default=[]) == []


def test_safe_json_loads_empty_string():
    assert safe_json_loads("") is None
    assert safe_json_loads("   ", default=False) is False
