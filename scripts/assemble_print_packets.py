#!/usr/bin/env python3
from __future__ import annotations

import csv
import html
import os
import subprocess
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "PrintPackets"


PACKETS = {
    "PSA": {
        "title": "PSA Print Packet",
        "subtitle": "Proto-South American Catgirl working notes",
        "files": [
            "PSA/PSA.md",
            "PSA/vocab.md",
            "PSA/slots.md",
            "PSA/Conversation 1 (Gloss).md",
            "PSA/Conversation 1.txt",
            "PSA/exersizes_notes.md",
        ],
    },
    "GE": {
        "title": "GE Print Packet",
        "subtitle": "Golden Empire working notes",
        "files": [],
    },
    "PWT": {
        "title": "PWT Print Packet",
        "subtitle": "Proto-Windic / Proto-Wind-Tribe working notes",
        "files": [
            "PWT/Phonology.md",
            "PWT/Grammar.md",
            "PWT/Counting.md",
            "PWT/Babalon.md",
            "PWT/Babalon.txt",
            "PWT/sorted.txt",
            "PWT/raw.txt",
        ],
    },
    "Sahumank": {
        "title": "Sahumank Print Packet",
        "subtitle": "Sahumank / Sahumãk working notes",
        "files": [
            "Sahumãk/sahumãk.md",
            "Sahumãk/SVG/Syllables.png",
            "Sahumãk/Grammar.md",
            "Sahumãk/vocab.csv",
            "Sahumãk/Adpositions.csv",
            "Sahumãk/MainVerbs.csv",
            "Sahumãk/WestWallCommentary.md",
            "Sahumãk/WestWall(Gloss).txt",
            "Sahumãk/WestWall_en.txt",
            "Sahumãk/Relay Final.txt",
            "Sahumãk/The Founding.md",
            "Sahumãk/Sahumãk Historical and Archaeological .md",
            "Sahumãk/SettingInfo.md",
            "Sahumãk/LaterHistoriography.md",
            "Sahumãk/Scribal Comprehension.md",
        ],
    },
}


CSS = """
@page { margin: 0.65in; }
body {
  color: #111;
  font-family: "DejaVu Serif", Georgia, serif;
  font-size: 10.5pt;
  line-height: 1.35;
}
h1, h2, h3, h4 { page-break-after: avoid; }
h1 { font-size: 22pt; margin-top: 0; }
h2 { font-size: 16pt; border-bottom: 1px solid #bbb; padding-bottom: 0.12in; margin-top: 0.3in; }
h3 { font-size: 13pt; }
table { border-collapse: collapse; width: 100%; font-size: 8.5pt; }
th, td { border: 1px solid #ccc; padding: 3px 5px; vertical-align: top; }
th { background: #eee; }
pre {
  white-space: pre-wrap;
  font-family: "DejaVu Sans Mono", monospace;
  font-size: 9pt;
  border-left: 3px solid #ccc;
  padding-left: 0.12in;
}
code { font-family: "DejaVu Sans Mono", monospace; }
img { max-width: 100%; height: auto; }
.pagebreak { page-break-before: always; }
.source-note { color: #555; font-size: 9pt; }
.notes-page {
  page-break-before: always;
  min-height: 9in;
  background-image: repeating-linear-gradient(to bottom, transparent 0, transparent 0.31in, #ddd 0.32in);
}
.notes-page h2 { border: 0; }
.glyphs { font-family: "Sahumank", "DejaVu Sans", sans-serif; }
""".strip()


def title_from_path(path: str) -> str:
    name = Path(path).name
    for suffix in (".md", ".txt", ".csv", ".png"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
    return name.replace("_", " ").strip()


def fence_text(text: str) -> str:
    return "```text\n" + text.rstrip() + "\n```\n"


def csv_to_markdown(path: Path) -> str:
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        return ""
    header = rows[0]
    out = []
    out.append("| " + " | ".join(escape_cell(c) for c in header) + " |")
    out.append("| " + " | ".join("---" for _ in header) + " |")
    for row in rows[1:]:
        row = row + [""] * (len(header) - len(row))
        out.append("| " + " | ".join(escape_cell(c) for c in row[: len(header)]) + " |")
    return "\n".join(out) + "\n"


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def section_for(path_text: str) -> str:
    path = ROOT / path_text
    title = title_from_path(path_text)
    suffix = path.suffix.lower()

    if suffix == ".png":
        return f"## {title}\n\n![{title}]({path_text})\n"
    if suffix == ".csv":
        return f"## {title}\n\n{csv_to_markdown(path)}"

    text = path.read_text(encoding="utf-8").rstrip()
    if suffix == ".txt":
        return f"## {title}\n\n{fence_text(text)}"
    return text + "\n"


def build_markdown(name: str, spec: dict[str, object]) -> Path:
    out_path = OUT / f"{name}.md"
    files = list(spec["files"])
    lines = [
        f"# {spec['title']}",
        "",
        str(spec["subtitle"]),
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Source Inventory",
        "",
    ]
    if files:
        lines.extend(f"- `{p}`" for p in files)
    else:
        lines.append("- No source files were present in this directory.")
    lines.extend(["", '<div class="pagebreak"></div>', ""])

    if files:
        for idx, file_path in enumerate(files):
            if idx:
                lines.extend(["", '<div class="pagebreak"></div>', ""])
            lines.append(f'<p class="source-note">Source: <code>{html.escape(file_path)}</code></p>')
            lines.append("")
            lines.append(section_for(file_path))
    else:
        lines.extend([
            "## No Current Source Material",
            "",
            "The `GE` directory exists, but contains no files at packet generation time.",
            "",
            "Use the notes pages below to draft the first grammar, lexicon, texts, or historical notes.",
        ])

    for i in range(1, 4):
        lines.extend([
            "",
            '<div class="notes-page">',
            "",
            f"## Field Notes {i}",
            "",
            "</div>",
        ])

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path


def run_pandoc(md_path: Path) -> None:
    css_path = OUT / "print.css"
    html_path = md_path.with_suffix(".html")
    docx_path = md_path.with_suffix(".docx")

    subprocess.run(
        [
            "pandoc",
            str(md_path),
            "--from",
            "markdown+raw_html-yaml_metadata_block",
            "--standalone",
            "--toc",
            "--self-contained",
            "--css",
            str(css_path),
            "--metadata",
            f"title={md_path.stem}",
            "-o",
            str(html_path),
        ],
        check=True,
        cwd=ROOT,
    )
    subprocess.run(
        [
            "pandoc",
            str(md_path),
            "--from",
            "markdown+raw_html-yaml_metadata_block",
            "--toc",
            "--reference-location",
            "block",
            "-o",
            str(docx_path),
        ],
        check=True,
        cwd=ROOT,
    )


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / "print.css").write_text(CSS + "\n", encoding="utf-8")
    for name, spec in PACKETS.items():
        md = build_markdown(name, spec)
        run_pandoc(md)


if __name__ == "__main__":
    main()
