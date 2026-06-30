# Example: Enterprise Knowledge Base

## User

A small company wants to build an internal knowledge-base assistant for policies, SOPs, technical notes, and customer-facing documents.

Constraints:

- internal business data
- Chinese documents
- controlled budget
- wants a safe PoC before full rollout

## Suggested path

1. Compare Qwen, Kimi, GPT-family, and local open-source options.
2. Start with a small document set and strict redaction rules.
3. Measure answer quality, citation behavior, hallucination risk, latency, and cost.
4. If sensitive customer data is involved, evaluate hybrid or private deployment.

## Why this is a leverage play

A knowledge-base assistant can save many repeated search and explanation tasks, but only if it is grounded and trusted.

The first PoC should avoid broad rollout. Start with one team and one document domain.

## Command

```bash
python selector.py \
  --scenario knowledge_base \
  --sensitivity internal \
  --budget medium \
  --deployment hybrid \
  --output examples/knowledge-base-report.md
```
