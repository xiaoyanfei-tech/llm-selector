# Contributing

Thanks for helping improve `llm-selector`.

This project is not trying to be a universal benchmark. It is a practical selection framework for OPCs, small teams, and SMEs.

## Good contributions

- new real-world selection scenarios
- anonymized case studies
- model-family notes
- better risk descriptions
- improved report wording
- support for new business scenarios
- bug fixes to the CLI
- documentation in English or Chinese

## What not to include

Do not submit:

- API keys
- private URLs
- customer records
- contracts
- internal IPs
- confidential screenshots
- vendor NDA information

## Adding a model or model family

Update `models.json` with:

- display name
- provider/ecosystem
- best-fit tags
- strengths
- risks
- verification advice

Keep the language practical and non-hype. Avoid claiming a model is universally best.

## Adding a scenario

Update `scenarios.json` with:

- display name
- model weights
- scenario notes

Weights are heuristic fit scores, not benchmark results. They should reflect practical business fit.

## Sharing a case

Prefer anonymized cases:

```text
Industry: small software agency
Scenario: AI coding + document summary
Data sensitivity: internal
Budget: low
Recommended shortlist: GLM-5.2 / Qwen / Claude
Outcome: chose GLM-5.2 gateway, verified endpoint, ran 7-day trial
```

Use the GitHub issue template: `Share selection result`.

## Development

No dependencies are required.

```bash
python -m py_compile selector.py
python selector.py --scenario ai_coding --json
```

Before submitting, run a security scan if available:

```bash
python path/to/audit-before-publish/audit.py --path .
```
