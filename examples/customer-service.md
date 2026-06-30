# Example: Customer Service Chatbot

## User

An SME wants to use an LLM chatbot for first-line customer service.

Constraints:

- customer-facing answers must be controlled
- needs escalation to humans
- customer data may be sensitive
- cost must be predictable

## Suggested path

1. Do not start with a fully autonomous chatbot.
2. Start with internal answer drafting or agent-assist.
3. Compare Qwen, GPT-family, DeepSeek, and local/hybrid options.
4. Add human escalation and logging policy before external launch.

## Why this is a leverage play

Customer service AI can reduce repetitive workload, but wrong answers have direct business risk. The best first step is usually agent-assist, not full automation.

## Command

```bash
python selector.py \
  --scenario customer_service \
  --sensitivity customer \
  --budget medium \
  --deployment hybrid \
  --output examples/customer-service-report.md
```
