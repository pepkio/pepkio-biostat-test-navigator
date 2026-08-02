"""Pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest
from dotenv import load_dotenv

# Load monorepo .env for local integration runs (never log keys).
_monorepo_env = Path(__file__).resolve().parents[3] / ".env"
if _monorepo_env.is_file():
    load_dotenv(_monorepo_env)

_package_env = Path(__file__).resolve().parents[1] / ".env"
if _package_env.is_file():
    load_dotenv(_package_env)


@pytest.fixture
def mock_manifest() -> dict:
    return {
        "schema_version": "1.0",
        "tool_id": "biostat-test-navigator",
        "title": "Biostat Test Navigator",
        "execution_mode": "sync",
        "examples": [
            {
                "name": "qpcr_two_group_mann_whitney",
                "input": {
                    "template_id": "qpcr",
                    "outcome_type": "continuous",
                    "comparison_type": "two_groups",
                    "group_count": 2,
                    "paired": False,
                    "groups": [
                        {"name": "Control", "values": [1.02, 0.98, 1.05, 1.01]},
                        {"name": "Treatment", "values": [2.45, 2.51, 2.38, 2.62]},
                    ],
                },
                "output": {"ready": True, "primary_test_key": "mann_whitney"},
            },
            {
                "name": "survival_log_rank",
                "input": {
                    "template_id": "survival",
                    "outcome_type": "survival",
                    "comparison_type": "two_groups",
                    "group_count": 2,
                },
                "output": {"ready": True, "primary_test_key": "log_rank"},
            },
            {
                "name": "categorical_fisher_small_cells",
                "input": {
                    "outcome_type": "categorical",
                    "comparison_type": "two_groups",
                    "categorical_table": [[8, 2], [3, 12]],
                },
                "output": {"ready": True, "primary_test_key": "fisher_exact"},
            },
        ],
    }


@pytest.fixture
def mock_run_response() -> dict:
    return {
        "run_id": "run_biostat_123",
        "status": "completed",
        "result": {
            "ready": True,
            "preliminary": False,
            "primary_test": "Mann-Whitney U test",
            "primary_test_key": "mann_whitney",
            "rationale": "At least one group has fewer than 5 observations...",
        },
        "error": None,
        "result_url": "https://tools.pepkio.com/api/tools/v1/runs/run_biostat_123",
        "permalink": "https://tools.pepkio.com/r/run_biostat_123",
    }
