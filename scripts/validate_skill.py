#!/usr/bin/env python3
"""Check the local package without network access or external dependencies.

Supports the inline and reference Markdown links used by this package. This is
structural validation, not a complete Markdown/YAML parser or a UX evaluation.
"""

import argparse
from collections import Counter, deque
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


# Reviewed catalog from the source indexes; update intentionally if they change.
PRINCIPLES = frozenset(
    "aesthetic-usability-effect choice-overload chunking cognitive-bias "
    "cognitive-load doherty-threshold fitts-law flow goal-gradient-effect "
    "hick-law jakob-law common-region proximity pragnanz similarity "
    "uniform-connectedness mental-model miller-law occams-razor "
    "active-user-paradox pareto-principle parkinsons-law peak-end-rule "
    "postels-law selective-attention serial-position-effect teslers-law "
    "von-restorff-effect working-memory zeigarnik-effect".split()
)

INLINE_LINK = re.compile(
    r"!?\[[^\]\n]+\]\((<[^>\n]+>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\)"
)
REFERENCE_LINK = re.compile(
    r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", re.MULTILINE
)


def outside_fences(content):
    """Return prose and whether all fenced examples were closed."""
    lines = []
    marker = None
    width = 0
    for line in content.splitlines():
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            value, tail = fence.groups()
            if marker is None:
                marker, width = value[0], len(value)
            elif value[0] == marker and len(value) >= width and not tail.strip():
                marker = None
            continue
        if marker is None:
            lines.append(line)
    return "\n".join(lines), marker is None


def headings(content):
    """Build ordinary GitHub-style heading IDs, including duplicate suffixes."""
    seen = Counter()
    result = set()
    for line in content.splitlines():
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", match.group(1))
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        occurrence = seen[slug]
        seen[slug] += 1
        result.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    result.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', content))
    return result


def link_targets(content):
    return [m.group(1).strip("<>") for pattern in (INLINE_LINK, REFERENCE_LINK)
            for m in pattern.finditer(content)]


def validate(root):
    root = root.resolve()
    errors = []
    entry = root / "SKILL.md"
    if not entry.is_file():
        return ["SKILL.md is missing"], 0

    documents = sorted(root.rglob("*.md"))
    prose = {}
    graph = {path: set() for path in documents}
    for path in documents:
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(root)}: cannot read: {exc}")
            continue
        if not content.strip():
            errors.append(f"{path.relative_to(root)}: empty document")
        body, closed = outside_fences(content)
        prose[path] = body
        if not closed:
            errors.append(f"{path.relative_to(root)}: unclosed code fence")
        if re.search(r"^\s*\[TODO:[^\n]*\]\s*$", body, re.MULTILINE):
            errors.append(f"{path.relative_to(root)}: unfinished scaffold marker")

    content = entry.read_text(encoding="utf-8")
    front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", content, re.DOTALL)
    if not front:
        errors.append("SKILL.md: missing or unclosed frontmatter")
    else:
        values = {}
        for line in front.group(1).splitlines():
            match = re.match(r"^([a-z][a-z-]*):\s*(.*?)\s*$", line)
            if match:
                key, value = match.groups()
                if key in values:
                    errors.append(f"SKILL.md: duplicate frontmatter key {key}")
                values[key] = value.strip("\"'")
        name = values.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append("SKILL.md: name must be a valid slug, at most 64 characters")
        if name != root.name:
            errors.append("SKILL.md: name must match the package folder")
        description = values.get("description", "")
        if not description or len(description) > 1024 or any(c in description for c in "<>"):
            errors.append("SKILL.md: provide a plain, nonempty description up to 1024 characters")
        if "disable-model-invocation" in values:
            errors.append("SKILL.md: this package must remain eligible for automatic selection")

    for path, body in prose.items():
        for target in link_targets(body):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            try:
                destination.relative_to(root)
            except ValueError:
                errors.append(f"{path.relative_to(root)}: nonportable local link {target}")
                continue
            if not destination.is_file():
                errors.append(f"{path.relative_to(root)}: missing link target {target}")
                continue
            if destination in graph:
                graph[path].add(destination)
                if parsed.fragment and unquote(parsed.fragment) not in headings(prose.get(destination, "")):
                    errors.append(f"{path.relative_to(root)}: missing heading for {target}")

    principle_dir = root / "references" / "principles"
    actual = {p.stem for p in principle_dir.glob("*.md") if p.stem != "index"}
    if actual != PRINCIPLES:
        missing = ", ".join(sorted(PRINCIPLES - actual)) or "none"
        unexpected = ", ".join(sorted(actual - PRINCIPLES)) or "none"
        errors.append(f"principle catalog differs: missing={missing}; unexpected={unexpected}")
    index = principle_dir / "index.md"
    linked = {p.stem for p in graph.get(index, set()) if p.parent == principle_dir}
    if not PRINCIPLES.issubset(linked):
        errors.append("principle index must link every catalog card")
    for slug in sorted(actual):
        card = principle_dir / f"{slug}.md"
        sources = [urlsplit(t) for t in link_targets(prose.get(card, ""))]
        official = [s for s in sources if s.netloc == "lawsofux.com"]
        if not any(s.path.startswith("/es/") and s.path != "/es/" for s in official):
            errors.append(f"principles/{slug}.md: missing Spanish concept source")
        if not any(s.path not in ("/", "") and not s.path.startswith("/es/") for s in official):
            errors.append(f"principles/{slug}.md: missing English concept source")

    visited = set()
    pending = deque([entry])
    while pending:
        path = pending.popleft()
        if path in visited:
            continue
        visited.add(path)
        pending.extend(graph.get(path, set()) - visited)
    for orphan in sorted(set(documents) - visited):
        errors.append(f"{orphan.relative_to(root)}: no reading route from SKILL.md")
    return errors, len(documents)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors, count = validate(args.path)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {count} Markdown documents, {len(PRINCIPLES)} principles, and local reading routes.")
    print("External links and behavioral correctness require separate verification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
