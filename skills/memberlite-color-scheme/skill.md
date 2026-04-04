---
name: Memberlite Color Scheme
slug: memberlite-color-scheme
category: PMPro
one_shot: true
uses_profile: false
description: Extracts a color palette from your logo and outputs a complete custom Memberlite color scheme — all 17 color values ready to enter in the WordPress Customizer or apply via CSS custom properties.
keywords: [Memberlite, color scheme, CSS, branding, PMPro theme, logo colors, custom CSS, WordPress theme, color palette, customizer]
feature: design
quiz:
  - step: 1
    heading: "Your Brand Colors"
    hint: "Provide as much color detail as you can. Hex codes produce the most accurate results. A logo URL works too if the image is publicly accessible."
    inputs:
      - name: brand_name
        label: "Your brand or site name"
        type: text
        placeholder: "e.g. Yoga Business Academy"
      - name: primary_color
        label: "Primary brand color — the dominant color in your logo or brand"
        type: text
        placeholder: "e.g. #1a4a8e or 'deep navy blue'"
      - name: secondary_color
        label: "Secondary color — supporting or complementary tone"
        type: text
        placeholder: "e.g. #4a9a6e or 'warm sage green'"
      - name: action_color
        label: "(Optional) Accent / action color — used for CTAs and highlights, often the most saturated"
        type: text
        placeholder: "e.g. #f5a623 or 'bright amber orange'"
      - name: logo_url
        label: "(Optional) Logo URL — paste a publicly accessible link and colors will be extracted directly"
        type: url
        placeholder: "e.g. https://yoursite.com/wp-content/uploads/logo.png"
      - name: header_style
        label: "What style of site header do you want?"
        type: radio
        options: [Light header (dark text on white or light background), Dark header (light text on dark or colored background), Brand-colored header (brand primary as background)]
      - name: footer_style
        label: "What style of footer do you want?"
        type: radio
        options: [Dark footer, Light footer, Brand-colored footer]
---

# Memberlite Color Scheme

Extract your brand colors from a logo and generate a complete, ready-to-apply Memberlite color scheme — all 17 color values assigned, with instructions for applying them in WordPress.

## How to Provide Your Logo

**Option 1 — URL:**
Paste the URL to your logo image. If your tool supports web fetching, it will analyze the image directly.

**Option 2 — Upload:**
If your AI tool supports image uploads, attach your logo file to the conversation.

**Option 3 — Describe your colors:**
Provide your primary brand color(s) by hex code or description (e.g., "deep navy blue and warm gold"). The more specific, the better the output.

---

## Step 1: Extract the Color Palette

From the logo (or description), identify the following brand colors:

| Role | What to look for |
|------|-----------------|
| **Primary** | The dominant brand color — most prominent in the logo |
| **Secondary** | A supporting color — often a lighter or complementary tone |
| **Action / Accent** | The high-energy color for CTAs, highlights, attention — often the most saturated |
| **Dark text** | Near-black for body text — extracted from the logo's darkest tone, or standard `222222` |
| **Background** | Usually white or off-white; sometimes a light tint of the primary |

If the logo is monochromatic, suggest a complementary accent color that pairs well with it.

Present the extracted palette before assigning values:

```
Brand Palette Extracted:
  Primary:   #[hex] — [description]
  Secondary: #[hex] — [description]
  Action:    #[hex] — [description]
  Dark text: #[hex]
  Background: #[hex]
```

Flag any WCAG AA contrast failures (4.5:1 for body text, 3:1 for large text/UI).

---

## Step 2: Map to All 17 Memberlite Color Settings

Memberlite uses exactly 17 color settings. Assign a value to each one.

The CSS custom properties these generate follow the pattern `--memberlite--color--{css_var}`.

| Setting Key | CSS Variable | Label | Assignment Strategy |
|-------------|-------------|-------|---------------------|
| `color_primary` | `--memberlite--color--primary` | Primary | → Brand primary |
| `color_secondary` | `--memberlite--color--secondary` | Secondary | → Brand secondary |
| `color_action` | `--memberlite--color--action` | Action | → Brand action/accent |
| `color_button` | `--memberlite--color--button` | Buttons | → Brand primary or action (depends on contrast) |
| `color_link` | `--memberlite--color--link` | Links | → Brand primary (must pass contrast on white bg) |
| `color_meta_link` | `--memberlite--color--meta-link` | Meta Links | → Brand secondary or a muted tone of primary |
| `color_text` | `--memberlite--color--text` | Text | → Dark text (near-black) |
| `background_color` | `--memberlite--color--site-background` | Site Background | → White or light brand background |
| `color_borders` | `--memberlite--color--borders` | Borders | → Light gray (e.g., `e0e0e0`) or light tint of primary |
| `header_textcolor` | `--memberlite--color--header-text` | Header Text | → Dark or light depending on header bg |
| `bgcolor_header` | `--memberlite--color--header-background` | Header Background | → White, light, or brand primary |
| `bgcolor_site_navigation` | `--memberlite--color--site-navigation-background` | Site Navigation Background | → Matches or complements header bg |
| `color_site_navigation` | `--memberlite--color--site-navigation` | Site Navigation | → Readable on nav bg; often dark text or white |
| `bgcolor_page_masthead` | `--memberlite--color--page-masthead-background` | Page Masthead Background | → Brand primary (strong, rich) |
| `color_page_masthead` | `--memberlite--color--page-masthead` | Page Masthead | → White or light (for contrast on masthead bg) |
| `bgcolor_footer_widgets` | `--memberlite--color--footer-widgets-background` | Footer Widgets Background | → Dark, light, or brand color |
| `color_footer_widgets` | `--memberlite--color--footer-widgets` | Footer Widgets | → Readable on footer bg |

---

## Step 3: Output the Color Scheme

### A. Customizer Values (Primary Method)

Apply these in **Appearance > Customize > Colors** in WordPress. Enter each hex value (without the `#`):

```
Primary:                      [hex without #]
Secondary:                    [hex without #]
Action:                       [hex without #]
Buttons:                      [hex without #]
Links:                        [hex without #]
Meta Links:                   [hex without #]
Text:                         [hex without #]
Site Background:              [hex without #]
Borders:                      [hex without #]
Header Text:                  [hex without #]
Header Background:            [hex without #]
Site Navigation Background:   [hex without #]
Site Navigation:              [hex without #]
Page Masthead Background:     [hex without #]
Page Masthead:                [hex without #]
Footer Widgets Background:    [hex without #]
Footer Widgets:               [hex without #]
```

**Note:** The Customizer "Color Scheme" dropdown has a "Custom" option — select that before entering individual values, or your custom values may be overwritten when a preset scheme is applied.

---

### B. CSS Custom Properties Override (Advanced / Child Theme)

For child themes or additional CSS that needs to override Memberlite's generated values, use these properties (generated from the same values above):

```css
/* Memberlite Custom Color Scheme — [Brand Name] */
/* Apply in: Appearance > Customize > Additional CSS OR child theme style.css */

:root {
    --memberlite--color--primary:                    #[hex];
    --memberlite--color--secondary:                  #[hex];
    --memberlite--color--action:                     #[hex];
    --memberlite--color--button:                     #[hex];
    --memberlite--color--link:                       #[hex];
    --memberlite--color--meta-link:                  #[hex];
    --memberlite--color--text:                       #[hex];
    --memberlite--color--site-background:            #[hex];
    --memberlite--color--borders:                    #[hex];
    --memberlite--color--header-text:                #[hex];
    --memberlite--color--header-background:          #[hex];
    --memberlite--color--site-navigation-background: #[hex];
    --memberlite--color--site-navigation:            #[hex];
    --memberlite--color--page-masthead-background:   #[hex];
    --memberlite--color--page-masthead:              #[hex];
    --memberlite--color--footer-widgets-background:  #[hex];
    --memberlite--color--footer-widgets:             #[hex];
}
```

---

## Step 4: Closest Built-In Scheme Reference

Memberlite ships with 10 preset color schemes. After generating the custom palette, note which built-in scheme it's closest to — useful if the user wants a starting point before customizing:

| Scheme | Character |
|--------|-----------|
| Default | Navy primary, teal secondary, orange action |
| Evergreen | Forest greens, vibrant pink action |
| Seaside Linen | Warm tan background, deep blue, chartreuse action |
| Deep Harbor | Cool blue tones, sage green |
| Midnight Violet | Dark mode, purple |
| Cocoa Ash | Dark warm browns, orange action |
| Gotham | Dark blues, peach accent |
| Soft Spruce | Clean grays, green primary, amber action |
| Iron Ember | Charcoal, rust orange |
| Slate Harbor | Deep navy, teal secondary, coral action |

Suggest: "Your palette is closest to [Scheme]. Start with that preset, then apply your custom overrides."

---

## Output Format

```
## [Brand Name] — Memberlite Color Scheme

### Extracted Palette
Primary:    #[hex] — [description]
Secondary:  #[hex] — [description]
Action:     #[hex] — [description]
(+ any additional colors)

### Accessibility Check
[List any contrast failures and suggested adjustments]

### Closest Built-In Scheme
[Scheme name + brief note]

### Customizer Values
[17-row table: Label → hex (no #)]

### CSS Custom Properties Block
[Full :root { } block, ready to copy]
```
