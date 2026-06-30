# llm-selector

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](#usage)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![SME AI Advisor](https://img.shields.io/badge/SME-AI%20advisor-orange)](#who-is-this-for)

> Choose the right LLM, then verify you're actually using it.

`llm-selector` is a lightweight, zero-dependency advisor for small and medium-sized businesses choosing between GLM, Qwen, DeepSeek, Kimi, Claude, GPT, and local open-source models.

It is not another benchmark leaderboard. It starts from the customer's business scenario, budget, data sensitivity, and deployment preference, then generates a practical shortlist and next-step report.

## Why this exists

Most LLM benchmarks answer: "Which model scores higher on a dataset?"

SMEs usually ask something more practical:

- Which model should we use for AI coding, documents, customer service, or internal knowledge?
- Should we use hosted APIs, domestic providers, hybrid routing, or private deployment?
- What risks should we review before sending company data to a model?
- If a gateway claims to route to GLM-5.2, how do we verify it?
- What should our first PoC look like?

`llm-selector` turns those questions into a simple selection report.

## Who is this for?

- SME founders, OPCs, freelancers, and IT managers evaluating LLM adoption
- Developers helping a company or individual choose an AI stack
- Teams comparing GLM, Qwen, DeepSeek, Kimi, Claude, GPT, and local models
- Consultants preparing an initial AI model selection report
- Anyone who needs practical model-selection guidance before building a PoC

## What it does

The CLI asks about:

- business scenario
- data sensitivity
- budget preference
- deployment preference

Then it outputs:

- top 3 model/model-family recommendations
- why each option fits
- risks to review
- verification advice
- suggested next steps for PoC

## Usage

```bash
git clone https://github.com/xiaoyanfei-tech/llm-selector.git
cd llm-selector
python selector.py
```

Non-interactive example:

```bash
python selector.py \
  --scenario ai_coding \
  --scenario document_summary \
  --sensitivity internal \
  --budget medium \
  --deployment domestic \
  --output report.md
```

Machine-readable output:

```bash
python selector.py --scenario ai_coding --json
```

Share or feedback templates:

```bash
python selector.py --share-template
python selector.py --feedback-template
```

## Example output

```text
Wrote report.md
Top recommendations:
- GLM-5.2 (10)
- Qwen (7)
- DeepSeek (6)
```

The generated Markdown report includes:

```md
# SME LLM Selection Report

> Choose the right LLM, then verify you're actually using it.

## Recommended shortlist

### 1. GLM-5.2
Why it fits:
- Strong fit for Claude Code-style AI coding
- Long-context friendly

Risks to review:
- Verify the endpoint is really GLM-5.2 before trusting a gateway

Verification: Run verify-glm...
```

## Relationship with verify-glm

`llm-selector` helps choose the right model direction.

[`verify-glm`](https://github.com/xiaoyanfei-tech/verify-glm) verifies whether a GLM-5.2 endpoint is actually behaving like GLM-5.2.

Together:

```text
Choose the right LLM → verify you're actually using it → run a focused PoC
```

## Supported scenarios

- AI coding / developer assistant
- Enterprise knowledge base / RAG
- Customer service chatbot
- Document summary / contract reading
- Translation / bilingual writing
- Data analysis / report assistant
- Office automation / internal assistant

## Supported model families

- GLM-5.2
- Qwen
- DeepSeek
- Kimi
- Claude
- GPT family
- Local open-source models

## Commercial-ready next steps

This repo can be used as a lead-capture and consulting workflow:

- Start with the CLI selection report
- Read [`ROADMAP.md`](ROADMAP.md) to see where the project is going
- Read [`CONTRIBUTING.md`](CONTRIBUTING.md) to contribute scenarios, cases, or model notes
- Read [`docs/vision.md`](docs/vision.md) for the long-term product thesis
- Read [`docs/go-to-market.md`](docs/go-to-market.md) for the market-first strategy
- Read [`docs/market-validation.md`](docs/market-validation.md) to track evidence and traction
- Read [`docs/case-studies.md`](docs/case-studies.md) for free consultation case studies based on real public questions
- Read [`docs/methodology.md`](docs/methodology.md) to understand the decision framework
- Use [`docs/client-intake.md`](docs/client-intake.md) to collect business context
- Use [`docs/packages.md`](docs/packages.md) to choose the smallest useful next step
- Use [`docs/report-template.md`](docs/report-template.md) for a paid selection report
- Use [`docs/poc-plan.md`](docs/poc-plan.md) for a 2-4 week implementation plan
- Use [`docs/services.md`](docs/services.md) to describe available consulting deliverables

Potential paid deliverables:

- OPC / personal LLM selection
- LLM selection report
- AI coding stack recommendation
- endpoint verification report
- PoC plan and integration checklist

## 中文说明

中文用户请看 [`README.zh-CN.md`](README.zh-CN.md)。

## Need help?

Need help choosing an LLM stack?

Open a selection request:

https://github.com/xiaoyanfei-tech/llm-selector/issues/new/choose

If you are choosing an LLM stack for yourself, an OPC, a small team, or a small/medium-sized business, this tool can produce a first-pass report. For deeper help, open an issue with your use case:

- business scenario
- data sensitivity
- estimated monthly usage
- preferred providers or deployment constraints
- current tools such as Claude Code, Cursor, Dify, FastGPT, or internal systems

Possible consulting deliverables:

- OPC / personal LLM selection
- LLM selection report
- AI coding stack recommendation
- enterprise knowledge-base model recommendation
- endpoint verification report
- PoC plan and integration checklist

## Limitations

- This is a practical decision aid, not a universal benchmark.
- Model quality, price, and availability change quickly.
- Always validate recommendations with your own tasks and data policy.
- The included model data is intentionally simple and should be updated as the market changes.

## License

MIT — see [LICENSE](LICENSE).
