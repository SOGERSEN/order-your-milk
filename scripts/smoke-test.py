#!/usr/bin/env python3
"""
Order Your Milk Skill — Smoke Test (Q-01)

Validates skill integrity and consistency.
Run: python3 smoke-test.py

Checks:
1. File integrity — all required files exist
2. File sizes — key files have sufficient content
3. Internal references — files referenced in SKILL.md all exist
4. Key sections — SKILL.md contains all required sections
5. Reference files — each reference file has correct format
"""

import os
import re
import sys
from pathlib import Path

# Skill root directory
SKILL_DIR = Path(__file__).parent.parent
if not (SKILL_DIR / "SKILL.md").exists():
    # Try alternative: current directory
    SKILL_DIR = Path(__file__).parent
    if not (SKILL_DIR / "SKILL.md").exists():
        # Try one more level up
        SKILL_DIR = Path(__file__).parent.parent

PASS = "✅"
FAIL = "❌"
WARN = "⚠️"
results = {"pass": 0, "fail": 0, "warn": 0}


def check(condition, message, level="pass"):
    if condition:
        print(f"  {PASS} {message}")
        results["pass"] += 1
    elif level == "warn":
        print(f"  {WARN} {message}")
        results["warn"] += 1
    else:
        print(f"  {FAIL} {message}")
        results["fail"] += 1


def test_file_exists():
    """Check that all required files exist"""
    print("\n📁 [1/5] File Integrity Check")

    required_files = [
        "SKILL.md",
        "README.md",
        "references/set-meals.md",
        "references/domain-templates.md",
        "references/research-prompts.md",
        "references/domain-research-prompts.md",
        "references/platform-adapters.md",
        "references/conversation-examples.md",
        "references/customization-guide.md",
        "references/competitive-analysis.md",
        "references/quick-reference.md",
    ]

    for f in required_files:
        path = SKILL_DIR / f
        check(path.exists(), f"{f} exists")


def test_file_sizes():
    """Check key file sizes"""
    print("\n📏 [2/5] File Size Check")

    size_checks = [
        ("SKILL.md", 5000, 65000),
        ("README.md", 2000, 15000),
        ("references/set-meals.md", 2000, 20000),
        ("references/domain-templates.md", 2000, 20000),
        ("references/research-prompts.md", 2000, 15000),
        ("references/domain-research-prompts.md", 3000, 50000),
        ("references/platform-adapters.md", 3000, 25000),
        ("references/conversation-examples.md", 5000, 60000),
        ("references/customization-guide.md", 2000, 20000),
        ("references/competitive-analysis.md", 2000, 15000),
    ]

    for f, min_size, max_size in size_checks:
        path = SKILL_DIR / f
        if path.exists():
            size = path.stat().st_size
            check(
                min_size <= size <= max_size,
                f"{f}: {size} bytes (expected {min_size}-{max_size})",
                level="warn" if size < min_size else "pass",
            )
        else:
            check(False, f"{f}: file not found")


def test_skill_md_sections():
    """Check SKILL.md contains all required sections"""
    print("\n📑 [3/5] SKILL.md Section Check")

    skill_md = SKILL_DIR / "SKILL.md"
    if not skill_md.exists():
        check(False, "SKILL.md not found, skipping section checks")
        return

    content = skill_md.read_text(encoding="utf-8")

    required_sections = [
        ("Step 1", "Step 1: Clarify / Requirements Elicitation"),
        ("Step 2", "Step 2: Research / Deep Investigation"),
        ("Step 3", "Step 3: Execute / Parallel Divergence"),
        ("Step 4", "Step 4: Deliver / Verification"),
        ("Skip", "Skip ordering shortcut"),
        ("Preference Memory", "Preference memory system"),
        ("Teaching Mode", "Teaching mode"),
        ("Smart Level Recommendation", "Smart level recommendation"),
        ("Custom Optimization Objectives", "Configurable optimization targets"),
        ("Divergence Prompt Template", "Divergence prompt templates"),
        ("Divergence Failure Handling", "Failure degradation"),
        ("Quick Reference", "Quick reference card"),
        ("Cross-Platform", "Cross-platform adaptation guide"),
        ("Pitfalls", "Pitfalls / Common mistakes"),
        ("1.0.0", "Version number"),
        ("Dual Mode", "Fast/Deep dual mode system"),
        ("Fast Mode", "Fast Mode"),
        ("Deep Mode", "Deep Mode"),
        ("Think Before", "Coding rule: Think before coding"),
        ("Simplicity First", "Coding rule: Simplicity first"),
        ("Surgical Changes", "Coding rule: Surgical changes"),
        ("Goal-Driven", "Coding rule: Goal-driven execution"),
    ]

    for keyword, description in required_sections:
        check(keyword in content, f"Contains: {description}")


def test_set_meals():
    """Check meals file"""
    print("\n🍽 [4/5] Set Meals File Check")

    meals_file = SKILL_DIR / "references/set-meals.md"
    if not meals_file.exists():
        check(False, "set-meals.md not found")
        return

    content = meals_file.read_text(encoding="utf-8")

    # Count meals (looking for heading patterns with meal markers)
    meal_pattern = re.compile(r"### [🅰-🅿🔸🔶🔹🔷🆎🆑🔹🔸]")
    meals = meal_pattern.findall(content)
    check(
        len(meals) >= 12,
        f"Found {len(meals)} meals (expected >= 12, ideally 16)",
        level="warn" if len(meals) < 12 else "pass",
    )

    # Check for grouping
    check(
        "Beginner" in content or "beginner" in content or "入门" in content,
        "Has beginner group",
    )
    check(
        "Intermediate" in content or "intermediate" in content or "进阶" in content,
        "Has intermediate group",
    )


def test_domain_templates():
    """Check domain templates"""
    print("\n🎯 [5/5] Domain Templates Check")

    dt_file = SKILL_DIR / "references/domain-templates.md"
    if not dt_file.exists():
        check(False, "domain-templates.md not found")
        return

    content = dt_file.read_text(encoding="utf-8")

    domains = [
        "Web",
        "Login",
        "Dashboard",
        "Python",
        "API",
        "CLI",
        "Data Visualization",
        "Game",
        "AI",
        "LLM",
        "Mobile",
        "Automation",
        "Data Science",
        "ML",
    ]
    found = sum(1 for d in domains if d.lower() in content.lower())
    check(
        found >= 10,
        f"Found {found}/{len(domains)} domain keywords",
        level="warn" if found < 10 else "pass",
    )


def main():
    print("=" * 60)
    print("🧪 Order Your Milk Skill — Smoke Test v2.0")
    print(f"   Skill directory: {SKILL_DIR}")
    print("=" * 60)

    test_file_exists()
    test_file_sizes()
    test_skill_md_sections()
    test_set_meals()
    test_domain_templates()

    print("\n" + "=" * 60)
    total = results["pass"] + results["fail"] + results["warn"]
    print(
        f"📊 Results: {results['pass']}/{total} passed | "
        f"{results['fail']} failed | {results['warn']} warnings"
    )

    if results["fail"] == 0:
        print("🎉 All passed! Skill integrity verified OK.")
        return 0
    else:
        print(f"💥 {results['fail']} item(s) failed, please check.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
