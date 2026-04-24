#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate-plugin.py - UMPA プラグイン検証ツール

プラグインの構造とファイルが UMPA 仕様に従っているかを検証します。
"""

import os
import json
import sys
from pathlib import Path

# UTF-8 エンコーディングを強制
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

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
            with open(plugin_json, encoding='utf-8') as f:
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

    return errors, warnings

def validate_single_plugin(plugin_dir):
    """単一のプラグインを検証して結果を表示"""
    errors, warnings = check_plugin_structure(plugin_dir)

    print("\n" + "="*50)
    print(f"Validation: {plugin_dir}")
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

def validate_project_root():
    """プロジェクトルートの全プラグインを検証"""
    root = Path(".")
    plugins_to_check = []

    # Check for template/
    if (root / "template").is_dir():
        if (root / "template" / ".claude-plugin" / "plugin.json").exists():
            plugins_to_check.append("template")

    # Check for examples/
    if (root / "examples").is_dir():
        for example_dir in (root / "examples").iterdir():
            if example_dir.is_dir() and not example_dir.name.startswith("."):
                if (example_dir / ".claude-plugin" / "plugin.json").exists():
                    plugins_to_check.append(str(example_dir))

    if not plugins_to_check:
        print("❌ No valid plugins found to validate.")
        print("   Expected: template/ or examples/*/ with .claude-plugin/plugin.json")
        return 1

    all_valid = True
    for plugin in plugins_to_check:
        result = validate_single_plugin(plugin)
        if result != 0:
            all_valid = False

    print("\n" + "="*50)
    print("Overall Summary")
    print("="*50)
    if all_valid:
        print("✅ All plugins are valid!")
        return 0
    else:
        print("❌ Some plugins have errors or warnings.")
        return 1

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "help"]:
        print("Usage: python validate-plugin.py [plugin_directory]")
        print()
        print("Examples:")
        print("  python validate-plugin.py              # Validate all plugins (template/ and examples/)")
        print("  python validate-plugin.py template/    # Validate template/")
        print("  python validate-plugin.py my-plugin/   # Validate my-plugin/")
        sys.exit(0)

    if len(sys.argv) > 1:
        # Validate specific directory
        sys.exit(validate_single_plugin(sys.argv[1]))
    else:
        # Validate all plugins in project root
        sys.exit(validate_project_root())
