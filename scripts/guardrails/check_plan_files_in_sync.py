#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def _run(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def _changed_files(base: str, head: str) -> set[str]:
    out = _run("git", "diff", "--name-only", f"{base}..{head}")
    return {line.strip() for line in out.splitlines() if line.strip()}


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


def main() -> int:
    probe = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if probe.returncode != 0:
        print("Skipping plan sync guardrail: not running inside a git work tree.")
        return 0

    inferred = _infer_range_from_github_event()
    if inferred and inferred[0] and inferred[1]:
        base, head = inferred
    else:
        head = _run("git", "rev-parse", "HEAD")
        try:
            base = _run("git", "rev-parse", "HEAD~1")
        except subprocess.CalledProcessError:
            print("Skipping plan sync guardrail: unable to infer diff base.")
            return 0

    changed = _changed_files(base, head)
    plan_md = "PLAN.md"
    plan_json = "plan.json"

    md_changed = plan_md in changed
    json_changed = plan_json in changed

    if md_changed ^ json_changed:
        print("Plan files out of sync:")
        print(f"- {plan_md} changed: {md_changed}")
        print(f"- {plan_json} changed: {json_changed}")
        print("Update both files together or revert the partial change.")
        return 1

    print("OK: PLAN.md and plan.json are in sync (change-wise).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
