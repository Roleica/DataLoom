# DataLoom

**Weaving data into insights** — a multi-agent style **research pipeline** for macro and quantitative workflows: requirements → retrieval → analysis plan → (sandboxed) execution → drafting → packaged delivery.

This repository is a **runnable skeleton**: six stages, stable artifact layout, optional ZIP bundle. It does **not** call LLMs or execute generated code by default (safe defaults for experiments and demos).

## Features

- **Requirements capture** — structured PRD-style outputs (pluggable LLM / UI).
- **Tiered data acquisition** — API-first (e.g. AkShare, FRED), uploads second, crawling last with explicit risk notes.
- **Sandbox execution** — hook for isolated Python runs, charts, and auditable tables.
- **Interpretation & layout** — chapter drafting and export hooks (e.g. Word/PDF) left for integration.

## Quick start

```bash
git clone https://github.com/Roleica/DataLoom.git
cd DataLoom
python3 run_demo.py --topic "Your research topic"
# Optional fixed run folder:
python3 run_demo.py --topic "demo" --run-id demo-run-1 --auto
```

Artifacts are written under `runs/<run_id>/` (ignored by git).

## Layout

```
.
├── LICENSE
├── README.md
├── requirements.txt
├── run_demo.py
└── framework/
    ├── context.py
    ├── pipeline.py
    └── stages/
```

Replace each `framework/stages/*.py` `run()` with your LLM, retrieval, and sandbox integrations.

## Roadmap

1. Adapter layer for models and APIs (secrets via environment variables).
2. Workflow engine with human-in-the-loop checkpoints and rollback.
3. Dedicated execution service: allowlisted imports, timeouts, restricted networking.

## License

MIT — see [LICENSE](./LICENSE).
