---
name: Content Access Strategy
slug: content-access-strategy
category: Strategy
one_shot: true
uses_profile: true
description: Designs a content access strategy around what to keep free, what to gate, and how to structure gating across membership levels. You want your free content to build trust and your gated content to drive and retain memberships.
keywords: [content access, content gating, free vs paid content, membership levels, content strategy, content protection, PMPro access, member content]
feature: strategy
quiz:
  - step: 1
    heading: "Membership Type & Levels"
    hint: "The right access structure looks completely different for a podcast membership vs. a course library vs. a paid community."
    inputs:
      - name: membership_type
        label: "What type of membership site is this?"
        type: select
        options: [Blog / News, Courses and Coaching, Paid Community, Paid Newsletter, Association / NPO, Podcast, Video Library, Member Directory, Hybrid]
      - name: level_details
        label: "List your membership levels, including the name, price, and billing period for each."
        type: textarea
        placeholder: "Free - no cost\nMember - $29/month or $249/year\nVIP - $99/month (includes coaching calls)"
        from_profile: levels
      - name: has_free_tier
        label: "Do you have a free access option?"
        type: radio
        options: [Yes — a free membership level with limited access, Yes — a time-limited free trial, Yes — freemium (always free, limited features), No — everything is paid]
  - step: 2
    heading: "Content Inventory"
    hint: "You can't design access strategy without knowing what content exists. Be specific about types and volume."
    inputs:
      - name: content_types
        label: "What types of content do you have or plan to have? Select all that apply."
        type: checkbox-group
        options: [Blog posts, Videos, Podcast episodes, Online courses or lessons, Community forum threads, Resources / downloads / templates, Live events or calls, Member directory listings, Newsletter issues or archive]
      - name: content_volume
        label: "How much content exists today? And how much is planned?"
        type: textarea
        placeholder: "e.g. Today: 60 blog posts (40 free, 20 gated), 12 courses (2 free preview, 10 gated), no community yet. Planning to add monthly live calls."
      - name: content_frequency
        label: "Is new content added regularly, or is it a fixed library?"
        type: radio
        options: [New content added regularly (weekly or more), New content added occasionally (monthly or less), Fixed library — not actively growing, Mixed — varies by content type]
  - step: 3
    heading: "Business Goals & Current State"
    hint: "The access strategy that maximizes SEO looks different from the one that maximizes paid conversion. Tell us what you're optimizing for."
    inputs:
      - name: primary_goal
        label: "What's your primary goal right now?"
        type: radio
        options: [Grow free subscribers or members, Increase free-to-paid conversion, Improve retention of paid members, Drive organic search traffic, All equally important]
      - name: seo_importance
        label: "How important is organic search traffic to your business?"
        type: radio
        options: [Very important — we rely on search traffic, Somewhat important, Not a focus right now]
      - name: current_access_structure
        label: "Describe your current access setup — what's free, what's gated, at which levels. Leave blank if starting from scratch."
        type: textarea
        placeholder: "e.g. Currently everything is either fully public or fully gated at our single paid level. No free tier. Blog posts are public. All courses require membership."
      - name: conversion_rate
        label: "Current free-to-paid conversion rate, if known"
        type: text
        placeholder: "e.g. 8%, or 'not sure'"
      - name: whats_working
        label: "Any content you know is performing well? Any you suspect isn't earning its keep?"
        type: textarea
        placeholder: "e.g. Our beginner posts get lots of traffic but nobody joins from them. Our case study posts seem to convert better but we have fewer of them..."
---

# Content Access Strategy

Design what's free, what's gated, and how access is structured across your membership levels so your free content builds trust and your paid content justifies the investment.

This is one of the most consequential decisions a membership site makes. Get it wrong and your free content gives too much away (nothing left to sell), or too little (nothing to build trust or organic traffic). Most membership sites evolve their access strategy by accident. This skill makes it intentional.

---

## Before Starting

**Check for context profile first:**
If a context profile is available, read it to understand the membership type, content volume, levels, and audience. Only ask for what isn't already covered.

## Step 1: Understand the Situation

Gather this context before making recommendations:

### 1. Membership Type
- What type of membership is this? (courses, community, newsletter, association, podcast, coaching, directory, blog/news)
- How many membership levels? What are the names and prices?
- Is there a free level, free trial, or freemium tier?

### 2. Content Inventory
- What types of content do you have or plan to have?
  (e.g., blog posts, videos, podcast episodes, courses/lessons, forum threads, resources/downloads, live events, directory listings)
- How much content exists today vs. what's planned?
- Is new content added regularly, or is it a fixed library?

### 3. Business Goals
- Primary goal: subscriber growth, paid member conversion, or retention?
- Is organic search traffic important? (free content = SEO potential)
- Do you have an email list you're growing?

### 4. Current State (if applicable)
- Is there an existing access structure? What's working or not?
- What's the current free-to-paid conversion rate, if known?
- Any content that performs especially well?

---

## Step 2: Apply the Access Strategy Framework

### The Core Principle

**Free content earns attention. Gated content earns money. The ratio between them should always favor free.**

Most new membership sites gate too much, too early. If visitors can't find enough value in your free content to trust you, they won't pay for more.

A healthy free-to-paid ratio depends on membership type:

| Type | Free content guideline | Gated content |
|------|------------------------|---------------|
| Blog & News | Most posts free, premium posts for deep analysis | Feature articles, archives, full newsletters |
| Courses & Coaching | 1 free course or free preview lessons | Full courses, coaching calls, live sessions |
| Community | Public landing page, some forum visibility | Active community, member profiles, discussion threads |
| Paid Newsletter | 1-2 free issues/month, full archive open | Weekly/daily issues, full archive |
| Association & NPO | Public resources, event listings | Member directory, discounted events, exclusive resources |
| Podcasting | All public episodes free | Bonus/extended episodes, ad-free feed, community |
| Video | Trailers/previews free | Full videos, series, live recordings |
| Member Directory | Directory exists publicly (or basic info) | Full profiles, contact info, networking |

---

### The Three Zones

Think of content in three zones:

**Zone 1: Free & Discoverable**
Optimized for search and social. Builds your reputation. Attracts strangers.
- Long-form how-to guides, explainers, introductory posts
- Public podcast episodes
- Free course or sample lessons
- Preview issues of the newsletter
- Publicly visible directory listings (limited info)

**Zone 2: Free but Gated (Email Capture)**
Valuable enough to exchange an email for. Bridges strangers to subscribers.
- Lead magnets (guides, templates, email courses)
- Free preview of a course
- Free member level with limited access

**Zone 3: Members Only**
Worth paying for. Deep, ongoing, specific, exclusive.
- The core content library (full courses, all episodes, premium articles)
- Community and interaction
- Live access (calls, events, Q&A)
- Tools, templates, downloads
- Direct access to you or experts

---

### Multi-Level Access Design

If there are multiple paid levels, use a clear principle for each tier:

| Tier | What it adds |
|------|-------------|
| Lowest paid | Access to the core content library |
| Mid tier | Plus: live interaction (calls, community) |
| Highest tier | Plus: direct access, custom work, or priority support |

**Common mistake:** Putting everything in the lowest tier and having nothing meaningful to justify the higher tiers. If you can't articulate why the upgrade is worth it, your upgrade rate will reflect that.

---

### What to Gate vs. Leave Free

**Gate these:**
- Evergreen content with clear, ongoing value (your best work)
- Interactive components (community, comments, calls)
- Your content library (not just the latest, but the full archive)
- Direct access to you
- Tools and downloadable resources

**Don't gate these:**
- Your best introductory or opinion content (it should be discoverable)
- Content that builds context for the value you sell
- FAQ, "about," and sales pages
- Content you want ranking in search

**Gray area:**
- Some newsletter archives (consider: open archives build trust)
- Older content (consider: opening it periodically)
- Short-form vs. long-form versions (free summary, paid deep dive)

---

## Step 3: Deliver the Access Map

After gathering context, produce a content access map:

### Access Map Format

```
CONTENT ACCESS MAP: [Membership Name]
Generated: [date]

FREE (PUBLIC)
─────────────────────────────────────────
[Content type]     → [Rationale]
[Content type]     → [Rationale]

FREE (EMAIL CAPTURE)
─────────────────────────────────────────
[Content type]     → [Lead magnet or free tier]
[Content type]     → [Lead magnet or free tier]

[LEVEL 1 NAME]: $[price]/[period]
─────────────────────────────────────────
[Content type]     → [Rationale]
[Content type]     → [Rationale]

[LEVEL 2 NAME]: $[price]/[period] (if applicable)
─────────────────────────────────────────
[Content type]     → [Rationale] (adds to Level 1)
```

### Followed by:

**Recommendations:**
- 3-5 specific recommendations based on the audit
- Flag any content that's currently gated but would perform better as free
- Flag any content that's currently free but would justify gating

**Free/Paid Ratio Assessment:**
- Is the free content sufficient to build trust and attract search traffic?
- Is the gated content compelling enough to justify the membership fee?

**Quick Win Opportunities:**
- 1-2 immediate changes that would have the most impact on conversion or retention

---

## Related Skills

- **pricing-strategy**: For designing the right tier structure and price points
- **membership-level-description**: For writing the copy for each level
- **membership-sales-page**: For the page that converts visitors to members
- **paywall-upgrade-cro**: For upgrading free members to paid tiers
