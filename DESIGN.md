# Design System Strategy: High-End Editorial Landing Page

## 1. Overview & Creative North Star: "The Glacial Editorial"
This design system moves away from the "generic SaaS" aesthetic into the realm of high-end digital editorialism. The Creative North Star is **The Glacial Editorial**—a philosophy that treats the web browser as a premium physical space. 

Rather than relying on rigid, boxed-in grids, this system leverages **intentional asymmetry and tonal depth** to guide the eye. We use the "Icy Lake" palette not just for decoration, but to create a sense of vast, quiet power. The experience should feel like walking through a contemporary art gallery: spacious, sophisticated, and quietly confident. We achieve this by breaking the standard 12-column expectations, utilizing overlapping elements, and favoring "breathing room" (negative space) as a core functional component.

---

## 2. Colors: The Icy Palette & Tonal Logic
Our palette is a sophisticated blend of deep nautical anchors and crystalline highlights.

### The "No-Line" Rule
To maintain a premium feel, **1px solid borders are strictly prohibited for sectioning.** We define boundaries through tonal shifts. A section should end and another begin simply by transitioning from `surface` (#f7f9fb) to `surface-container-low` (#f2f4f6). This creates a "soft" boundary that feels intentional and modern.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of frosted glass sheets.
*   **Base:** `surface` (#f7f9fb)
*   **Secondary Sections:** `surface-container-low` (#f2f4f6)
*   **Interactive Cards:** `surface-container-lowest` (#ffffff) sitting on top of `surface-container` (#eceef0).
*   **Deep Anchors:** Use `primary` (#001629) or `tertiary` (#06161a) for high-impact footer or header backgrounds.

### The "Glass & Gradient" Rule
For floating elements or hero visual assets, use Glassmorphism. Apply a background color of `surface_container_lowest` at 60% opacity with a `20px` backdrop-blur. 
*   **Signature Textures:** Use subtle linear gradients for CTAs, moving from `primary` (#001629) to `primary_container` (#002b49) at a 135-degree angle. This adds a "soulful" depth that mimics the light refracting through deep water.

---

## 3. Typography: Editorial Authority
The type system pairs the geometric precision of **Manrope** with the high-legibility utility of **Inter**.

*   **Display & Headlines (Manrope):** These are your "voice." `display-lg` (3.5rem) should be used with tight letter-spacing (-0.02em) to create an authoritative, editorial impact. Use asymmetry—align these headlines to the far left or slightly "off-center" to break the grid.
*   **Body & Titles (Inter):** These are your "information." `body-lg` (1rem) is the workhorse. It must always have generous line-height (1.6) to ensure the "Spacious" feel requested.
*   **Hierarchy as Identity:** By using a massive scale jump between `display-lg` and `body-lg`, we create a high-contrast visual rhythm that feels like a premium print magazine.

---

## 4. Elevation & Depth: Tonal Layering
Traditional drop shadows are too "dirty" for an icy lake aesthetic. We use **Tonal Layering**.

*   **The Layering Principle:** Depth is achieved by "stacking." Place a `surface-container-lowest` card on a `surface-container-low` section. The slight delta in brightness creates a "lift" that is felt rather than seen.
*   **Ambient Shadows:** If a shadow is required for a floating CTA or Modal, use a "Cyan-Tinted Shadow."
    *   *Offset: 0 12px 32px | Color: #001629 at 6% opacity.*
    *   This mimics natural light passing through ice, rather than a generic grey shadow.
*   **The "Ghost Border" Fallback:** If a container needs more definition (e.g., in a search input), use a **Ghost Border**: `outline-variant` (#c3c7ce) at **15% opacity**. Never use a 100% opaque border.

---

## 5. Components: Refined Interaction

### Buttons
*   **Primary:** A gradient from `primary` to `primary_container`. No border. Roundedness: `md` (0.375rem). Text: `title-sm` (Inter, Semibold, White).
*   **Secondary:** `secondary_container` background with `on_secondary_container` text.
*   **Tertiary:** No background. `primary` text with an underline that only appears on hover.

### Cards & Lists
*   **NO DIVIDER LINES.** To separate items in a list or cards in a grid, use `2rem` of vertical white space or a subtle background toggle between `surface` and `surface-container-low`.
*   **Hover State:** Cards should transition from `surface-container` to `surface-container-lowest` on hover, accompanied by the Cyan-Tinted Ambient Shadow.

### Input Fields
*   **Style:** Minimalist. No bottom line or full box. Use a subtle `surface-container-high` fill with a `sm` (0.125rem) radius. 
*   **Interaction:** On focus, the background transitions to `surface-container-lowest` with a 1px "Ghost Border" in `primary_fixed_dim`.

### Signature Component: The "Ice-Chip" 
*   **Chips:** For categories or tags, use `secondary_fixed_dim` (#b0cade) with 30% opacity. This creates a "frosted" look that perfectly complements the Icy Lake theme.

---

## 6. Do's and Don'ts

### Do
*   **DO** use whitespace as a functional tool. If a section feels crowded, double the padding.
*   **DO** use asymmetrical layouts. Let a photo overlap a text container by 40px to create depth.
*   **DO** use the `primary` navy color for text on `surface` backgrounds to maintain high contrast and sophistication.

### Don't
*   **DON'T** use pure black (#000000). Our darkest anchor is `tertiary` (#06161a).
*   **DON'T** use standard 1px borders to separate content. It breaks the "Glacial" flow.
*   **DON'T** use aggressive "bounce" animations. Transitions should be slow, linear, or ease-out (e.g., 400ms) to mimic the stillness of a frozen lake.
*   **DON'T** use high-saturation accent colors. Stay within the icy blue/navy/grey spectrum to preserve the sophisticated palette.