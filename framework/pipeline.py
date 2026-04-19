from __future__ import annotations

from pathlib import Path

from framework.context import RunContext, utc_run_id
from framework.stages import analysis_plan, delivery, drafting, execution_stub, requirements, research_outline


class ResearchPipeline:
    """Serial pipeline with optional auto-confirm (demo: no real LLM calls)."""

    def __init__(self, workspace: Path | None = None) -> None:
        self.workspace = (workspace or Path(__file__).resolve().parent.parent).resolve()

    def run(self, topic: str, *, auto_confirm: bool = False, run_id: str | None = None) -> RunContext:
        rid = run_id or utc_run_id()
        ctx = RunContext(run_id=rid, topic=topic.strip(), root=self.workspace, auto_confirm=auto_confirm)
        ctx.run_dir.mkdir(parents=True, exist_ok=True)

        requirements.run(ctx)
        research_outline.run(ctx)
        analysis_plan.run(ctx)
        execution_stub.run(ctx)
        drafting.run(ctx)
        delivery.run(ctx)
        return ctx
