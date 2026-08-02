# Pepkio Biostat Test Navigator Python Client

Python client for the Pepkio `biostat-test-navigator` tool.

## Installation

```bash
pip install pepkio-biostat-test-navigator
```

Set your Pepkio API key in the environment:

```bash
export PEPKIO_API_KEY="your-api-key"
```

## Python Usage

```python
from pepkio_biostat_test_navigator import PepkioClient

client = PepkioClient()

# Run a statistical test recommendation
result = client.run(
    {
        "template_id": "qpcr",
        "outcome_type": "continuous",
        "comparison_type": "two_groups",
        "group_count": 2,
        "paired": False,
        "groups": [
            {"name": "Control", "values": [1.02, 0.98, 1.05, 1.01]},
            {"name": "Treatment", "values": [2.45, 2.51, 2.38, 2.62]},
        ],
    }
)

print(result.result["primary_test"])
```

## CLI Usage

```bash
pepkio-biostat-test-navigator manifest
pepkio-biostat-test-navigator run --example qpcr_two_group_mann_whitney
```
