# SME LLM Selection Report

> Choose the right LLM, then verify you're actually using it.

## Inputs

- Scenarios: AI coding / developer assistant, Enterprise knowledge base / RAG
- Data sensitivity: Customer / contract / operational data
- Budget: Medium / controlled PoC budget
- Deployment preference: Hybrid deployment

## Recommended shortlist

### 1. Qwen — score 9

Provider/ecosystem: Alibaba / open-source Qwen ecosystem

Why it fits:
- Strong Chinese ecosystem
- Good open-source/private deployment options
- Broad tooling support

Risks to review:
- Model size and serving cost vary widely
- Private deployment requires ops capability

Verification: Use task-specific samples and tokenizer/metadata checks when routed through gateways.

### 2. GLM-5.2 — score 8

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

### 3. Local open-source model — score 8

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

## Scenario notes

- Prioritize coding-agent compatibility, tool use, latency, and long-context behavior.
- If using Claude Code through a GLM gateway, verify the endpoint with verify-glm.
- Prioritize retrieval quality, Chinese document handling, data governance, and cost per query.

## Suggested next steps

1. Pick the top 1-2 models and run a small PoC with real but non-sensitive samples.
2. Measure quality, latency, monthly cost, data handling, and user adoption.
3. If using a third-party LLM gateway, verify that the routed model is actually the claimed model.
4. If GLM-5.2 is selected for Claude Code or an LLM gateway, run verify-glm: https://github.com/xiaoyanfei-tech/verify-glm
5. For sensitive data, prefer private deployment, hybrid routing, or strict data-redaction workflows.

## If you need a business-ready recommendation

Open a GitHub issue using the Business LLM selection request template:

https://github.com/xiaoyanfei-tech/llm-selector/issues/new/choose

Include your scenario, data sensitivity, budget range, deployment preference, and existing tools. Do not include API keys, private URLs, customer records, contracts, or confidential screenshots.

Possible deliverables:

- LLM selection report
- AI coding stack recommendation
- endpoint verification report
- 2-4 week PoC plan

## Important note

This report is a practical selection aid, not a universal benchmark. Final decisions should be validated with your own tasks, data policy, and cost profile.
