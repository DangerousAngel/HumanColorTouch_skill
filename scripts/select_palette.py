#!/usr/bin/env python3
"""
HumanColorTouch Palette Selector & Exporter
Developed by DangerousAngel (https://github.com/DangerousAngel)

Zero-dependency CLI tool for AI agents and developers to query palettes.json
by slug, category, temperature, tag, or mode, and export CSS variables,
Tailwind theme extensions, or JSON.
"""

import argparse
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DATA = os.path.join(os.path.dirname(SCRIPT_DIR), "palettes", "palettes.json")


def load_palettes(path=DEFAULT_DATA):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["palettes"]


def format_css(p, mode):
    roles = p["semantic_roles"]["dark_mode" if mode == "dark" else "light_mode"]
    lines = [
        f'/* HumanColorTouch: {p["name"]} ({mode} mode) */',
        ":root {",
        f'  --hct-bg: {roles["background"]};',
        f'  --hct-surface: {roles["surface"]};',
        f'  --hct-primary: {roles["primary"]};',
        f'  --hct-accent: {roles["accent"]};',
        f'  --hct-text: {roles["text"]};',
    ]
    for i, c in enumerate(p["colors"], 1):
        lines.append(f'  --hct-swatch-{i}: {c["hex"]};')
    lines.append("}")
    return "\n".join(lines)


def format_tailwind(p, mode):
    roles = p["semantic_roles"]["dark_mode" if mode == "dark" else "light_mode"]
    swatches = {f"swatch-{i}": c["hex"] for i, c in enumerate(p["colors"], 1)}
    config = {
        "theme": {
            "extend": {
                "colors": {
                    "hct": {
                        "bg": roles["background"],
                        "surface": roles["surface"],
                        "primary": roles["primary"],
                        "accent": roles["accent"],
                        "text": roles["text"],
                        **swatches
                    }
                }
            }
        }
    }
    return json.dumps(config, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Query HumanColorTouch curated palettes.")
    parser.add_argument("--slug", help="Exact palette slug (e.g. deep-sea)")
    parser.add_argument("--category", help="Filter by category (e.g. oceanic-tech, organic-earthy)")
    parser.add_argument("--temp", choices=["warm", "cool", "balanced"], help="Filter by color temperature")
    parser.add_argument("--tag", help="Filter by domain tag (e.g. saas, editorial, dark-ui)")
    parser.add_argument("--mode", choices=["light", "dark"], default="light", help="Target UI mode for export")
    parser.add_argument("--format", choices=["summary", "css", "tailwind", "json"], default="summary")
    parser.add_argument("--list-categories", action="store_true", help="List available categories")
    args = parser.parse_args()

    palettes = load_palettes()

    if args.list_categories:
        cats = sorted(set(p["category"] for p in palettes))
        print("\n".join(cats))
        return

    results = palettes
    if args.slug:
        results = [p for p in results if p["slug"] == args.slug]
    if args.category:
        results = [p for p in results if p["category"] == args.category]
    if args.temp:
        results = [p for p in results if p["temperature"] == args.temp]
    if args.tag:
        t = args.tag.lower()
        results = [p for p in results if any(t in tag.lower() for tag in p["tags"])]

    if not results:
        print("No matching palettes found.", file=sys.stderr)
        sys.exit(1)

    if args.format == "summary":
        for p in results:
            swatches = " ".join(c["hex"] for c in p["colors"])
            print(f'[{p["id"]:02d}] {p["name"]} ({p["slug"]}) | {p["category"]} | {p["temperature"]} | {swatches}')
    elif args.format == "css":
        print(format_css(results[0], args.mode))
    elif args.format == "tailwind":
        print(format_tailwind(results[0], args.mode))
    elif args.format == "json":
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))


if __name__ == "__main__":
    main()
