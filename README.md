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

### 1. Use as an AI Agent Skill (Claude Code, Gemini, OpenClaw, Agent Skills Spec)
Clone this repository into your agent's skills directory:

```bash
git clone https://github.com/DangerousAngel/HumanColorTouch_skill.git
```

Point your agent to `SKILL.md`. The agent will automatically reference `palettes/palettes.json`, `references/PALETTE_CATALOG.md`, and `templates/ui_tokens_template.css` when generating interfaces, dashboards, or visual layouts.

### 2. Use with Any LLM (ChatGPT, Gemini Gems, Cursor `.cursorrules`)
Copy the prompt block from `SYSTEM_PROMPT.md` into your system instructions or `.cursorrules` file.

### 3. Query & Export Palettes via CLI
No external Python packages are required:

```bash
# List all available aesthetic categories
python scripts/select_palette.py --list-categories

# Find oceanic/tech palettes
python scripts/select_palette.py --category oceanic-tech

# Export Deep Sea as dark-mode CSS variables
python scripts/select_palette.py --slug deep-sea --mode dark --format css

# Export Olive Garden Feast as Tailwind config
python scripts/select_palette.py --slug olive-garden-feast --mode light --format tailwind
```

## Included Categories

- **Oceanic & Tech**: `Deep Sea`, `Ocean Blue Serenity`, `Coastal Blues`, `Deep Ocean Blue`, `Ocean Blue Adventure`, `Sky Blue Freshness`, `Blue Gradient`
- **Organic & Earthy**: `Olive Garden Feast`, `Meadow Green`, `Leafy Green Garden`, `Fresh Greens`, `Warm Neutral Tones`, `Earthy Tones`, `Earthy Green`, `Autumn Harvest`
- **Minimal & Neutral**: `Neutral Harmony Bliss`, `Light Steel`, `Golden Summer Fields`, `Soft Sand`, `Soft Lavender`, `Monochrome Beach`, `Vintage Charm`
- **Warm & Dramatic**: `Ocean Sunset`, `Dark Sunset`, `Fiery Red Sunset`, `Crimson Hues`, `Bold Berry`
- **Energetic & Modern**: `Refreshing Summer Fun`, `Summer Dream`, `Golden Summer Glow`, `Tropical Sunrise`, `Sunny Beach Day`
- **Luxury & High-Contrast**: `Black & Gold Elegance`, `Golden Twilight`, `Vivid Nightfall`, `Velvet Plum & Rose`
- **Editorial & Bold**: `Fiery Ocean`, `Summer Ocean Breeze`, `Espresso & Cyan Pop`
- **Soft Pastel & Playful**: `Pastel Dreamland Adventure`, `Soft Pink Delight`, `Pastel Serenity`, `Candy Pop Confetti`

## License

MIT License — Copyright (c) 2026 DangerousAngel.
