# Example: OPC Developer AI Stack

## User

A one-person company / independent developer wants an AI stack for:

- daily coding
- document drafting
- client proposal writing
- occasional data analysis

Constraints:

- low monthly budget
- fast setup
- no complex self-hosting
- wants to avoid paying for tools that do not improve daily output

## Suggested path

1. Start with Claude Code / Cursor-style AI coding workflow.
2. Compare GLM-5.2, DeepSeek, and Claude/GPT-family options depending on availability and budget.
3. If using a GLM-compatible gateway, verify the endpoint with verify-glm.
4. Track one week of usage: tasks completed, time saved, token/cost behavior, failure cases.

## Why this is a leverage play

For an OPC, the goal is not to buy the most expensive model. The goal is to buy back focused hours.

A good first stack should:

- reduce coding and writing time
- stay within a predictable monthly budget
- avoid complex infrastructure
- be easy to stop if ROI is not visible within 7 days

## Command

```bash
python selector.py \
  --scenario ai_coding \
  --scenario document_summary \
  --sensitivity internal \
  --budget low \
  --deployment api \
  --output examples/opc-developer-report.md
```
