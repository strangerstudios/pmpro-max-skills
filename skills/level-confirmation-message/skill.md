---
name: Level Confirmation Message
slug: level-confirmation-message
category: PMPro
one_shot: true
uses_profile: true
description: Writes the post-checkout confirmation message members see immediately after joining — turning a transactional moment into a warm welcome that sets expectations and drives the first action.
keywords: [confirmation message, PMPro confirmation, post-checkout message, member welcome, level settings, onboarding, first impression]
---

# Level Confirmation Message

Write the message a new member sees immediately after completing checkout — before they've done anything else. This is PMPro's "Confirmation Message" field in each level's settings.

Most sites leave this blank or use a generic message. A good confirmation message does three things: confirms they made a good decision, tells them exactly what to do next, and sets the tone for the experience ahead.

## Before Writing

**Check for context profile first:**
If a context profile is available, read it before asking questions. Use that context to understand the membership type, audience, and what the site contains.

## Step 1: Gather Required Information

| Field | Notes |
|-------|-------|
| Level name | Which membership tier is this for? |
| What type of membership is this? | Course, community, newsletter, association, coaching, podcast, directory |
| What is the single most important next step? | The ONE thing they should do right now |
| Next-step URL | Link to the start page, community, course, etc. |
| What else should they know? | Important links, how to access content, what to expect |
| Anything to set expectations about? | e.g., "Your first issue arrives Friday," "Calls are every Tuesday at noon ET" |
| Tone preference | Warm/celebratory, professional, calm/practical |

If the site has multiple levels, collect this info per level — each level often needs a different message.

---

## Step 2: Write the Confirmation Message

### Structure

```
[1. Confirmation + warmth — 1-2 sentences]
[2. What they just unlocked — 1-2 sentences]
[3. The immediate next step — 1 clear action with a link]
[4. Supporting next steps — 2-3 additional links or actions, if relevant]
[5. Expectation-setting — anything time-sensitive or important to know now]
[6. Closing — warm, optional]
```

**Length:** 80-200 words. Shorter is better. This is not a sales page — they already joined.

**Format for PMPro:** HTML is supported in the confirmation message field. Use `<p>`, `<strong>`, `<a href="">`, and `<ul>/<li>` as needed. No complex layouts.

---

## Writing Rules

**One clear next step, not five.**
If you give someone five things to do, they'll do none of them. Name one primary action. Additional links can be secondary.

**Don't re-sell them on what they just bought.**
They already joined. Skip the "you've made a great decision" preamble and move straight to orienting them.

**Match the moment:**
The confirmation screen is often read while still sitting at the checkout. They're oriented toward "what happens now?" — answer that clearly.

**Vary by membership type:**
- **Course / training:** "Your first step is [Module 1 / Start Here page]."
- **Community:** "Head to [Forum / Slack / Discord] and introduce yourself."
- **Newsletter:** "Your first issue arrives [day/frequency]. In the meantime, check out [best past issue]."
- **Association:** "Your member directory listing is [active / pending]. Start by [completing your profile]."
- **Coaching:** "Check your email — [coach name] will be in touch within [timeframe] to schedule your first call."

**HTML note:** Wrap the primary CTA in a button-style link:
```html
<p><a href="[URL]" style="background:#[color];color:#fff;padding:10px 20px;border-radius:4px;text-decoration:none;display:inline-block;">[Button Text]</a></p>
```
The color should match the site's brand.

---

## Output Format

```
## [Level Name] — Confirmation Message

**Plain text version:**
[Clean copy for reference]

**HTML version:**
[HTML formatted, ready to paste into PMPro Level Settings > Confirmation Message]

**Notes:**
- Primary CTA: [What and where]
- Suggested button color: #[hex] (based on membership type / context profile)
- Length: [X words]
```
