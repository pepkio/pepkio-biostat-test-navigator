# pepkio-biostat-test-navigator

Python client for the Pepkio `biostat-test-navigator` tool.

## Installation

```bash
pip install pepkio-biostat-test-navigator
```

## Quickstart

```python
from pepkio_biostat_test_navigator import PepkioClient

client = PepkioClient()

# Get tool manifest
manifest = client.get_manifest()

# Run example
inp = client.get_example_input("qpcr_two_group_mann_whitney")
result = client.run(inp)
print(result.result["primary_test"])
```

## CLI Usage

```bash
pepkio-biostat-test-navigator manifest
pepkio-biostat-test-navigator run --example qpcr_two_group_mann_whitney
```
