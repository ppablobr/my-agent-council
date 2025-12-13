#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


def _run(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def _infer_range_from_github_event() -> tuple[str, str] | None:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path or not Path(event_path).exists():
        return None

    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    with open(event_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if event_name == "pull_request":
        return data["pull_request"]["base"]["sha"], data["pull_request"]["head"]["sha"]

    if event_name == "push":
        return data.get("before"), data.get("after")

    return None


def _changed_files(base: str, head: str) -> set[str]:
    out = _run("git", "diff", "--name-only", f"{base}..{head}")
    return {line.strip() for line in out.splitlines() if line.strip()}


def main() -> int:
    if os.environ.get("ALLOW_DOCS_SKIP", "").lower() in {"1", "true", "yes"}:
        print("Skipping traceability guardrail: ALLOW_DOCS_SKIP is set.")
        return 0

    probe = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if probe.returncode != 0:
        print("Skipping traceability guardrail: not running inside a git work tree.")
        return 0

    inferred = _infer_range_from_github_event()
    if inferred and inferred[0] and inferred[1]:
        base, head = inferred
    else:
        head = _run("git", "rev-parse", "HEAD")
        try:
            base = _run("git", "rev-parse", "HEAD~1")
        except subprocess.CalledProcessError:
            print("Skipping traceability guardrail: unable to infer diff base.")
            return 0

    changed = _changed_files(base, head)

    code_changed = any(p.startswith("app/") for p in changed)
    if not code_changed:
        print("OK: no app/ changes detected.")
        return 0

    spec_paths = {
        "BACKLOG.md",
        "ROADMAP.md",
        "RISKS.md",
        "DECISIONS.md",
        "product_manager/PRD.md",
        "product_manager/STRUCTURE.md",
        "product_manager/PROJECT_RULES.md",
    }

    spec_changed = any(p in spec_paths or p.startswith("docs/adr/") for p in changed)
    if spec_changed:
        print("OK: app/ changes include corresponding spec updates.")
        return 0

    print("Traceability guardrail failed:")
    print("- Detected changes under app/ without corresponding spec updates.")
    print("- Update at least one of: PRD/backlog/roadmap/decisions/ADR (or set ALLOW_DOCS_SKIP=true).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
