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
