#!/usr/bin/env python3
"""
OPPT Dataset Loading Examples

This script demonstrates how to load and work with the OPPT dataset
from HuggingFace.

Requirements:
    pip install datasets

Usage:
    python load_dataset.py
"""

from datasets import load_dataset
from collections import Counter
import json


def main():
    # Load the dataset from HuggingFace
    print("Loading OPPT dataset from HuggingFace...")
    dataset = load_dataset("Open-Privacy-Policy-Taxonomy/oppt-privacy-policies")

    print(f"\nDataset loaded: {len(dataset['train'])} segments")

    # Basic exploration
    print("\n" + "=" * 50)
    print("BASIC EXPLORATION")
    print("=" * 50)

    # Show first example
    example = dataset["train"][0]
    print(f"\nFirst segment:")
    print(f"  Company: {example['company']}")
    print(f"  Category: {example['primary_category']}")
    print(f"  Consensus: {example['category_consensus_type']}")
    print(f"  Text preview: {example['text'][:100]}...")

    # Category distribution
    print("\n" + "=" * 50)
    print("CATEGORY DISTRIBUTION")
    print("=" * 50)

    categories = Counter(dataset["train"]["primary_category"])
    for cat, count in categories.most_common():
        pct = count / len(dataset["train"]) * 100
        print(f"  {cat}: {count} ({pct:.1f}%)")

    # Consensus type distribution
    print("\n" + "=" * 50)
    print("CONSENSUS TYPES")
    print("=" * 50)

    consensus_types = Counter(dataset["train"]["category_consensus_type"])
    for ct, count in consensus_types.most_common():
        pct = count / len(dataset["train"]) * 100
        print(f"  {ct}: {count} ({pct:.1f}%)")

    # Companies
    print("\n" + "=" * 50)
    print("COMPANIES")
    print("=" * 50)

    companies = set(dataset["train"]["company"])
    print(f"  Total companies: {len(companies)}")
    print(f"  Sample: {sorted(companies)[:10]}")

    # Working with attributes
    print("\n" + "=" * 50)
    print("WORKING WITH ATTRIBUTES")
    print("=" * 50)

    # Find a FIRST_PARTY example and show its attributes
    for item in dataset["train"]:
        if item["primary_category"] == "FIRST_PARTY":
            attrs = json.loads(item["attributes_annotator_1"])
            print(f"\nFIRST_PARTY example from {item['company']}:")
            print(f"  Attributes: {json.dumps(attrs, indent=4)}")
            break

    # Filtering examples
    print("\n" + "=" * 50)
    print("FILTERING EXAMPLES")
    print("=" * 50)

    # Filter to unanimous agreements only
    unanimous = dataset["train"].filter(
        lambda x: x["category_consensus_type"] == "unanimous"
    )
    print(f"\n  Unanimous agreements: {len(unanimous)} segments")

    # Filter to a specific company
    anthropic = dataset["train"].filter(
        lambda x: x["company"] == "anthropic"
    )
    print(f"  Anthropic segments: {len(anthropic)}")

    # Filter to REGIONAL category
    regional = dataset["train"].filter(
        lambda x: x["primary_category"] == "REGIONAL"
    )
    print(f"  REGIONAL segments: {len(regional)}")

    print("\n" + "=" * 50)
    print("Done!")
    print("=" * 50)


if __name__ == "__main__":
    main()
