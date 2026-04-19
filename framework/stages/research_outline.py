"""Stage 2: Deep research & outline (demo: folder scaffold + placeholder README)."""

from __future__ import annotations

from framework.context import RunContext


def run(ctx: RunContext) -> None:
    refs = ctx.run_dir / "references" / "stage2"
    refs.mkdir(parents=True, exist_ok=True)
    (refs / "README.md").write_text(
        "# 参考资料（占位）\n\n"
        "生产环境：在此落地检索结果文件，并写入来源与摘要。\n",
        encoding="utf-8",
    )

    outline = {
        "sections": [
            {"title": "引言与问题提出", "goal": "界定研究问题"},
            {"title": "文献与机制综述", "goal": "理论框架"},
            {"title": "数据与实证设计", "goal": "变量、样本、模型"},
            {"title": "实证结果", "goal": "图表与检验"},
            {"title": "结论与政策含义", "goal": "归纳与建议"},
        ],
        "topic": ctx.topic,
    }
    ctx.data["outline"] = outline
    ctx.write_json("02_outline.json", outline)
    ctx.write_text(
        "02_outline.md",
        "# 报告整体大纲（占位）\n\n"
        + "\n".join(f"- **{s['title']}**：{s['goal']}" for s in outline["sections"])
        + "\n",
    )
