---
name: WordPress Page Blocks
slug: wordpress-page-blocks
category: PMPro
one_shot: true
uses_profile: false
description: Converts page copy — from the Membership Sales Page skill or any other source — into WordPress block editor code view HTML, ready to paste directly into the WordPress editor.
keywords: [WordPress blocks, block editor, code view, Gutenberg, page builder, WordPress copy, block editor HTML, WordPress page]
feature: design
quiz:
  - step: 1
    heading: "Your Page Copy & Settings"
    hint: "Paste your page copy and describe the layout. Output is block editor code view HTML — paste it directly into WordPress via the Code Editor (⋮ menu → Code editor)."
    inputs:
      - name: page_copy
        label: "Paste the full page copy you want to convert. Include all sections — headlines, body, bullets, testimonials, FAQs, CTAs."
        type: textarea
        placeholder: "HERO\nHeadline: Build a Yoga Membership That Pays You Consistently\nSubheadline: Join 400+ yoga teachers inside Yoga Business Academy...\n\nTHE PROBLEM\n..."
      - name: section_structure
        label: "Describe the sections and any layout notes. Which sections are present?"
        type: textarea
        placeholder: "Full-width hero section, 3-column benefits grid, testimonial quote, PMPro levels shortcode, accordion FAQ, centered CTA at bottom"
      - name: pmpro_shortcode
        label: "Which PMPro shortcode goes in the levels / pricing section?"
        type: radio
        options: [[pmpro_levels], [advanced_levels_page], No PMPro shortcode needed]
      - name: brand_color
        label: "Primary brand color hex code (for CTA button styling)"
        type: text
        placeholder: "e.g. #006799"
      - name: layout_notes
        label: "(Optional) Any multi-column sections, special blocks, or layout preferences?"
        type: textarea
        placeholder: "e.g. The benefits section should be 3 columns on desktop. The hero should have a dark overlay. The FAQ should be collapsible if possible."
---

# WordPress Page Blocks

Take page copy (from the **membership-sales-page** skill, a draft doc, or anywhere else) and convert it into WordPress block editor code view HTML, ready to paste into WordPress.

## How to Use This Skill

1. Paste your page copy (or a section of it) into the conversation
2. Describe the layout intent: full-width hero? two-column benefits? accordion FAQ?
3. This skill outputs block editor code view HTML you can paste directly into WordPress:
   - Go to your page in WordPress
   - Click the **⋮ options menu** → **Code editor** (or press `Ctrl/Cmd + Shift + Alt + M`)
   - Paste the output, then switch back to Visual editor to review

---

## Before Converting

Ask for any missing context:

- **Page copy:** Full text or section(s) to convert (required)
- **Section structure:** Which sections are present? (hero, benefits, FAQ, CTA, etc.)
- **Layout preferences:** Any multi-column sections? Button styles?
- **PMPro shortcode:** Which shortcode goes in the levels section — `[pmpro_levels]` or `[advanced_levels_page]`?
- **Brand color for buttons:** Hex code (e.g., `#006799`) — used for CTA button background

---

## Block Reference

Use these block patterns for each content type:

### Paragraph
```html
<!-- wp:paragraph -->
<p>[Text here]</p>
<!-- /wp:paragraph -->
```

### Heading (H1)
```html
<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">[Heading text]</h1>
<!-- /wp:heading -->
```

### Heading (H2)
```html
<!-- wp:heading {"level":2} -->
<h2 class="wp-block-heading">[Heading text]</h2>
<!-- /wp:heading -->
```

### Heading (H3)
```html
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">[Heading text]</h3>
<!-- /wp:heading -->
```

### Button (single)
```html
<!-- wp:buttons -->
<div class="wp-block-buttons">
  <!-- wp:button {"backgroundColor":"[color-slug]","style":{"color":{"background":"#[hex]"}}} -->
  <div class="wp-block-button"><a class="wp-block-button__link has-background wp-element-button" href="[URL]" style="background-color:#[hex]">[Button text]</a></div>
  <!-- /wp:button -->
</div>
<!-- /wp:buttons -->
```

### Unordered List
```html
<!-- wp:list -->
<ul class="wp-block-list">
  <!-- wp:list-item -->
  <li>[Item]</li>
  <!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
```

### Separator / Divider
```html
<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->
```

### Quote / Testimonial
```html
<!-- wp:quote -->
<blockquote class="wp-block-quote">
  <!-- wp:paragraph -->
  <p>[Quote text]</p>
  <!-- /wp:paragraph -->
  <cite>[Name, Title or Context]</cite>
</blockquote>
<!-- /wp:quote -->
```

### PMPro Shortcode (Levels Table)
```html
<!-- wp:shortcode -->
[pmpro_levels]
<!-- /wp:shortcode -->
```

Or for Advanced Levels Page Add On:
```html
<!-- wp:shortcode -->
[advanced_levels_page]
<!-- /wp:shortcode -->
```

### Two Columns
```html
<!-- wp:columns -->
<div class="wp-block-columns">
  <!-- wp:column -->
  <div class="wp-block-column">
    [column 1 blocks here]
  </div>
  <!-- /wp:column -->
  <!-- wp:column -->
  <div class="wp-block-column">
    [column 2 blocks here]
  </div>
  <!-- /wp:column -->
</div>
<!-- /wp:columns -->
```

### FAQ (Details / Accordion — requires Gutenberg or theme support)
For simple FAQ without a plugin, use heading + paragraph pairs:
```html
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">[Question]</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>[Answer]</p>
<!-- /wp:paragraph -->
```

### Cover Block (Hero with background)
```html
<!-- wp:cover {"overlayColor":"black","minHeight":400,"isDark":true} -->
<div class="wp-block-cover is-dark" style="min-height:400px">
  <span aria-hidden="true" class="wp-block-cover__background has-black-background-color has-background-dim"></span>
  <div class="wp-block-cover__inner-container">
    [heading and paragraph blocks here]
  </div>
</div>
<!-- /wp:cover -->
```

---

## Conversion Process

Work section by section. For each section of the provided copy:

1. Identify the content type (heading, body, list, quote, CTA, shortcode)
2. Wrap it in the appropriate block markup
3. Preserve the copy exactly. Don't rewrite.
4. Use the two-column block for any side-by-side layouts
5. Place the PMPro shortcode block where the levels table belongs

---

## Output Format

Deliver the complete block editor code view HTML in a single code block, ready to paste.

After the code block, add a brief **Paste Instructions** note:

```
PASTE INSTRUCTIONS
──────────────────
1. Open your page in WordPress
2. Click the ⋮ menu (top right) → "Code editor" (or Ctrl/Cmd + Shift + Alt + M)
3. Select all existing content and replace with this code
4. Switch back to Visual editor to review
5. Update/Publish
```

If the output is very long, offer to deliver it one section at a time.
