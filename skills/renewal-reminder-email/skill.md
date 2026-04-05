---
name: Renewal Reminder Email
slug: renewal-reminder-email
category: Email
one_shot: true
uses_profile: true
description: Writes a 3-email proactive renewal sequence (30 days, 7 days, expiry day) to reduce passive churn before a membership expires — warm, value-focused, not alarming.
keywords: [renewal email, membership renewal, expiring membership, renewal reminder, retention email, subscription renewal, PMPro renewal, membership expiry]
feature: copywriting
quiz:
  - step: 1
    heading: "Membership Details"
    hint: "Annual renewals are high-stakes; monthly are lower-stakes. The output changes based on what's expiring."
    inputs:
      - name: membership_name
        label: "Membership name"
        type: text
        placeholder: "e.g. Yoga Business Academy"
      - name: level_name
        label: "Which membership level is expiring?"
        type: text
        placeholder: "e.g. Member, Studio Pro, Annual"
      - name: membership_type
        label: "What type of membership is this?"
        type: select
        options: [Online Courses / Training, Paid Community, Association or NPO, Paid Newsletter, Coaching Program, Podcast Membership, Member Directory, Hybrid]
      - name: billing_period
        label: "Billing period for this level"
        type: radio
        options: [Monthly, Annual]
      - name: renewal_price
        label: "Price at renewal"
        type: text
        placeholder: "e.g. $49/month or $397/year"
      - name: renewal_url
        label: "URL where members go to renew"
        type: url
        placeholder: "e.g. https://yoursite.com/membership-account/"
      - name: auto_vs_manual
        label: "Is billing automatic, or do members need to take action to renew?"
        type: radio
        options: [Auto-renew — billing is automatic (focus is preventing cancellations and failed payments), Manual renewal — members must take action to renew (focus is motivating the click)]
      - name: output_mode
        label: "What do you need?"
        type: radio
        options: [Single improved renewal email (better than the PMPro default), Full 3-email sequence (30 days out, 7 days out, expiry day)]
  - step: 2
    heading: "Value & Messaging"
    hint: "Renewal emails that reinforce value outperform ones that just warn about losing access."
    inputs:
      - name: most_valuable_thing
        label: "The most valuable thing about this membership — what would members miss most if they let it lapse?"
        type: textarea
        placeholder: "e.g. The monthly live Q&A calls — that direct feedback on their specific business is irreplaceable. The private community they've built relationships in over the past year..."
      - name: recent_additions
        label: "Any notable new content, improvements, or features added since they joined? (Reinforces value)"
        type: textarea
        placeholder: "e.g. Added 8 new courses on pricing and email marketing, launched a members-only podcast feed, upgraded the community platform..."
      - name: tone
        label: "Tone of the renewal emails"
        type: select
        options: [Warm and personal — like a note from a friend, Matter-of-fact and practical — informational and clear, Celebratory — they're hitting a membership milestone]
---

# Renewal Reminder Email Sequence

Write a 3-email renewal reminder sequence sent before a membership expires, reducing passive churn by reminding members of the value they're about to lose before it disappears.

## PMPro Context

PMPro sends a single built-in renewal reminder email (configurable in the PMPro Email settings). That single email does the minimum.

This skill helps you write either:
1. **An improved single renewal reminder email** — a better version of the built-in email to replace the default
2. **A 3-email proactive sequence** — sent through a connected email service (ConvertKit, Mailchimp, ActiveCampaign, etc.) at 30 days, 7 days, and the expiry day

For a sequence, the emails are sent through your email provider, not PMPro. PMPro's built-in reminder can still send on the day of expiry as a fallback.

---

## Before Writing

**Check for context profile first:**
If a context profile is available, read it before asking questions. Use that context to understand the membership type, audience, and pricing.

## Step 1: Gather Required Information

| Field | Notes |
|-------|-------|
| Membership name and level | Which level is expiring? |
| Membership type | Course, community, newsletter, association, coaching, podcast, directory |
| Billing period | Monthly or annual? (annual renewals are higher stakes) |
| Price at renewal | $X/month or $X/year |
| Renewal URL | Where do they go to renew? (usually PMPro account page or checkout) |
| The most valuable thing about the membership | What would they miss most if they let it lapse? |
| Any notable new content or improvements since they joined | Recent additions that reinforce value |
| Tone | Warm and personal, matter-of-fact, celebratory (if milestone) |
| Output mode | Single improved email OR full 3-email sequence? |

---

## Step 2: Write the Renewal Sequence

### Email 1 — 30 Days Before Expiry
**Purpose:** Heads-up, value reinforcement. No urgency yet.
**Tone:** Friendly, not alarming. A note, not a warning.

Must include:
- Acknowledge that renewal is coming up (matter-of-fact, not scary)
- Reinforce one specific piece of value they've had access to
- Mention what's new or coming up, and give them something to look forward to
- One low-pressure CTA: "Your renewal is set automatically" (if auto-renew) or "Renew early if you'd like" (if manual)
- Don't make them feel like they're about to lose something at this stage

### Email 2 — 7 Days Before Expiry
**Purpose:** Gentle urgency. Remind them what's at stake.
**Tone:** Helpful, specific, clear about what happens if they let it expire.

Must include:
- Clear subject line noting the timing ("Your membership renews in 7 days")
- Specific reminder of what they'll lose access to if they don't renew
- A brief "what's been good" callback — remind them of value received
- If billing is automatic: reassure them it's handled, but confirm their card is current
- If manual renewal: a clear, direct CTA to renew now
- Payment update link if needed

### Email 3 — Expiry Day
**Purpose:** Final opportunity. Clear, direct, no anxiety-inducing language.
**Tone:** Direct and helpful, not desperate.

Must include:
- Very short — 100-150 words max
- State clearly: today is the day
- One direct CTA: "Renew today →"
- What they'll lose access to (specific is better than vague)
- Make reactivation feel easy: "It takes less than a minute"
- No guilt, no drama — matter-of-fact and respectful

---

## Writing Rules

**Reinforce value, not fear.**
Renewal emails fail when they read like late notices. The member isn't delinquent. Their membership is ending. Write to remind them why they joined, not to warn them about what they'll lose.

**Be specific about value.**
"You'll lose access to the community" is weaker than "You'll lose access to 600+ active members, weekly office hours, and the full course library you've been working through."

**Annual renewals deserve more attention.**
A $249 annual renewal is a bigger moment than a $29/month. For annual memberships, Email 1 should arrive 60 days out, not 30. Adjust if needed.

**Auto-renew vs. manual renew changes the tone:**
- Auto-renew: reassure and remind; the goal is to prevent cancellations and failed payments
- Manual renew: motivate action; the goal is to get them to click

**Keep Email 3 very short.**
On expiry day, they either renew or they don't. A long email won't change that. Make it easy to say yes.

---

## Output Format

```
---
**Email 1 — 30 Days Out**
**Subject:** [Subject line]

[Email body]

**CTA:** [Button text] → [URL]

---
**Email 2 — 7 Days Out**
**Subject:** [Subject line]

[Email body]

**CTA:** [Button text] → [URL]

---
**Email 3 — Expiry Day**
**Subject:** [Subject line]

[Email body]

**CTA:** [Button text] → [URL]
---
```

After the sequence, include a **Setup Notes** section:
- Which emails can be sent through PMPro's built-in notifications vs. an external ESP
- Recommended timing if different from defaults (e.g., 60/14/1 for annual memberships)
- Any PMPro merge tags relevant for personalizing the email (e.g., `!!display_name!!`, `!!membership_expiration!!`)
