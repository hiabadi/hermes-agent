"""Tests for proxy normalization utilities."""
import os
from utils import normalize_proxy_url, normalize_proxy_env_vars

def test_handles_empty_and_null_proxy_urls():
    assert normalize_proxy_url(None) is None
    assert normalize_proxy_url("") is None
    assert normalize_proxy_url("   ") is None

def test_rewrites_socks_to_socks5_for_compatibility():
    assert normalize_proxy_url("socks://127.0.0.1:1080") == "socks5://127.0.0.1:1080"
    assert normalize_proxy_url("SOCKS://proxy.local:9050") == "socks5://proxy.local:9050"

def test_preserves_valid_proxy_schemes():
    assert normalize_proxy_url("socks5://127.0.0.1:1080") == "socks5://127.0.0.1:1080"
    assert normalize_proxy_url("http://user:pass@proxy.local") == "http://user:pass@proxy.local"
    assert normalize_proxy_url("https://proxy.local") == "https://proxy.local"

def test_strips_whitespace_from_proxy_urls():
    assert normalize_proxy_url("  socks://proxy.local  ") == "socks5://proxy.local"
    assert normalize_proxy_url("\nhttp://proxy.local\t") == "http://proxy.local"

def test_normalizes_proxy_environment_variables_in_place(monkeypatch):
    monkeypatch.setenv("HTTP_PROXY", "socks://127.0.0.1:1080")
    monkeypatch.setenv("https_proxy", "http://proxy.local")
    monkeypatch.setenv("ALL_PROXY", "   ")

    normalize_proxy_env_vars()

    assert os.environ["HTTP_PROXY"] == "socks5://127.0.0.1:1080"
    assert os.environ["https_proxy"] == "http://proxy.local"
    assert os.environ["ALL_PROXY"] == "   "
