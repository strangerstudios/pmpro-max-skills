---
name: Level Confirmation Message
slug: level-confirmation-message
category: PMPro
one_shot: true
uses_profile: true
description: Writes the post-checkout confirmation message members see immediately after joining — turning a transactional moment into a warm welcome that sets expectations and drives the first action.
keywords: [confirmation message, PMPro confirmation, post-checkout message, member welcome, level settings, onboarding, first impression]
feature: copywriting
quiz:
  - step: 1
    heading: "Membership Level Info"
    hint: "This message appears the moment someone completes checkout. It's their very first experience inside your membership."
    inputs:
      - name: level_name
        label: "Which membership level is this for?"
        type: text
        placeholder: "e.g. Member, Studio Pro, Annual Member, Founding Member"
      - name: membership_type
        label: "What type of membership is this?"
        type: select
        options: [Online Courses / Training, Paid Community, Association or NPO, Paid Newsletter, Coaching Program, Podcast Membership, Member Directory, Hybrid]
      - name: tone
        label: "Tone of the confirmation message"
        type: radio
        options: [Warm and celebratory, Professional and matter-of-fact, Calm and practical]
      - name: brand_color
        label: "Primary brand color hex code (for the button style)"
        type: text
        placeholder: "e.g. #006799"
  - step: 2
    heading: "Next Steps & Expectations"
    hint: "Be specific. A new member who sees 'check your email' when they expected to start a course is frustrated. Tell them exactly where to go."
    inputs:
      - name: primary_next_step
        label: "The single most important thing they should do right now. One action."
        type: textarea
        placeholder: "e.g. Head to Module 1 of the Foundations Course and watch the first 3 lessons — that's where everything starts."
      - name: primary_next_step_url
        label: "URL for that primary next step"
        type: url
        placeholder: "e.g. https://yoursite.com/membership-account/courses/foundations/"
      - name: secondary_steps
        label: "(Optional) 2-3 additional helpful links or actions. One per line with the URL."
        type: textarea
        placeholder: "Join the community forum > https://yoursite.com/community/\nDownload your member welcome kit > https://yoursite.com/welcome-kit/\nBook your onboarding call > https://yoursite.com/book/"
      - name: expectations
        label: "Anything important to set expectations about right now? Timing, cadence, what happens next."
        type: textarea
        placeholder: "e.g. Your first monthly live Q&A call is the first Tuesday of each month at noon ET. New lessons drop every Monday."
      - name: extra_context
        label: "Anything else they need to know immediately? (e.g., how to access the app, where to get support)"
        type: textarea
        placeholder: "e.g. If you have any questions, email us at support@yoursite.com — we typically reply within 1 business day."
---

# Level Confirmation Message

Write the message a new member sees immediately after completing checkout, before they've done anything else. This is PMPro's "Confirmation Message" field in each level's settings.

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

If the site has multiple levels, collect this info per level, as each level often needs a different message.

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

**Length:** 80-200 words. Shorter is better. This is not a sales page. They already joined.

**Format for PMPro:** HTML is supported in the confirmation message field. Use `<p>`, `<strong>`, `<a href="">`, and `<ul>/<li>` as needed. No complex layouts.

---

## Writing Rules

**One clear next step, not five.**
If you give someone five things to do, they'll do none of them. Name one primary action. Additional links can be secondary.

**Don't re-sell them on what they just bought.**
They already joined. Skip the "you've made a great decision" preamble and move straight to orienting them.

**Match the moment:**
The confirmation screen is often read while still sitting at the checkout. They're oriented toward "what happens now?" Answer that clearly.

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

Deliver the output directly. No preamble, no "here's your confirmation message," no commentary after the Notes block.

**Plain text version** is clean copy for reference. **HTML version** is what gets pasted into PMPro > Memberships > Levels > [Level] > Confirmation Message. Both should always be included.

```
## [Level Name] — Confirmation Message

**Plain text version:**
[Clean copy for reference — no HTML tags]

**HTML version:**
[HTML formatted, ready to paste into PMPro Level Settings > Confirmation Message]

**Notes:**
- Primary CTA: [What and where]
- Suggested button color: #[hex] (based on membership type / context profile)
- Length: [X words]
```
