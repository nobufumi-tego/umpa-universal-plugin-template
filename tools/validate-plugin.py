#!/usr/bin/env python3
"""
validate-plugin.py - UMPA プラグイン検証ツール

プラグインの構造とファイルが UMPA 仕様に従っているかを検証します。
"""

import os
import json
import sys
from pathlib import Path

def check_plugin_structure(plugin_dir="."):
    """プラグイン構造を検証"""
    errors = []
    warnings = []

    plugin_path = Path(plugin_dir)

    # Check plugin.json
    plugin_json = plugin_path / ".claude-plugin" / "plugin.json"
    if not plugin_json.exists():
        errors.append("❌ Missing: .claude-plugin/plugin.json")
    else:
        try:
            with open(plugin_json) as f:
                config = json.load(f)
                required_fields = ["name", "description", "version", "author"]
                missing_fields = [f for f in required_fields if f not in config]
                if missing_fields:
                    errors.append(f"❌ plugin.json missing fields: {missing_fields}")
                else:
                    print(f"✅ plugin.json valid")
        except json.JSONDecodeError as e:
            errors.append(f"❌ plugin.json is invalid JSON: {e}")

    # Check skills directory
    skills_dir = plugin_path / "skills"
    if not skills_dir.exists():
        errors.append("❌ Missing: skills/ directory")
    else:
        skill_count = 0
        for skill in skills_dir.iterdir():
            if skill.is_dir() and not skill.name.startswith("."):
                skill_md = skill / "SKILL.md"
                if skill_md.exists():
                    skill_count += 1
                    print(f"✅ Found skill: {skill.name}/SKILL.md")
                else:
                    errors.append(f"❌ Missing: skills/{skill.name}/SKILL.md")

        if skill_count == 0:
            warnings.append("⚠️  No skills found in skills/ directory")

    # Check references structure
    references_dir = plugin_path / "references"
    if references_dir.exists():
        languages = [d.name for d in references_dir.iterdir() if d.is_dir()]
        if languages:
            print(f"✅ Found languages: {', '.join(languages)}")

            required_files = ["README.md", "01-concept.md", "02-step-by-step.md",
                            "03-case-studies.md", "04-advanced.md"]

            for lang in languages:
                lang_dir = references_dir / lang
                for req_file in required_files:
                    if not (lang_dir / req_file).exists():
                        warnings.append(f"⚠️  Missing: references/{lang}/{req_file}")
        else:
            warnings.append("⚠️  No language folders found in references/")
    else:
        warnings.append("⚠️  Missing: references/ directory")

    # Summary
    print("\n" + "="*50)
    print("Validation Summary")
    print("="*50)

    if errors:
        print(f"\n❌ Errors ({len(errors)}):")
        for error in errors:
            print(f"  {error}")

    if warnings:
        print(f"\n⚠️  Warnings ({len(warnings)}):")
        for warning in warnings:
            print(f"  {warning}")

    if not errors and not warnings:
        print("\n✅ All checks passed! Plugin structure is valid.")
        return 0

    return 1 if errors else 0

if __name__ == "__main__":
    plugin_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(check_plugin_structure(plugin_dir))
