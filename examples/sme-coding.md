# Example: SME AI Coding + Document Summary

This example represents a small engineering/service company that wants:

- AI coding assistance
- document/contract summarization
- internal business data only
- medium PoC budget
- domestic provider preference

Run:

```bash
python selector.py \
  --scenario ai_coding \
  --scenario document_summary \
  --sensitivity internal \
  --budget medium \
  --deployment domestic \
  --output examples/sme-coding-report.md
```

Expected top candidates:

- GLM-5.2
- Qwen
- Kimi / DeepSeek depending on scoring updates

Recommended next step:

- If GLM-5.2 is selected through a gateway, run verify-glm before trusting the setup.
