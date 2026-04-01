# PMPro Max Skills

A library of AI prompt skills for membership site operators. Built by the [Paid Memberships Pro](https://www.paidmembershipspro.com) team.

Each skill is a focused prompt file you load into Claude, ChatGPT, or any AI tool to complete a specific development, marketing, sales, or operational task for your membership site.

---

## How to Use a Skill

### Option 1 — Run it on PaidMembershipsPro.com (PMPro Max membership required)

Skills marked as **one-shot** can be run directly inside your [member dashboard](https://www.paidmembershipspro.com/membership-account/). Paste your context, click Generate, and get a complete output in one step.

[Learn more about PMPro Max →](https://www.paidmembershipspro.com/pricing/)

### Option 2 — Use it in Claude

1. Open [claude.ai](https://claude.ai) and start a new conversation
2. Copy the contents of the `skill.md` file you want
3. Paste it into the chat
4. Include your personal [Context Profile](https://www.paidmembershipspro.com/membership-account/) for the best results.
5. Follow the prompts. The skill will guide you through what it needs

### Option 3 — Use it in ChatGPT

Same as Claude. Open [chat.openai.com](https://chat.openai.com), start a new chat (GPT-4o or better), paste the skill, and follow the prompts.

### Option 4 — Use it in Claude Code

If you use [Claude Code](https://claude.ai/code), you can load skills from this repo directly into your project's `.claude/skills/` directory.

For best results, you should store a copy of your [Context Profile](https://www.paidmembershipspro.com/membership-account/) in your project. This could be added in your project's CLAUDE.md file or stored separately and referenced in CLAUDE.md like `@docs/context-profile.md`.

---

## What's in Each Skill File

Every skill starts with frontmatter that describes it:

```yaml
---
name: Email Welcome Sequence
slug: email-welcome-sequence
category: Email
one_shot: true
uses_profile: true
description: Generate a 5-email welcome sequence for new subscribers.
keywords: [email, welcome, onboarding, subscribers, newsletter]
---
```

| Field | What it means |
|---|---|
| `one_shot` | `true` = give context once, get a complete output. `false` = works better as a back-and-forth conversation. |
| `uses_profile` | `true` = this skill works best when you include your site/audience context (see below). |

---

## Your Context Profile

Skills that use your context profile (`uses_profile: true`) work better when you tell the AI who you are, what you sell, and who you serve. You can do this two ways:

**On PaidMembershipsPro.com:** Your AI Context Profile is saved to your account and added automatically.

**In your own AI tool:** Before pasting the skill, attach your ContextProfile.md OR start your message with something like:

```
## My Context

Site: [your site URL]
What I sell: [your membership offer, tiers, pricing]
Who I serve: [your audience, their pain point, their goal]
Content I create: [blog, YouTube, newsletter, social]
Email platform: [ConvertKit, Mailchimp, etc.]
Stage: [pre-launch / just launched / growing / established]
```

The more specific you are, the better the output.

---

## Skill Index

See [index.json](index.json) for the full machine-readable index, or browse the [`skills/`](skills/) directory.

### Lead Magnets
- [Brainstorm Hyper-Relevant Lead Magnet Ideas](skills/brainstorm-hyper-relevant-lead-magnet-ideas/) — one-shot
- [Brainstorm AI-Powered Lead Magnet Ideas](skills/brainstorm-ai-powered-lead-magnet-ideas/) — back-and-forth
- [Brainstorm Money-Making Lead Magnet Ideas](skills/brainstorm-money-making-lead-magnet-ideas/) — back-and-forth
- [Analyze My Content and Brainstorm 10 Lead Magnet Ideas](skills/analyze-my-content-and-brainstorm-10-lead-magnet-ideas/) — one-shot
- [Brainstorm a Curation Lead Magnet](skills/brainstorm-a-curation-lead-magnet/) — one-shot
- [Generate Lead Magnet Names](skills/generate-lead-magnet-names/) — back-and-forth
- [Generate an Email Course Value Proposition](skills/generate-an-email-course-value-proposition/) — back-and-forth
- [Generate Mockup Images for a Lead Magnet Landing Page](skills/generate-mockup-images-for-a-lead-magnet-landing-page/) — one-shot

### Email
- [Email Welcome Sequence](skills/email-welcome-sequence/) — one-shot
- [Newsletter Welcome Sequence](skills/newsletter-welcome-sequence/) — one-shot
- [Post-Purchase Email Sequence](skills/post-purchase-email-sequence/) — back-and-forth
- [Re-Engagement Email Sequence](skills/re-engagement-email-sequence/) — one-shot
- [Objection Handling Email](skills/objection-handling-email/) — one-shot
- [Webinar Promo Email Sequence](skills/webinar-promo-email-sequence/) — one-shot
- [Abandoned Cart Objections](skills/abandoned-cart-objections/) — one-shot

### Strategy
- [Pricing Strategy](skills/pricing-strategy/) — back-and-forth
- [Launch Strategy](skills/launch-strategy/) — back-and-forth
- [Site Architecture](skills/site-architecture/) — one-shot

### Content
- [Content Strategy](skills/content-strategy/) — back-and-forth
- [Brainstorm a 30-Day Content Series](skills/brainstorm-a-30-day-content-series/) — one-shot

### Copy
- [Copywriting](skills/copywriting/) — back-and-forth

### CRO
- [Signup Flow CRO](skills/signup-flow-cro/) — back-and-forth
- [Onboarding CRO](skills/onboarding-cro/) — back-and-forth
- [Paywall & Upgrade CRO](skills/paywall-upgrade-cro/) — back-and-forth

### Retention
- [Churn Prevention](skills/churn-prevention/) — back-and-forth

### Social
- [LinkedIn Post](skills/linkedin-post/) — one-shot
- [Instagram Post](skills/instagram-post/) — one-shot

---

## Contributing

Skills in this repo are maintained by the PMPro team. Community contributions welcome.

- Each skill lives in its own folder: `skills/[slug]/skill.md`
- Follow the frontmatter format above
- After adding or editing a skill, run `scripts/generate-index.py` to update `index.json`
- Open a PR with a brief description of what the skill does and who it's for
