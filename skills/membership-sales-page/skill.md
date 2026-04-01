---
name: Membership Sales Page
slug: membership-sales-page
category: Copy
one_shot: true
uses_profile: true
description: Writes a complete membership sales page — hero, problem, solution, what's included, social proof, FAQ, and CTA — with a shortcode placeholder for the PMPro levels table. One-shot output ready to build in WordPress.
keywords: [membership sales page, sales page copy, landing page, membership page, PMPro levels, conversion copy, membership marketing]
---

# Membership Sales Page

Write a complete membership sales page from scratch — every section, in order, ready to build in WordPress. The levels/pricing table uses a PMPro shortcode placeholder; this skill doesn't rebuild what PMPro already does well.

**Two ways to use this output:**
1. **Paste and format manually** — use the copy as your source, build the page in the WordPress block editor or your page builder.
2. **Convert to block editor code** — run the output through the **wordpress-page-blocks** skill to get block editor code view HTML ready to paste directly into WordPress.

---

## Before Writing

**Check for context profile first:**
If a context profile is available, read it before asking questions. Use that context to understand the membership type, offer, audience, and pricing.

## Step 1: Gather Required Information

Ask for any fields that are missing:

**About the membership:**
| Field | Example |
|-------|---------|
| Membership name | The Photography Guild, SENsible SENCO |
| Membership type | Courses, community, newsletter, association, coaching, podcast, directory |
| Target audience (one sentence) | Who is this specifically for? |
| The core problem they have | What are they struggling with before they join? |
| The transformation or outcome | What does life look like after joining? |
| Price(s) and billing period(s) | $29/mo, $249/year, etc. |
| Levels table shortcode to use | `[pmpro_levels]` OR `[advanced_levels_page]` |

**What's included:**
| Field | Example |
|-------|---------|
| Primary benefit (the headline offer) | 40+ courses, weekly calls, etc. |
| Supporting benefits (3-6 more) | Forum, resource library, office hours, etc. |
| Who this is NOT for | Optional but powerful |

**Social proof:**
| Field | Example |
|-------|---------|
| Member count or time in business | "Join 800+ members" or "running since 2019" |
| 1-2 member testimonials | Name, title/context, quote |
| Any notable results or outcomes | "Members report X" |

**Objections:**
| Field | Example |
|-------|---------|
| 3-5 FAQs or known objections | Price, commitment, fit, cancellation policy |

---

## Step 2: Write the Sales Page

Produce all sections in order. Each section is clearly labeled for easy building in WordPress.

---

### SECTION 1 — Hero

**Purpose:** Establish who this is for, what they get, and make them want to keep reading.

Components:
- **Headline** (H1): Outcome-first or audience-first. Not the membership name — that goes in the subheadline.
- **Subheadline** (H2 or large paragraph): Expand the headline. Name the membership. Invite the right person.
- **Hero CTA button**: "Join [Membership Name]" or "See Membership Options" → links to the levels section
- **Social proof line** (optional but strong): "[X] members" or "Trusted by [audience type] since [year]"

---

### SECTION 2 — The Problem

**Purpose:** Make the right reader feel seen. Describe their current situation with specificity.

Components:
- 2-4 paragraphs OR a list of "if you've ever felt..." statements
- Name the frustration, the wasted time, the wrong tool, the isolation
- End with a transitional sentence pointing toward the solution

---

### SECTION 3 — The Solution (Membership Introduction)

**Purpose:** Introduce the membership as the answer, without over-explaining.

Components:
- 1-2 paragraphs introducing the membership by name
- Frame it as the thing that solves the specific problem named above
- What makes it different: the approach, the community, the format

---

### SECTION 4 — What's Included

**Purpose:** Make the value tangible and specific.

Components:
- Section headline: "Everything included in [Membership Name]" or "What you get"
- Each benefit as a named item + 1-2 sentence description (outcome-oriented)
- If there are multiple tiers, name the key difference at the bottom: "Compare all plans below →"

---

### SECTION 5 — Levels / Pricing Table

**Purpose:** Let the member choose their tier. This uses PMPro — don't rebuild it.

Output for this section:

```
[Place the following shortcode here to display your membership levels and pricing:]

[pmpro_levels]

— OR, if using the Advanced Levels Page Add On —

[advanced_levels_page]
```

Below the shortcode placeholder, add:
- Guarantee or cancellation policy (1-2 sentences): "Cancel anytime, no questions asked."
- Payment security note: "Secure checkout powered by [Stripe/PayPal]."

---

### SECTION 6 — Who This Is For (and Who It's Not)

**Purpose:** Help the right person self-select. Reduce refunds and churn by qualifying before checkout.

Components:
- "This is for you if..." (3-5 bullets)
- "This is NOT for you if..." (2-3 bullets, honest)

---

### SECTION 7 — Social Proof

**Purpose:** Validate the decision with evidence from real members.

Components:
- 1-2 member testimonials (name, role/context, quote)
- Format: blockquote style with attribution
- If no testimonials yet: use member count, tenure, or notable outcomes instead

---

### SECTION 8 — FAQ

**Purpose:** Handle the final objections that stop fence-sitters.

Components:
- 4-6 Q&A pairs covering: price/value, cancellation, what's included, who it's for, how it works
- Keep answers honest and direct — don't over-reassure

---

### SECTION 9 — Final CTA

**Purpose:** Close with clarity and confidence.

Components:
- Restate the headline benefit in one sentence
- One CTA button: "Join [Membership Name]" or "Become a Member" → links to levels section
- Optional: secondary CTA if there's a free tier or lead magnet ("Not ready? Start with our free [X].")

---

## Writing Rules

**Specificity over enthusiasm.**
"40+ courses, 800 members, weekly live calls" beats "an incredible community with tons of resources."

**Write to one person.**
The ideal member. Use "you" throughout. Avoid "our members" until the social proof section.

**Earn the scroll.**
Each section should create enough curiosity or value to pull the reader to the next one.

**The levels table does the selling at the price level.**
Your job in the copy is to get them to the table already wanting to join. Let PMPro handle the mechanics.

---

## Output Format

Deliver all 9 sections in order, clearly labeled:

```
# SECTION 1 — HERO
[Headline]
[Subheadline]
[CTA button text + destination]
[Social proof line]

# SECTION 2 — THE PROBLEM
[Copy]

... (continue through all 9 sections)
```

After the full page copy, include a **Build Notes** section:
- Recommended page layout notes (full-width hero? two-column benefits?)
- Which shortcode to use based on their setup
- Any placeholder copy that still needs real numbers or testimonials
- Tip: "To convert this output to WordPress block editor code, run it through the **wordpress-page-blocks** skill."
