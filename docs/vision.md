# Vision

AI model selection is becoming a business decision layer.

Benchmarks are useful, but they do not answer the full customer question:

> Which model should I use for my workflow, budget, data policy, and deployment constraints?

`llm-selector` starts from the customer side instead of the benchmark side.

## Thesis

The number of LLM options will keep growing:

- GLM
- Qwen
- DeepSeek
- Kimi
- Claude
- GPT
- local open-source models
- gateways that route between them

For OPCs, small teams, and SMEs, the problem is not lack of options. The problem is decision risk.

They need:

- a shortlist
- risk framing
- a small PoC plan
- endpoint verification
- cost and data-safety awareness

## Product wedge

The first wedge is a free open-source CLI that generates practical selection reports.

The second wedge is verification:

```text
llm-selector chooses
verify-glm verifies
```

The long-term opportunity is a decision platform for AI adoption:

```text
scenario intake → model shortlist → verification → PoC plan → case feedback → better recommendations
```

## Why this can become defensible

The defensible asset is not the initial code. It is the compounding case library:

- real user scenarios
- actual model choices
- PoC outcomes
- cost/quality tradeoffs
- gateway verification results
- model-fit matrix by scenario

A public benchmark says which model scores higher. A case library says which stack worked for which business constraint.

## Market posture

Win trust before monetizing heavily.

- Free first-pass report
- Low-friction issue intake
- Small paid review only when needed
- PoC before large spend
- Expand only after ROI evidence

This keeps adoption easy while preserving a path to consulting, reports, and future platform revenue.
