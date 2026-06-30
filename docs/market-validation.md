# Market Validation

This document tracks evidence that OPCs, small teams, and SMEs need practical LLM selection help.

It should be updated with real interviews, issues, anonymized cases, and paid conversations.

## Hypotheses

1. OPCs and independent developers need help choosing an AI coding stack.
2. SMEs do not want a benchmark; they want a practical recommendation for their workflow.
3. Data sensitivity and deployment constraints strongly affect model choice.
4. Third-party gateways create a verification need after model selection.
5. Users prefer a free first-pass report before paying for deeper help.

## Target customer segments

| Segment | Pain | Likely first product |
|---------|------|----------------------|
| OPC / solo founder | too many tools, limited budget, wants productivity quickly | personal AI stack recommendation |
| Independent developer | wants Claude Code/Cursor/Cline setup that actually works | AI coding stack plan |
| SME founder | wants AI adoption but lacks technical clarity | selection memo |
| IT manager | needs safe model choice for internal data | PoC plan + risk review |
| Small engineering team | wants team rollout for AI coding | AI coding stack recommendation |

## Public GitHub demand signals

The following signals are based on public GitHub issues and repository activity. They are summarized as demand patterns, not copied as user-specific cases.

### AI coding stack and provider setup

Public issues in AI coding assistant projects repeatedly show that users struggle with model and provider selection after choosing tools such as Continue or Cline.

Observed patterns:

- users ask for clearer provider/model lists and dynamic model discovery
- users request support for OpenAI-compatible gateways and new providers
- Qwen, DeepSeek, Kimi, GLM, local Ollama, LM Studio, and Vertex-style providers often need tool-specific configuration
- local/self-hosted endpoints can fail differently across VS Code, JetBrains, and CLI workflows
- users need guidance on which model is suitable for coding, autocomplete, agent mode, tool calling, and long context

Implication for `llm-selector`:

- AI coding stack selection should be a first wedge.
- Recommendations should include not only the model family, but also the tool/provider fit and verification steps.

### OpenAI-compatible does not mean compatible

Multiple public issues around OpenAI-compatible providers show recurring failures:

- missing or unsupported request fields
- provider-specific headers or base URLs not being honored
- tool calling incompatibility
- streamed response and usage metadata differences
- context window claims not matching real behavior

Implication for `llm-selector`:

- The project should explain compatibility risk in simple business language.
- The phrase "OpenAI-compatible" should be treated as a starting assumption, not proof.
- Endpoint verification should be part of the recommendation path.

### Model identity, routing, and cost trust

Public issue patterns include users reporting model mismatch, unintended model routing, unexpected credits spent, and provider pinning limitations.

Observed patterns:

- UI-selected model and actually used model can diverge
- gateway routing can create uncertainty about which model is serving requests
- context length and usage metadata problems make cost forecasting difficult
- users want stronger controls before scaling usage

Implication for `llm-selector`:

- "Choose the right LLM, then verify you're actually using it" is supported by real user pain.
- Cost-control and endpoint-trust checks should be part of every paid recommendation.

### Private deployment, RAG, and intranet constraints

Public issues in workflow/RAG platforms such as Dify show repeated private-deployment friction:

- adding model suppliers in private or intranet deployments
- local model and local embedding configuration failures
- offline/private RAG deployment questions
- token usage tracking and provider credential validation problems
- deployment dependency complexity for smaller teams

Implication for `llm-selector`:

- SME recommendations must account for deployment preference and data sensitivity early.
- Private/hybrid deployment advice is a separate product need, not just an enterprise afterthought.

### Competitive whitespace

Small repos exist around choosing LLMs, model routers, and leaderboard-based selection, but there does not appear to be a dominant GitHub-native project focused on SME/OPC business selection plus endpoint verification.

Implication for `llm-selector`:

- The project should avoid competing as a benchmark leaderboard.
- The stronger niche is customer-side decision support: scenario, budget, data sensitivity, deployment, tool fit, and verification.

### 10 investor-readable business cases

These cases translate public GitHub demand signals into business logic an investor can understand. They are not customer claims; they show repeated, public evidence of budget-relevant pain.

| # | Public signal | Customer profile | Business pain | Current workaround | Why budget exists | `llm-selector` product angle |
|---|---------------|------------------|---------------|--------------------|-------------------|------------------------------|
| 1 | [continuedev/continue#12581](https://github.com/continuedev/continue/issues/12581) | Developer or small team evaluating a new LLM gateway | Provider choice is fragmented; teams cannot tell whether a new gateway is ready for their coding workflow. | Wait for tool maintainers to add docs or manually test provider configs. | A working AI coding setup can save developer hours, but failed setup wastes engineering time. | Sell an AI coding stack recommendation that maps model, gateway, tool, and setup risk. |
| 2 | [continuedev/continue#12875](https://github.com/continuedev/continue/issues/12875) | Team trying to use a third-party OpenAI-compatible endpoint | "OpenAI-compatible" still fails in real clients, creating setup delays and uncertainty about vendor reliability. | Debug opaque API errors internally or switch providers without knowing root cause. | Teams pay to avoid wasting engineering cycles on endpoint integration failures. | Offer endpoint compatibility checks before a team commits to a provider. |
| 3 | [continuedev/continue#9797](https://github.com/continuedev/continue/issues/9797) | Cost-conscious developer using local models for coding | Advertised context length does not equal usable context in a real local stack. | Tune local server/client settings by trial and error. | Local models are attractive for cost and privacy, but only if setup is productive. | Add local-model stack fit scoring: model, serving layer, client behavior, context limits. |
| 4 | [continuedev/continue#10495](https://github.com/continuedev/continue/issues/10495) | Developer or company using local/self-hosted LLMs | If the model behavior or identity is unclear, users lose confidence in outputs and compliance assumptions. | Manually inspect prompts, model templates, and responses. | Trust and compliance are buying criteria when internal work or customer data is involved. | Bundle model identity and behavior verification into selection reports. |
| 5 | [cline/cline#10596](https://github.com/cline/cline/issues/10596) | AI coding power user or small engineering team using a gateway | Provider routing can silently multiply inference costs. | Monitor bills after the fact or avoid gateways. | Cost surprises create a clear willingness to pay for prevention and provider guidance. | Position cost-control review as a paid add-on for AI coding rollouts. |
| 6 | [cline/cline#9433](https://github.com/cline/cline/issues/9433) | Team using OpenAI-compatible providers in daily coding workflows | Missing usage metadata makes context and spend hard to manage. | Rely on rough estimates or external billing dashboards. | Finance and engineering need usage visibility before scaling from one user to a team. | Score providers on observability: usage fields, token accounting, billing transparency. |
| 7 | [cline/cline#9847](https://github.com/cline/cline/issues/9847) | Non-expert user choosing an AI coding assistant | Model selection is not enough; endpoint configuration blocks adoption. | Search docs, copy examples, or ask community forums. | The buyer is paying for a working outcome, not a model name. | Turn recommendations into practical setup playbooks for specific tools. |
| 8 | [langgenius/dify#37881](https://github.com/langgenius/dify/issues/37881) | SME or IT team deploying AI behind corporate network controls | Offline/proxied environments break plugins and dependencies, delaying deployment. | Ask IT to open network access or patch deployment manually. | Private deployment projects already imply implementation budget and risk ownership. | Sell private-deployment readiness checks for AI workflows. |
| 9 | [langgenius/dify#35772](https://github.com/langgenius/dify/issues/35772) | Organization running multiple AI apps or workflows | LLM spend cannot be attributed by app, team, or workflow. | Manual billing reconciliation or one shared provider account. | Cost allocation becomes necessary once AI usage spreads beyond a single experiment. | Add governance criteria: app-level tracking, chargeback, usage reporting. |
| 10 | [open-webui/open-webui#26222](https://github.com/open-webui/open-webui/issues/26222) | SME building private knowledge-base/RAG workflows | API success does not guarantee reliable knowledge-base behavior in production. | Manually retest RAG flows or switch platforms after failure. | Internal knowledge-base projects are tied to productivity and data-control budgets. | Offer RAG stack selection and deployment-risk review, not only model recommendations. |

### Investor interpretation

These cases show a repeatable commercial pattern:

1. **The buyer is not buying a benchmark.** They are buying a working AI workflow.
2. **The failure point is often integration, not model intelligence.** Provider, endpoint, client, context, billing, and deployment constraints decide success.
3. **The pain has budget logic.** The cost of failed setup, wrong routing, privacy risk, or unreliable RAG is higher than a lightweight selection review.
4. **The wedge starts with developers but expands to SMEs.** AI coding users expose the pain first; the same selection logic applies to knowledge base, support, document, and private deployment use cases.
5. **The defensible asset is a case library.** Every public issue, selection request, and anonymized outcome improves future recommendations.

### Commercial thesis

`llm-selector` can become the customer-side decision layer before LLM adoption:

```text
Model confusion → free selection report → endpoint/risk review → paid stack recommendation → PoC plan → implementation support
```

The business is not "selling model rankings." The business is reducing failed AI adoption decisions for small teams and SMEs.

## Interview log

| Date | Segment | Problem | Current workaround | Willingness to pay | Notes |
|------|---------|---------|--------------------|--------------------|-------|
| TBD | TBD | TBD | TBD | TBD | TBD |

## Selection request log

Use this table for direct `llm-selector` requests. Public GitHub research above should be used as market evidence, not counted as direct product requests.

| Date | Link | Segment | Scenario | Outcome |
|------|------|---------|----------|---------|
| TBD | TBD | TBD | TBD | TBD |

## Paid signal log

Track only non-sensitive summaries.

| Date | Segment | Paid for | Outcome | Follow-up |
|------|---------|----------|---------|-----------|
| TBD | TBD | TBD | TBD | TBD |

## What would invalidate the idea?

- Users can choose confidently without help.
- Users only want free advice and never request deeper review.
- Model choice is dominated by one vendor in the target segment.
- The pain is not frequent enough to support a business.
- Existing consultants or platforms solve the problem better for SMEs/OPCs.

## What would strengthen the idea?

- Repeated similar selection requests.
- Users sharing generated reports.
- Real companies asking for a PoC plan.
- Developers asking for AI coding stack recommendations.
- Gateway users asking for endpoint verification.
- Users returning with outcomes and cost data.
