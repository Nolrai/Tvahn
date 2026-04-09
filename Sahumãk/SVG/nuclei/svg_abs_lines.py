#!/usr/bin/env python3

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


COMMANDS = set("MmLlHhVvZz")
UNSUPPORTED = set("CcSsQqTtAaRr")


def tokenize_path(d: str) -> list[str]:
    """
    Split an SVG path string into command and number tokens.
    """
    token_re = re.compile(r"""
        [MmLlHhVvZzCcSsQqTtAaRr] |
        [-+]?
        (?:
            (?:\d+\.\d*) |
            (?:\.\d+) |
            (?:\d+)
        )
        (?:[eE][-+]?\d+)?
    """, re.VERBOSE)
    return token_re.findall(d)


def is_command(tok: str) -> bool:
    return len(tok) == 1 and tok.isalpha()


def fmt_num(x: float) -> str:
    """
    Format numbers cleanly for SVG output.
    """
    if abs(x - round(x)) < 1e-12:
        return str(int(round(x)))
    s = f"{x:.12g}"
    return s


def parse_number(tok: str) -> float:
    return float(tok)


def convert_path_to_absolute_lines(d: str) -> str:
    """
    Convert a path string to canonical absolute commands using only M/L/Z.

    Supported input commands:
      M m L l H h V v Z z

    Unsupported commands raise ValueError.
    """
    tokens = tokenize_path(d)
    if not tokens:
        return d

    for tok in tokens:
        if tok in UNSUPPORTED:
            raise ValueError(f"unsupported path command: {tok}")

    out: list[str] = []

    i = 0
    cmd = None

    cx = 0.0
    cy = 0.0
    subpath_start_x = 0.0
    subpath_start_y = 0.0

    def have_more_numbers(idx: int) -> bool:
        return idx < len(tokens) and not is_command(tokens[idx])

    while i < len(tokens):
        tok = tokens[i]
        if is_command(tok):
            cmd = tok
            i += 1
        elif cmd is None:
            raise ValueError("path data starts with numbers before any command")

        if cmd is None:
            raise ValueError("internal parser error: missing command")

        if cmd == "M":
            # First pair is moveto, additional pairs are treated as lineto
            if i + 1 >= len(tokens):
                raise ValueError("M requires at least one coordinate pair")

            x = parse_number(tokens[i])
            y = parse_number(tokens[i + 1])
            i += 2

            cx, cy = x, y
            subpath_start_x, subpath_start_y = cx, cy
            out.extend(["M", fmt_num(cx), fmt_num(cy)])

            while have_more_numbers(i):
                if i + 1 >= len(tokens):
                    raise ValueError("odd number of coordinates after M")
                x = parse_number(tokens[i])
                y = parse_number(tokens[i + 1])
                i += 2
                cx, cy = x, y
                out.extend(["L", fmt_num(cx), fmt_num(cy)])

        elif cmd == "m":
            if i + 1 >= len(tokens):
                raise ValueError("m requires at least one coordinate pair")

            dx = parse_number(tokens[i])
            dy = parse_number(tokens[i + 1])
            i += 2

            cx += dx
            cy += dy
            subpath_start_x, subpath_start_y = cx, cy
            out.extend(["M", fmt_num(cx), fmt_num(cy)])

            # After initial moveto, subsequent pairs are relative lineto
            while have_more_numbers(i):
                if i + 1 >= len(tokens):
                    raise ValueError("odd number of coordinates after m")
                dx = parse_number(tokens[i])
                dy = parse_number(tokens[i + 1])
                i += 2
                cx += dx
                cy += dy
                out.extend(["L", fmt_num(cx), fmt_num(cy)])

        elif cmd == "L":
            while have_more_numbers(i):
                if i + 1 >= len(tokens):
                    raise ValueError("odd number of coordinates after L")
                x = parse_number(tokens[i])
                y = parse_number(tokens[i + 1])
                i += 2
                cx, cy = x, y
                out.extend(["L", fmt_num(cx), fmt_num(cy)])
            if i == len(tokens) or (i < len(tokens) and is_command(tokens[i])):
                pass

        elif cmd == "l":
            while have_more_numbers(i):
                if i + 1 >= len(tokens):
                    raise ValueError("odd number of coordinates after l")
                dx = parse_number(tokens[i])
                dy = parse_number(tokens[i + 1])
                i += 2
                cx += dx
                cy += dy
                out.extend(["L", fmt_num(cx), fmt_num(cy)])

        elif cmd == "H":
            while have_more_numbers(i):
                x = parse_number(tokens[i])
                i += 1
                cx = x
                out.extend(["L", fmt_num(cx), fmt_num(cy)])

        elif cmd == "h":
            while have_more_numbers(i):
                dx = parse_number(tokens[i])
                i += 1
                cx += dx
                out.extend(["L", fmt_num(cx), fmt_num(cy)])

        elif cmd == "V":
            while have_more_numbers(i):
                y = parse_number(tokens[i])
                i += 1
                cy = y
                out.extend(["L", fmt_num(cx), fmt_num(cy)])

        elif cmd == "v":
            while have_more_numbers(i):
                dy = parse_number(tokens[i])
                i += 1
                cy += dy
                out.extend(["L", fmt_num(cx), fmt_num(cy)])

        elif cmd in ("Z", "z"):
            cx, cy = subpath_start_x, subpath_start_y
            out.append("Z")

        else:
            raise ValueError(f"unsupported path command: {cmd}")

    return " ".join(out)


def iter_path_elements(root: ET.Element):
    """
    Yield all SVG path elements regardless of namespace.
    """
    for elem in root.iter():
        if elem.tag.endswith("path"):
            yield elem


def convert_svg_file(input_path: Path, output_path: Path) -> None:
    tree = ET.parse(input_path)
    root = tree.getroot()

    converted = 0
    skipped = 0

    for path_elem in iter_path_elements(root):
        d = path_elem.get("d")
        if not d:
            continue

        try:
            new_d = convert_path_to_absolute_lines(d)
        except ValueError as e:
            skipped += 1
            elem_id = path_elem.get("id", "<no id>")
            print(f"Skipping path {elem_id}: {e}", file=sys.stderr)
            continue

        path_elem.set("d", new_d)
        converted += 1

    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    print(f"Converted {converted} path(s), skipped {skipped} path(s).")


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print(f"Usage: {sys.argv[0]} input.svg [output.svg]", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    if len(sys.argv) == 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_name(input_path.stem + ".absolute.svg")

    convert_svg_file(input_path, output_path)
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())