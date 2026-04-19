"""Stage 5: Interpretation & drafting (demo)."""

from __future__ import annotations

from framework.context import RunContext


def run(ctx: RunContext) -> None:
    chapters = ctx.run_dir / "draft" / "chapters"
    chapters.mkdir(parents=True, exist_ok=True)
    body = (
        f"## 示例章节\n\n研究主题：**{ctx.topic}**\n\n"
        "（占位正文）生产环境：在此写入分章节生成内容，并嵌入图表引用。\n"
    )
    (chapters / "01_intro.md").write_text(body, encoding="utf-8")
    ctx.write_text("05_full_draft.md", "# 研报正文汇编（占位）\n\n" + body)
    ctx.data["drafting"] = {"chapters": ["draft/chapters/01_intro.md"]}
