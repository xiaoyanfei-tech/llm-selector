# LLM Selection Report Template

## Executive summary

- Recommended primary model:
- Recommended backup model:
- Recommended deployment approach:
- Key reason:
- Main risk:
- First PoC scenario:

## Business scenario

- Company type:
- Target workflow:
- Users:
- Data sensitivity:
- Budget profile:
- Deployment preference:

## Shortlist

| Rank | Model / family | Fit | Main strength | Main risk | Verification needed |
|------|----------------|-----|---------------|-----------|---------------------|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

## Cost and deployment notes

- Token usage assumptions:
- Expected monthly usage:
- Hosted API considerations:
- Private deployment considerations:
- Support/ops considerations:

## Data and security review

- Data classes involved:
- Data that must not leave company systems:
- Redaction requirements:
- Logging policy:
- Access control requirements:

## Endpoint verification plan

- Claimed model:
- Gateway/provider:
- Verification checks:
  - [ ] API echo
  - [ ] tokenizer/behavior fingerprint
  - [ ] context-window test
  - [ ] metadata/usage-shape check
  - [ ] latency/cost sanity check
- Tools:
  - [ ] verify-glm, if GLM-5.2 is selected

## PoC plan

- Duration:
- Pilot users:
- Sample tasks:
- Success metrics:
- Rollback plan:

## Recommendation

State the final recommendation in plain business language.

## Appendix

- Test prompts:
- Assumptions:
- Open questions:
