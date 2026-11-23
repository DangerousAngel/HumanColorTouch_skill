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

### Use as an AI Agent Skill (Claude Code, Gemini, OpenClaw, Agent Skills Spec)
Clone this repository into your agent's skills directory:

```bash
git clone https://github.com/DangerousAngel/HumanColorTouch_skill.git
```

Point your agent to `SKILL.md`. The agent will automatically reference `palettes/palettes.json`, `references/PALETTE_CATALOG.md`, and `templates/ui_tokens_template.css` when generating interfaces, dashboards, or visual layouts.

## License

MIT License — Copyright (c) 2026 DangerousAngel.
