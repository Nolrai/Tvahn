#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "PrintPackets"

PAGE_W, PAGE_H = 2550, 3300
MARGIN_X, MARGIN_Y = 210, 180
LINE_GAP = 10
PARA_GAP = 18
BG = "white"
INK = "#111111"
MUTED = "#555555"
RULE = "#cccccc"

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
FONT = FONT_DIR / "DejaVuSans.ttf"
FONT_BOLD = FONT_DIR / "DejaVuSans-Bold.ttf"
FONT_MONO = FONT_DIR / "DejaVuSansMono.ttf"
SAHUMANK_FONT = ROOT / "Sahumãk/SVG/myfont/Sahumank-Regular.ttf"


def load_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


FONTS = {
    "body": load_font(FONT, 34),
    "body_bold": load_font(FONT_BOLD, 34),
    "small": load_font(FONT, 28),
    "h1": load_font(FONT_BOLD, 68),
    "h2": load_font(FONT_BOLD, 48),
    "h3": load_font(FONT_BOLD, 40),
    "mono": load_font(FONT_MONO, 27),
    "glyph": load_font(SAHUMANK_FONT, 34) if SAHUMANK_FONT.exists() else load_font(FONT, 34),
    "glyph_mono": load_font(SAHUMANK_FONT, 27) if SAHUMANK_FONT.exists() else load_font(FONT_MONO, 27),
}


def is_private_use(ch: str) -> bool:
    return 0xE000 <= ord(ch) <= 0xF8FF


class Renderer:
    def __init__(self, title: str) -> None:
        self.title = title
        self.pages: list[Image.Image] = []
        self.page_no = 0
        self.new_page()

    @property
    def draw(self) -> ImageDraw.ImageDraw:
        return ImageDraw.Draw(self.pages[-1])

    def new_page(self) -> None:
        if self.pages:
            self.footer()
        self.pages.append(Image.new("RGB", (PAGE_W, PAGE_H), BG))
        self.page_no += 1
        self.y = MARGIN_Y

    def footer(self) -> None:
        d = ImageDraw.Draw(self.pages[-1])
        footer = f"{self.title} - {self.page_no}"
        d.text((MARGIN_X, PAGE_H - 95), footer, fill=MUTED, font=FONTS["small"])
        d.line((MARGIN_X, PAGE_H - 120, PAGE_W - MARGIN_X, PAGE_H - 120), fill=RULE, width=2)

    def ensure(self, height: int) -> None:
        if self.y + height > PAGE_H - 150:
            self.new_page()

    def text_width(self, text: str, font: ImageFont.FreeTypeFont, glyph_font: ImageFont.FreeTypeFont) -> float:
        return sum((glyph_font if is_private_use(ch) else font).getlength(ch) for ch in text)

    def draw_mixed(self, xy: tuple[int, int], text: str, font: ImageFont.FreeTypeFont, fill: str = INK) -> None:
        x, y = xy
        glyph_font = FONTS["glyph_mono"] if font == FONTS["mono"] else FONTS["glyph"]
        for ch in text:
            active = glyph_font if is_private_use(ch) else font
            self.draw.text((x, y), ch, fill=fill, font=active)
            x += int(active.getlength(ch))

    def wrap(self, text: str, font: ImageFont.FreeTypeFont, width: int) -> list[str]:
        glyph_font = FONTS["glyph_mono"] if font == FONTS["mono"] else FONTS["glyph"]
        words = re.split(r"(\s+)", text.strip())
        lines: list[str] = []
        current = ""
        for part in words:
            candidate = current + part
            if current and self.text_width(candidate, font, glyph_font) > width:
                lines.append(current.rstrip())
                current = part.lstrip()
            else:
                current = candidate
        if current.strip():
            lines.append(current.rstrip())
        return lines or [""]

    def paragraph(self, text: str, font: ImageFont.FreeTypeFont | None = None, fill: str = INK, indent: int = 0) -> None:
        font = font or FONTS["body"]
        max_w = PAGE_W - 2 * MARGIN_X - indent
        lines = self.wrap(text, font, max_w)
        line_h = font.size + LINE_GAP
        self.ensure(line_h * len(lines) + PARA_GAP)
        for line in lines:
            self.draw_mixed((MARGIN_X + indent, self.y), line, font, fill=fill)
            self.y += line_h
        self.y += PARA_GAP

    def heading(self, text: str, level: int) -> None:
        font = FONTS["h1"] if level == 1 else FONTS["h2"] if level == 2 else FONTS["h3"]
        self.ensure(font.size * 2)
        if level == 1 and self.y > MARGIN_Y + 20:
            self.new_page()
        for line in self.wrap(text, font, PAGE_W - 2 * MARGIN_X):
            self.draw_mixed((MARGIN_X, self.y), line, font)
            self.y += font.size + 14
        if level == 2:
            self.draw.line((MARGIN_X, self.y, PAGE_W - MARGIN_X, self.y), fill=RULE, width=2)
            self.y += 18
        else:
            self.y += 20

    def image(self, image_path: Path) -> None:
        src = Image.open(image_path).convert("RGB")
        max_w = PAGE_W - 2 * MARGIN_X
        max_h = PAGE_H - 2 * MARGIN_Y - 160
        scale = min(max_w / src.width, max_h / src.height)
        size = (int(src.width * scale), int(src.height * scale))
        self.ensure(size[1] + 40)
        resized = src.resize(size, Image.Resampling.LANCZOS)
        x = MARGIN_X + (max_w - size[0]) // 2
        self.pages[-1].paste(resized, (x, self.y))
        self.y += size[1] + 40

    def lined_notes_page(self, label: str) -> None:
        self.new_page()
        self.heading(label, 2)
        y = self.y + 30
        while y < PAGE_H - 190:
            self.draw.line((MARGIN_X, y, PAGE_W - MARGIN_X, y), fill="#dddddd", width=2)
            y += 92
        self.new_page()

    def finish(self) -> None:
        self.footer()


def strip_inline_markup(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("`", "")
    text = text.replace("**", "")
    text = text.replace("__", "")
    return text


def render_markdown(md_path: Path) -> Path:
    renderer = Renderer(md_path.stem)
    in_code = False
    code_buf: list[str] = []
    lines = md_path.read_text(encoding="utf-8").splitlines()

    def flush_code() -> None:
        nonlocal code_buf
        if not code_buf:
            return
        for raw in code_buf:
            if not raw:
                renderer.y += FONTS["mono"].size + LINE_GAP
                continue
            renderer.paragraph(raw, FONTS["mono"])
        code_buf = []

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_buf.append(line)
            continue

        if '<div class="pagebreak">' in line:
            renderer.new_page()
            continue
        if '<div class="notes-page">' in line:
            continue
        if line == "</div>":
            continue

        image_match = re.match(r"!\[[^\]]*\]\(([^)]+)\)", line)
        if image_match:
            renderer.image(ROOT / image_match.group(1))
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.*)", line)
        if heading_match:
            level = min(len(heading_match.group(1)), 3)
            text = strip_inline_markup(heading_match.group(2))
            if text.startswith("Field Notes"):
                renderer.lined_notes_page(text)
            else:
                renderer.heading(text, level)
            continue

        if not line.strip():
            renderer.y += PARA_GAP
            continue

        if line.startswith("|"):
            renderer.paragraph(line, FONTS["mono"])
        elif line.startswith("- "):
            renderer.paragraph("• " + strip_inline_markup(line[2:]), indent=35)
        else:
            renderer.paragraph(strip_inline_markup(line), FONTS["body"])

    flush_code()
    renderer.finish()
    pdf_path = md_path.with_suffix(".pdf")
    renderer.pages[0].save(
        pdf_path,
        save_all=True,
        append_images=renderer.pages[1:],
        resolution=300,
    )
    return pdf_path


def pdf_to_ps(pdf_path: Path) -> Path:
    ps_path = pdf_path.with_suffix(".ps")
    subprocess.run(
        ["mutool", "convert", "-F", "ps", "-o", str(ps_path), str(pdf_path)],
        check=True,
        cwd=ROOT,
    )
    return ps_path


def main() -> None:
    for name in ("PSA", "GE", "PWT", "Sahumank"):
        pdf = render_markdown(OUT / f"{name}.md")
        pdf_to_ps(pdf)


if __name__ == "__main__":
    main()
