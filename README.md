# incident-comms-check

> Validate incident communication drafts for impact, ETA, and owner clarity.

## Quick start Overview

Validate incident communication drafts for impact, ETA, and owner clarity. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts incident update draft. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
incident-comms-check examples/sample.txt
incident-comms-check examples/sample.txt --json --fail-on medium
python -m incident_comms_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `unknown-impact` | high | impact is not clear |
| `missing-eta` | medium | ETA is missing |
| `ownerless-update` | low | communication owner is missing |

## Validation Notes

```bash
ruff check .
pytest
python -m incident_comms_check --help
```

Example risky input:

```text
incident update impact unknown eta missing owner none
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
