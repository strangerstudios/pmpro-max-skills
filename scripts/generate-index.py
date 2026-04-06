#!/usr/bin/env python3
"""
generate-index.py
Reads frontmatter from all skill.md files in the skills/ directory
and writes a fresh index.json at the repo root.

Usage:
    python3 scripts/generate-index.py
"""

import json
import os
import re
import sys

SKILLS_DIR = os.path.join(os.path.dirname(__file__), '..', 'skills')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'index.json')

REQUIRED_FIELDS = ['name', 'slug', 'category', 'one_shot', 'uses_profile', 'description', 'keywords']


def parse_frontmatter(filepath):
    """Parse YAML-like frontmatter from a markdown file. Returns dict or None."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None

    raw = match.group(1)
    data = {}

    for line in raw.splitlines():
        line = line.strip()
        if not line or ':' not in line:
            continue

        key, _, value = line.partition(':')
        key = key.strip()
        value = value.strip()

        # Boolean
        if value.lower() == 'true':
            data[key] = True
        elif value.lower() == 'false':
            data[key] = False
        # Inline array: [a, b, c]
        elif value.startswith('[') and value.endswith(']'):
            inner = value[1:-1]
            data[key] = [item.strip().strip('"').strip("'") for item in inner.split(',') if item.strip()]
        # Plain string
        else:
            data[key] = value.strip('"').strip("'")

    return data


def build_index():
    skills = []
    errors = []

    if not os.path.isdir(SKILLS_DIR):
        print(f"Error: skills/ directory not found at {SKILLS_DIR}", file=sys.stderr)
        sys.exit(1)

    for slug in sorted(os.listdir(SKILLS_DIR)):
        skill_path = os.path.join(SKILLS_DIR, slug, 'skill.md')
        if not os.path.isfile(skill_path):
            continue

        fm = parse_frontmatter(skill_path)
        if fm is None:
            errors.append(f"  {slug}: no frontmatter found")
            continue

        missing = [f for f in REQUIRED_FIELDS if f not in fm]
        if missing:
            errors.append(f"  {slug}: missing fields: {', '.join(missing)}")
            continue

        skills.append({
            "name": fm['name'],
            "slug": fm['slug'],
            "category": fm['category'],
            "one_shot": fm['one_shot'],
            "processing": fm.get('processing', 'site'),
            "uses_profile": fm['uses_profile'],
            "description": fm['description'],
            "keywords": fm['keywords'],
            "url": f"skills/{slug}/skill.md"
        })

    if errors:
        print("Warnings — skills skipped due to missing/invalid frontmatter:", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(skills, f, indent=2)
        f.write('\n')

    print(f"index.json updated — {len(skills)} skills indexed.")
    if errors:
        print(f"{len(errors)} skills skipped. See warnings above.")


if __name__ == '__main__':
    build_index()
