# OPP-115 to OPPT v1.0 Mapping

This document describes how the OPPT v1.0 taxonomy relates to the original OPP-115 annotation scheme from Wilson et al. (ACL 2016).

## Background

The OPP-115 corpus established the foundational taxonomy for privacy policy annotation. OPPT v1.0 extends this taxonomy to address regulatory developments since 2016, particularly GDPR, CCPA/CPRA, and emerging AI regulations.

## Category Mapping

### Direct Mappings (1:1)

These OPPT categories correspond directly to OPP-115 categories:

| OPPT v1.0 | OPP-115 | Notes |
|-----------|---------|-------|
| `FIRST_PARTY` | First Party Collection/Use | Identical scope |
| `THIRD_PARTY` | Third Party Sharing/Collection | Identical scope |
| `USER_CHOICE` | User Choice/Control | Identical scope |
| `USER_ACCESS` | User Access, Edit and Deletion | Identical scope |
| `RETENTION` | Data Retention | Identical scope |
| `SECURITY` | Data Security | Identical scope |
| `POLICY_CHANGE` | Policy Change | Identical scope |
| `INTL_SPECIFIC` | International and Specific Audiences | Identical scope |
| `OTHER` | Other | Identical scope |

### Expanded Categories

| OPPT v1.0 | OPP-115 | Changes |
|-----------|---------|---------|
| `TRACKING` | Do Not Track | **Significantly expanded**: OPP-115's "Do Not Track" focused narrowly on DNT signals. OPPT's TRACKING covers the full tracking ecosystem: cookies, pixels, SDKs, analytics, targeted advertising, and signal responses (DNT, GPC). |

### New Categories (No OPP-115 Equivalent)

These categories address post-2016 regulatory requirements:

| OPPT v1.0 | Rationale |
|-----------|-----------|
| `REGIONAL` | GDPR (2018) and CCPA (2020) require jurisdiction-specific disclosures. OPP-115 predates these laws. |
| `SALE_SHARING` | CCPA/CPRA introduced specific "sale" and "sharing" disclosure requirements not addressed in OPP-115. |
| `AUTOMATED_DECISIONS` | GDPR Article 22 and EU AI Act require transparency about automated decision-making and profiling. |
| `SENSITIVE_DATA` | GDPR Article 9 and CCPA's "sensitive personal information" category require explicit handling of special categories. |

## Conversion Guide

### Converting OPPT to OPP-115

To map OPPT annotations to OPP-115 categories:

```python
OPPT_TO_OPP115 = {
    'FIRST_PARTY': 'First Party Collection/Use',
    'THIRD_PARTY': 'Third Party Sharing/Collection',
    'USER_CHOICE': 'User Choice/Control',
    'USER_ACCESS': 'User Access, Edit and Deletion',
    'RETENTION': 'Data Retention',
    'SECURITY': 'Data Security',
    'POLICY_CHANGE': 'Policy Change',
    'TRACKING': 'Do Not Track',  # Expanded scope
    'INTL_SPECIFIC': 'International and Specific Audiences',
    'OTHER': 'Other',

    # New categories - no direct mapping
    'REGIONAL': None,  # Often overlaps with substantive categories
    'SALE_SHARING': None,  # Could map to THIRD_PARTY
    'AUTOMATED_DECISIONS': None,  # Could map to FIRST_PARTY
    'SENSITIVE_DATA': None,  # Could map to FIRST_PARTY
}
```

### Handling New Categories

When converting to OPP-115:

| OPPT Category | Suggested OPP-115 Mapping |
|---------------|--------------------------|
| `REGIONAL` | Map based on content: USER_ACCESS for rights, USER_CHOICE for controls, Other for procedures |
| `SALE_SHARING` | Third Party Sharing/Collection |
| `AUTOMATED_DECISIONS` | First Party Collection/Use |
| `SENSITIVE_DATA` | First Party Collection/Use |

### Converting OPP-115 to OPPT

OPP-115 annotations can be directly mapped to OPPT using the inverse of the table above. However, OPP-115 annotations may not capture nuances that OPPT distinguishes (e.g., sale vs. sharing, regional vs. general rights).

## Attribute Comparison

### Shared Attribute Concepts

Both taxonomies use similar attribute types:

| Concept | OPP-115 | OPPT |
|---------|---------|------|
| Data type | Personal Information Type | personal_information_type |
| Purpose | Purpose | purpose |
| Collection method | Collection Mode | collection_mode |
| Third party type | Third Party Entity | third_party_entity |
| Access rights | Access Type | access_type |

### OPPT Additions

OPPT adds attributes not in OPP-115:

- **Signal response** (TRACKING): DNT/GPC honor status
- **Sale status** (SALE_SHARING): Explicit sale/no-sale declaration
- **Legal basis** (REGIONAL): GDPR-required processing grounds
- **Decision type** (AUTOMATED_DECISIONS): Profiling category
- **Sensitive data type** (SENSITIVE_DATA): Special category identification

## Research Compatibility

### Using Both Datasets

Researchers can:

1. **Compare classifications**: Use the direct mappings to compare OPPT-2026 and OPP-115 annotations on similar content
2. **Combine datasets**: Convert OPPT to OPP-115 schema for larger training sets (with loss of new-category nuance)
3. **Extend OPP-115**: Use OPPT categories to re-annotate OPP-115 policies with modern categories

### Limitations of Comparison

- **Temporal gap**: OPP-115 policies (2016) predate GDPR/CCPA; comparisons reflect different regulatory eras
- **Segmentation differences**: OPP-115 uses paragraph-level; OPPT uses heading-level segmentation
- **TRACKING expansion**: OPPT's broader TRACKING category is not directly comparable to OPP-115's narrow DNT focus

## References

- Wilson, S., et al. (2016). "The creation and analysis of a website privacy policy corpus." Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics.
- [OPP-115 Dataset](https://usableprivacy.org/data)
- [GDPR to OPP-115 Mapping](https://par.nsf.gov/biblio/10257054) - Torre et al. (2020)
