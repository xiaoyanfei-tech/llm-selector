#!/usr/bin/env python3
"""llm-selector — SME-focused LLM selection advisor.

A small zero-dependency CLI that asks practical business questions and writes a
Markdown recommendation report. It is not a benchmark; it is a decision helper.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent

SENSITIVITY_BOOSTS = {
    "public": {},
    "internal": {"qwen": 1, "local-open-source": 1},
    "customer": {"local-open-source": 3, "qwen": 1, "deepseek": 1},
    "regulated": {"local-open-source": 5, "qwen": 1},
}

BUDGET_BOOSTS = {
    "low": {"deepseek": 2, "qwen": 1, "local-open-source": 1},
    "medium": {"glm-5.2": 1, "qwen": 1, "deepseek": 1},
    "high": {"claude": 1, "gpt": 1, "glm-5.2": 1},
}

DEPLOYMENT_BOOSTS = {
    "api": {"glm-5.2": 1, "deepseek": 1, "qwen": 1, "kimi": 1, "gpt": 1, "claude": 1},
    "domestic": {"glm-5.2": 2, "qwen": 2, "deepseek": 2, "kimi": 1},
    "private": {"local-open-source": 4, "qwen": 2},
    "hybrid": {"local-open-source": 2, "qwen": 1, "glm-5.2": 1, "deepseek": 1},
}


def load_json(name: str) -> dict[str, Any]:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def ask_choice(title: str, options: list[tuple[str, str]], default: str) -> str:
    print(f"\n{title}")
    for idx, (_, label) in enumerate(options, 1):
        print(f"  {idx}. {label}")
    raw = input(f"Choose [default {default}]: ").strip()
    if not raw:
        return default
    try:
        idx = int(raw)
        if 1 <= idx <= len(options):
            return options[idx - 1][0]
    except ValueError:
        pass
    keys = {key for key, _ in options}
    return raw if raw in keys else default


def ask_multi(title: str, options: list[tuple[str, str]], default: list[str]) -> list[str]:
    print(f"\n{title}")
    for idx, (_, label) in enumerate(options, 1):
        print(f"  {idx}. {label}")
    raw = input("Choose one or more, comma-separated [default 1]: ").strip()
    if not raw:
        return default
    selected: list[str] = []
    by_index = {str(i): key for i, (key, _) in enumerate(options, 1)}
    keys = {key for key, _ in options}
    for part in raw.replace("，", ",").split(","):
        item = part.strip()
        if item in by_index:
            selected.append(by_index[item])
        elif item in keys:
            selected.append(item)
    return selected or default


def score_models(
    scenarios: list[str], sensitivity: str, budget: str, deployment: str,
    scenario_data: dict[str, Any], models: dict[str, Any]
) -> dict[str, int]:
    scores = {name: 0 for name in models}
    for scenario in scenarios:
        for model, points in scenario_data[scenario]["weights"].items():
            scores[model] += points
    for boosts in (SENSITIVITY_BOOSTS[sensitivity], BUDGET_BOOSTS[budget], DEPLOYMENT_BOOSTS[deployment]):
        for model, points in boosts.items():
            scores[model] += points
    return scores


def build_report(
    scenarios: list[str], sensitivity: str, budget: str, deployment: str,
    scores: dict[str, int], models: dict[str, Any], scenario_data: dict[str, Any]
) -> str:
    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    top = ranked[:3]

    labels = {
        "public": "Public or low-sensitivity data",
        "internal": "Internal business data",
        "customer": "Customer / contract / operational data",
        "regulated": "Regulated or highly sensitive data",
        "low": "Low / cost-sensitive",
        "medium": "Medium / controlled PoC budget",
        "high": "High / quality-first budget",
        "api": "Hosted API first",
        "domestic": "Domestic providers preferred",
        "private": "Private or local deployment preferred",
        "hybrid": "Hybrid deployment",
    }

    lines = [
        "# SME LLM Selection Report",
        "",
        "> Choose the right LLM, then verify you're actually using it.",
        "",
        "## Inputs",
        "",
        f"- Scenarios: {', '.join(scenario_data[s]['display'] for s in scenarios)}",
        f"- Data sensitivity: {labels[sensitivity]}",
        f"- Budget: {labels[budget]}",
        f"- Deployment preference: {labels[deployment]}",
        "",
        "## Recommended shortlist",
        "",
    ]

    for idx, (model_key, score) in enumerate(top, 1):
        model = models[model_key]
        lines.extend([
            f"### {idx}. {model['display']} — score {score}",
            "",
            f"Provider/ecosystem: {model['provider']}",
            "",
            "Why it fits:",
            *[f"- {item}" for item in model["strengths"]],
            "",
            "Risks to review:",
            *[f"- {item}" for item in model["risks"]],
            "",
            f"Verification: {model['verification']}",
            "",
        ])

    lines.extend([
        "## Scenario notes",
        "",
    ])
    seen_notes: list[str] = []
    for scenario in scenarios:
        for note in scenario_data[scenario]["notes"]:
            if note not in seen_notes:
                seen_notes.append(note)
                lines.append(f"- {note}")

    lines.extend([
        "",
        "## Suggested next steps",
        "",
        "1. Pick the top 1-2 models and run a small PoC with real but non-sensitive samples.",
        "2. Measure quality, latency, monthly cost, data handling, and user adoption.",
        "3. If using a third-party LLM gateway, verify that the routed model is actually the claimed model.",
        "4. If GLM-5.2 is selected for Claude Code or an LLM gateway, run verify-glm: https://github.com/xiaoyanfei-tech/verify-glm",
        "5. For sensitive data, prefer private deployment, hybrid routing, or strict data-redaction workflows.",
        "",
        "## Important note",
        "",
        "This report is a practical selection aid, not a universal benchmark. Final decisions should be validated with your own tasks, data policy, and cost profile.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

    parser = argparse.ArgumentParser(description="SME LLM selection advisor")
    parser.add_argument("--scenario", action="append", help="Scenario key; can be repeated")
    parser.add_argument("--sensitivity", choices=list(SENSITIVITY_BOOSTS), default=None)
    parser.add_argument("--budget", choices=list(BUDGET_BOOSTS), default=None)
    parser.add_argument("--deployment", choices=list(DEPLOYMENT_BOOSTS), default=None)
    parser.add_argument("--output", default="llm-selection-report.md", help="Markdown report output path")
    parser.add_argument("--json", action="store_true", help="Print machine-readable recommendation JSON")
    args = parser.parse_args()

    models = load_json("models.json")
    scenario_data = load_json("scenarios.json")

    scenario_options = [(key, value["display"]) for key, value in scenario_data.items()]
    scenarios = args.scenario or ask_multi("Primary business scenarios", scenario_options, ["ai_coding"])
    scenarios = [s for s in scenarios if s in scenario_data] or ["ai_coding"]

    sensitivity = args.sensitivity or ask_choice("Data sensitivity", [
        ("public", "Public / low sensitivity"),
        ("internal", "Internal business data"),
        ("customer", "Customer / contract / operational data"),
        ("regulated", "Regulated or highly sensitive data"),
    ], "internal")

    budget = args.budget or ask_choice("Budget preference", [
        ("low", "Cost-sensitive"),
        ("medium", "Controlled PoC budget"),
        ("high", "Quality-first"),
    ], "medium")

    deployment = args.deployment or ask_choice("Deployment preference", [
        ("api", "Hosted API first"),
        ("domestic", "Domestic providers preferred"),
        ("private", "Private/local deployment preferred"),
        ("hybrid", "Hybrid"),
    ], "domestic")

    scores = score_models(scenarios, sensitivity, budget, deployment, scenario_data, models)
    report = build_report(scenarios, sensitivity, budget, deployment, scores, models, scenario_data)
    output = Path(args.output)
    output.write_text(report, encoding="utf-8")

    if args.json:
        ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        print(json.dumps({"scores": scores, "top": ranked[:3], "report": str(output)}, ensure_ascii=False, indent=2))
    else:
        print(f"Wrote {output}")
        print("Top recommendations:")
        for model, score in sorted(scores.items(), key=lambda item: item[1], reverse=True)[:3]:
            print(f"- {models[model]['display']} ({score})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
