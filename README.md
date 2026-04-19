# Intelligent Data Analysis & Automated Reporting — Framework Demo

中文需求见仓库内 [`核心需求v1.md`](./核心需求v1.md)。**第一次上传 GitHub** 请看 [`首次上传GitHub指南.md`](./首次上传GitHub指南.md)。本目录是一个**可运行的六阶段流水线骨架**：演示目录约定、产物文件与打包流程；**默认不接 LLM、不执行任意生成代码**（安全起见），便于作为整体架构起点。

## 能力评判（Agent / 本框架各自能做什么）

| 需求模块 | 单靠「对话里的 Agent」 | 工程化产品（本 demo 指向的方向） |
|----------|-------------------------|-----------------------------------|
| 多轮澄清 + 结构化 PRD | 可以辅助起草，但需持久化与会话状态 | 需后端/DB + 审批 UI |
| 深度检索 + 文献下载 + README | 可部分代劳，质量依赖检索 API 与版权 | 需接入搜索/学术 API、存储与去重 |
| 内置 API 推荐（AkShare 等） | 可写示例代码与说明 | 需版本锁定、失败重试、合规说明 |
| 自动生成并**执行**分析代码 | 在 Cursor 里可迭代，但**不适合**在无沙箱服务器上盲跑 | **必须**隔离执行（容器/沙箱）、资源与网络策略 |
| 长文分章撰写 + 二次检索 | 模型可做，需分块与引用规范 | 需 RAG/引用校验与人工复核流程 |
| Word/PDF 排版 + ZIP 交付 | 可生成脚本思路 | 需模板、`python-docx`/LaTeX、字体与样式规范 |

结论：**需求文档描述的是一套完整产品**；当前仓库的 Agent 能很好完成「编排设计、代码草稿、单步调试」，但**全流程无人值守**需要本 README 中表格右侧那一列的工程能力。本 demo 把「阶段边界 + 产物路径」先固定下来，便于你逐步替换每一格为真实实现。

## 运行

```bash
cd "/path/to/数据分析自动化项目"
python3 run_demo.py --topic "你的研究主题"
# 可选：固定一次运行的目录名
python3 run_demo.py --topic "demo" --run-id demo-run-1 --auto
```

输出在 `runs/<run_id>/`，含 JSON/Markdown 占位、`references/`、`code/`、`draft/` 以及 `*_bundle.zip`。

## 目录结构

```
.
├── README.md
├── 核心需求v1.md
├── requirements.txt      # 目前无强制依赖；可选库见注释
├── run_demo.py
└── framework/
    ├── context.py        # RunContext：run 目录与写文件
    ├── pipeline.py       # 六阶段串行编排
    └── stages/           # 各阶段占位实现，可替换为 LLM/工具调用
```

## 下一步（往 GitHub 产品化）

1. 为每个 `stages/*.py` 的 `run()` 增加「调用 LLM / 检索 / 工具」的适配层，密钥走环境变量。
2. 用状态机或工作流引擎（Temporal、LangGraph 等）替换简单串行，支持**回溯与人工审批节点**。
3. 阶段四单独服务：仅接受白名单 import、超时、只读网络或代理后的数据 API。

## License

MIT — 见 [`LICENSE`](./LICENSE)。
