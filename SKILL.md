---
name: human-color-touch
description: >
  Gives AI agents human-eye color sensibility using 48 curated, human-voted color palettes.
  Eliminates generic AI color defaults (neon purple-cyan gradients, harsh pure black/white,
  unbalanced saturation) and enforces natural visual hierarchy, 60-30-10 proportion, and
  WCAG AA/AAA contrast compliance across web apps, dashboards, marketing pages, and slides.
version: 1.0.0
author: DangerousAngel (https://github.com/DangerousAngel)
license: MIT
---

# HumanColorTouch Skill

Developed by **DangerousAngel** (`https://github.com/DangerousAngel`).

## Purpose

AI-generated interfaces are immediately recognizable when they default to oversaturated neon accents, generic indigo-to-cyan gradients, or sterile `#000000` / `#FFFFFF` contrast. **HumanColorTouch** equips the AI agent with 48 curated, human-favored palettes and a deterministic design workflow so every UI, presentation, visualization, or brand artifact feels intentionally crafted by a human designer.

## Mandatory Operating Rules

1. **Select From the Curated Dataset First**:
   - Always pick a single primary palette from `palettes/palettes.json` (or `references/PALETTE_CATALOG.md`) that matches the project's domain, emotional tone, and light/dark mode requirement.
   - Never mix random swatches from unrelated palettes unless explicitly requested by the user.

2. **Ban Generic "AI Slop" Color Habits**:
   - Do **not** default to generic purple-blue-pink neon gradients (`#6366F1` -> `#EC4899`) unless the user explicitly asks for cyberpunk/neon.
   - Do **not** use pure `#000000` backgrounds with `#FFFFFF` text unless using `Black & Gold Elegance` intentionally; prefer warm off-whites (`#FAF0CA`, `#FEFAE0`, `#F4F1DE`, `#F8F9FA`) and deep tinted inks (`#0D1B2A`, `#001219`, `#22223B`, `#2F3E46`, `#212529`).
   - Do **not** place two high-saturation colors directly on top of each other.

3. **Enforce the 60-30-10 Proportion Rule**:
   - **60% Dominant Neutral / Canvas**: Background and breathing space (lightest warm/cool neutral or deepest tinted dark).
   - **30% Secondary / Structure**: Cards, sidebars, borders, subtle surface elevation, and secondary headers.
   - **10% Accent / Action**: Primary CTAs, active indicators, key metrics, and focal highlights.

4. **Verify WCAG 2.1 Contrast Ratios**:
   - Normal body text MUST meet at least **4.5:1** contrast (WCAG AA).
   - Large text (>= 18pt or 14pt bold) and UI controls MUST meet at least **3.0:1**.
   - Use the pre-computed `semantic_roles` in `palettes/palettes.json` or run `scripts/select_palette.py` to verify contrast before emitting CSS/HTML.

5. **Respect Optical Luminance (`is_light`)**:
   - Each swatch in `palettes/palettes.json` includes `luminance` (0.0 to 1.0) and `is_light` metadata.
   - Place dark text on `is_light: true` surfaces and light text on `is_light: false` surfaces.

## Agent Workflow

When asked to design or style a UI, webpage, dashboard, chart, or visual asset:

1. **Identify Intent & Mood**: Classify the request into one of six aesthetic categories:
   - `oceanic-tech` — SaaS, cloud infrastructure, developer tools, analytics, security.
   - `organic-earthy` — Wellness, sustainability, artisan brands, food, editorial.
   - `minimal-neutral` — Documentation, architecture, productivity, portfolios, clean corporate.
   - `warm-dramatic` — Luxury, hospitality, storytelling, cinema, heatmaps.
   - `energetic-modern` — Consumer apps, travel, education, product launches.
   - `soft-pastel` — Creative studios, calm apps, lifestyle, playful brands.
   - `luxury-contrast` — Executive dashboards, fintech, high-impact dark mode.
   - `editorial-bold` — News, bold branding, modern agencies.

2. **Select a Palette**:
   - Query `palettes/palettes.json` or run:
     ```bash
     python scripts/select_palette.py --category oceanic-tech --mode dark --format css
     ```
   - State the chosen palette name and hex codes concisely in your design rationale.

3. **Map to Semantic Tokens**:
   - Never hardcode raw hex values throughout components.
   - Emit CSS custom properties (`--hct-bg`, `--hct-surface`, `--hct-primary`, `--hct-accent`, `--hct-text`, `--hct-border`) using `templates/ui_tokens_template.css` or `palettes/palettes.css`.

4. **Apply Subtle Depth & Elevation**:
   - In light mode, elevate cards with a lighter surface + soft tinted border (10-15% opacity of the darkest swatch) instead of heavy black drop shadows.
   - In dark mode, step surfaces slightly lighter than the canvas (`surface` > `background`) and use crisp 1px translucent borders (`rgba(..., 0.12)`).

## Reference Files

- `palettes/palettes.json` — Full dataset of all 48 curated palettes with hex, RGB, relative luminance, temperature, mood tags, and WCAG-verified semantic tokens.
- `palettes/palettes.css` — Drop-in CSS custom properties for all 48 palettes (light and dark modes).
- `references/PALETTE_CATALOG.md` — Categorized visual/text catalog for rapid palette lookup.
- `references/HUMAN_COLOR_PRINCIPLES.md` — Theory and practical rules behind human-eye color perception.
- `templates/ui_tokens_template.css` — Production CSS token and component starter sheet.
- `scripts/select_palette.py` — Zero-dependency CLI selector, WCAG contrast checker, and CSS/Tailwind exporter.
- `SYSTEM_PROMPT.md` — Standalone prompt for LLMs without native skill-file loading.
