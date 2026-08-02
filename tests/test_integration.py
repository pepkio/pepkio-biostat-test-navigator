"""Integration tests against live Pepkio Tools API."""

from __future__ import annotations

import os

import pytest

from pepkio_biostat_test_navigator.client import PepkioClient

# Local first, then production (param order).
ENVIRONMENTS = [
    ("local", "https://tools.localtest.me"),
    ("production", "https://tools.pepkio.com"),
]


def _api_key_for(base_url: str) -> str | None:
    if "localtest.me" in base_url:
        return os.getenv("LOCAL_PEPKIO_API_KEY") or os.getenv("PEPKIO_API_KEY")
    return os.getenv("PEPKIO_API_KEY")


@pytest.fixture(params=ENVIRONMENTS, ids=["local", "production"])
def live_client(request):
    env_name, default_base_url = request.param
    base_url = os.getenv("PEPKIO_API_BASE_URL") or default_base_url
    api_key = _api_key_for(base_url)
    if not api_key:
        pytest.skip(f"No API key for {env_name} (set LOCAL_PEPKIO_API_KEY or PEPKIO_API_KEY)")
    with PepkioClient(api_key=api_key, base_url=base_url) as client:
        yield client


def test_get_manifest(live_client: PepkioClient):
    manifest = live_client.get_manifest(refresh=True)
    assert manifest["tool_id"] == "biostat-test-navigator"
    names = live_client.list_examples()
    assert "qpcr_two_group_mann_whitney" in names


def test_run_qpcr_example(live_client: PepkioClient):
    inp = live_client.get_example_input("qpcr_two_group_mann_whitney")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.run_id
    assert result.permalink
    assert result.result is not None
    assert result.result.get("ready") is True
    assert result.result.get("primary_test_key") == "mann_whitney"
    assert result.error is None


def test_run_survival_example(live_client: PepkioClient):
    inp = live_client.get_example_input("survival_log_rank")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("ready") is True
    assert result.result.get("primary_test_key") == "log_rank"


def test_run_categorical_example(live_client: PepkioClient):
    inp = live_client.get_example_input("categorical_fisher_small_cells")
    result = live_client.run(inp)
    assert result.status == "completed"
    assert result.result is not None
    assert result.result.get("ready") is True
    assert result.result.get("primary_test_key") == "fisher_exact"
