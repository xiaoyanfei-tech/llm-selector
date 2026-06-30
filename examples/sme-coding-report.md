# SME LLM Selection Report

> Choose the right LLM, then verify you're actually using it.

## Inputs

- Scenarios: AI coding / developer assistant, Document summary / contract reading
- Data sensitivity: Internal business data
- Budget: Medium / controlled PoC budget
- Deployment preference: Domestic providers preferred

## Recommended shortlist

### 1. GLM-5.2 — score 10

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

### 2. Qwen — score 9

Provider/ecosystem: Alibaba / open-source Qwen ecosystem

Why it fits:
- Strong Chinese ecosystem
- Good open-source/private deployment options
- Broad tooling support

Risks to review:
- Model size and serving cost vary widely
- Private deployment requires ops capability

Verification: Use task-specific samples and tokenizer/metadata checks when routed through gateways.

### 3. Claude — score 7

Provider/ecosystem: Anthropic / approved providers

Why it fits:
- Strong coding and agentic workflows
- Excellent writing and reasoning UX
- Mature Claude Code ecosystem

Risks to review:
- Availability, data policy, and cost may be constraints for some SMEs
- International routing/compliance requirements must be reviewed

Verification: Verify policy/compliance fit and cost under realistic usage.

## Scenario notes

- Prioritize coding-agent compatibility, tool use, latency, and long-context behavior.
- If using Claude Code through a GLM gateway, verify the endpoint with verify-glm.
- Prioritize long-context handling, citation, and hallucination control.

## Suggested next steps

1. Pick the top 1-2 models and run a small PoC with real but non-sensitive samples.
2. Measure quality, latency, monthly cost, data handling, and user adoption.
3. If using a third-party LLM gateway, verify that the routed model is actually the claimed model.
4. If GLM-5.2 is selected for Claude Code or an LLM gateway, run verify-glm: https://github.com/xiaoyanfei-tech/verify-glm
5. For sensitive data, prefer private deployment, hybrid routing, or strict data-redaction workflows.

## Important note

This report is a practical selection aid, not a universal benchmark. Final decisions should be validated with your own tasks, data policy, and cost profile.
