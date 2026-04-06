---
name: Email Welcome Sequence
slug: email-welcome-sequence
category: Email
one_shot: true
processing: prompt
uses_profile: true
description: Generate a complete 5-email welcome sequence for new subscribers using a proven framework that builds trust, agitates pain, demonstrates value, and drives sales.
keywords: [email, welcome, onboarding, subscribers, newsletter, drip, sequence, nurture]
feature: copywriting
quiz:
  - step: 1
    heading: "Your Details"
    hint: "The basics about you and your offer. These details will appear throughout all 5 emails."
    inputs:
      - name: your_name
        label: "Your name (as it will appear in emails)"
        type: text
        placeholder: "e.g. Jane Smith"
      - name: membership_type
        label: "What type of membership or product do you sell?"
        type: select
        options: [Online Courses / Training, Paid Community, Association or NPO, Paid Newsletter, Coaching Program, Podcast Membership, Hybrid]
      - name: product_name
        label: "Product or membership name"
        type: text
        placeholder: "e.g. Yoga Business Academy"
      - name: price_point
        label: "Price point"
        type: text
        placeholder: "e.g. $497 one-time, $97/month, $249/year"
      - name: lead_magnet_name
        label: "What did subscribers download to join your list? (Your lead magnet name)"
        type: text
        placeholder: "e.g. The 5-Day Membership Launch Checklist"
  - step: 2
    heading: "Your Audience & Offer"
    hint: "The deeper context that makes these emails feel personal and specific."
    inputs:
      - name: target_audience
        label: "Describe your target audience — who they are, what they're trying to accomplish."
        type: textarea
        placeholder: "e.g. Yoga teachers 2-10 years in who want to build recurring online income without burning out or becoming a full-time content creator..."
        from_profile: audience
      - name: core_problem
        label: "The main pain point your audience experiences — the central struggle they face."
        type: textarea
        placeholder: "e.g. They love teaching but feel trapped trading hours for dollars, with no idea how to build predictable income online..."
      - name: unique_method
        label: "Your unique method, framework, or approach — what makes how you solve this different from everything else out there?"
        type: textarea
        placeholder: "e.g. The Sustainable Studio Method — build a $3-5k/month membership using only 3 hours/week of content creation..."
      - name: guarantee
        label: "Your guarantee or refund policy"
        type: text
        placeholder: "e.g. 30-day money-back guarantee, no questions asked"
  - step: 3
    heading: "Your Success Story"
    hint: "A real customer story for Email 3 — the more specific and relatable, the better it converts."
    inputs:
      - name: customer_name
        label: "Name of a real customer for the success story"
        type: text
        placeholder: "e.g. Maria K."
      - name: customer_background
        label: "Their situation before finding you — make it as relatable as possible to your audience."
        type: textarea
        placeholder: "e.g. Maria was a 12-year veteran yoga teacher making $2,100/month from private clients, working 45 hours a week and exhausted..."
      - name: customer_transformation
        label: "What changed after using your product? Specific results, metrics, and timeframes."
        type: textarea
        placeholder: "e.g. Within 90 days she had 47 paying members at $49/month, added $2,300/month in recurring income, and reduced her in-person hours by 30%..."
      - name: customer_quote
        label: "(Optional) A direct quote from this customer"
        type: textarea
        placeholder: "e.g. 'I can't believe I waited so long. This paid for itself in the first month and I finally feel like I have a real business.'"
---

# 5-Day Welcome Email Sequence

Generate a high-converting 5-email welcome sequence that builds trust, agitates pain, demonstrates value, and drives sales.

## Before Writing

**Check for context profile first:**
If a context profile is available, read it before asking questions. Use that context to understand the user's membership niche, audience, and offer. Only ask for information not already covered.

## Step 1: Gather Required Information

Before writing, collect these inputs (ask for any that are missing):

| Field | Example |
|-------|---------|
| Your Name | Jane Smith |
| Membership Type / Niche | courses & coaching, paid community, association, paid newsletter, podcast membership |
| Core Problem You Solve | Main pain point your audience experiences |
| Product/Service Name | What you're selling |
| Product Category | Membership / Course / Coaching / Community / Newsletter / etc. |
| Price Point | $497, $97/mo, etc. |
| Lead Magnet Name | What subscribers downloaded to join the list |
| Target Audience | Specific demographic/psychographic |
| Unique Method/Approach | Your proprietary system or framework |
| Success Story | Customer name, before/after, timeframe, specific results |
| Guarantee Terms | Refund policy or risk-reversal offer |

If the user has provided all details upfront, skip straight to writing.

---

## Step 2: Write All 5 Emails

For each email, produce exactly this structure:

```
**Subject Line:** [5-8 words, curiosity-driven]

**Email Body:** [250-450 words]

**Key Psychological Triggers:** [list]

**Call-to-Action:** [specific action]
```

---

## Email Frameworks

### Day 1 — Problem Agitation
*Trigger: Pain amplification + relatability*

- Open with a pattern interrupt or bold statement
- Share a personal struggle that mirrors the reader's pain
- Name 3 specific negative symptoms/consequences they're experiencing
- "Twist the knife" with a vivid low-point moment
- Tease the solution without revealing it
- Preview what's coming tomorrow

### Day 2 — Solution Introduction
*Trigger: Hope + curiosity + authority*

- Open by calling out what doesn't work (common mistake story)
- Share the discovery moment that changed everything
- Reveal personal transformation with specific metrics (numbers, timeframes)
- Introduce the product/method by name
- Position it as the result of hard-won experience
- Build anticipation: "Tomorrow I'm sharing a story from someone just like you…"

### Day 3 — Social Proof
*Trigger: Credibility through third-party validation*

- Lead with the customer's before state (make it relatable)
- Walk through their transformation narrative with a timeline
- Include their initial skepticism, then what changed their mind
- Share specific, measurable results
- Soft-introduce the product with a link to learn more

### Day 4 — Product Details
*Trigger: Value demonstration + risk reversal*

- Position this as a complete system, not just another solution
- Detail 4+ core features with specific benefit explanations (not feature lists — outcomes)
- Differentiate from generic alternatives
- State the guarantee clearly and confidently
- Present pricing with a value-stack framing

### Day 5 — Closing / Urgency
*Trigger: Urgency + scarcity + final objection handling*

- Recap the journey and value delivered across the sequence
- Address the 5 most common objections directly and briefly
- Paint the "pain of staying stuck" vs. "cost of action"
- Reinforce the guarantee
- Include 2-3 CTA variations (link text variety)
- Offer personal availability for questions

---

## Writing Rules (Apply to All Emails)

**Formatting**
- Max 1-3 sentences per paragraph
- Use bold sparingly for emphasis
- Short scannable structure (mobile-first)
- Bullet points only when listing 3+ items

**Voice**
- Conversational, like writing to a friend
- Specific over generic: use exact numbers, names, timeframes
- Emotion first, logic second
- No hype language; let results speak

**Copywriting Techniques**
- Bucket brigade transitions ("Here's the thing…", "But wait—", "And that's when…")
- Future pacing ("Imagine opening your inbox and seeing…")
- Sensory language that creates mental images
- Objection anticipation woven naturally into copy

---

## Quality Checklist

Before delivering the sequence, verify each email:

- [ ] Subject line is 5-8 words and curiosity-driven
- [ ] Opens with a pattern interrupt (not "Hi, I'm…")
- [ ] Contains at least one specific number or metric
- [ ] Has a single, clear CTA
- [ ] Flows naturally into the next day's preview (Days 1-4)
- [ ] 250-450 words
- [ ] No paragraph longer than 3 sentences

---

## Output Format

Deliver all 5 emails sequentially. After the sequence, add a brief **Customization Notes** section flagging any placeholders the user needs to fill in (e.g., `[INSERT CUSTOMER NAME]`, `[ADD SPECIFIC RESULT HERE]`).
