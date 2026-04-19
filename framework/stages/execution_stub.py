"""Stage 4: Code gen + execution (demo: no arbitrary code execution)."""

from __future__ import annotations

from textwrap import dedent

from framework.context import RunContext


def run(ctx: RunContext) -> None:
    code_dir = ctx.run_dir / "code"
    code_dir.mkdir(parents=True, exist_ok=True)
    stub_py = code_dir / "analysis_stub.py"
    stub_py.write_text(
        dedent(
            '''
            """AUTO-GENERATED STUB — replace with real codegen + sandboxed run."""


            def main():
                print("Demo: run AkShare/clean/plot in an isolated sandbox in production.")


            if __name__ == "__main__":
                main()
            '''
        ).strip()
        + "\n",
        encoding="utf-8",
    )

    results = {
        "note": "Demo 未执行模型生成代码；生产需 Docker/Firecracker 等沙箱。",
        "artifacts": [str(stub_py.relative_to(ctx.run_dir))],
    }
    ctx.data["execution"] = results
    ctx.write_json("04_execution_results.json", results)
    ctx.write_text(
        "04_execution_report.md",
        "# 数据分析执行报告（占位）\n\n"
        "- 图表、指标与解读应在沙箱跑通后写入此目录。\n",
    )
