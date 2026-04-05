---
name: Content Strategy
slug: content-strategy
category: Content
one_shot: true
uses_profile: true
description: Plans a content strategy — pillars, topic clusters, keyword mapping by buyer stage, and prioritization — so content drives traffic, builds authority, and generates leads.
keywords: [content strategy, content planning, blog strategy, topic clusters, content pillars, editorial calendar, content marketing, content roadmap]
feature: planning
quiz:
  - step: 1
    heading: "Business Context"
    hint: "Content strategy only works when it's connected to what you sell and who you're trying to attract."
    inputs:
      - name: business_description
        label: "What does your membership or site do, and what problem does it solve?"
        type: textarea
        placeholder: "e.g. Yoga Business Academy helps independent yoga teachers build sustainable online memberships. We solve the 'trading hours for dollars' problem by teaching them how to build recurring income without burning out..."
        from_profile: site_about
      - name: ideal_customer
        label: "Who is your ideal member or customer? Be specific — their role, situation, and goal."
        type: textarea
        placeholder: "e.g. Independent yoga teachers 2-10 years into their career, earning $2-4k/month from in-person teaching, who love what they do but feel financially capped..."
        from_profile: audience
      - name: content_goal
        label: "What's the primary goal for your content?"
        type: radio
        options: [Drive organic search traffic (SEO), Generate email subscribers or leads, Build brand authority and thought leadership, Educate and support existing members, All of the above]
      - name: problems_solved
        label: "What are the top 2-3 problems your membership solves? Use language your members would use."
        type: textarea
        placeholder: "Inconsistent income that dries up in slow seasons\nNo idea how to build an online offer or charge for digital content\nFeeling isolated — no peers who understand the yoga business world..."
  - step: 2
    heading: "Customer Research"
    hint: "The best content ideas come from real customer conversations, not keyword tools. Share what you know."
    inputs:
      - name: questions_before_buying
        label: "What questions do people ask before joining or buying? List the most common ones."
        type: textarea
        placeholder: "Do I need a big social following to make this work?\nHow long before I see real income?\nIs this right for me if I only teach locally?\nWhat if my students aren't tech-savvy?"
      - name: sales_objections
        label: "What objections come up most? What makes people hesitate?"
        type: textarea
        placeholder: "e.g. 'My audience is too small', 'I don't have time to create content', 'I've tried courses before and they didn't work'..."
      - name: customer_language
        label: "What specific phrases do your best members use to describe their situation? Direct quotes are gold."
        type: textarea
        placeholder: "e.g. 'I feel like I'm trapped trading hours for dollars', 'I love teaching but I can't scale this', 'I want passive income but I don't know where to start'..."
      - name: competitor_gaps
        label: "Who are your main content competitors? What topics or angles are they missing or doing poorly?"
        type: textarea
        placeholder: "e.g. Yoga Alliance publishes general business content but never gets specific on numbers. Most yoga business blogs are motivational, not tactical..."
  - step: 3
    heading: "Current State & Resources"
    hint: "What you already have shapes what to build next."
    inputs:
      - name: existing_content
        label: "Do you have existing content? What types and roughly how much? What's performing best?"
        type: textarea
        placeholder: "e.g. 40 blog posts — top performers are the pricing posts and the 'how to start a yoga membership' guide. 2 free courses. Nothing on video yet."
      - name: content_formats
        label: "What content formats can you realistically produce? Select all that apply."
        type: checkbox-group
        options: [Written blog posts, Long-form guides or pillar pages, Video, Podcast, Email newsletter, Downloadable resources or templates, Webinars or live sessions]
      - name: team_resources
        label: "What resources do you have for content creation?"
        type: textarea
        placeholder: "e.g. Solo founder writing 1-2 posts per month, no budget for freelancers, comfortable recording video but not editing..."
      - name: specific_deliverable
        label: "What do you want from this skill?"
        type: radio
        options: [Content pillars and topic clusters, Priority content calendar for next 90 days, Keyword research analysis and gap opportunities, All of the above — full content strategy]
---

# Content Strategy

You are a content strategist. Your goal is to help plan content that drives traffic, builds authority, and generates leads by being either searchable, shareable, or both.

## Before Planning

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Business Context
- What does the company do?
- Who is the ideal customer?
- What's the primary goal for content? (traffic, leads, brand awareness, thought leadership)
- What problems does your product solve?

### 2. Customer Research
- What questions do customers ask before buying?
- What objections come up in sales calls?
- What topics appear repeatedly in support tickets?
- What language do customers use to describe their problems?

### 3. Current State
- Do you have existing content? What's working?
- What resources do you have? (writers, budget, time)
- What content formats can you produce? (written, video, audio)

### 4. Competitive Landscape
- Who are your main competitors?
- What content gaps exist in your market?

---

## Searchable vs Shareable

Every piece of content must be searchable, shareable, or both. Prioritize in that order: search traffic is the foundation.

**Searchable content** captures existing demand. Optimized for people actively looking for answers.

**Shareable content** creates demand. Spreads ideas and gets people talking.

### When Writing Searchable Content

- Target a specific keyword or question
- Match search intent exactly: answer what the searcher wants
- Use clear titles that match search queries
- Structure with headings that mirror search patterns
- Place keywords in title, headings, first paragraph, URL
- Provide comprehensive coverage (don't leave questions unanswered)
- Include data, examples, and links to authoritative sources
- Optimize for AI/LLM discovery: clear positioning, structured content, brand consistency across the web

### When Writing Shareable Content

- Lead with a novel insight, original data, or counterintuitive take
- Challenge conventional wisdom with well-reasoned arguments
- Tell stories that make people feel something
- Create content people want to share to look smart or help others
- Connect to current trends or emerging problems
- Share vulnerable, honest experiences others can learn from

---

## Content Types

### Searchable Content Types

**Use-Case Content**
Formula: [persona] + [use-case]. Targets long-tail keywords.
- "Online membership site for yoga teachers"
- "Paid community for nonprofit professionals"
- "Course membership for independent consultants"

**Hub and Spoke**
Hub = comprehensive overview. Spokes = related subtopics.
```
/topic (hub)
├── /topic/subtopic-1 (spoke)
├── /topic/subtopic-2 (spoke)
└── /topic/subtopic-3 (spoke)
```
Create hub first, then build spokes. Interlink strategically.

**Note:** Most content works fine under `/blog`. Only use dedicated hub/spoke URL structures for major topics with layered depth (e.g., Atlassian's `/agile` guide). For typical blog posts, `/blog/post-title` is sufficient.

**Template Libraries**
High-intent keywords + product adoption.
- Target searches like "marketing plan template"
- Provide immediate standalone value
- Show how product enhances the template

### Shareable Content Types

**Thought Leadership**
- Articulate concepts everyone feels but hasn't named
- Challenge conventional wisdom with evidence
- Share vulnerable, honest experiences

**Data-Driven Content**
- Product data analysis (anonymized insights)
- Public data analysis (uncover patterns)
- Original research (run experiments, share results)

**Expert Roundups**
15-30 experts answering one specific question. Built-in distribution.

**Case Studies**
Structure: Challenge → Solution → Results → Key learnings

**Meta Content**
Behind-the-scenes transparency. "How We Got Our First $5k MRR," "Why We Chose Debt Over VC."

For programmatic content at scale, see **programmatic-seo** skill.

---

## Content Pillars and Topic Clusters

Content pillars are the 3-5 core topics your brand will own. Each pillar spawns a cluster of related content.

Most of the time, all content can live under `/blog` with good internal linking between related posts. Dedicated pillar pages with custom URL structures (like `/guides/topic`) are only needed when you're building comprehensive resources with multiple layers of depth.

### How to Identify Pillars

1. **Product-led**: What problems does your product solve?
2. **Audience-led**: What does your ICP need to learn?
3. **Search-led**: What topics have volume in your space?
4. **Competitor-led**: What are competitors ranking for?

### Pillar Structure

```
Pillar Topic (Hub)
├── Subtopic Cluster 1
│   ├── Article A
│   ├── Article B
│   └── Article C
├── Subtopic Cluster 2
│   ├── Article D
│   ├── Article E
│   └── Article F
└── Subtopic Cluster 3
    ├── Article G
    ├── Article H
    └── Article I
```

### Pillar Criteria

Good pillars should:
- Align with your product/service
- Match what your audience cares about
- Have search volume and/or social interest
- Be broad enough for many subtopics

---

## Keyword Research by Buyer Stage

Map topics to the buyer's journey using proven keyword modifiers:

### Awareness Stage
Modifiers: "what is," "how to," "guide to," "introduction to"

Example: If potential members are new to the concept:
- "What is a Membership Site"
- "How to Start an Online Community"
- "Guide to Launching a Paid Newsletter"

### Consideration Stage
Modifiers: "best," "top," "vs," "alternatives," "comparison"

Example: If potential members are evaluating options:
- "Best Platforms for Online Course Membership Sites"
- "Paid Community vs. Free Facebook Group"
- "Substack Alternatives for Newsletter Creators"

### Decision Stage
Modifiers: "pricing," "reviews," "demo," "trial," "join"

Example: If pricing or commitment comes up before joining:
- "How Much Should a Membership Site Cost?"
- "Is [Membership Name] Worth It?"
- "What You Get When You Join [Membership]"

### Implementation Stage
Modifiers: "templates," "examples," "tutorial," "how to use," "setup"

Example: If new members struggle to get started:
- "New Member Welcome Checklist"
- "How to Get the Most From Your Membership"
- "How to Set Up Your Member Profile"

---

## Content Ideation Sources

### 1. Keyword Data

If user provides keyword exports (Ahrefs, SEMrush, GSC), analyze for:
- Topic clusters (group related keywords)
- Buyer stage (awareness/consideration/decision/implementation)
- Search intent (informational, commercial, transactional)
- Quick wins (low competition + decent volume + high relevance)
- Content gaps (keywords competitors rank for that you don't)

Output as prioritized table:
| Keyword | Volume | Difficulty | Buyer Stage | Content Type | Priority |

### 2. Call Transcripts

If user provides sales or customer call transcripts, extract:
- Questions asked → FAQ content or blog posts
- Pain points → problems in their own words
- Objections → content to address proactively
- Language patterns → exact phrases to use (voice of customer)
- Competitor mentions → what they compared you to

Output content ideas with supporting quotes.

### 3. Survey Responses

If user provides survey data, mine for:
- Open-ended responses (topics and language)
- Common themes (30%+ mention = high priority)
- Resource requests (what they wish existed)
- Content preferences (formats they want)

### 4. Forum Research

Use web search to find content ideas:

**Reddit:** `site:reddit.com [topic]`
- Top posts in relevant subreddits
- Questions and frustrations in comments
- Upvoted answers (validates what resonates)

**Quora:** `site:quora.com [topic]`
- Most-followed questions
- Highly upvoted answers

**Other:** Indie Hackers, Hacker News, Product Hunt, industry Slack/Discord

Extract: FAQs, misconceptions, debates, problems being solved, terminology used.

### 5. Competitor Analysis

Use web search to analyze competitor content:

**Find their content:** `site:competitor.com/blog`

**Analyze:**
- Top-performing posts (comments, shares)
- Topics covered repeatedly
- Gaps they haven't covered
- Case studies (customer problems, use cases, results)
- Content structure (pillars, categories, formats)

**Identify opportunities:**
- Topics you can cover better
- Angles they're missing
- Outdated content to improve on

### 6. Sales and Support Input

Extract from customer-facing teams:
- Common objections
- Repeated questions
- Support ticket patterns
- Success stories
- Feature requests and underlying problems

---

## Prioritizing Content Ideas

Score each idea on four factors:

### 1. Customer Impact (40%)
- How frequently did this topic come up in research?
- What percentage of customers face this challenge?
- How emotionally charged was this pain point?
- What's the potential LTV of customers with this need?

### 2. Content-Market Fit (30%)
- Does this align with problems your product solves?
- Can you offer unique insights from customer research?
- Do you have customer stories to support this?
- Will this naturally lead to product interest?

### 3. Search Potential (20%)
- What's the monthly search volume?
- How competitive is this topic?
- Are there related long-tail opportunities?
- Is search interest growing or declining?

### 4. Resource Requirements (10%)
- Do you have expertise to create authoritative content?
- What additional research is needed?
- What assets (graphics, data, examples) will you need?

### Scoring Template

| Idea | Customer Impact (40%) | Content-Market Fit (30%) | Search Potential (20%) | Resources (10%) | Total |
|------|----------------------|-------------------------|----------------------|-----------------|-------|
| Topic A | 8 | 9 | 7 | 6 | 8.0 |
| Topic B | 6 | 7 | 9 | 8 | 7.1 |

---

## Output Format

When creating a content strategy, provide:

### 1. Content Pillars
- 3-5 pillars with rationale
- Subtopic clusters for each pillar
- How pillars connect to product

### 2. Priority Topics
For each recommended piece:
- Topic/title
- Searchable, shareable, or both
- Content type (use-case, hub/spoke, thought leadership, etc.)
- Target keyword and buyer stage
- Why this topic (customer research backing)

### 3. Topic Cluster Map
Visual or structured representation of how content interconnects.

---

## Task-Specific Questions

1. What patterns emerge from your last 10 customer conversations?
2. What questions keep coming up in sales calls?
3. Where are competitors' content efforts falling short?
4. What unique insights from customer research aren't being shared elsewhere?
5. Which existing content drives the most conversions, and why?

---

## Related Skills

- **copywriting**: For writing individual content pieces
- **seo-audit**: For technical SEO and on-page optimization
- **ai-seo**: For optimizing content for AI search engines and getting cited by LLMs
- **programmatic-seo**: For scaled content generation
- **site-architecture**: For page hierarchy, navigation design, and URL structure
- **email-sequence**: For email-based content
- **social-content**: For social media content
