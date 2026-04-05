---
name: Membership CTA Block
slug: membership-cta-block
category: PMPro
one_shot: true
uses_profile: true
description: Generates a styled HTML/CSS call-to-action block for promoting your membership anywhere on your site — with instructions for saving it as a WordPress Synced Pattern for easy reuse.
keywords: [CTA block, call to action, membership promotion, HTML CTA, WordPress CTA, synced pattern, membership widget, conversion block, inline promotion]
feature: copywriting
quiz:
  - step: 1
    heading: "Your Membership & Message"
    hint: "This block gets dropped into blog posts, resource pages, and anywhere you want to invite visitors to join. The headline and copy should feel native to whatever page it appears on."
    inputs:
      - name: membership_name
        label: "Membership name"
        type: text
        placeholder: "e.g. Yoga Business Academy"
      - name: target_audience
        label: "Who are you writing to in this block? One sentence."
        type: textarea
        placeholder: "e.g. Yoga teachers who want to build recurring online income without burning out..."
        from_profile: audience
      - name: headline
        label: "Headline for this CTA block — OR describe the context and we'll write one for you."
        type: textarea
        placeholder: "e.g. 'Ready to build a yoga membership that pays you consistently?' OR 'leave blank and write something for a yoga business blog post about pricing'"
      - name: value_proposition
        label: "What do members get or what problem does this solve? 1-3 key points."
        type: textarea
        placeholder: "40+ courses on building a yoga business online\nMonthly live Q&A calls with real feedback\nA private community of 400+ yoga teachers"
      - name: price
        label: "(Optional) Price to show in the block — including this significantly increases clicks"
        type: text
        placeholder: "e.g. From $49/month"
  - step: 2
    heading: "Style & Links"
    hint: "The visual details that make this block match your brand."
    inputs:
      - name: cta_button_text
        label: "CTA button text"
        type: text
        placeholder: "e.g. Join Now, Become a Member, See Plans, Get Started"
      - name: cta_url
        label: "CTA button URL"
        type: url
        placeholder: "e.g. https://yoursite.com/membership-account/levels/"
      - name: secondary_cta
        label: "(Optional) Secondary CTA text — typically a login link or a softer next step"
        type: text
        placeholder: "e.g. Already a member? Log in here."
      - name: visual_style
        label: "Visual style"
        type: radio
        options: [Minimal / clean — understated, lots of white space, Bold / high-contrast — attention-grabbing, Warm / inviting — friendly and approachable]
      - name: brand_color
        label: "Primary brand color hex code (for button and accent)"
        type: text
        placeholder: "e.g. #006799"
---

# Membership CTA Block

Generate a drop-in HTML/CSS call-to-action block to promote your membership on any page: blog posts, resource pages, the homepage, anywhere. Built to paste into WordPress and saved as a Synced Pattern so you can reuse and update it sitewide from one place.

## What This Is (and Isn't)

This is a **standalone promotional block** — a section you add intentionally to a page or post to invite visitors to join.

It is **not** the locked content message (which appears automatically when content is protected). For that, see the **locked-content-teaser** skill.

---

## Before Writing

**Check for context profile first:**
If a context profile is available, read it to understand the membership name, audience, and pricing before asking questions.

## Step 1: Gather Required Information

| Field | Notes |
|-------|-------|
| Membership name | |
| Target audience | Who you're writing to in this block |
| Headline | Or describe the context and the skill will write it |
| The core value proposition | What do they get / what problem does this solve? |
| CTA button text | e.g., "Join Now," "Become a Member," "See Plans," "Get Started" |
| CTA button URL | Your levels page or a specific landing page |
| Price (optional) | Including it increases conversions; leaving it out is fine for awareness blocks |
| Secondary CTA (optional) | e.g., "Learn more →" or "Already a member? Log in." |
| Visual style | Minimal/clean, bold/high-contrast, warm/inviting |
| Brand primary color | Hex code for button and accent color |

---

## Step 2: Write the CTA Block

### Components

**1. Eyebrow (optional)** — 2-4 word label above the headline
- Examples: "For [audience]", "Membership", "Join Us"

**2. Headline** — The main reason to act
- Lead with outcome or invitation, not the membership name
- Example: "Get the [outcome] you've been looking for." / "Join [X] [audience] building [thing]."

**3. Supporting text** — 1-3 sentences expanding the headline
- What's included (keep it to 1-2 highlights, not a full list)
- Who it's for
- Any urgency or context

**4. Primary CTA button**

**5. Secondary CTA or login link** (recommended)

---

## Step 3: Output the HTML/CSS Block

Produce clean, self-contained HTML with inline styles (so it works anywhere in WordPress without relying on theme CSS):

```html
<div style="background:#[bg-color];border:1px solid #[border-color];border-radius:8px;padding:32px 40px;margin:40px 0;text-align:center;max-width:680px;margin-left:auto;margin-right:auto;">
  <!-- Eyebrow (optional) -->
  <p style="font-size:13px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:#[accent-color];margin:0 0 12px 0;">[Eyebrow]</p>

  <!-- Headline -->
  <h2 style="font-size:1.75rem;font-weight:700;color:#[headline-color];margin:0 0 16px 0;line-height:1.2;">[Headline]</h2>

  <!-- Supporting text -->
  <p style="font-size:1rem;color:#[text-color];margin:0 0 28px 0;line-height:1.6;">[Supporting text. 1-3 sentences max.]</p>

  <!-- Primary CTA button -->
  <a href="[CTA_URL]" style="display:inline-block;background:#[button-color];color:#fff;font-weight:600;font-size:1rem;padding:14px 32px;border-radius:6px;text-decoration:none;margin-bottom:12px;">[Button Text]</a>

  <!-- Secondary CTA or login link (optional) -->
  <p style="font-size:0.875rem;color:#[muted-text-color];margin:12px 0 0 0;">
    [Already a member? <a href="/membership-account/" style="color:#[accent-color];text-decoration:underline;">Log in here</a>.]
  </p>
</div>
```

Fill in all color placeholders with real hex values from the brand.

---

## Step 4: WordPress Synced Pattern Instructions

A **Synced Pattern** (formerly "Reusable Block") lets you save this CTA once and insert it anywhere on your site. Update it once, and every instance updates automatically. Perfect for a membership CTA you want on dozens of posts.

**To save as a Synced Pattern:**

1. In the WordPress block editor, add an **HTML block** (`/html` or Custom HTML)
2. Paste the CTA code into the HTML block
3. Click the HTML block to select it
4. Open the block options menu (**⋮**) in the toolbar
5. Click **"Create pattern"**
6. Name it (e.g., "Membership CTA — Main") and check **"Synced"**
7. Click **"Create"**

**To insert it anywhere:**
- Type `/pattern` in the block editor
- Or use the block inserter and search "Patterns"
- Select your saved pattern

**To update it sitewide:**
- Go to **Appearance > Patterns** (or **Patterns** in the WordPress sidebar)
- Find your pattern and edit it
- All instances on the site update automatically

---

## Output Format

```
## Membership CTA Block

**Copy:**
Eyebrow: [text]
Headline: [text]
Body: [text]
Button: [text] → [URL]
Secondary: [text]

---

**HTML Block (paste into WordPress Custom HTML block):**

[HTML code here]

---

**Setup instructions:**
[Summary of Synced Pattern steps above, condensed]
```
