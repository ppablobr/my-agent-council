#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


RE_INLINE_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
RE_REF_DEF = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)\s*$", re.MULTILINE)


def _strip_title(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    for quote in ('"', "'"):
        marker = f" {quote}"
        if marker in target:
            return target.split(marker, 1)[0].strip()
    return target


def _is_external(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:"))


def _resolve_target(md_file: Path, target: str, repo_root: Path) -> Path | None:
    target = _strip_title(target)
    if not target or target.startswith("#") or _is_external(target):
        return None

    target_no_fragment = target.split("#", 1)[0].strip()
    if not target_no_fragment:
        return None

    if target_no_fragment.startswith("/"):
        return (repo_root / target_no_fragment.lstrip("/")).resolve()

    return (md_file.parent / target_no_fragment).resolve()


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    broken: list[str] = []

    for md_file in repo_root.rglob("*.md"):
        if any(part in {".git", "node_modules"} for part in md_file.parts):
            continue

        content = md_file.read_text(encoding="utf-8", errors="replace")
        targets = []
        targets.extend(RE_INLINE_LINK.findall(content))
        targets.extend(RE_REF_DEF.findall(content))

        for target in targets:
            resolved = _resolve_target(md_file, target, repo_root)
            if resolved is None:
                continue

            if resolved.exists():
                if resolved.is_dir():
                    if (resolved / "README.md").exists() or (resolved / "readme.md").exists():
                        continue
                    continue
                continue

            broken.append(f"{md_file.relative_to(repo_root)} -> {target}")

    if broken:
        print("Broken relative links found:")
        for entry in broken:
            print(f"- {entry}")
        return 1

    print("OK: no broken relative links found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
