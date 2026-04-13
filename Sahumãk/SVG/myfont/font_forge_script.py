#!/usr/bin/env python3
import fontforge
import os
import re
import sys

FONT_NAME = "Sahumank"
FAMILY_NAME = "Sahumank"
FULL_NAME = "Sahumank Regular"
OUTPUT_FILE = "Sahumank-Regular.ttf"
MAPPING_FILE = "Sahumank-mapping.txt"

GLYPH_DIR = "glyphs"

EM_SIZE = 1200
ASCENT = 600
DESCENT = 600

ADVANCE_WIDTH = 900  # or 850–1000 depending on spacing taste

SCALE_X = 1.0
SCALE_Y = 1.0
SHIFT_X = 0
SHIFT_Y = 0


CATEGORY_STARTS = {
    "on": 0xE800,
    "nu": 0xE810,
    "sy": 0xE900,
}

CATEGORY_LIMITS = {
    "on": 0xE80F,
    "nu": 0xE83F,
    "sy": 0xE9FF,
}

CATEGORY_LABELS = {
    "on": "onset",
    "nu": "nucleus",
    "sy": "syllable",
}

FILENAME_RE = re.compile(
    r"^(on|nu|sy)_([0-9]{3})_([a-z0-9_]+)\.svg$"
)

def parse_file(filename: str):
    """
    Parse filenames like:
      on_006_k.svg
      nu_005_o.svg
      sy_015_pwu.svg

    Returns:
      (category, index, label)
    or
      (None, None, None)
    """
    m = FILENAME_RE.match(filename)
    if not m:
        return None, None, None

    category, raw_index, label = m.groups()
    return category.lower(), int(raw_index), label

def sanitize_glyph_name(category: str, label: str) -> str:
    safe = label.replace("-", "_").replace(" ", "_")
    safe = "".join(ch if ch.isalnum() or ch == "_" else "_" for ch in safe)
    return f"{category}_{safe}"


def main():
    if not os.path.isdir(GLYPH_DIR):
        print(f"Error: glyph directory not found: {GLYPH_DIR}", file=sys.stderr)
        sys.exit(1)

    categorized = {k: [] for k in CATEGORY_STARTS}
    skipped = []

    for filename in os.listdir(GLYPH_DIR):
        if not filename.lower().endswith(".svg"):
            continue

        category, index, label = parse_file(filename)
        if category is None:
            skipped.append(filename)
            continue

        categorized[category].append((index, label, filename))

    # Sort by numeric index, then label as tie-breaker
    for category in categorized:
        categorized[category].sort(key=lambda x: (x[0], x[1]))

    font = fontforge.font()
    font.encoding = "UnicodeFull"
    font.fontname = FONT_NAME.replace(" ", "")
    font.familyname = FAMILY_NAME
    font.fullname = FULL_NAME
    font.em = EM_SIZE
    font.ascent = ASCENT
    font.descent = DESCENT

    mapping_lines = []
    used_codepoints = set()

    for category in ["on", "nu", "sy"]:
        start = CATEGORY_STARTS[category]
        limit = CATEGORY_LIMITS[category]
        items = categorized[category]

        if start + len(items) - 1 > limit:
            print(
                f"Error: category '{category}' has too many glyphs "
                f"({len(items)} items for range U+{start:04X}-U+{limit:04X})",
                file=sys.stderr
            )
            sys.exit(1)

        for offset, (src_index, label, filename) in enumerate(items):
            codepoint = start + offset

            if codepoint in used_codepoints:
                print(f"Error: duplicate codepoint allocation U+{codepoint:04X}", file=sys.stderr)
                sys.exit(1)

            used_codepoints.add(codepoint)

            glyph = font.createChar(codepoint)
            glyph.glyphname = sanitize_glyph_name(category, label)

            full_path = os.path.join(GLYPH_DIR, filename)
            glyph.importOutlines(full_path)

            print(f"{filename} after import: {glyph.boundingBox()}")

            if SCALE_X != 1.0 or SCALE_Y != 1.0:
                glyph.transform((SCALE_X, 0, 0, SCALE_Y, 0, 0))
                print(f"{filename} after scale: {glyph.boundingBox()}")

            if SHIFT_X != 0 or SHIFT_Y != 0:
                glyph.transform((1, 0, 0, 1, SHIFT_X, SHIFT_Y))
                print(f"{filename} after shift: {glyph.boundingBox()}")

            glyph.removeOverlap()
            glyph.correctDirection()
            glyph.width = ADVANCE_WIDTH

            mapping_lines.append(
                f"U+{codepoint:04X}\t{glyph.glyphname}\t{CATEGORY_LABELS[category]}"
                f"\t{filename}\tindex={src_index}"
            )

    font.os2_winascent = ASCENT
    font.os2_windescent = DESCENT
    font.hhea_ascent = ASCENT
    font.hhea_descent = -DESCENT
    font.hhea_linegap = 0

    font.generate(OUTPUT_FILE)

    with open(MAPPING_FILE, "w", encoding="utf-8") as f:
        f.write("# Codepoint\tGlyphName\tCategory\tSourceFile\tSourceIndex\n")
        for line in mapping_lines:
            f.write(line + "\n")

        if skipped:
            f.write("\n# Skipped files\n")
            for name in sorted(skipped):
                f.write(f"# {name}\n")

    print(f"Generated font: {OUTPUT_FILE}")
    print(f"Wrote mapping:  {MAPPING_FILE}")

    if skipped:
        print("Skipped files:")
        for name in sorted(skipped):
            print(f"  {name}")


if __name__ == "__main__":
    main()