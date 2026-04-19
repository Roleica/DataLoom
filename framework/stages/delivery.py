"""Stage 6: Packaging (demo: master README + optional zip)."""

from __future__ import annotations

import zipfile

from framework.context import RunContext


def run(ctx: RunContext) -> None:
    master = ctx.run_dir / "README_DELIVERY.md"
    master.write_text(
        "# 交付包说明（总控 README）\n\n"
        f"- **run_id**: `{ctx.run_id}`\n"
        f"- **topic**: {ctx.topic}\n\n"
        "## 目录约定\n\n"
        "- `01_prd.*` — 需求\n"
        "- `02_outline.*` — 大纲\n"
        "- `03_analysis_plan.*` — 数据分析技术大纲\n"
        "- `04_*` — 执行产物\n"
        "- `05_*` / `draft/` — 正文\n"
        "- `references/` — 资料\n\n"
        "生产环境：在此生成 Word/PDF，并打包代码、数据与过程文档。\n",
        encoding="utf-8",
    )

    zip_path = ctx.run_dir / f"{ctx.run_id}_bundle.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(ctx.run_dir.rglob("*")):
            if p.is_file() and p != zip_path:
                zf.write(p, arcname=str(p.relative_to(ctx.run_dir)))
    ctx.data["delivery"] = {"zip": str(zip_path.name)}
    ctx.write_json("06_delivery.json", {"readme": str(master.name), "zip": zip_path.name})
