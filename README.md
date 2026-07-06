# Incident Comms Check

> A small command-line review pass for incident response.

![Incident Comms Check cover](assets/readme-cover.svg)

Validate incident communication drafts for impact, ETA, and owner clarity. In practice it is a narrow guardrail for incident response, ownership, release risk, and follow-up notes: one command, a concrete report, and very little ceremony.

## Signals in plain English

- `unknown-impact` (high): impact is not clear. Fix: state affected users, tenants, or functions.
- `missing-eta` (medium): ETA is missing. Fix: provide next update time or recovery estimate.
- `ownerless-update` (low): communication owner is missing. Fix: assign a comms owner.

## Input and report

The reader accepts text, JSON, JSONL, or CSV. The default report is readable in a terminal or pull request; `--json` keeps the same findings available to automation.

## Demo

```bash
git clone https://github.com/mertefekurt/incident-comms-check.git
cd incident-comms-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
incident-comms-check examples/sample.txt
incident-comms-check examples/sample.txt --json
```

## Sanity checks

```bash
ruff check .
pytest
python -m incident_comms_check --help
```
