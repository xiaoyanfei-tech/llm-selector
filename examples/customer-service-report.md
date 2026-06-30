# SME / OPC LLM Selection Report

> Choose the right LLM, then verify you're actually using it.

## Executive summary

Recommended first shortlist: **Local open-source model, Qwen, DeepSeek**.

Primary recommendation: **Local open-source model** because it best matches the selected scenario, budget, data sensitivity, and deployment preference.

Investment posture: start with a small, measurable PoC instead of committing to a large platform contract. Private/hybrid data handling should be reviewed before broad rollout.

## Decision

Start with **Local open-source model** as the first candidate and keep the #2 option as a fallback during PoC. Do not scale spend until quality, cost, and endpoint trust are measured with real tasks.

## Inputs

- Scenarios: Customer service chatbot
- Data sensitivity: Customer / contract / operational data
- Budget: Medium / controlled PoC budget
- Deployment preference: Hybrid deployment

## Recommended shortlist

### 1. Local open-source model — score 7

Provider/ecosystem: Self-hosted Qwen/DeepSeek/Llama-style models

Why it fits:
- Best fit when data must stay internal
- Full control over deployment and logs
- Potentially predictable cost at scale

Risks to review:
- Needs GPU/ops expertise
- Quality may lag top hosted models for some tasks
- Maintenance burden is real

Verification: Run a small PoC with your own data and measure latency, cost, quality, and ops effort.

### 2. Qwen — score 6

Provider/ecosystem: Alibaba / open-source Qwen ecosystem

Why it fits:
- Strong Chinese ecosystem
- Good open-source/private deployment options
- Broad tooling support

Risks to review:
- Model size and serving cost vary widely
- Private deployment requires ops capability

Verification: Use task-specific samples and tokenizer/metadata checks when routed through gateways.

### 3. DeepSeek — score 5

Provider/ecosystem: DeepSeek / compatible gateways

Why it fits:
- Strong reasoning/coding value
- Often attractive for cost-sensitive teams
- Good for analysis-heavy workflows

Risks to review:
- Latency and availability depend on provider/gateway
- Reasoning models may increase token usage

Verification: Validate reasoning behavior, latency, and actual token usage with your own tasks.

## Risk register

| Risk | Severity | Mitigation |
|------|----------|------------|
| Model/provider mismatch | Medium | Verify third-party gateways before trusting production use. |
| Cost grows faster than value | Medium | Start with a small PoC and track requests, token usage, and time saved. |
| Sensitive data exposure | High | Use redaction, private deployment, or hybrid routing for sensitive workflows. |
| User adoption failure | Medium | Pilot with a small group and measure real workflow improvement. |

## Scenario notes

- Prioritize stability, controllability, knowledge-base grounding, and escalation workflow.

## Suggested next steps

1. Run a 7-day OPC/personal trial or a 2-4 week team PoC before committing to a larger contract.
2. Pick the top 1-2 models and test with real but non-sensitive samples.
3. Measure quality, latency, monthly cost, data handling, and actual time saved.
4. If using a third-party LLM gateway, verify that the routed model is actually the claimed model.
5. If GLM-5.2 is selected for Claude Code or an LLM gateway, run verify-glm: https://github.com/xiaoyanfei-tech/verify-glm
6. Expand only when the PoC shows measurable ROI or workflow leverage.

## If you need a business-ready recommendation

Open a GitHub issue using the Business LLM selection request template:

https://github.com/xiaoyanfei-tech/llm-selector/issues/new/choose

Include your scenario, data sensitivity, budget range, deployment preference, and existing tools. Do not include API keys, private URLs, customer records, contracts, or confidential screenshots.

Possible deliverables:

- OPC / personal LLM selection
- LLM selection report
- AI coding stack recommendation
- endpoint verification report
- 2-4 week PoC plan

## Important note

This report is a practical selection aid, not a universal benchmark. Final decisions should be validated with your own tasks, data policy, and cost profile.
