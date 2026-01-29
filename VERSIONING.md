# OPPT Versioning

OPPT uses **two-axis versioning** to independently track the taxonomy (category definitions) and corpus (collected policies).

## Version Identifiers

| Axis | Format | Current |
|------|--------|---------|
| Taxonomy | `OPPT v{major}.{minor}` | OPPT v1.0 |
| Corpus | `OPPT-T{tax}_C{corpus}_{granularity}_{date}` | OPPT-T1_C1.0_Section_Jan2026 |

### Full Corpus Identifier

```
OPPT-T1_C1.0_Section_Jan2026
      │  │    │       │
      │  │    │       └── Collection date (MonthYear)
      │  │    └────────── Granularity level
      │  └─────────────── Corpus version (major.minor)
      └────────────────── Taxonomy version (major only)
```

## Taxonomy Versioning

The taxonomy defines the 14 categories and their attribute schemas.

### Bump Criteria

| Change Type | Version Bump | Examples |
|-------------|--------------|----------|
| New category added | Major | Adding a 15th category |
| Category removed or merged | Major | Merging two categories into one |
| Category renamed | Major | `FIRST_PARTY` → `DATA_COLLECTION` |
| Category definition changed substantially | Major | Changing what content belongs in a category |
| Attribute added to a category | Minor | Adding new attribute to FIRST_PARTY |
| Attribute values expanded | Minor | Adding new options to existing attribute |
| Clarification without semantic change | Minor | Improving examples or guidance |
| Typo fixes, formatting | None | No version change |

### Compatibility

- **Major version changes** may require re-annotation of existing data
- **Minor version changes** are backward-compatible; existing annotations remain valid

## Corpus Versioning

The corpus is the collection of annotated privacy policy segments.

### Bump Criteria

| Change Type | Version Bump | Examples |
|-------------|--------------|----------|
| New policies added | Minor | Adding 50 new company policies |
| Policies removed | Minor | Removing outdated or problematic policies |
| Re-annotation with new taxonomy | Major | Applying OPPT v2.0 to existing policies |
| Annotation methodology change | Major | Switching from 3-model to 5-model consensus |
| Annotation corrections | Minor | Fixing annotation errors |
| Metadata additions | Minor | Adding new fields to the schema |

### Granularity Levels

| Level | Description |
|-------|-------------|
| `Section` | Policy segmented by heading/section structure |
| `Paragraph` | Policy segmented by paragraph |
| `Sentence` | Policy segmented by sentence |

### Date Format

The date component uses `MonYYYY` format (e.g., `Jan2026`) indicating when the corpus version was finalized.

## Version History

### Taxonomy Versions

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | January 2026 | Initial release. 14 categories extending OPP-115 with REGIONAL, SALE_SHARING, AUTOMATED_DECISIONS, SENSITIVE_DATA. TRACKING evolved from DNT. |

### Corpus Versions

| Identifier | Date | Description |
|------------|------|-------------|
| OPPT-T1_C1.0_Section_Jan2026 | January 2026 | Initial release. 3,651 segments from 123 companies. Three-model consensus (Claude Haiku 4.5, GPT-5.2, Gemini-3-flash) with human arbiter. |

## Citing Specific Versions

When citing OPPT, specify both the taxonomy and corpus version:

```bibtex
@misc{brackin2026jurisdiction,
  title={Jurisdiction as Concealment: How Privacy Policies Hide Substantive Disclosures in Regional Compliance Sections},
  author={Brackin, Thomas},
  year={2026},
  eprint={2601.20792},
  archivePrefix={arXiv},
  primaryClass={cs.CY},
  note={Introduces OPPT v1.0 taxonomy and OPPT-T1\_C1.0\_Section\_Jan2026 corpus}
}
```

For reproducibility, always reference the full corpus identifier (e.g., `OPPT-T1_C1.0_Section_Jan2026`) rather than just "the OPPT dataset."

## Future Versions

Planned future work:
- **Sentence-level corpus**: `OPPT-T1_C1.1_Sentence_*` — same policies at finer granularity
- **Expanded corpus**: Additional companies and policy updates
- **Taxonomy refinements**: Based on community feedback and regulatory evolution
