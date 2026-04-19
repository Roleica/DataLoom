#!/usr/bin/env python3
"""DataLoom CLI: run the six-stage demo pipeline (no third-party deps)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow `python run_demo.py` from repo root without installing the package
_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from framework.pipeline import ResearchPipeline  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="DataLoom: six-stage research pipeline demo (mock stages).")
    p.add_argument("--topic", default="中国经济发展对中国工业外贸发展的影响研究", help="研究主题")
    p.add_argument("--auto", action="store_true", help="标记为自动确认（影响占位 PRD 状态字段）")
    p.add_argument("--run-id", default=None, help="固定 run 目录名（默认 UTC 时间戳）")
    args = p.parse_args()

    pipeline = ResearchPipeline(workspace=_ROOT)
    ctx = pipeline.run(args.topic, auto_confirm=args.auto, run_id=args.run_id)
    print(f"Done. Artifacts: {ctx.run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
