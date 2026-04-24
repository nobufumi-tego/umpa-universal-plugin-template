#!/bin/bash

# add-language.sh - UMPA プラグインに新しい言語を追加

set -e

if [ $# -ne 1 ]; then
    echo "Usage: ./add-language.sh <language-code>"
    echo "Example: ./add-language.sh zh-CN"
    exit 1
fi

LANG_CODE=$1
PLUGIN_DIR=${2:-.}

# Create language directory
mkdir -p "$PLUGIN_DIR/references/$LANG_CODE"

# Copy base template files from English
if [ -d "$PLUGIN_DIR/references/en" ]; then
    cp "$PLUGIN_DIR/references/en/README.md" "$PLUGIN_DIR/references/$LANG_CODE/README.md"
    cp "$PLUGIN_DIR/references/en/01-concept.md" "$PLUGIN_DIR/references/$LANG_CODE/01-concept.md"
    cp "$PLUGIN_DIR/references/en/02-step-by-step.md" "$PLUGIN_DIR/references/$LANG_CODE/02-step-by-step.md"
    cp "$PLUGIN_DIR/references/en/03-case-studies.md" "$PLUGIN_DIR/references/$LANG_CODE/03-case-studies.md"
    cp "$PLUGIN_DIR/references/en/04-advanced.md" "$PLUGIN_DIR/references/$LANG_CODE/04-advanced.md"

    echo "✅ Created language directory: references/$LANG_CODE"
    echo "📝 Next steps:"
    echo "   1. Translate the files in references/$LANG_CODE/"
    echo "   2. Update the language code in README.md frontmatter"
    echo "   3. Commit and push"
else
    echo "❌ Error: English template not found in $PLUGIN_DIR/references/en/"
    exit 1
fi
