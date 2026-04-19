"""Stage 3: Data analysis technical outline (demo)."""

from __future__ import annotations

from framework.context import RunContext


def run(ctx: RunContext) -> None:
    plan = {
        "data_sources_priority": [
            {"tier": 1, "name": "内置 API（AkShare / FRED / 官方统计等）", "note": "推荐优先"},
            {"tier": 2, "name": "用户上传 CSV/Excel", "note": "次优先"},
            {"tier": 3, "name": "临时爬虫", "note": "兜底，需风险提示"},
        ],
        "methods": ["描述统计", "可视化", "（可选）回归/时间序列 — 生产接入计量模板"],
        "expected_outputs": ["summary.json", "figures/*.png"],
        "topic": ctx.topic,
    }
    ctx.data["analysis_plan"] = plan
    ctx.write_json("03_analysis_plan.json", plan)
    ctx.write_text(
        "03_analysis_plan.md",
        "# 数据分析技术大纲（占位）\n\n"
        "## 数据采集路径（优先级）\n\n"
        + "\n".join(f"{x['tier']}. **{x['name']}** — {x['note']}" for x in plan["data_sources_priority"])
        + "\n\n## 方法\n\n"
        + "\n".join(f"- {m}" for m in plan["methods"])
        + "\n",
    )
