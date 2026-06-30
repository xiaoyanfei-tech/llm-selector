# Example: Sensitive Data / Private Deployment

## User

A company handles contracts, customer records, or regulated documents and wants to adopt LLMs without sending sensitive data to public APIs.

Constraints:

- high data sensitivity
- strict logging and access requirements
- may need local or hybrid deployment
- quality still matters

## Suggested path

1. Start with a data classification review.
2. Separate public/internal/sensitive workflows.
3. Compare local open-source models, Qwen private deployment, and hybrid routing.
4. Use hosted premium models only for redacted or non-sensitive tasks.
5. Measure ops effort honestly before committing to private deployment.

## Why this is a leverage play

Private deployment can reduce data exposure but increases operational burden. The best financial decision may be hybrid: keep sensitive data local, use hosted models for non-sensitive productivity tasks.

## Command

```bash
python selector.py \
  --scenario knowledge_base \
  --scenario document_summary \
  --sensitivity regulated \
  --budget high \
  --deployment private \
  --output examples/sensitive-private-report.md
```
