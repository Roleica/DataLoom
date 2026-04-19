"""Stage 1: Requirements capture & PRD (demo: template only, no LLM)."""

from __future__ import annotations

from framework.context import RunContext


def run(ctx: RunContext) -> None:
    prd = {
        "topic": ctx.topic,
        "variables": ["待与用户/模型多轮澄清"],
        "time_range": "待定",
        "audience": "研究读者",
        "depth": "标准",
        "status": "auto_confirmed" if ctx.auto_confirm else "draft",
    }
    ctx.data["prd"] = prd
    ctx.write_json("01_prd.json", prd)
    ctx.write_text(
        "01_prd.md",
        f"# 研究需求文档（PRD）\n\n**主题：** {ctx.topic}\n\n"
        "## 结构化摘要\n\n"
        "本文件由框架 demo 生成：生产环境应在此接入多轮对话与 LLM，"
        "产出经用户确认的版本。\n",
    )
