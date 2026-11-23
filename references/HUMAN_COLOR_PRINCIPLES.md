# Human-Eye Color Principles

Why do human-designed interfaces feel calm, cohesive, and trustworthy while default AI-generated UIs often feel jarring or artificial?

## 1. Tinted Neutrals Over Pure Achromatic Extremes
In physical environments, light is never perfectly neutral. Daylight carries a cool blue cast; indoor tungsten light carries warm amber. Human designers mimic this by tinting whites and blacks slightly toward the palette's dominant hue:
- Instead of `#FFFFFF`, use warm cream (`#FEFAE0`, `#F4F1DE`, `#FDF0D5`) or cool mist (`#F8F9FA`, `#EBF2FA`, `#F1FAEE`).
- Instead of `#000000`, use deep navy ink (`#0D1B2A`, `#001219`), forest charcoal (`#132A13`, `#283618`), or plum slate (`#22223B`).

## 2. The 60-30-10 Proportion Rule
Human visual comfort depends on resting space. If every component shouts with equal saturation, the eye experiences fatigue:
- **60% Canvas**: Low-chroma background that lets content breathe.
- **30% Structural Surfaces**: Cards, navigation panels, dividers, and secondary typography.
- **10% Focal Accent**: Reserved strictly for primary actions, active states, and critical callouts.

## 3. Optical Luminance and Simultaneous Contrast
Two colors with identical numeric saturation can look wildly different in brightness because human cone cells are most sensitive to green (~71.5%), moderately sensitive to red (~21.3%), and least sensitive to blue (~7.2%).
- This is why WCAG relative luminance uses:
  `L = 0.2126 * R + 0.7152 * G + 0.0722 * B` (in linearized sRGB).
- A vivid yellow (`#FFD60A`) has very high luminance and requires dark ink (`#000814`), whereas a vivid navy (`#03045E`) has very low luminance and requires light ink (`#CAF0F8`).

## 4. Dark Mode Elevation Without Muddy Shadows
Drop shadows are nearly invisible on dark backgrounds. Human UI designers communicate depth in dark mode by:
1. Using the darkest palette tone for the base canvas (e.g., `#0D1B2A` in *Deep Sea*).
2. Stepping elevated cards one shade lighter (`#1B263B`).
3. Adding subtle 1px borders at 10-18% opacity of a lighter cool/warm swatch (`#778DA9`).

## 5. Semantic Restraint
Never assign all 5 to 10 swatches of a palette to random UI widgets. In multi-stop palettes (such as *Ocean Sunset* or *Meadow Green*), treat the gradient scale as a **tonal ramp** for hover states, borders, charts, and badges—while keeping the core UI anchored to 1 background, 1 surface, 1 text ink, and 1 primary accent.
