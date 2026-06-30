# Methodology

`llm-selector` is not a benchmark leaderboard. It is a practical decision framework for choosing an LLM stack with limited time, limited budget, and real operational constraints.

## Core principle

> Choose the right LLM for the business job, then verify you are actually using it.

The goal is not to find a universal "best model". The goal is to reduce decision risk for a specific user, scenario, budget, and data policy.

## Financial leverage view

For SMEs and OPCs, AI adoption should work like intelligent leverage:

- small upfront experiment
- clear downside control
- measurable productivity upside
- fast feedback loop
- no large vendor lock-in before evidence

This project intentionally lowers the first step:

1. free selection report from the CLI
2. low-friction issue template for context
3. small PoC before large spend
4. verification before trust
5. expand only after measurable ROI

## Scoring dimensions

The current scoring is a transparent heuristic based on:

- business scenario fit
- data sensitivity
- deployment preference
- budget profile
- AI coding/tooling compatibility
- long-context needs
- private deployment needs
- endpoint verification risk

The score is not a universal model ranking. It is a fit score for a decision context.

## Why scenario fit comes first

Different users need different models:

- AI coding needs tool compatibility, latency, coding ability, and long-context reliability
- knowledge bases need retrieval quality, Chinese document handling, and data governance
- document-heavy workflows need long-context reading and summarization
- sensitive-data workflows may need private or hybrid deployment
- OPC users need cost control, low setup burden, and daily productivity ROI

## Why verification is part of selection

Choosing a model is not enough. If a team uses a third-party gateway, it must verify that the routed model is actually the claimed model.

For GLM-5.2, this project links to `verify-glm` for tokenizer fingerprinting, reasoning-token metadata, and optional long-context probing.

## Update policy

Model markets move quickly. The data files should be updated when:

- model capability changes materially
- pricing or access changes
- a new model becomes relevant for SMEs/OPCs
- real customer PoC results reveal a better fit
- gateway behavior introduces new verification risk

## What this does not claim

- It does not prove one model is universally best.
- It does not replace a real PoC.
- It does not replace legal/compliance review.
- It does not guarantee model identity through cryptographic proof.

It provides a structured first decision, then points to verification and PoC steps.
