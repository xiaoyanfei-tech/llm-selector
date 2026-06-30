# llm-selector 中文说明

> 先帮企业和个人选对大模型，再验证它真的接对了。

`llm-selector` 是一个面向中小企业、OPC（一人公司）、独立开发者和个人高频 AI 用户的大模型选型助手。

它不是又一个 benchmark 排行榜，而是从真实业务场景出发，结合预算、数据敏感性、部署偏好和工具链，生成一份可执行的大模型选型建议。

## 适合谁？

- 中小企业老板 / IT 负责人
- OPC / 一人公司 / solo founder
- freelancer / 独立顾问
- 正在选择 Claude Code / Cursor / Cline 的个人开发者
- 帮公司落地 AI 工具的工程师
- 想比较 GLM、Qwen、DeepSeek、Kimi、Claude、GPT、本地模型的人

## 解决什么问题？

很多用户不缺模型新闻，缺的是决策：

- 我应该用 GLM、Qwen、DeepSeek、Kimi、Claude、GPT 还是本地模型？
- 我应该用 API、国内供应商、混合部署，还是私有化？
- 我的数据能不能发给外部模型？
- 我用 Claude Code / Cursor 应该配哪个模型？
- 如果网关声称是 GLM-5.2，怎么验证它真的没换模型？
- 第一个 PoC 应该怎么做？

`llm-selector` 的目标是降低第一步决策成本。

## 使用方法

```bash
git clone https://github.com/xiaoyanfei-tech/llm-selector.git
cd llm-selector
python selector.py
```

非交互示例：

```bash
python selector.py \
  --scenario ai_coding \
  --scenario document_summary \
  --sensitivity internal \
  --budget medium \
  --deployment domestic \
  --output report.md
```

## 输出内容

生成的报告包含：

- 推荐模型 shortlist
- 为什么适合
- 主要风险
- endpoint 验证建议
- PoC 下一步
- 如果需要进一步商业建议，如何提交需求

## 商业化但低门槛

我们不希望用高价格吓跑早期用户。这个项目的策略是：

1. 免费 CLI 先给出初步建议
2. 用户通过 issue 提交场景
3. 从小服务开始：个人/OPC 选型、选型 memo、AI Coding 栈建议
4. 只有在有明确 ROI 的情况下，才推进 PoC 或更深入服务

## 可提供的帮助

- OPC / 个人 AI 工具栈选型
- 中小企业大模型选型报告
- AI Coding Stack Recommendation
- Endpoint Verification Report
- 2-4 周 PoC 计划

## 和 verify-glm 的关系

`llm-selector` 帮你选模型方向。

`verify-glm` 帮你验证 GLM-5.2 endpoint 是否真的像 GLM-5.2。

组合路径：

```text
选对模型 → 验证接入真实 → 小规模 PoC → 决定是否扩大投入
```

## 提交需求

打开 GitHub issue：

https://github.com/xiaoyanfei-tech/llm-selector/issues/new/choose

请不要在公开 issue 中提交 API key、私有 URL、客户数据、合同、内部 IP 或保密截图。
