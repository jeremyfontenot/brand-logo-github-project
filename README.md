# Brand Logo Project

This repository documents how I designed and packaged my personal IT brand logo system, including source-ready logo exports, color extraction workflow, and brand documentation.

## What This Project Contains

- Core logo assets used as the visual source of truth
- Automated color extraction workflow in Python
- Generated brand color guides (Markdown and HTML)
- Brand standards and profile documentation
- Reproducible folder structure for publishing and collaboration

## Repository Structure

```text
brand-logo-github-project/
  assets/
    core/                # Primary logo files used to derive branding
    references/          # Visual reference variants and background treatments
    outputs/             # Generated artifacts (color guides, tokens)
  docs/
    Jeremy_Fontenot_Brand_Standards.md
    Jeremy_Fontenot_Profile_Cloud_First.md
    LOGO_CREATION_WORKFLOW.md
  scripts/
    extract_brand_colors.py
  requirements.txt
  .gitignore
  LICENSE
```

## Quick Start

1. Clone the repository.
2. Install dependencies.
3. Run the color extraction script.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\extract_brand_colors.py
```

Generated files are written to `assets/outputs/`:

- `Brand_Color_Guide.md`
- `Brand_Color_Guide.html`
- `brand-tokens.css`

## Source Inputs

The script processes these core files by default:

- `assets/core/Primary Logo.png`
- `assets/core/Master Logo.png`
- `assets/core/Master Logo-Dark.png`
- `assets/core/jeremy-fontenot-logo_primary_1024.png`
- `assets/core/JFITPRO.png`

## Visual Evolution References

These reference visuals are included to document logo treatment across background styles:

- `assets/references/Brand Image.png`
- `assets/references/logo_dark_background.png`
- `assets/references/logo_light_background.png`

## Documentation Included

- `docs/LOGO_CREATION_WORKFLOW.md` for design and production workflow
- `docs/Jeremy_Fontenot_Brand_Standards.md` for usage standards
- `docs/Jeremy_Fontenot_Profile_Cloud_First.md` for profile and positioning
- `assets/outputs/Brand_Color_Guide.md` and `assets/outputs/Brand_Color_Guide.html` for extracted palette references

## Notes

- This repository preserves final assets and a reproducible color analysis workflow.
- Color extraction is deterministic to avoid unnecessary output diffs between runs.
- `brand-tokens.css` now uses semantic family + canonical scale naming (50-950 only, e.g., `--brand-neutral-50`, `--brand-blue-700`) for easier design-system use.
- The visual design process itself was iterative; this repo captures the documented process and final outputs for publication.

## Publishing to GitHub

```powershell
git init
git add .
git commit -m "Initial commit: brand logo project with docs and workflow"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```
