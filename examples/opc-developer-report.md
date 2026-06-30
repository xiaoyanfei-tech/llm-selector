# SME / OPC LLM Selection Report

> Choose the right LLM, then verify you're actually using it.

## Executive summary

Recommended first shortlist: **GLM-5.2, Qwen, Claude**.

Primary recommendation: **GLM-5.2** because it best matches the selected scenario, budget, data sensitivity, and deployment preference.

Investment posture: start with a small, measurable PoC instead of committing to a large platform contract. Data risk appears manageable for a small PoC if normal redaction rules are followed.

## Decision

Start with **GLM-5.2** as the first candidate and keep the #2 option as a fallback during PoC. Do not scale spend until quality, cost, and endpoint trust are measured with real tasks.

## Inputs

- Scenarios: AI coding / developer assistant, Document summary / contract reading
- Data sensitivity: Internal business data
- Budget: Low / cost-sensitive
- Deployment preference: Hosted API first

## Recommended shortlist

### 1. GLM-5.2 — score 8

Provider/ecosystem: Zhipu / GLM-compatible gateways

Why it fits:
- Strong fit for Claude Code-style AI coding
- Long-context friendly
- Good Chinese/English mixed workflows
- Useful when you need OpenAI/Anthropic-compatible gateway routing

Risks to review:
- Verify the endpoint is really GLM-5.2 before trusting a gateway
- Gateway compatibility and metadata can vary

Verification: Run verify-glm to check tokenizer fingerprint, reasoning_tokens, and optional 1M context support.

### 2. Qwen — score 8

Provider/ecosystem: Alibaba / open-source Qwen ecosystem

Why it fits:
- Strong Chinese ecosystem
- Good open-source/private deployment options
- Broad tooling support

Risks to review:
- Model size and serving cost vary widely
- Private deployment requires ops capability

Verification: Use task-specific samples and tokenizer/metadata checks when routed through gateways.

### 3. Claude — score 8

Provider/ecosystem: Anthropic / approved providers

Why it fits:
- Strong coding and agentic workflows
- Excellent writing and reasoning UX
- Mature Claude Code ecosystem

Risks to review:
- Availability, data policy, and cost may be constraints for some SMEs
- International routing/compliance requirements must be reviewed

Verification: Verify policy/compliance fit and cost under realistic usage.

## Risk register

| Risk | Severity | Mitigation |
|------|----------|------------|
| Model/provider mismatch | Medium | Verify third-party gateways before trusting production use. |
| Cost grows faster than value | Medium | Start with a small PoC and track requests, token usage, and time saved. |
| Sensitive data exposure | High | Use redaction, private deployment, or hybrid routing for sensitive workflows. |
| User adoption failure | Medium | Pilot with a small group and measure real workflow improvement. |

## Scenario notes

- Prioritize coding-agent compatibility, tool use, latency, and long-context behavior.
- If using Claude Code through a GLM gateway, verify the endpoint with verify-glm.
- Prioritize long-context handling, citation, and hallucination control.

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
