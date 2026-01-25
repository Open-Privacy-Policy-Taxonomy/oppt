# Annotation Methodology

This document describes how the OPPT dataset was created.

## Overview

The dataset was created using a four-stage pipeline:

1. **Policy Collection**: Privacy policies collected as markdown documents
2. **Segmentation**: Automatic heading-based segmentation
3. **Classification**: Three independent LLM annotators classify each segment
4. **Consensus**: Majority vote with human arbitration for three-way disagreements

---

## Stage 1: Policy Collection

### Company Selection

123 companies selected to represent:

- Major technology platforms (Google, Apple, Microsoft, Meta, Amazon)
- AI/ML companies (OpenAI, Anthropic, Midjourney)
- Financial services (PayPal, Robinhood, Stripe)
- Healthcare/fitness (Peloton, BetterHelp)
- Data brokers (Gravy Analytics, Experian, LexisNexis)
- Social platforms (TikTok, Discord, Reddit)
- And more across 14+ industries

### Collection Process

- Policies downloaded from company websites (January 2026)
- Converted to markdown with preserved heading structure
- Stored with metadata (collection date, source URL)

---

## Stage 2: Segmentation

### Heading-Based Approach

Unlike paragraph-level segmentation used in OPP-115, we use **heading-based segmentation**:

```
## Data Collection           → Segment 1
  paragraph 1                   (all content under heading)
  paragraph 2

## Data Sharing              → Segment 2
  paragraph 3
```

### Rationale

1. **Deterministic**: No ambiguity about segment boundaries
2. **Aligned with document structure**: Authors organized content intentionally
3. **More context per segment**: Complete topic coverage
4. **Reproducible**: Any researcher can recreate identical segments

---

## Stage 3: Classification

### Three-Annotator Multi-Vendor Design

Each segment is classified independently by three LLM annotators from different vendors:

| Annotator | Model |
|-----------|-------|
| annotator_1 | Claude Haiku 4.5 (Anthropic) |
| annotator_2 | GPT-5.2 (OpenAI) |
| annotator_3 | Gemini-3-flash-preview (Google) |

### Why Multi-Vendor?

- Reduces individual model bias through vendor diversity
- Identifies ambiguous segments through disagreement
- Provides built-in quality control via majority voting
- Ensures no single vendor's training data dominates

### Annotator Instructions

All annotators receive identical instructions:

1. Classify each segment into one of 14 OPPT categories
2. Assign secondary categories if content spans topics
3. Document reasoning for classification
4. Annotate category-specific attributes

### Attribute Annotation

Following OPP-115 methodology, each classification includes structured attributes. For example, a FIRST_PARTY classification includes:

| Attribute | Example Values |
|-----------|----------------|
| action | Collect, Use, Track |
| personal_information_type | Contact, Location, Financial |
| purpose | Service, Marketing, Analytics |
| collection_mode | Explicit, Implicit |
| identifiability | Identifiable, Aggregated, Anonymous |

---

## Stage 4: Consensus Resolution

### Agreement Outcomes

| Outcome | Criteria | Action |
|---------|----------|--------|
| Unanimous | All 3 agree | Accept |
| Majority | 2 of 3 agree | Accept majority |
| Three-Way Split | All 3 differ | Human review |

### Agreement Rates

| Metric | Value |
|--------|-------|
| Unanimous (3/3) | 78.3% |
| Majority (2/3) | 20.5% |
| Three-way (human resolved) | 1.3% |

### Pairwise Agreement

| Pair | Agreement |
|------|-----------|
| Claude-GPT | 83.8% |
| Claude-Gemini | 85.5% |
| GPT-Gemini | 86.1% |

---

## Quality Assurance

### Automated Checks

- Valid JSON structure
- Category values from approved taxonomy
- All segment IDs present in all annotator outputs
- Cross-vendor consistency validation

### Manual Review Triggers

- Three-way disagreement
- Unusual category distribution
- High proportion of OTHER classifications

---

## Comparison to OPP-115

| Aspect | OPP-115 | OPPT |
|--------|---------|------|
| Policies | 115 | 123 |
| Segments | 23,000 | 3,651 |
| Segmentation | Paragraph-level | Heading-based |
| Annotators | 3 law students | 3 LLM agents |
| Categories | 10 | 14 |
| Era | Pre-GDPR (2016) | Post-GDPR/CCPA (2026) |

---

## Limitations

1. **LLM Variability**: Different model versions may produce slightly different results
2. **Temporal Snapshot**: Policies change; annotations reflect January 2026
3. **Heading Dependency**: Requires well-structured policies
4. **Boundary Cases**: Some content genuinely spans multiple categories

---

## References

- Wilson, S., et al. (2016). "The creation and analysis of a website privacy policy corpus." ACL 2016.
- Gilardi, F., et al. (2023). "ChatGPT outperforms crowd workers for text-annotation tasks." PNAS.
