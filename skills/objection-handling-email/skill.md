---
name: Objection Handling Email
slug: objection-handling-email
category: Email
one_shot: true
uses_profile: true
description: Writes a single 400–600 word objection-handling email using a proven 7-step framework that acknowledges, reframes, and overcomes a specific sales hesitation.
keywords: [objection handling, sales email, conversion email, email copywriting, price objection, hesitation, email marketing, sales funnel]
feature: copywriting
quiz:
  - step: 1
    heading: "Your Product & The Objection"
    hint: "Each email addresses one specific objection. Pick the one that kills the most sales for you."
    inputs:
      - name: product_name
        label: "Product or membership name"
        type: text
        placeholder: "e.g. Yoga Business Academy"
      - name: product_type
        label: "What type of product is this?"
        type: select
        options: [Membership site, Online course, Coaching program, Paid community, Paid newsletter, Other]
      - name: price
        label: "Price"
        type: text
        placeholder: "e.g. $297, $97/month, $49/month"
      - name: objection
        label: "Which objection does this email address?"
        type: radio
        options: [It's too expensive, I don't have time for this, I'm not sure it'll work for me, I'm not ready yet — I need to get a few things in place first, I've tried things like this before and it didn't work, Other]
      - name: objection_custom
        label: "(If 'Other') Write the objection in your prospect's exact words"
        type: textarea
        placeholder: "e.g. 'I only have 50 Instagram followers — I don't have an audience to sell to yet'..."
      - name: target_audience
        label: "Who is your target audience? Describe who is most likely to have this objection."
        type: textarea
        placeholder: "e.g. Yoga teachers in years 2-10 of their career, earning under $4,000/month, who love teaching but feel stuck on the income ceiling..."
        from_profile: audience
  - step: 2
    heading: "Benefits & Customer Story"
    hint: "The social proof that makes the reframe believable."
    inputs:
      - name: benefit_1
        label: "Key benefit #1 — a specific outcome your product delivers"
        type: textarea
        placeholder: "e.g. A proven system for building a $3-5k/month membership from scratch, even if you have a tiny audience..."
      - name: benefit_2
        label: "Key benefit #2"
        type: textarea
        placeholder: "e.g. Monthly live Q&A calls where you get direct feedback on your specific business..."
      - name: benefit_3
        label: "Key benefit #3"
        type: textarea
        placeholder: "e.g. A private community of 400+ yoga teachers who are actually building this — not just talking about it..."
      - name: customer_name
        label: "Name of a real customer for the success story"
        type: text
        placeholder: "e.g. Maria K."
      - name: customer_background
        label: "Their situation before finding you — relatable to your audience"
        type: textarea
        placeholder: "e.g. Maria had the exact same objection — she thought she needed 10,000 followers before she could charge for anything online. She had 340..."
      - name: customer_transformation
        label: "What changed? Specific results and timeframe."
        type: textarea
        placeholder: "e.g. 6 months after joining with 340 followers, she had 58 paying members at $49/month — $2,842/month in recurring income. No ads, no viral content."
      - name: customer_quote
        label: "(Optional) A direct quote from this customer"
        type: textarea
        placeholder: "e.g. 'I wish I'd stopped waiting and just started. The audience I needed was already there — I just didn't know how to reach them.'"
---

# Objection Handling Email (7-Step Framework)

Write a single, conversational 400-600 word email that reframes one specific objection and drives action.

## Before Writing

**Check for context profile first:**
If a context profile is available, read it before asking questions. Use that context to understand the user's membership offer, audience, and price point. Only ask for what isn't already covered.

## Step 1: Gather Inputs

Collect all fields below before writing. Ask for any that are missing.

| Field | Example |
|-------|---------|
| Product type | membership, course, coaching program, paid community, paid newsletter, etc. |
| Product name | |
| Price | $297, $97/mo, etc. |
| The specific objection to address | "It's too expensive" / "I don't have time" / "I'm not sure it'll work for me" |
| Benefit 1 | |
| Benefit 2 | |
| Benefit 3 | |
| Target audience description | |
| Customer name (for story) | |
| Customer background | |
| Customer transformation | what changed after using the product |
| Customer quote (optional) | |

---

## Step 2: Write the Email

Follow this exact 7-step structure, in order. Do not skip or reorder steps.

### 1. Subject Line
- Directly state the objection — no softening, no clever wordplay
- Example: "It's too expensive" or "You don't have time for this"
- The bluntness is intentional: it signals you're about to address it head-on

### 2. Sub-subject (Preview Text)
- Follow up with a benefit-focused question that creates intrigue
- Example: "But what if it's the one thing that changes everything?"

### 3. Opening — Acknowledge and Validate
- Open with: **"Hey there!"**
- Immediately name the objection in the first sentence
- Follow with: **"You aren't alone!"** — normalize it, explain that many people feel this way
- Tone: empathetic, not defensive

### 4. Reframe — Shift the Perspective
- Start with: **"OK..."**
- Completely flip the objection — turn the perceived barrier into the reason to act
- Example for price: reframe cost as the cost of *not* solving the problem
- Example for time: reframe the investment as time *saved* long-term
- Keep it punchy — 2-3 short paragraphs max

### 5. Evidence — Back It Up with Numbers
- Include specific data, stats, or metrics that support the reframe
- Follow with: **"And no, we aren't just throwing numbers in the air"** — then add your credibility (case studies, customer count, years in business, etc.)
- Specificity is everything here: "83% of customers" beats "most customers"

### 6. Social Proof — Voice of Doubt → Customer Story
- Transition with: **"Yea, yea... of course you would say that"** (or similar self-aware line)
- Then pivot to the customer story:
  - Who they were before (relatable background)
  - What changed after using the product (specific transformation)
  - A direct quote from them if available
- The story should mirror the target audience's situation closely

### 7. Pricing Ladder + CTA
- Open with: **"So, how much would you pay to unlock these sorts of outcomes?"**
- Then list descending anchor prices (things they already spend money on that cost more)
- Example:
  - A year of gym membership? $600
  - One business coach session? $500
  - [Product Name]? Just $[price]
- Close with a CTA that:
  - States the clear next step (click, buy, book a call)
  - Emphasizes the future benefit they're moving toward
  - Contrasts with the alternative (staying stuck / the cost of doing nothing)

---

## Formatting Rules

- **Tone:** Conversational, direct, confident — sounds like a person, not a marketing email
- **Paragraphs:** 1-3 sentences max, generous white space
- **Length:** 400-600 words total
- **Bold:** Use sparingly for key phrases and the required script lines
- **Humor:** Light and occasional — self-aware beats trying-too-hard
- **One CTA:** Single link, clear action, no competing options
- **Voice:** Write to one person, not a list — "you" not "you all" or "subscribers"
- **No:** Pushy language, exclamation point overload, or anything that sounds like a late-night infomercial

---

## Required Script Lines (Use Verbatim)

These specific phrases must appear in the email:

1. **"Hey there!"** — email opening
2. **"You aren't alone!"** — validation section
3. **"OK..."** — reframe transition
4. **"And no, we aren't just throwing numbers in the air"** — evidence credibility bridge
5. **"Yea, yea... of course you would say that"** (or close variation) — skepticism-to-proof transition
6. **"So, how much would you pay to unlock these sorts of outcomes?"** — pricing ladder opener

---

## Output Format

\`\`\`
**Subject:** [State the objection directly]
**Preview text:** [Benefit-focused question]

[Email body — 400-600 words following the 7-step structure]

[CTA]
\`\`\`

After the email, include a one-line **"What makes this work"** note explaining the core psychological mechanism the email uses — useful for the user to understand why the structure is built the way it is.
