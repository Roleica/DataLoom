from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class RunContext:
    """Shared state for one pipeline execution."""

    run_id: str
    topic: str
    root: Path
    auto_confirm: bool = False
    data: dict[str, Any] = field(default_factory=dict)

    @property
    def run_dir(self) -> Path:
        return self.root / "runs" / self.run_id

    def artifact_path(self, name: str) -> Path:
        return self.run_dir / name

    def write_json(self, name: str, payload: dict[str, Any]) -> Path:
        path = self.artifact_path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        import json

        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def write_text(self, name: str, content: str) -> Path:
        path = self.artifact_path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path


def utc_run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
