# DataLoom

**A safe-by-default research automation framework for macro, finance, and quantitative workflows.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Pipeline](https://img.shields.io/badge/Pipeline-6%20Stages-1f6feb)](#pipeline-design)
[![Execution](https://img.shields.io/badge/Execution-Safe--by--default-orange)](#safe-by-default)

## Language / 语言

- [English](#english)
- [中文](#中文)

---

## English

## Overview

DataLoom is a runnable research pipeline skeleton for macro, finance, and
quantitative analysis workflows. It turns a research topic into a structured set
of artifacts: requirements, research outline, technical analysis plan, execution
stub, draft report, and delivery bundle.

The project is designed as a foundation for building agentic research systems.
It does not call LLMs or execute generated code by default, which makes it safe
for demos, experiments, and architecture prototyping.

The name reflects the product idea: weaving scattered data, assumptions,
analysis steps, and written interpretation into a reproducible research package.

## What It Does

| Capability | Description |
| --- | --- |
| Requirements capture | Generates a PRD-style research brief for the requested topic. |
| Research structuring | Produces an outline and reference folder convention for downstream research. |
| Analysis planning | Defines prioritized data sources, methods, and expected analytical outputs. |
| Safe execution hook | Creates an execution stub instead of running arbitrary generated code by default. |
| Draft generation | Builds a report draft structure with chapter-level artifacts. |
| Packaged delivery | Produces a run-level delivery README and ZIP bundle. |
| Reproducible artifacts | Writes every run into a stable `runs/<run_id>/` folder layout. |

## Why It Matters

Research automation is rarely just a single model call. A useful workflow needs
requirements clarification, source tracking, analysis planning, controlled code
execution, interpretation, and final packaging. DataLoom provides that workflow
shape in a small, inspectable Python codebase.

For portfolio and engineering purposes, the project demonstrates how to design a
multi-stage research system with clear artifact boundaries, auditability, and
safe defaults before integrating real LLM, API, and sandbox services.

## Pipeline Design

```text
Research topic
      |
      v
01 Requirements / PRD
      |
      v
02 Research outline and references
      |
      v
03 Data analysis plan
      |
      v
04 Sandboxed execution hook
      |
      v
05 Drafting and interpretation
      |
      v
06 Packaged delivery
```

## Generated Artifacts

A demo run writes files under `runs/<run_id>/`:

```text
runs/<run_id>/
├── 01_prd.json
├── 01_prd.md
├── 02_outline.json
├── 02_outline.md
├── 03_analysis_plan.json
├── 03_analysis_plan.md
├── 04_execution_results.json
├── 04_execution_report.md
├── 05_full_draft.md
├── 06_delivery.json
├── README_DELIVERY.md
├── code/
│   └── analysis_stub.py
├── draft/
│   └── chapters/
├── references/
│   └── stage2/
└── <run_id>_bundle.zip
```

## Architecture

| Layer | Role |
| --- | --- |
| `run_demo.py` | CLI entry point for running the demo pipeline. |
| `framework/context.py` | Shared run state, artifact path management, JSON/text writers. |
| `framework/pipeline.py` | Serial orchestration of the six research stages. |
| `framework/stages/requirements.py` | Stage 1: research requirement and PRD artifact. |
| `framework/stages/research_outline.py` | Stage 2: outline and reference directory convention. |
| `framework/stages/analysis_plan.py` | Stage 3: data source and method planning. |
| `framework/stages/execution_stub.py` | Stage 4: safe execution placeholder for future sandbox integration. |
| `framework/stages/drafting.py` | Stage 5: draft report structure. |
| `framework/stages/delivery.py` | Stage 6: delivery README and ZIP packaging. |

## Safe by Default

DataLoom intentionally avoids unsafe behavior in the default demo:

- It does not call external LLM APIs.
- It does not execute model-generated code.
- It does not access private data sources.
- It writes generated outputs to `runs/`, which is ignored by git.

Production integrations can be added through explicit adapters for models, data
APIs, retrieval tools, and sandboxed execution services.

## Quick Start

```bash
git clone https://github.com/Roleica/DataLoom.git
cd DataLoom
python3 run_demo.py --topic "Your research topic"
```

Use a fixed run folder for repeatable demos:

```bash
python3 run_demo.py --topic "demo" --run-id demo-run-1 --auto
```

The project uses only Python standard library modules for the core demo.
Optional integrations are listed in `requirements.txt` as comments.

## Customization

Replace each `framework/stages/*.py` `run()` function with real integrations:

| Extension point | Example integration |
| --- | --- |
| Requirements | LLM-driven requirement clarification, web UI, or chat interface. |
| Retrieval | AkShare, FRED, official statistics APIs, uploaded Excel/CSV files. |
| Execution | Docker, Firecracker, or another restricted Python sandbox. |
| Drafting | LLM report drafting, chart insertion, Word/PDF export. |
| Delivery | Report bundle, data appendix, source citation package, audit log. |

## Roadmap

1. Model and data adapter layer with environment-based secrets.
2. Human-in-the-loop checkpoints between stages.
3. Sandboxed execution service with allowlisted imports, timeouts, and restricted networking.
4. Structured citation and source audit module.
5. Word/PDF export for final research delivery.

## Repository Scope

This repository is a runnable framework skeleton. It contains no private data,
API keys, proprietary model prompts, generated research outputs, or confidential
analysis materials.

## License

MIT

---

## 中文

## 项目概览

DataLoom 是一套面向宏观、金融和量化研究场景的研究自动化流水线框架。

它可以把一个研究主题转化为一组结构化产物：研究需求文档、研究大纲、数据分析技术
计划、执行占位、报告草稿和交付包。

这个项目更像一个 agentic research system 的底层骨架。默认版本不会调用大模型，也不会
执行模型生成代码，因此适合用于 demo、实验和架构原型展示。

项目名 DataLoom 的含义是：把分散的数据、假设、分析步骤和文字解读编织成一份可复现
的研究交付包。

## 项目能力

| 能力 | 说明 |
| --- | --- |
| 需求捕获 | 根据研究主题生成 PRD 风格的研究需求文档。 |
| 研究结构化 | 生成研究大纲，并建立参考资料目录约定。 |
| 分析规划 | 定义数据源优先级、分析方法和预期输出。 |
| 安全执行入口 | 默认只生成执行占位，不直接运行任意生成代码。 |
| 报告草稿 | 生成报告正文和章节级草稿结构。 |
| 交付打包 | 生成交付 README 和 ZIP 包。 |
| 可复现产物 | 每次运行都写入稳定的 `runs/<run_id>/` 目录。 |

## 项目价值

研究自动化通常不是一次简单的大模型调用。一个真正可用的研究流程需要需求澄清、资料
追踪、分析规划、受控代码执行、结果解读和最终打包交付。

DataLoom 用一个小而清晰的 Python 项目展示了这种工作流形态：阶段边界明确、产物可追溯、
默认行为安全，并为后续接入真实 LLM、数据 API 和沙箱执行服务预留接口。

## 流水线设计

```text
研究主题
      |
      v
01 需求文档 / PRD
      |
      v
02 研究大纲与参考资料
      |
      v
03 数据分析技术计划
      |
      v
04 沙箱执行入口
      |
      v
05 报告草稿与解读
      |
      v
06 交付包
```

## 生成产物

一次 demo 运行会在 `runs/<run_id>/` 下生成：

```text
runs/<run_id>/
├── 01_prd.json
├── 01_prd.md
├── 02_outline.json
├── 02_outline.md
├── 03_analysis_plan.json
├── 03_analysis_plan.md
├── 04_execution_results.json
├── 04_execution_report.md
├── 05_full_draft.md
├── 06_delivery.json
├── README_DELIVERY.md
├── code/
│   └── analysis_stub.py
├── draft/
│   └── chapters/
├── references/
│   └── stage2/
└── <run_id>_bundle.zip
```

## 技术架构

| 层级 | 作用 |
| --- | --- |
| `run_demo.py` | 命令行入口，用于运行 demo 流水线。 |
| `framework/context.py` | 管理单次运行状态、产物路径、JSON 和文本写入。 |
| `framework/pipeline.py` | 串行编排六个研究阶段。 |
| `framework/stages/requirements.py` | 阶段 1：研究需求和 PRD 产物。 |
| `framework/stages/research_outline.py` | 阶段 2：研究大纲和参考资料目录约定。 |
| `framework/stages/analysis_plan.py` | 阶段 3：数据源和方法计划。 |
| `framework/stages/execution_stub.py` | 阶段 4：安全执行占位，后续可接入沙箱。 |
| `framework/stages/drafting.py` | 阶段 5：报告草稿结构。 |
| `framework/stages/delivery.py` | 阶段 6：交付 README 和 ZIP 打包。 |

## 默认安全

DataLoom 的默认 demo 刻意避免高风险行为：

- 不调用外部大模型 API。
- 不执行模型生成代码。
- 不访问私有数据源。
- 生成结果写入 `runs/`，该目录已被 git 忽略。

生产环境可以通过显式 adapter 接入模型、数据 API、检索工具和沙箱执行服务。

## 快速开始

```bash
git clone https://github.com/Roleica/DataLoom.git
cd DataLoom
python3 run_demo.py --topic "你的研究主题"
```

使用固定 run 目录，便于重复 demo：

```bash
python3 run_demo.py --topic "demo" --run-id demo-run-1 --auto
```

核心 demo 只依赖 Python 标准库。可选扩展依赖以注释形式列在 `requirements.txt` 中。

## 自定义

可以替换每个 `framework/stages/*.py` 中的 `run()` 函数，接入真实能力：

| 扩展点 | 示例 |
| --- | --- |
| 需求澄清 | 大模型多轮澄清、Web UI 或对话入口。 |
| 数据检索 | AkShare、FRED、官方统计 API、用户上传 Excel/CSV。 |
| 执行环境 | Docker、Firecracker 或其他受限 Python 沙箱。 |
| 报告生成 | 大模型撰写、图表插入、Word/PDF 导出。 |
| 交付打包 | 报告包、数据附录、来源引用包、审计日志。 |

## 路线图

1. 基于环境变量管理密钥的模型和数据 adapter 层。
2. 阶段间人工确认检查点。
3. 带 allowlist、超时和网络限制的沙箱执行服务。
4. 结构化引用和来源审计模块。
5. 面向最终研究交付的 Word/PDF 导出。

## 仓库范围

当前仓库是可运行的框架骨架，不包含私有数据、API Key、专有提示词、生成的研究报告或
任何保密分析材料。

## 开源协议

MIT
