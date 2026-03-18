#!/usr/bin/env python3
"""
Extract dominant colors from brand images and generate Markdown, HTML, and CSS guides.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import colorsys
import re

import numpy as np
from PIL import Image


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


def get_color_name(rgb: tuple[int, int, int]) -> str:
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    h = h * 360

    if s < 0.1:
        return "Black" if v < 0.5 else "White"
    if v < 0.3:
        return "Dark"

    if s > 0.7:
        if h < 15 or h >= 345:
            return "Red"
        if h < 45:
            return "Orange"
        if h < 65:
            return "Yellow"
        if h < 150:
            return "Green"
        if h < 200:
            return "Cyan"
        if h < 260:
            return "Blue"
        if h < 290:
            return "Purple"
        if h < 330:
            return "Magenta"

    return "Neutral"


def slugify_label(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = rgb
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255


def get_color_family(rgb: tuple[int, int, int]) -> str:
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    h = h * 360

    # Treat low-saturation colors as neutrals for more practical token families.
    if s < 0.15 or v < 0.15:
        return "neutral"

    if h < 15 or h >= 345:
        return "red"
    if h < 45:
        return "orange"
    if h < 65:
        return "yellow"
    if h < 150:
        return "green"
    if h < 200:
        return "cyan"
    if h < 260:
        return "blue"
    if h < 290:
        return "purple"
    if h < 330:
        return "magenta"
    return "neutral"


def get_scale_steps(count: int) -> list[int]:
    canonical = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
    if count <= 0:
        return []
    if count == 1:
        return [500]
    if count >= len(canonical):
        return canonical

    indices = np.linspace(0, len(canonical) - 1, count).round().astype(int)
    return [canonical[int(i)] for i in indices]


def get_dominant_colors(
    image_path: Path,
    num_colors: int = 6,
    sample_size: int = 10000,
    min_distance: float = 50.0,
    seed: int | None = 42,
) -> list[tuple[int, int, int]]:
    image = Image.open(image_path).convert("RGBA")
    pixels = np.array(image).reshape(-1, 4)

    # Ignore fully transparent pixels; these commonly appear around logos and skew results.
    pixels = pixels[pixels[:, 3] > 0]
    if len(pixels) == 0:
        return []

    pixels = pixels[:, :3]

    if len(pixels) > sample_size:
        rng = np.random.default_rng(seed)
        indices = rng.choice(len(pixels), sample_size, replace=False)
        pixels = pixels[indices]

    color_counts = Counter(tuple(map(int, p)) for p in pixels)
    sorted_colors = sorted(color_counts.items(), key=lambda item: item[1], reverse=True)

    selected: list[tuple[int, int, int]] = []
    for color, _count in sorted_colors:
        if len(selected) >= num_colors:
            break

        too_close = False
        for existing in selected:
            dist = sum((a - b) ** 2 for a, b in zip(color, existing)) ** 0.5
            if dist < min_distance:
                too_close = True
                break

        if not too_close:
            selected.append((color[0], color[1], color[2]))

    return selected


def collect_unique_palette(colors_by_image: dict[str, list[tuple[int, int, int]]]) -> list[tuple[int, int, int]]:
    seen: set[tuple[int, int, int]] = set()
    ordered: list[tuple[int, int, int]] = []
    for colors in colors_by_image.values():
        for color in colors:
            if color not in seen:
                seen.add(color)
                ordered.append(color)
    return ordered


def generate_markdown(colors_by_image: dict[str, list[tuple[int, int, int]]], out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Brand Color Guide")
    lines.append("")
    lines.append("Palette extracted from core logo assets.")
    lines.append("")

    for image_name, colors in colors_by_image.items():
        lines.append(f"## {image_name}")
        lines.append("")
        lines.append("| Color | Hex | RGB | Name |")
        lines.append("|---|---|---|---|")

        for rgb in colors:
            hex_color = rgb_to_hex(rgb)
            r, g, b = rgb
            name = get_color_name(rgb)
            lines.append(
                f"| ![{hex_color}](https://via.placeholder.com/24/{hex_color[1:]}) | `{hex_color}` | `rgb({r}, {g}, {b})` | {name} |"
            )

        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def generate_html(colors_by_image: dict[str, list[tuple[int, int, int]]], out_path: Path) -> None:
    html_parts: list[str] = [
        "<!doctype html>",
        "<html lang=\"en\">",
        "<head>",
        "  <meta charset=\"utf-8\">",
        "  <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">",
        "  <title>Brand Color Guide</title>",
        "  <style>",
        "    body { font-family: Segoe UI, Arial, sans-serif; margin: 24px; background: #f8fafc; color: #0f172a; }",
        "    .section { margin-bottom: 28px; }",
        "    .swatches { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; }",
        "    .swatch { border: 1px solid #cbd5e1; border-radius: 8px; overflow: hidden; background: #fff; }",
        "    .chip { height: 84px; display: flex; align-items: center; justify-content: center; font-weight: 600; }",
        "    .meta { padding: 10px; font-size: 12px; line-height: 1.4; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <h1>Brand Color Guide</h1>",
        "  <p>Extracted from core logo assets.</p>",
    ]

    for image_name, colors in colors_by_image.items():
        html_parts.append(f"  <div class=\"section\"><h2>{image_name}</h2><div class=\"swatches\">")
        for rgb in colors:
            hex_color = rgb_to_hex(rgb)
            r, g, b = rgb
            label = get_color_name(rgb)
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            text_color = "#ffffff" if luminance < 0.5 else "#000000"
            html_parts.append(
                "".join(
                    [
                        "<div class=\"swatch\">",
                        f"<div class=\"chip\" style=\"background:{hex_color};color:{text_color};\">{hex_color}</div>",
                        f"<div class=\"meta\">rgb({r}, {g}, {b})<br>{label}</div>",
                        "</div>",
                    ]
                )
            )
        html_parts.append("</div></div>")

    html_parts.extend(["</body>", "</html>"])
    out_path.write_text("\n".join(html_parts), encoding="utf-8")


def generate_css_tokens(colors_by_image: dict[str, list[tuple[int, int, int]]], out_path: Path) -> None:
    palette = collect_unique_palette(colors_by_image)
    lines: list[str] = [
        ":root {",
    ]

    families: dict[str, list[tuple[int, int, int]]] = {}
    for rgb in palette:
        family = get_color_family(rgb)
        families.setdefault(family, []).append(rgb)

    ordered_families = ["neutral", "blue", "cyan", "green", "yellow", "orange", "red", "purple", "magenta"]
    present_families = [name for name in ordered_families if name in families]
    max_canonical_steps = 11

    for family in present_families:
        shades = sorted(families[family], key=relative_luminance, reverse=True)
        if len(shades) > max_canonical_steps:
            # Downsample to canonical scale count so we always emit 50-950 only.
            indices = np.linspace(0, len(shades) - 1, max_canonical_steps).round().astype(int)
            shades = [shades[int(i)] for i in indices]
        scales = get_scale_steps(len(shades))
        lines.append(f"  /* {family} */")
        for scale, rgb in zip(scales, shades):
            hex_color = rgb_to_hex(rgb)
            token = f"--brand-{slugify_label(family)}-{scale}"
            lines.append(f"  {token}: {hex_color};")

    lines.append("}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    input_dir = project_root / "assets" / "core"
    output_dir = project_root / "assets" / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    priority_files = [
        "Primary Logo.png",
        "Master Logo.png",
        "jeremy-fontenot-logo_primary_1024.png",
        "JFITPRO.png",
        "Master Logo-Dark.png",
    ]

    colors_by_image: dict[str, list[tuple[int, int, int]]] = {}

    for file_index, filename in enumerate(priority_files):
        image_path = input_dir / filename
        if image_path.exists():
            colors_by_image[filename] = get_dominant_colors(
                image_path,
                seed=1000 + file_index,
            )

    if not colors_by_image:
        raise FileNotFoundError("No input images found in assets/core.")

    md_out = output_dir / "Brand_Color_Guide.md"
    html_out = output_dir / "Brand_Color_Guide.html"
    css_out = output_dir / "brand-tokens.css"

    generate_markdown(colors_by_image, md_out)
    generate_html(colors_by_image, html_out)
    generate_css_tokens(colors_by_image, css_out)

    print(f"Generated: {md_out}")
    print(f"Generated: {html_out}")
    print(f"Generated: {css_out}")


if __name__ == "__main__":
    main()
