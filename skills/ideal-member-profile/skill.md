---
name: Ideal Member Profile
slug: ideal-member-profile
category: Strategy
one_shot: true
processing: prompt
uses_profile: true
description: Builds a vivid, specific ideal member profile through a structured interview — covering who they are, where they are now, what they want, what stops them, and what makes them buy and stay. Output can be used to sharpen all other skills and to refine your context profile.
keywords: [ideal member, buyer persona, member profile, target audience, ICP, ideal customer, audience research, membership marketing, customer avatar]
feature: strategy
quiz:
  - step: 1
    heading: "The Real Person"
    hint: "Think of your single best current member — or the person you'd most love to clone. Give them a name."
    inputs:
      - name: member_name
        label: "Give your ideal member a first name."
        type: text
        placeholder: "e.g. Sarah"
      - name: member_age_life
        label: "How old are they, and what's their life situation — job, family, daily context?"
        type: textarea
        placeholder: "e.g. 38, yoga teacher in Austin, two kids, runs a small studio part-time..."
      - name: money_relationship
        label: "What's their relationship with money? Describe their income situation and what financial success would actually feel like to them."
        type: textarea
        placeholder: "e.g. Earns $40-60k teaching, wants to break $100k without burning out — success feels like paying herself a real salary..."
      - name: tech_comfort
        label: "How tech-comfortable are they?"
        type: radio
        options: [Non-technical — avoids anything complicated, Can follow tutorials and use AI to unblock themselves, Dangerously capable — troubleshoots independently, Developer / highly technical]
  - step: 2
    heading: "Where They Are Right Now"
    hint: "Describe their current situation — what they're doing, what's working, and where they're stuck."
    inputs:
      - name: current_situation
        label: "What are they currently doing to solve the problem your membership addresses? Tools, platforms, approaches they're trying."
        type: textarea
        placeholder: "e.g. Piecing together free YouTube tutorials and a generic business coach who doesn't understand yoga..."
      - name: whats_working
        label: "What have they already figured out on their own? What's working for them?"
        type: textarea
        placeholder: "e.g. Great at the teaching itself, has a loyal small student base, good word of mouth..."
      - name: whats_stuck
        label: "Where are they frustrated, stuck, or plateaued? What keeps not working?"
        type: textarea
        placeholder: "e.g. No idea how to price memberships, burns out during slow seasons, inconsistent income..."
      - name: measurable_goal
        label: "What is their primary measurable goal — the specific outcome, number, or milestone they're chasing?"
        type: textarea
        placeholder: "e.g. $5,000/month in recurring revenue from an online membership"
      - name: emotional_goal
        label: "What do they actually want to feel — not just achieve? The emotional goal behind the number."
        type: textarea
        placeholder: "e.g. Stability and confidence that she can sustain this career long-term without sacrificing her teaching..."
  - step: 3
    heading: "Blockers, Beliefs & Buying"
    hint: "This is where we find the real reasons people hesitate — and what finally makes them act."
    inputs:
      - name: top_fear
        label: "What is their #1 fear or hesitation — the thing that keeps them from moving forward even when they know what to do?"
        type: textarea
        placeholder: "e.g. Fear that her audience is too small, or that no one will pay for online content when they can get it free on YouTube..."
      - name: overthinking_pattern
        label: "How does overthinking or self-sabotage show up for them? What do they do instead of taking action?"
        type: textarea
        placeholder: "e.g. Researches tools obsessively instead of launching, waits until she 'has more content ready'..."
      - name: what_stopped_best_members
        label: "What almost stopped your best current members from joining? What were they on the fence about?"
        type: textarea
        placeholder: "e.g. Price felt high, thought they needed to be more established first, worried they wouldn't have time..."
      - name: limiting_belief
        label: "What do they believe right now that's true but limiting? The mindset or assumption keeping them stuck."
        type: textarea
        placeholder: "e.g. 'My students won't pay for online — they come for the in-person experience'..."
      - name: what_unlocks_action
        label: "What reframe or permission do they need to hear to unlock action?"
        type: textarea
        placeholder: "e.g. Seeing a yoga teacher exactly like them successfully running a $3k/month online membership..."
  - step: 4
    heading: "Buying Triggers, Retention & Messaging"
    hint: "The final pieces: what makes them join, stay, and leave — and the exact words they use."
    inputs:
      - name: buying_triggers
        label: "What triggers them to finally buy? Describe the 2-3 moments or circumstances when they become a customer."
        type: textarea
        placeholder: "e.g. After a bad month of income, when they see a peer launch successfully, or after a specific insight from your content..."
      - name: what_keeps_them
        label: "What keeps them paying and coming back after they join?"
        type: textarea
        placeholder: "e.g. The community accountability, live Q&A calls, feeling like they're not figuring it out alone..."
      - name: churn_triggers
        label: "What causes them to cancel or disengage?"
        type: textarea
        placeholder: "e.g. If life gets busy and they feel behind, or if they don't see progress in the first 30 days..."
      - name: where_they_hang_out
        label: "Where do they spend time online — platforms, communities, search habits?"
        type: textarea
        placeholder: "e.g. Instagram, yoga business Facebook groups, YouTube tutorials, Google searches for 'how to make money teaching yoga online'..."
      - name: their_words
        label: "What exact phrases or words do they use to describe their problem? Quotes from real people are gold."
        type: textarea
        placeholder: "e.g. 'I love teaching but I can't scale this', 'I feel like I'm trading hours for dollars', 'I need passive income but I don't know where to start'..."
      - name: transformation
        label: "Complete this transformation: 'Before joining, members are ___. After joining, they ___.' Use their language."
        type: textarea
        placeholder: "e.g. Before: overwhelmed yoga teachers trading time for dollars. After: running a sustainable online membership that pays them consistently..."
---

# Ideal Member Profile

Build a vivid, specific profile of the person your membership is built for. Not a demographic sketch, but a real portrait: who they are, what they're struggling with, what they want, what's stopping them, and what finally makes them join and stay.

Every other skill in this library works better when it knows who it's writing for. This skill produces that foundation.

**Output options:**
- A standalone ideal member profile document (use in any skill, share with collaborators)
- A context profile update — paste the "Ideal Member" section into your PMPro Max profile to personalize future skill outputs automatically

---

## Before Starting

**Check for context profile first:**
If a context profile is available, read it before asking questions. Use what's already there and skip any questions already answered. If the profile has a thin or missing audience section, this skill fills it in.

---

## How This Works

This is a structured interview, not a form. Ask questions in small groups (2-3 at a time), listen to the answers, and follow up where details are thin. The goal is specificity: a profile nobody could confuse with someone else's.

Work through the 7 sections below, in order.

---

## Section 1: The Real Person

Ask these together:

> To build a profile we can actually use, I want to describe your ideal member as a specific, real person (not just a demographic). Let's start here:
>
> 1. Give them a name. How old are they? Where do they live? What's their life situation — job, family, daily context?
> 2. What's their relationship with money? What's their income situation, and what would "financial success" actually feel like to them?
> 3. How comfortable are they with technology — are they completely non-technical, "dangerously capable" (can follow tutorials, use AI to unblock themselves, troubleshoot), or closer to a developer?

**What to listen for:** Specificity signals the person knows their audience. Vague answers ("anyone who wants to...") need a follow-up: "Think of your best current customer or the person you most enjoyed working with. Describe them."

---

## Section 2: Where They Are Right Now

Ask together:

> Now let's look at where they are before they find you:
>
> 4. What are they currently doing? (Their work, their side project, their tools, their platforms, how they're currently trying to solve the problem your membership addresses)
> 5. What's already working for them? What have they figured out on their own?
> 6. What's not working — where are they stuck, frustrated, or plateaued?

**What to listen for:** The gap between what's working and what's not is where the membership's value lives. If they can't articulate this gap clearly, probe: "What's the thing they keep trying that never quite works?"

---

## Section 3: What They Want

Ask together:

> 7. What is their primary measurable goal — the specific outcome, number, or milestone they're chasing?
> 8. What's the emotional goal behind that? What do they actually want to *feel* — not just achieve?
> 9. If everything worked out, what does their life or work look like in 12 months?

**What to listen for:** The measurable goal is what they say they want. The emotional goal is what they actually want. Both matter, but the emotional goal drives buying decisions. If they only give a measurable goal ("$5k/month"), push for the feeling: "Why does that number matter — what does hitting it change for them?"

---

## Section 4: The Blocker

Ask together:

> 10. What is their #1 fear or hesitation — the thing that keeps them from moving forward, even when they know what to do?
> 11. How does overthinking or self-sabotage show up for them? What do they do instead of shipping?
> 12. What almost stopped your best members from joining? What were they on the fence about?

**What to listen for:** The blocker is usually fear of failure or fear of commitment, but it often looks like "I need to research more" or "I need to get X right first." The overthinking pattern is often more honest than the stated fear.

---

## Section 5: Beliefs, Triggers, and Churn

Ask in two parts:

**Part A — Beliefs:**
> 13. What do they believe right now that's true but limiting them? (The mindset or assumption that keeps them stuck)
> 14. What do they need to hear — the reframe or permission — that unlocks action for them?

**Part B — Buying and staying:**
> 15. What triggers them to finally buy? Name the 2-3 moments when they become a customer.
> 16. What keeps them paying / coming back after they join?
> 17. What causes them to cancel or disengage?

**What to listen for:** The "what they need to hear" answer often becomes the thesis of your best marketing. The churn triggers reveal retention risks worth designing against.

---

## Section 6: How to Reach Them

Ask together:

> 18. Where do they hang out — platforms, communities, search, word of mouth?
> 19. What types of content do they trust, save, or share? (Frameworks, checklists, case studies, behind-the-scenes, math breakdowns, tutorials?)
> 20. What language do they use to describe their own problem? Any exact quotes or phrases you've heard from real people?

**What to listen for:** The exact phrases people use to describe their problem are gold for copy. If the user has heard people say a specific thing repeatedly, that phrase often belongs in the headline of their sales page.

---

## Section 7: The Transformation and Messaging

Ask together:

> 21. What's the hero transformation your membership delivers — where do members start, and where do they end up? (Complete the sentence: "From: ___ > To: ___")
> 22. What are the 3-5 messaging angles that make your ideal member feel most "seen" — the themes that make them think "this is exactly me"?

---

## Output: The Ideal Member Profile

After completing the interview, produce the full profile in this format:

---

```
# Ideal Member Profile — [Membership Name]

## The Person

**Name:** [First name]
**Age:** [Age]
**Location:** [City/region/context]
**Life situation:** [Job, family, daily context — 2-3 sentences]
**Income/money relationship:** [1-2 sentences]
**Tech comfort:** [Non-technical / Capable / Dangerously capable / Developer]

## Where They Are Right Now

[2-3 paragraphs: what they're doing, what's working, what's not — told as a mini-narrative, not a list]

## What They Want

**Primary goal:** [The measurable outcome]
**Emotional goal:** [The feeling behind the goal]
**12-month success picture:** [What their life/work looks like if everything works]

## The Blocker

**#1 fear:** [The thing that stops them]
**How overthinking shows up:** [The self-sabotage pattern]
**What almost stopped your best members:** [The fence they were on]

## What They Believe and Need to Hear

**Core belief (limiting):** [What they believe that's true but holding them back]
**What unlocks action:** [The reframe or permission they need]

## Buying and Staying

**Buying triggers:**
1. [Moment 1]
2. [Moment 2]
3. [Moment 3]

**What keeps them:** [Retention drivers]
**What causes cancel:** [Churn triggers]

## How to Reach Them

**Where they hang out:** [Platforms and communities]
**Content they trust:** [Formats and types]
**Their words:** [Quotes and phrases they actually use]

## The Transformation

**From:** [Current state]
**To:** [Desired state]

**In their words:** "[A short statement in their voice that captures it]"

## Messaging Angles

1. [Theme that makes them feel seen]
2. [Theme]
3. [Theme]
4. [Theme, if applicable]
5. [Theme, if applicable]
```

---

## After the Profile

Once the profile is complete, offer two things:

**1. Context profile update:**
> "Want to add this to your PMPro Max context profile? Here's the section to paste in:"

Produce a condensed "Ideal Member" section formatted for the context profile, 150-250 words summarizing the key points.

**2. What to run next:**
> "Now that we have your ideal member profile, these skills will use it automatically:
> - **membership-sales-page** — writes to this specific person
> - **membership-level-description** — frames benefits in their language
> - **email-welcome-sequence** — opens with their exact situation
> - **free-content-audit** — evaluates your free content against this person"
