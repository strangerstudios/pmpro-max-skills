---
name: Free Content Audit
slug: free-content-audit
category: Strategy
one_shot: true
uses_profile: true
description: Audits the free-facing content on a membership site to evaluate whether it's attracting the right visitors, building enough trust to convert, and creating a clear path from free to paid.
keywords: [free content, content audit, membership conversion, content strategy, free to paid, content review, SEO, trust building, membership marketing]
feature: strategy
quiz:
  - step: 1
    heading: "About Your Site"
    hint: "The audit evaluates your free content against who it should be attracting. The more detail you share, the more specific the recommendations."
    inputs:
      - name: site_url
        label: "Your website URL"
        type: url
        placeholder: "e.g. https://yogabusinessacademy.com"
      - name: membership_type
        label: "What type of membership site is this?"
        type: select
        options: [Blog / News, Courses and Coaching, Paid Community, Paid Newsletter, Association / NPO, Podcast, Video Library, Member Directory, Hybrid]
      - name: site_age
        label: "How established is the site?"
        type: radio
        options: [Brand new — less than 6 months, Growing — 6 to 24 months, Established — 2 or more years]
      - name: content_inventory
        label: "Roughly how much free content exists? List what you have and approximately how much."
        type: textarea
        placeholder: "e.g. 45 blog posts (mix of short and long-form), 3 free podcast episodes, 1 free introductory course, no video content..."
      - name: free_tier_exists
        label: "Do you have a free membership level, or is content either fully public or fully gated?"
        type: radio
        options: [Yes — we have a free membership level with limited gated access, No — content is either completely public or completely gated]
  - step: 2
    heading: "Goals & What You Already Know"
    hint: "Tell us what you're trying to accomplish and what you already suspect. This sharpens the audit."
    inputs:
      - name: primary_goal
        label: "What's the primary job of your free content right now?"
        type: radio
        options: [Attract search traffic and new visitors (SEO), Build trust and demonstrate expertise, Convert visitors to paying members, All three equally]
      - name: traffic_sources
        label: "Where do most new visitors come from? Select all that apply."
        type: checkbox-group
        options: [Organic search (Google), Social media, Email marketing, Word of mouth / referrals, Paid ads, Direct traffic]
      - name: conversion_rate
        label: "Free-to-paid conversion rate, if known"
        type: text
        placeholder: "e.g. 6%, or 'I don't know'"
      - name: whats_performing
        label: "Any content you know is performing well — traffic, shares, or conversions?"
        type: textarea
        placeholder: "e.g. Our pricing guide gets the most traffic from Google. Our case study posts seem to convert visitors to members at a higher rate."
      - name: content_gaps
        label: "Any content types or topics you've been avoiding that might be worth adding?"
        type: textarea
        placeholder: "e.g. We've never done comparison content or SEO-focused how-to guides. We mostly write opinion pieces."
      - name: ideal_member_context
        label: "Who is your ideal member? (If you've completed the Ideal Member Profile skill, paste a summary here.)"
        type: textarea
        placeholder: "e.g. Independent yoga teachers 2-10 years in, earning $2-4k/month, who want to build online recurring income..."
        from_profile: audience
---

# Free Content Audit

Audit the free content on your membership site (blog posts, public pages, podcast episodes, videos, social profiles) to answer one question: **Is your free content doing its job?**

Free content has three jobs for a membership site:
1. **Attract** the right visitor (search, social, referral)
2. **Build trust** that the paid content is worth joining for
3. **Convert** — give visitors a clear reason and path to become members

Most membership sites are inconsistent on all three. This audit surfaces the gaps and gives you specific, prioritized action items.

---

## Before Starting

**Check for context profile first:**
If a context profile is available, read it to understand the membership type, audience, and offer. The audit evaluates content *against* the ideal member, and knowing who that is shapes every recommendation.

**Ideal member profile:**
If an **ideal-member-profile** has been completed, ask for it or reference it from the context profile. The audit is more useful when we know exactly who the free content should be attracting and convincing.

---

## Step 1: Understand the Site

Gather this context before auditing:

**About the site:**
- Site URL (if the tool can crawl it) or a content inventory they can paste
- What type of membership is this? (courses, community, newsletter, association, podcast, directory)
- How long has the site been active? How much free content exists?
- Is there currently a free membership level, or is everything either fully public or fully gated?

**About the goals:**
- What's the primary goal of the free content right now — SEO, trust-building, social sharing, or direct conversion?
- What's the current free-to-paid conversion rate (if known)?
- Where do most new visitors come from — search, social, email, referrals?

**What they already know:**
- Is there any content they feel is performing well? Any they suspect isn't?
- Any content type or topic they've been avoiding that might be worth trying?

---

## Step 2: Review the Free Content

Work through the free-facing content (either by crawling the URL or reviewing a list they provide). Evaluate across five dimensions:

---

### Dimension 1: Attraction — Is the right person finding this?

**Questions to answer:**
- Do the titles and topics match what the ideal member would search for or share?
- Is there a clear content focus, or does the site publish on too many topics to build authority with anyone specific?
- Is the most valuable free content optimized for search (long-form guides, how-to posts, comparison content) or only for social?
- Are there any obvious keyword gaps — topics the ideal member cares about that aren't covered at all?

**Flag:** Content that attracts general traffic but no one who would ever pay for a membership. Content that ranks but for the wrong audience.

---

### Dimension 2: Trust — Does it demonstrate expertise worth paying for?

**Questions to answer:**
- Does the free content show genuine depth of knowledge, or is it surface-level?
- Is there a consistent point of view, or does it feel like generic information anyone could publish?
- Are there real examples, specific outcomes, or original perspectives, or just recapped advice from elsewhere?
- Does the author/brand come across as credible and human? Or anonymous and corporate?

**Flag:** Content that's technically correct but indistinguishable from 100 other sites. Missing voice, missing specificity, missing proof.

---

### Dimension 3: Conversion — Is there a clear path from free to paid?

**Questions to answer:**
- Do free content pages include a CTA to join or learn more about the membership?
- Is the CTA specific to the content (e.g., "Want to go deeper on this? Members get the full course / community / library"), or generic ("Join our membership")?
- Is there a lead magnet or free offer capturing email addresses from visitors not ready to pay?
- Is the levels/pricing page easy to find from free content?

**Flag:** High-traffic free content with no CTA. Vague CTAs that don't connect to the content topic. No email capture for not-yet-ready visitors.

---

### Dimension 4: Alignment — Does the free content match what's behind the paywall?

**Questions to answer:**
- Does the free content preview the value inside the membership? Would a visitor reading it understand what they'd get by joining?
- Is there a coherent content funnel: free content introduces a topic > membership goes deeper?
- Or does the free content feel disconnected from what the membership actually delivers?

**Flag:** Free content on Topic A, membership delivers Topic B. Visitors have no reason to believe the paid content is what they're looking for.

---

### Dimension 5: Volume and Freshness — Is there enough, and is it current?

**Questions to answer:**
- Is there enough free content to build trust with a cold visitor, or does the site look thin?
- Is there recent content (within the last 3-6 months), or does the site look abandoned?
- Are there cornerstone/pillar pieces (long-form authoritative content), or only short posts and social reposts?

**Flag:** A membership sales page with only 3 blog posts behind it. A blog that hasn't published in 8 months. No pillar content, only fragmented short-form.

---

## Step 3: Deliver the Audit

### Format

```
## Free Content Audit — [Site Name]
Audited: [Date]

### Summary
[2-3 sentence honest assessment: what's the overall state of the free content?
Is it doing its job, partially, or not at all?]

### What's Working
[1-3 specific things to keep or double down on]

### The Gaps (Prioritized)

**Priority 1 — [Biggest gap, e.g., "No CTAs on high-traffic content"]**
- What's happening: [Specific observation]
- Why it matters: [Impact on attract/trust/convert]
- Fix: [Specific, actionable — what to do, not just what's wrong]

**Priority 2 — [Next gap]**
- What's happening:
- Why it matters:
- Fix:

**Priority 3 — [Next gap]**
...

### Quick Wins (Do This Week)
[2-3 specific actions that take < 2 hours each and would meaningfully improve the audit score]

### What to Build Next
[1-2 content types or pieces that are missing and would have the most impact]
```

---

## Audit Scoring (Internal Reference)

Use this to calibrate recommendations. The goal is not to produce a report card, but to prioritize what matters most:

| Dimension | Weak | Adequate | Strong |
|-----------|------|----------|--------|
| **Attraction** | Wrong audience, no SEO, no clear topic focus | Some relevant content, partial SEO | Consistent niche, strong search presence |
| **Trust** | Generic, no voice, could be anyone | Some expertise shows, some personality | Deep, specific, unmistakably theirs |
| **Conversion** | No CTAs anywhere | CTAs exist but generic | CTAs tied to content, email capture in place |
| **Alignment** | Free and paid feel unrelated | Some connection | Free content is a clear preview of paid |
| **Volume/Freshness** | Thin or stale | Decent volume, some recent content | Rich archive, regular publishing |

Prioritize the weakest dimension first: that's where fixing one thing produces the most lift.

---

## Related Skills

- **ideal-member-profile**: Define who the free content should be attracting before auditing against it
- **content-access-strategy**: Redesign what's free vs. gated based on audit findings
- **content-strategy**: Plan the new content to fill gaps surfaced in the audit
- **membership-cta-block**: Build the CTAs that free content is currently missing
- **locked-content-teaser**: Improve the message visitors see when they hit gated content
