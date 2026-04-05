---
name: Membership Level Description
slug: membership-level-description
category: PMPro
one_shot: true
uses_profile: true
description: Writes compelling level names, taglines, and benefit descriptions for the PMPro levels page — making the value of each tier instantly clear so browsers become members.
keywords: [membership level, level description, pricing page, tier description, PMPro levels, membership copy, tier copy, level benefits]
feature: copywriting
quiz:
  - step: 1
    heading: "Membership Overview"
    hint: "The context that shapes how each level is described and who each tier is written for."
    inputs:
      - name: membership_type
        label: "What type of membership is this?"
        type: select
        options: [Online Courses / Training, Paid Community, Association or NPO, Paid Newsletter, Coaching Program, Podcast Membership, Member Directory, Hybrid]
      - name: ideal_member
        label: "Who is your ideal member? One sentence describing who this is for."
        type: textarea
        placeholder: "e.g. Independent yoga teachers who want to build a sustainable online income without burning out..."
        from_profile: audience
      - name: level_count
        label: "How many membership levels are you describing?"
        type: radio
        options: [1 level, 2 levels, 3 levels, 4 or more levels]
  - step: 2
    heading: "Level Details"
    hint: "For best results, fill this out for every level — name, price, what's included, and the one thing that makes it worth it."
    inputs:
      - name: level_details
        label: "For each level: Name, Price + billing period, Who it's specifically for, What's included (list features, content, access), What the next tier adds (if any), The one thing that makes this tier worth it. Separate levels with a blank line."
        type: textarea
        placeholder: "LEVEL 1: Free\nPrice: Free\nFor: Anyone curious about yoga business\nIncludes: 3 starter lessons, newsletter access, community read-only\nBest reason: Get a taste before committing\n\nLEVEL 2: Member — $49/month\nFor: Teachers actively building their business\nIncludes: 40+ courses, monthly live calls, full community access, template library\nBest reason: The monthly live Q&A — bring your real questions and get real answers\n\nLEVEL 3: Studio Pro — $149/month\nFor: Teachers ready to scale with private support\nIncludes: Everything in Member + monthly 1:1 strategy call, private Slack channel, done-for-you content reviewed\nBest reason: The 1:1 monthly strategy call — your own advisor who knows your business"
        from_profile: levels
---

# Membership Level Description

Write membership level names, taglines, and benefit descriptions that make the value of each tier immediately clear, to the right person, at the right price.

## Before Writing

**Check for context profile first:**
If a context profile is available, read it to understand the user's membership type, audience, and existing level structure. Only ask for information not already covered.

## Step 1: Gather Required Information

Ask for all that are missing:

**Your membership site:**
- What type of membership do you run? (e.g., online courses, paid community, association, podcast, paid newsletter, coaching, directory)
- Who is your ideal member? (One sentence on who this is for)

**For each level, collect:**

| Field | Notes |
|-------|-------|
| Level name (current or working title) | Can suggest improvements |
| Price + billing period | e.g., $29/month, $199/year |
| Who this level is specifically for | Most useful for multi-tier sites |
| What's included | List features, content, access, perks |
| What's NOT included (if applicable) | What the next tier up adds |
| One thing that makes this level worth it | The "aha" reason to join at this tier |

You can write descriptions for one level or all tiers at once. If there are multiple levels, ask for info on all of them before writing.

---

## Step 2: Write Each Level Description

For each level, produce all of the following:

### Level Name
If the current name is generic (e.g., "Basic," "Pro," "Premium"), suggest 2-3 alternatives that communicate identity or outcome. Examples: "Member," "Practitioner," "Founding Member," "Insider," "All Access." Keep it short: one or two words.

### Tagline (1 sentence)
The level's value in a single sentence. Format: who it's for + what they get or achieve.
- "For practitioners ready to go deeper — weekly coaching calls, a private forum, and the full course library."
- "For associations looking to digitize their membership and grow revenue without changing platforms."
- "Everything you need to launch and grow a paid newsletter, in one place."

### Short Description (2-3 sentences)
Written for someone scanning the levels page. Should answer: What do I get? Is this right for me? Why is it worth the price?

Avoid:
- Bullet-point lists at this stage (those go in the benefits section below)
- Generic copy ("perfect for beginners" without substance)
- Feature-first language before establishing who it's for

### Benefits List (5-8 bullets)
Start with the most valuable or most differentiating items. Use outcome-oriented language where possible.

Format:
- **Feature name** — what it does for the member (not just what it is)

Example:
- **Weekly live Q&A calls** — bring your questions every Thursday and get answers in real time
- **Full course library** — 40+ hours of training organized by skill level, available on demand
- **Private member forum** — post questions, share progress, and connect with [X] active members

---

## Writing Rules

**Lead with identity, not just features:**
The best descriptions make the reader think "that's me" before they even see what's included.

**Match tone to the membership type:**
- Community / peer-learning: warm, collegial ("join [X] members who...")
- Professional / association: credible, authoritative
- Course / coaching: aspirational, outcome-driven
- Newsletter: direct, efficient, respects the reader's time

**Tiered sites: differentiate clearly**
If there are multiple levels, each description should make the upgrade path obvious without making the lower tier feel like a consolation prize.

**Price anchoring:**
Don't ignore the price in the copy. A good description acknowledges cost implicitly by making value feel obvious.

---

## Output Format

For each level:

```
## [Level Name] — [Price/Period]

**Suggested name alternatives:** (if applicable)

**Tagline:**
[One sentence]

**Short Description:**
[2-3 sentences]

**Benefits:**
- **[Feature]** — [outcome for member]
- ...
```

After all levels, add a **Notes** section flagging:
- Any level names that should be reconsidered and why
- Any benefits that need more specificity before publishing (e.g., "X hours of content" — how many hours exactly?)
- Whether the tier structure looks clear and compelling from a buyer's perspective
