# HumanColorTouch_skill

An AI Agent Skill repository developed by **DangerousAngel** (`https://github.com/DangerousAngel`) that equips AI coding and design agents with human-eye color sensibility.

Instead of defaulting to artificial, oversaturated "AI gradients" or harsh pure black-and-white contrast, agents using **HumanColorTouch** select from **48 curated, human-favored palettes**, enforce the 60-30-10 visual proportion rule, and automatically map colors to WCAG 2.1 AA-verified semantic tokens.

## Repository Structure

```text
HumanColorTouch_skill/
├── SKILL.md                         # Core AI agent skill instructions & YAML metadata
├── SYSTEM_PROMPT.md                 # Standalone prompt for any LLM without a skill loader
├── README.md                        # Repository documentation
├── LICENSE                          # MIT License
├── assets/
│   └── swatches/                    # SVG color frames for all 48 palettes
├── palettes/
│   ├── palettes.json                # All 48 palettes with RGB, luminance, tags, and semantic roles
│   └── palettes.css                 # Drop-in CSS variables for every palette (light & dark modes)
├── references/
│   ├── PALETTE_CATALOG.md           # Categorized lookup table of all 48 palettes
│   └── HUMAN_COLOR_PRINCIPLES.md    # Optical luminance, tinted neutrals, and proportion rules
├── templates/
│   └── ui_tokens_template.css       # Starter semantic CSS tokens & glassmorphism/card classes
└── scripts/
    └── select_palette.py            # Zero-dependency CLI selector & CSS/Tailwind exporter
```

## Quick Start

### Use as an AI Agent Skill (Claude Code, Gemini, OpenClaw, Agent Skills Spec)
Clone this repository into your agent's skills directory:

```bash
git clone https://github.com/DangerousAngel/HumanColorTouch_skill.git
```

Point your agent to `SKILL.md`. The agent will automatically reference `palettes/palettes.json`, `references/PALETTE_CATALOG.md`, and `templates/ui_tokens_template.css` when generating interfaces, dashboards, or visual layouts.

## Included Categories

### Oceanic & Tech

![](assets/swatches/ocean-blue-serenity.svg) ![](assets/swatches/sky-blue-freshness.svg) ![](assets/swatches/deep-sea.svg) ![](assets/swatches/coastal-blues.svg) ![](assets/swatches/ocean-blue-adventure.svg) ![](assets/swatches/deep-ocean-blue.svg) ![](assets/swatches/blue-gradient.svg)

### Organic & Earthy

![](assets/swatches/olive-garden-feast.svg) ![](assets/swatches/terracotta-rose-sage.svg) ![](assets/swatches/meadow-green.svg) ![](assets/swatches/leafy-green-garden.svg) ![](assets/swatches/fresh-greens.svg) ![](assets/swatches/warm-neutral-tones.svg) ![](assets/swatches/earthy-tones.svg) ![](assets/swatches/earthy-tones-2.svg) ![](assets/swatches/autumn-harvest.svg) ![](assets/swatches/earthy-green.svg)

### Minimal & Neutral

![](assets/swatches/neutral-harmony-bliss.svg) ![](assets/swatches/light-steel.svg) ![](assets/swatches/golden-summer-fields.svg) ![](assets/swatches/soft-sand.svg) ![](assets/swatches/soft-lavender.svg) ![](assets/swatches/muted-slate-stone.svg) ![](assets/swatches/monochrome-beach.svg) ![](assets/swatches/vintage-charm.svg)

### Warm & Dramatic

![](assets/swatches/ocean-sunset.svg) ![](assets/swatches/dark-sunset.svg) ![](assets/swatches/ocean-sunset-2.svg) ![](assets/swatches/fiery-red-sunset.svg) ![](assets/swatches/crimson-hues.svg) ![](assets/swatches/bold-berry.svg)

### Energetic & Modern

![](assets/swatches/refreshing-summer-fun.svg) ![](assets/swatches/summer-dream.svg) ![](assets/swatches/golden-summer-glow.svg) ![](assets/swatches/botanical-citrus-plum.svg) ![](assets/swatches/tropical-sunrise.svg) ![](assets/swatches/sunny-beach-day.svg)

### Luxury & High-Contrast

![](assets/swatches/black-gold-elegance.svg) ![](assets/swatches/velvet-plum-rose.svg) ![](assets/swatches/vivid-nightfall.svg) ![](assets/swatches/golden-twilight.svg)

### Editorial & Bold

![](assets/swatches/fiery-ocean.svg) ![](assets/swatches/summer-ocean-breeze.svg) ![](assets/swatches/espresso-cyan-pop.svg)

### Soft Pastel & Playful

![](assets/swatches/pastel-dreamland-adventure.svg) ![](assets/swatches/soft-pink-delight.svg) ![](assets/swatches/pastel-serenity.svg) ![](assets/swatches/candy-pop-confetti.svg)

## License

MIT License — Copyright (c) 2026 DangerousAngel.

