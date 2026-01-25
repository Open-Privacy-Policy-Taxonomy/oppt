# Open Privacy Policy Taxonomy (OPPT) v1.0

**Version:** 1.0
**Date:** January 2026
**Author:** Thomas Brackin

---

## Abstract

The Open Privacy Policy Taxonomy (OPPT) is a standardized framework for structuring, analyzing, and evaluating privacy policy disclosures. OPPT extends the foundational OPP-115 corpus (Wilson et al., ACL 2016) with four additional categories to address post-2018 regulatory developments including GDPR, CCPA/CPRA, and emerging AI transparency requirements.

---

## 1. Introduction

### 1.1 The Problem

Privacy policies have failed as a transparency mechanism:

- **Unreadable**: Average policy requires 29 minutes to read
- **Incomprehensible**: Written at college/graduate reading level
- **Unstandardized**: Every company uses different structure and terminology
- **Ineffective**: Only 9% of users read policies before accepting

### 1.2 Design Principles

1. **Empirically grounded** — Built on OPP-115, validated by GDPR alignment
2. **Regulatory-aligned** — Maps to GDPR Art. 13/14, CCPA, and emerging requirements
3. **User-centric** — Organized around what users need to know
4. **Machine-readable** — Enables automated analysis and comparison
5. **Universalist** — Substantive disclosures for all users, not hidden in regional sections

---

## 2. Category Definitions

OPPT defines **14 categories** for classifying privacy policy content.

### 2.1 Categories from OPP-115 (Unchanged)

| Code | Name | Description |
|------|------|-------------|
| `FIRST_PARTY` | First Party Collection/Use | What personal data the company collects directly and how they use it |
| `THIRD_PARTY` | Third Party Sharing/Collection | Data shared with or received from vendors, partners, advertisers, affiliates |
| `USER_CHOICE` | User Choice/Control | Opt-out mechanisms, preference settings, consent management |
| `USER_ACCESS` | User Access/Edit/Deletion | Rights to access, correct, delete, or port personal data |
| `RETENTION` | Data Retention | How long data is kept, deletion schedules, retention criteria |
| `SECURITY` | Data Security | Encryption, safeguards, breach notification procedures |
| `POLICY_CHANGE` | Policy Change | How users are notified of policy updates |
| `INTL_SPECIFIC` | International & Specific Audiences | Children's privacy (COPPA), international transfers |
| `OTHER` | Other | Introduction, definitions, contact information, boilerplate |

### 2.2 Evolved Category

| Code | Name | Description | Evolution |
|------|------|-------------|-----------|
| `TRACKING` | Tracking Technologies | Cookies, beacons, pixels, analytics, GPC/DNT signals, targeted advertising | Expanded from OPP-115's narrow "Do Not Track" |

### 2.3 New Categories (OPPT-specific)

| Code | Name | Description | Regulatory Driver |
|------|------|-------------|-------------------|
| `REGIONAL` | Regional Compliance | Jurisdiction-specific **procedures** for exercising rights, DPA contacts, legal bases | GDPR, CCPA state-specific requirements |
| `SALE_SHARING` | Data Sale/Sharing | Whether data is sold or shared for cross-context behavioral advertising | CCPA "Do Not Sell/Share" |
| `AUTOMATED_DECISIONS` | Automated Decision-Making | Profiling, algorithmic decisions, AI-driven processing | GDPR Art. 22, EU AI Act |
| `SENSITIVE_DATA` | Sensitive Personal Data | Special category data: biometric, health, genetic, racial, religious | GDPR Art. 9, state biometric laws |

---

## 3. Category Lineage

| OPP-115 Category | OPPT Category | Change |
|------------------|---------------|--------|
| First Party Collection/Use | `FIRST_PARTY` | Name standardized |
| Third Party Sharing/Collection | `THIRD_PARTY` | Name standardized |
| User Choice/Control | `USER_CHOICE` | Name standardized |
| User Access, Edit, and Deletion | `USER_ACCESS` | Name standardized |
| Data Retention | `RETENTION` | Name standardized |
| Data Security | `SECURITY` | Name standardized |
| Policy Change | `POLICY_CHANGE` | Name standardized |
| Do Not Track | `TRACKING` | **Expanded** |
| International and Specific Audiences | `INTL_SPECIFIC` | Name standardized |
| Other | `OTHER` | Name standardized |
| — | `REGIONAL` | **New** |
| — | `SALE_SHARING` | **New** |
| — | `AUTOMATED_DECISIONS` | **New** |
| — | `SENSITIVE_DATA` | **New** |

---

## 4. Design Philosophy

### 4.1 Universal vs. Procedural

OPPT distinguishes between:

| Type | Categories | Scope |
|------|------------|-------|
| **Substantive** | All except REGIONAL | What the company does with data — applies to ALL users |
| **Procedural** | REGIONAL | How to exercise rights in specific jurisdictions |

### 4.2 Anti-Hiding Principle

OPPT takes a normative stance: **Substantive disclosures should not be hidden in regional sections.**

**Bad Practice:**
```
[For California Residents]
We sell your personal information to data brokers.
```

**Good Practice:**
```
[Data Sale and Sharing]
We sell personal information to data brokers.
All users can opt out here: [link]

[For California Residents]
California residents have additional rights under CCPA...
```

---

## 5. Attribute Schema

Following OPP-115, each category has structured attributes. See [schema/attributes.json](../schema/attributes.json) for the machine-readable schema.

### 5.1 FIRST_PARTY / THIRD_PARTY Attributes

| Attribute | Values |
|-----------|--------|
| `action` | Collect, Use, Track, Share, Sell, Receive |
| `personal_information_type` | Contact, Location, Health, Financial, Biometric, etc. |
| `purpose` | Service, Advertising, Analytics, Legal Compliance, etc. |
| `collection_mode` | Explicit (user-provided), Implicit (automatic) |
| `identifiability` | Identifiable, Pseudonymous, Aggregated, Anonymous |

### 5.2 TRACKING Attributes

| Attribute | Values |
|-----------|--------|
| `tracking_technology` | First-party cookies, Third-party cookies, Pixels, Fingerprinting, SDKs |
| `tracking_purpose` | Analytics, Advertising, Personalization, Security |
| `signal_response` | Honors DNT, Honors GPC, Ignores signals |

### 5.3 REGIONAL Attributes

| Attribute | Values |
|-----------|--------|
| `jurisdiction` | California, EU/EEA, UK, Brazil, Virginia, Colorado, etc. |
| `content_type` | Rights enumeration, Request procedure, Legal basis, DPA contact |
| `additional_rights` | Right to know, Right to delete, Right to opt-out, Right to correct |

### 5.4 SENSITIVE_DATA Attributes

| Attribute | Values |
|-----------|--------|
| `sensitive_data_type` | Biometric, Health, Genetic, Precise geolocation, Religious, Sexual orientation |
| `collection_status` | Collects, Does not collect, With consent only |
| `legal_framework` | GDPR Article 9, CCPA Sensitive PI, BIPA, HIPAA |

### 5.5 AUTOMATED_DECISIONS Attributes

| Attribute | Values |
|-----------|--------|
| `decision_type` | Profiling, Credit decisions, Employment, Content moderation |
| `human_involvement` | Fully automated, Human review available, Human in the loop |
| `opt_out_available` | Yes, No, Upon request |

---

## 6. Regulatory Alignment

### 6.1 GDPR Article 13/14 Mapping

| GDPR Requirement | OPPT Category |
|------------------|---------------|
| Identity of controller | `OTHER` |
| Purposes of processing | `FIRST_PARTY` |
| Legal basis | `REGIONAL` |
| Recipients/categories | `THIRD_PARTY` |
| International transfers | `INTL_SPECIFIC` |
| Retention period | `RETENTION` |
| Data subject rights | `USER_ACCESS` |
| Automated decision-making | `AUTOMATED_DECISIONS` |

### 6.2 CCPA/CPRA Mapping

| CCPA Requirement | OPPT Category |
|------------------|---------------|
| Categories of PI collected | `FIRST_PARTY` |
| Sale/sharing disclosure | `SALE_SHARING` |
| Right to know | `USER_ACCESS` |
| Right to opt-out | `USER_CHOICE`, `SALE_SHARING` |
| Sensitive PI | `SENSITIVE_DATA` |

---

## 7. Validation

### 7.1 Corpus Statistics

Analysis of 123 privacy policies (3,651 segments):

| Category | Segments | % of Corpus |
|----------|----------|-------------|
| FIRST_PARTY | 823 | 22.5% |
| OTHER | 576 | 15.8% |
| THIRD_PARTY | 454 | 12.4% |
| REGIONAL | 433 | 11.9% |
| INTL_SPECIFIC | 232 | 6.4% |
| USER_ACCESS | 198 | 5.4% |
| TRACKING | 191 | 5.2% |
| USER_CHOICE | 178 | 4.9% |
| RETENTION | 139 | 3.8% |
| SECURITY | 121 | 3.3% |
| POLICY_CHANGE | 114 | 3.1% |
| SALE_SHARING | 76 | 2.1% |
| SENSITIVE_DATA | 69 | 1.9% |
| AUTOMATED_DECISIONS | 47 | 1.3% |

### 7.2 Evidence for New Categories

**REGIONAL** — Present in 85% of policies, accounting for 11.9% of all segments. Would have been misclassified as OTHER under OPP-115.

**SENSITIVE_DATA** — Present in 23% of policies. Driven by GDPR Art. 9 and state biometric laws.

**SALE_SHARING** and **AUTOMATED_DECISIONS** — Lower prevalence reflects that these practices are often hidden in REGIONAL sections (the jurisdiction-siloed disclosure pattern our research documents).

---

## 8. References

- Wilson, S., et al. (2016). "The creation and analysis of a website privacy policy corpus." ACL 2016.
- Dagstuhl Seminar 25021 (2025). "Grand Challenges for Research on Privacy Documents."

---

## Appendix: Glossary

- **Dark Pattern**: Design that subverts user autonomy or hides information
- **Substantive Disclosure**: Information about actual data practices
- **Procedural Disclosure**: Information about how to exercise rights
- **OPP-115**: Online Privacy Policies corpus of 115 annotated policies (2016)
- **Jurisdiction-Siloed Disclosure**: Substantive practices disclosed only in regional sections
