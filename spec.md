# llm-selector v0.1 — SME LLM Selection Advisor

## 目标
帮助中小企业根据业务场景、预算、数据敏感性、部署偏好和工具链，快速得到可执行的大模型选型建议。

## 变更范围
- 做什么
  - 提供一个开源 CLI 问卷，生成初步选型报告
  - 覆盖 AI Coding、知识库、客服、文档总结、翻译、数据分析、办公自动化等典型场景
  - 给出模型候选、接入建议、风险提醒和下一步 PoC 建议
  - 与 verify-glm 形成组合：选择 GLM-5.2 后提示验证 endpoint
- 不做什么
  - 不做通用 benchmark 平台
  - 不声称模型排名绝对准确
  - 不采集用户数据
  - 不包含 API key、供应商私有价格或敏感配置

## 场景描述
中小企业负责人或技术负责人想引入大模型，但不确定该选 GLM、Qwen、DeepSeek、Kimi、Claude、GPT 还是本地模型。工具通过问卷输出一份可读报告，降低决策成本。

## 验收标准
- CLI 能在 Python 3.8+ 无依赖运行
- README 清楚表达：Choose the right LLM, then verify you're actually using it
- 至少包含 7 个场景和 7 个模型/模型家族
- 能输出 Markdown 报告
- 安全审计无 CRITICAL/WARNING

## 技术约束
- Python 标准库，无第三方依赖
- 数据文件使用 JSON，便于未来扩展
- 不包含真实客户信息、密钥、内部地址
