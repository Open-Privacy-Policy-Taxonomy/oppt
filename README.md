# Open Privacy Policy Taxonomy (OPPT)

**A standardized framework for analyzing and structuring privacy policy disclosures.**

[![Dataset on HuggingFace](https://img.shields.io/badge/Dataset-HuggingFace-yellow)](https://huggingface.co/datasets/Open-Privacy-Policy-Taxonomy/oppt-privacy-policies)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![arXiv](https://img.shields.io/badge/arXiv-cs.CY-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)

---

## Overview

OPPT is a 14-category taxonomy for classifying privacy policy content, extending the foundational [OPP-115 corpus](https://usableprivacy.org/data) (Wilson et al., ACL 2016) to address modern regulatory requirements including GDPR, CCPA/CPRA, and emerging AI transparency laws.

| Resource | Description |
|----------|-------------|
| [**Dataset**](https://huggingface.co/datasets/Open-Privacy-Policy-Taxonomy/oppt-privacy-policies) | 3,651 annotated segments from 123 companies |
| [**Specification**](specification/OPPT_v1.0.md) | Full taxonomy with category definitions |
| [**Methodology**](methodology/ANNOTATION.md) | How the dataset was created |

## Quick Start

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("Open-Privacy-Policy-Taxonomy/oppt-privacy-policies")

# Explore
for example in dataset["train"]:
    print(f"{example['company']}: {example['primary_category']}")
    print(f"  Text: {example['text'][:100]}...")
    break
```

## The 14 OPPT Categories

| Category | Description | Source |
|----------|-------------|--------|
| `FIRST_PARTY` | Data collected/used by the company | OPP-115 |
| `THIRD_PARTY` | Data shared with third parties | OPP-115 |
| `USER_CHOICE` | Opt-out and control mechanisms | OPP-115 |
| `USER_ACCESS` | Data access and portability rights | OPP-115 |
| `RETENTION` | Data storage and deletion practices | OPP-115 |
| `SECURITY` | Data protection measures | OPP-115 |
| `POLICY_CHANGE` | Policy update procedures | OPP-115 |
| `TRACKING` | Cookies, analytics, tracking tech | **OPPT** (evolved from DNT) |
| `INTL_SPECIFIC` | International transfers, children's privacy | OPP-115 |
| `OTHER` | Administrative content | OPP-115 |
| `REGIONAL` | Jurisdiction-specific sections | **OPPT** (new) |
| `SALE_SHARING` | Data sale/sharing for advertising | **OPPT** (new) |
| `AUTOMATED_DECISIONS` | Profiling, algorithmic decisions | **OPPT** (new) |
| `SENSITIVE_DATA` | Health, biometric, genetic data | **OPPT** (new) |

## Key Finding: Jurisdiction-Siloed Disclosure

Our analysis reveals a systematic pattern where companies hide substantive privacy disclosures in regional compliance sections:

- **77 of 123 companies (62.6%)** have jurisdiction-siloed disclosures
- **282 instances** of substantive practices appearing only in regional sections
- Most commonly siloed: data sales, automated decisions, sensitive data handling

Users outside the named jurisdiction never see these disclosures unless they read the entire policy.

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Companies | 123 |
| Segments | 3,651 |
| Categories | 14 |
| Unanimous agreement | 78.3% |
| Majority agreement | 20.5% |
| Human-resolved | 1.3% |

## Repository Structure

```
oppt/
├── specification/
│   └── OPPT_v1.0.md          # Full taxonomy specification
├── methodology/
│   ├── ANNOTATION.md         # Annotation process
│   └── OPP115_MAPPING.md     # Mapping to OPP-115
├── examples/
│   ├── load_dataset.py       # Basic loading example
│   └── analysis.ipynb        # Example analysis
└── schema/
    └── attributes.json       # Machine-readable attribute schema
```

## Citation

If you use OPPT in your research, please cite:

```bibtex
@misc{brackin2026jurisdiction,
  title={Jurisdiction as Concealment: How Privacy Policies Hide Substantive Disclosures in Regional Compliance Sections},
  author={Brackin, Thomas},
  year={2026},
  eprint={XXXX.XXXXX},
  archivePrefix={arXiv},
  primaryClass={cs.CY}
}
```

## License

This work is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).

- **Academic/Research use**: Free with attribution
- **Commercial use**: Contact tebrackin@outlook.com for licensing

## Acknowledgments

OPPT builds on the foundational work of the [Usable Privacy Policy Project](https://usableprivacy.org/) and the OPP-115 corpus.

## Related Work

- Wilson, S., et al. (2016). "[The Creation and Analysis of a Website Privacy Policy Corpus](https://aclanthology.org/P16-1126/)." ACL 2016.
- Dagstuhl Seminar 25021 (2025). "[Grand Challenges for Research on Privacy Documents](https://drops.dagstuhl.de/entities/document/10.4230/DagRep.15.1.1)."

## Contact

- **Issues**: [GitHub Issues](https://github.com/Open-Privacy-Policy-Taxonomy/oppt/issues)
- **Email**: tebrackin@outlook.com
