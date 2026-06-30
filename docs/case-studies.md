# Free Consultation Case Studies

This is a library of free LLM selection consultations.

Each case starts from a real, public GitHub question where a user was trying to decide which model, provider, or stack to use. The user pain is abstracted into a general selection problem — no personal data is copied.

For each case we run `llm-selector`, then write the kind of short, practical answer we would give in a free consultation.

> These are advisory examples, not guarantees. Always validate with your own tasks, data policy, and cost profile.

How to read each case:

- **Source** — the public discussion that inspired the case
- **Situation** — the real-world selection problem
- **Constraints** — budget, hardware, language, privacy, tool, region
- **`llm-selector` inputs** — how we mapped it to scenario / sensitivity / budget / deployment
- **Shortlist** — the tool's top 3
- **Free consultation** — the practical recommendation
- **7-day action plan** — how to test before committing
- **Verification** — how to confirm the endpoint and control cost

---

## Case 1 — Smallest local model that runs on old hardware

- **Source:** [ggml-org/llama.cpp · discussion #25071](https://github.com/ggml-org/llama.cpp/discussions/25071)
- **Situation:** A beginner wants a local assistant on an old, low-spec machine and is unsure whether any model is usable at all.
- **Constraints:** ~4GB RAM, CPU-only, total beginner, wants fully local/offline.
- **`llm-selector` inputs:** scenario `office_automation`, sensitivity `public`, budget `low`, deployment `private`

```bash
python selector.py --scenario office_automation --sensitivity public --budget low --deployment private
```

- **Shortlist:** Local open-source (7) · Qwen (6) · GPT (3)

**Free consultation:**

On 4GB RAM, CPU-only, the realistic answer is a small local open-source model. Aim for a 1-2B class model in a low quant (for example a Q3/Q4 build) through `llama.cpp` or a friendly runtime. Do not expect agentic coding; expect a basic assistant for short tasks, drafting, and Q&A. Keep context small to avoid swapping.

**7-day action plan:**

1. Day 1-2: install a runtime and pull one small model (1-2B, Q4).
2. Day 3-4: test 5 real tasks you actually do (summaries, short replies, notes).
3. Day 5: if it's too slow, drop to a smaller model or lower quant.
4. Day 6-7: decide if local is good enough, or if a cheap hosted API is worth it for harder tasks.

**Verification:**

- Watch RAM and response time, not just output quality.
- If you later add a hosted API, keep sensitive content local and only send public content out.

---

## Case 2 — Best local model for a specific (non-English) language

- **Source:** [icereed/paperless-gpt · discussion #17](https://github.com/icereed/paperless-gpt/discussions/17)
- **Situation:** A user processes personal documents in a non-English language locally and needs a model that stays in that language and handles it well.
- **Constraints:** 8GB VRAM GPU, language fidelity required, privacy-oriented local pipeline.
- **`llm-selector` inputs:** scenario `translation`, sensitivity `internal`, budget `low`, deployment `private`

```bash
python selector.py --scenario translation --sensitivity internal --budget low --deployment private
```

- **Shortlist:** Qwen (7) · Local open-source (6) · GLM-5.2 (3)

**Free consultation:**

For local multilingual document work on 8GB VRAM, a Qwen-class model (7B, quantized) is a strong default because of solid multilingual behavior. Keep it local for privacy. The common failure here is the model silently answering in English — fix that with an explicit system prompt that pins the output language, and prefer instruction-tuned variants. If quality is not enough at 7B, the trade-off is either a smaller quant of a larger model or a privacy-safe hosted API for the hardest documents.

**7-day action plan:**

1. Day 1: run a 7B instruct model locally with a language-locked system prompt.
2. Day 2-3: test on 10 real documents in your language.
3. Day 4: log where it drifts to English or loses terminology.
4. Day 5-6: try one alternative model and compare.
5. Day 7: lock the model + prompt template that stays in-language.

**Verification:**

- Confirm output language consistency across long documents, not just short samples.
- Keep documents local; do not send personal files to external APIs without redaction.

---

## Case 3 — Is the cheaper "mini" model good enough?

- **Source:** [danny-avila/LibreChat · discussion #12733](https://github.com/danny-avila/LibreChat/discussions/12733)
- **Situation:** A team wants to use a cheaper/faster "mini" tier for summarization and is unsure whether it's good enough or whether the full model is required.
- **Constraints:** hosted API (cloud), wants lower cost and speed, summarization quality matters.
- **`llm-selector` inputs:** scenario `document_summary`, sensitivity `internal`, budget `medium`, deployment `api`

```bash
python selector.py --scenario document_summary --sensitivity internal --budget medium --deployment api
```

- **Shortlist:** Qwen (6) · GLM-5.2 (5) · Kimi (5)

**Free consultation:**

The right question is not "mini vs full" — it's "what's the cheapest model that passes my quality bar on real documents." For summarization, long-context handling and hallucination control matter more than raw size. Define a small eval set of real documents with a known "good summary," then test candidates. A mini tier often passes for routine summaries and fails on nuanced or long content. The cost-smart pattern is a tiered setup: cheap model for routine summaries, stronger model only when the input is long or high-stakes.

**7-day action plan:**

1. Day 1: pick 10 representative documents and write the ideal summary for each.
2. Day 2-3: run mini vs full vs a shortlisted alternative on all 10.
3. Day 4: score accuracy, missing points, and hallucinations.
4. Day 5: estimate monthly cost at your real volume for each option.
5. Day 6-7: choose a tiered routing rule (cheap by default, escalate on long/critical docs).

**Verification:**

- Track cost per 1,000 summaries, not just per request.
- Confirm the provider returns usage metadata so you can forecast spend.

---

## Case 4 — Execution stack for sensitive financial analysis

- **Source:** [openai/openai-python · discussion #2864](https://github.com/openai/openai-python/discussions/2864)
- **Situation:** A user doing spreadsheet/financial analysis must choose between a managed code-execution tool and a self-hosted sandbox, driven by governance and auditability.
- **Constraints:** sensitive financial data, needs audit logs, reproducibility, compliance.
- **`llm-selector` inputs:** scenario `data_analysis`, sensitivity `regulated`, budget `high`, deployment `hybrid`

```bash
python selector.py --scenario data_analysis --sensitivity regulated --budget high --deployment hybrid
```

- **Shortlist:** Local open-source (7) · GLM-5.2 (4) · Qwen (4)

**Free consultation:**

With regulated financial data, the execution environment matters as much as the model. For auditability and compliance, prefer a controlled sandbox you own (self-hosted execution with logging) over a fully managed black box, even if the managed option is more convenient. Keep raw data inside your boundary; let the model orchestrate and generate code, but run it in your audited environment. Model strength matters for code/SQL quality, but the governance layer is what makes this deployable. This is a hybrid pattern: strong model for reasoning, private execution for data.

**7-day action plan:**

1. Day 1-2: define what must be logged (inputs, code, outputs, who ran it).
2. Day 3-4: stand up a controlled sandbox (containerized execution + audit log).
3. Day 5: test a real analysis with synthetic or redacted data first.
4. Day 6: review the audit trail with whoever owns compliance.
5. Day 7: decide managed vs self-hosted based on the audit gap, not convenience.

**Verification:**

- Confirm no raw regulated data leaves your boundary.
- Confirm every code execution is logged and reproducible.

---

## Case 5 — Cheapest "good enough" API to build a chatbot

- **Source:** [github/community · discussion #198436](https://github.com/community/community/discussions/198436)
- **Situation:** A beginner building a chatbot wants the best price-to-quality API with a usable free tier.
- **Constraints:** student/beginner, wants a generous free tier, bilingual, easy SDK integration.
- **`llm-selector` inputs:** scenario `customer_service`, sensitivity `public`, budget `low`, deployment `api`

```bash
python selector.py --scenario customer_service --sensitivity public --budget low --deployment api
```

- **Shortlist:** Qwen (5) · DeepSeek (5) · GPT (4)

**Free consultation:**

For a beginner chatbot with public data and a tight budget, optimize for free/cheap tier + easy SDK + stable output. A low-cost provider (Qwen or DeepSeek tier) is a sensible start; keep a mainstream API as a fallback for quality comparison. Don't over-engineer: build the smallest working chatbot first, with a clear system prompt and a way to hand off to a human or a canned answer when unsure. Quality is "good enough if users get correct, on-topic answers," not benchmark score.

**7-day action plan:**

1. Day 1: pick one low-cost API and get a hello-world chatbot running.
2. Day 2-3: add your real FAQ/knowledge as context.
3. Day 4: test bilingual prompts and common user questions.
4. Day 5: add a fallback for "I don't know" instead of hallucinating.
5. Day 6-7: compare against one alternative API for quality and cost.

**Verification:**

- Track free-tier limits and what happens when you exceed them.
- Keep only public data in prompts at this stage.

---

## Case 6 — Which model for daily agentic coding

- **Source:** [openinterpreter/open-interpreter · discussion #1757](https://github.com/openinterpreter/open-interpreter/discussions/1757)
- **Situation:** An experienced independent developer wants the best model for daily agentic coding/execution, optimizing tool-call reliability and cost-per-successful-task, possibly via routing.
- **Constraints:** daily use, cost-conscious, multi-step tool loops, cache-friendliness matters.
- **`llm-selector` inputs:** scenario `ai_coding`, sensitivity `internal`, budget `medium`, deployment `hybrid`

```bash
python selector.py --scenario ai_coding --sensitivity internal --budget medium --deployment hybrid
```

- **Shortlist:** GLM-5.2 (6) · Qwen (5) · DeepSeek (5)

**Free consultation:**

For daily agentic coding, the metric is cost-per-successful-task and tool-call reliability, not benchmark rank. A strong coding model like GLM-5.2 is a good primary, with a cheaper model (DeepSeek/Qwen tier) as a router fallback for simple steps. The hybrid pattern works: route easy edits/autocomplete to the cheap model, escalate hard reasoning and multi-step tool loops to the stronger one. If you access GLM-5.2 through a gateway or Claude Code, verify the endpoint is actually GLM-5.2 before trusting it for daily work and before scaling spend.

**7-day action plan:**

1. Day 1: set your primary model and run 10 real coding tasks.
2. Day 2-3: track success rate, retries, and tool-call failures.
3. Day 4: add a cheaper fallback model for simple steps.
4. Day 5: measure cost per successful task for each route.
5. Day 6: verify the endpoint identity if using a gateway.
6. Day 7: lock a routing rule that balances cost and reliability.

**Verification:**

- If using a GLM gateway or Claude Code, run [`verify-glm`](https://github.com/xiaoyanfei-tech/verify-glm) to confirm the endpoint.
- Pin the provider where possible to avoid silent routing and cost inflation.

---

## How to get your own free case

These are examples. If you want a free first-pass selection for your own situation:

1. Run the CLI: `python selector.py`
2. Or open a selection request: https://github.com/xiaoyanfei-tech/llm-selector/issues/new/choose

Include your scenario, data sensitivity, budget range, deployment preference, and current tools. Do not include API keys, private URLs, customer records, contracts, or confidential screenshots.
