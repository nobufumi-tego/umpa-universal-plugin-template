#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate-json.py - JSON ファイル検証ツール

プロジェクト内のすべての JSON ファイルの構文を検証します。
"""

import json
import sys
from pathlib import Path

# UTF-8 エンコーディングを強制
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def validate_json_files(root_dir="."):
    """プロジェクト内のすべての JSON ファイルを検証"""
    root = Path(root_dir)
    valid_files = []
    invalid_files = []

    # .gitignore や node_modules などを除外
    exclude_dirs = {'.git', '.github', 'node_modules', '.venv', '__pycache__', '.claude'}

    # すべての .json ファイルを検索
    for json_file in root.rglob('*.json'):
        # 除外ディレクトリをスキップ
        if any(excluded in json_file.parts for excluded in exclude_dirs):
            continue

        try:
            with open(json_file, encoding='utf-8') as f:
                json.load(f)
            valid_files.append(str(json_file))
            print(f"✅ {json_file}")
        except json.JSONDecodeError as e:
            invalid_files.append((str(json_file), str(e)))
            print(f"❌ {json_file}")
            print(f"   Error: {e}")
        except Exception as e:
            invalid_files.append((str(json_file), str(e)))
            print(f"❌ {json_file}")
            print(f"   Error: {e}")

    # Summary
    print("\n" + "="*60)
    print("JSON Validation Summary")
    print("="*60)
    print(f"\n✅ Valid files: {len(valid_files)}")
    for f in sorted(valid_files):
        print(f"   {f}")

    if invalid_files:
        print(f"\n❌ Invalid files: {len(invalid_files)}")
        for f, error in invalid_files:
            print(f"   {f}")
            print(f"      {error}")
        return 1

    print(f"\n✅ All {len(valid_files)} JSON files are valid!")
    return 0

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "help"]:
        print("Usage: python validate-json.py [root_directory]")
        print()
        print("Examples:")
        print("  python validate-json.py          # Validate JSON files in current directory")
        print("  python validate-json.py ../      # Validate JSON files in parent directory")
        sys.exit(0)

    root = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(validate_json_files(root))
