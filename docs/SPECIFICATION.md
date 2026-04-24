================================================================================
           Universal Multilingual Plugin Architecture (UMPA)
           汎用多言語プラグイン・メタアーキテクチャ仕様書
================================================================================

Document Version: 1.0.0
Last Updated: April 24, 2026
Author: Nobufumi Yoshida (@ynobufumi)
Purpose: Template for ANY multilingual Claude Code plugin

Key Concept: "Write once, scale to 10+ languages + unlimited use cases"

================================================================================
## 1. ARCHITECTURE OVERVIEW / アーキテクチャ概要
================================================================================

### 1.1 Design Philosophy

This specification defines a **meta-architecture** that allows ANY Claude Code plugin
to scale across multiple languages with ZERO modifications to execution layer.

**Core Principle**:
  Separation of Concerns
  ├─ Execution Layer (English, Claude-facing) → skills/, commands/, agents/
  ├─ Learning Layer (Multilingual, human-facing) → references/
  └─ Configuration Layer → plugin.json, .mcp.json

**Benefits**:
  ✅ Write skill once (English) → Automatic 10+ language support
  ✅ Add language by folder addition only
  ✅ No code changes required
  ✅ Scales from 1 skill to 100 skills
  ✅ Scales from 2 languages to infinite languages

### 1.2 Applicable Use Cases

This UMPA applies to:
  ✅ Business Templates (Lean Canvas, Persona, Value Prop)
  ✅ Code Generation (React Components, Python Scripts)
  ✅ Writing Assistance (Blog Posts, Marketing Copy)
  ✅ Data Analysis (Charts, Reports, Visualizations)
  ✅ Project Management (Timelines, Roadmaps, Checklists)
  ✅ Learning/Education (Courses, Tutorials, Exercises)
  ✅ Technical Documentation (API Docs, Setup Guides)
  ✅ ANY task that benefits from multilingual guidance

### 1.3 Scalability Matrix

| Dimension | Min | Target | Max | Effort |
|-----------|-----|--------|-----|--------|
| Skills | 1 | 5 | 50+ | Linear |
| Languages | 1 | 5 | 20+ | Linear (folder-based) |
| Context Cost | N/A | ~1,200 tokens | N/A | Fixed |
| Learning Materials | ~50KB | ~500KB | ~5MB | Scales with langs |

================================================================================
## 2. UNIVERSAL DIRECTORY TEMPLATE / ユニバーサル・ディレクトリテンプレート
================================================================================

### 2.1 Plugin Root Structure (Protocol)

[plugin-name]/
│
├── .claude-plugin/
│   └── plugin.json                      ✅ [REQUIRED] Plugin metadata
│
├── skills/                              ✅ [REQUIRED] Agent skills (Execution)
│   ├── [skill-1]/
│   │   └── SKILL.md                    ← English process only
│   ├── [skill-2]/
│   │   └── SKILL.md
│   └── [skill-N]/
│       └── SKILL.md
│
├── commands/                            ⭕ [OPTIONAL] Slash commands
│   ├── [command-1].md
│   ├── [command-2].md
│   └── [command-N].md
│
├── agents/                              ⭕ [OPTIONAL] Custom agents
│   ├── [agent-1].md
│   ├── [agent-2].md
│   └── [agent-N].md
│
├── hooks/                               ⭕ [OPTIONAL] Event handlers
│   └── hooks.json
│
├── scripts/                             ⭕ [OPTIONAL] Utility scripts
│   ├── [script-1].py
│   ├── [script-2].sh
│   └── [script-N].js
│
├── templates/                           ⭕ [OPTIONAL] Template files
│   ├── [template-1].json
│   ├── [template-2].yaml
│   └── [template-N].md
│
├── .mcp.json                            ⭕ [OPTIONAL] MCP integration
│
├── references/                          ✅ [UNIVERSAL] Multilingual learning
│   ├── ja/                              ← Japanese
│   │   ├── README.md
│   │   ├── 01-concept.md
│   │   ├── 02-step-by-step.md
│   │   ├── 03-case-studies.md
│   │   └── 04-advanced.md
│   │
│   ├── en/                              ← English
│   │   └── (same structure)
│   │
│   ├── zh-CN/                           ← Simplified Chinese
│   │   └── (same structure)
│   │
│   ├── zh-TW/                           ← Traditional Chinese
│   │   └── (same structure)
│   │
│   ├── ko/                              ← Korean
│   │   └── (same structure)
│   │
│   ├── es/                              ← Spanish (future)
│   │   └── (same structure)
│   │
│   └── [lang-code]/                     ← Any additional language
│       └── (same structure)
│
├── README.md                            ✅ Plugin documentation (English)
├── CONTRIBUTING.md                      ✅ Contribution guidelines (English)
├── LICENSE                              ✅ License file
├── .gitignore
└── .github/
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        ├── feature_request.md
        └── translation_request.md

**Legend**:
  ✅ = REQUIRED (Anthropic official specification)
  ⭕ = OPTIONAL (use as needed for your plugin)

================================================================================
## 3. CORE COMPONENTS SPECIFICATION / コアコンポーネント仕様
================================================================================

### 3.1 .claude-plugin/plugin.json (REQUIRED - Anthropic Official)

```json
{
  "name": "[plugin-name]",
  "description": "[One-line description for plugin manager]",
  "version": "1.0.0",
  "author": {
    "name": "[Author Name]",
    "email": "[author@example.com]"
  },
  "homepage": "[https://github.com/...]",
  "repository": "[https://github.com/...]",
  "license": "MIT",
  "keywords": ["tag1", "tag2", "multilingual"]
}
```

**Key Rules**:
  - Located at: .claude-plugin/plugin.json (ONLY file in .claude-plugin/)
  - Format: Valid JSON
  - name: Used for skill namespacing (/name:skill-name)
  - version: Semantic versioning (MAJOR.MINOR.PATCH)
  - license: Recommend MIT (OSS-friendly)

---

### 3.2 skills/ Directory (REQUIRED - Anthropic Official)

Location: plugin root / skills/
Format: Subdirectories per skill, each with SKILL.md
Naming: [skill-name-lowercase-with-hyphens]/SKILL.md

Example:
```
skills/
├── lean-canvas/
│   └── SKILL.md
├── persona-builder/
│   └── SKILL.md
└── competitive-analysis/
    └── SKILL.md
```

**SKILL.md Template**:

```markdown
---
name: [skill-display-name]
description: [One-line: When to use this skill - user-facing trigger words]
version: 1.0.0
---

# [Skill Display Name]

## Overview

[1-2 sentence summary of what this skill does and when Claude uses it]

## Learning Resources

For learning and detailed guidance in your preferred language:
- **日本語**: See references/ja/
- **English**: See references/en/
- **中文（简体）**: See references/zh-CN/
- **中文（繁體）**: See references/zh-TW/
- **한국어**: See references/ko/

## Process

[Main instructions for Claude. Step-by-step, concise, English only]

### Step 1: [Action Name]
[Brief instruction]
[Context/examples if needed]

### Step 2: [Action Name]
[Brief instruction]

... (Continue for each step)

## Input Format

[What does Claude expect as input?]

## Output Format

[What format should Claude produce? Include example JSON/text]

```

**SKILL.md Writing Guidelines**:
  ✅ English only (Claude Code reads this)
  ✅ 400-600 words (Progressive Disclosure)
  ✅ Process-focused (HOW, not WHY)
  ✅ Link to references/ for conceptual depth
  ✅ Clear input/output format specification
  ❌ Don't include detailed explanations (references/ is for that)
  ❌ Don't include philosophy/background (references/ is for that)

---

### 3.3 commands/ Directory (OPTIONAL - Anthropic Official)

Location: plugin root / commands/
Format: Markdown files (flat, no subdirectories)
Naming: [command-name].md

Example:
```
commands/
├── review-canvas.md
├── compare-canvases.md
└── export-to-pdf.md
```

**Template**:

```markdown
---
description: [What this command does - user-facing description]
disable-model-invocation: [true/false]
---

# [Command Display Name]

## Purpose

[One paragraph describing purpose and use case]

## Input

User provides:
- [Input 1]: [Description]
- [Input 2]: [Description]

## Process

[How you (Claude) process the input]

## Output

[What you return - format and content]

## Examples

[Real example input/output]

```

---

### 3.4 agents/ Directory (OPTIONAL - Anthropic Official)

Location: plugin root / agents/
Format: Markdown files with YAML frontmatter

Example:
```
agents/
├── analyzer.md
└── reviewer.md
```

**Template**:

```markdown
---
description: [Agent role - what problem does it solve?]
capabilities:
  - [Capability 1]
  - [Capability 2]
  - [Capability 3]
---

# [Agent Name]

## Role

[Detailed description of this agent's role and expertise]

## Capabilities

- [Capability 1]: [Description]
- [Capability 2]: [Description]

## When to Activate

- [Trigger 1]
- [Trigger 2]

```

---

### 3.5 hooks/ Directory (OPTIONAL - Anthropic Official)

Location: plugin root / hooks/
Format: hooks.json

**Template**:

```json
{
  "hooks": {
    "[HookType]": [
      {
        "matcher": "[pattern]",
        "hooks": [
          {
            "type": "command",
            "command": "python ${CLAUDE_PLUGIN_ROOT}/scripts/script.py"
          }
        ]
      }
    ]
  }
}
```

Hook Types:
- PostToolUse: After Claude uses a tool
- PreToolUse: Before Claude uses a tool
- SessionStart: When session begins
- SessionEnd: When session ends

---

### 3.6 scripts/ Directory (OPTIONAL - Anthropic Official)

Location: plugin root / scripts/
Format: Python, Bash, JavaScript, etc.

Key Rules:
  ✅ Executable scripts (executed, not loaded into context)
  ✅ Use ${CLAUDE_PLUGIN_ROOT} for portable paths
  ✅ Output to stdout or files (results consumed by Claude)
  ❌ Source code NOT included in context (only output matters)

Example:
```bash
# scripts/validate.py
#!/usr/bin/env python3

import json
import sys

def validate_canvas(canvas_json):
    # Validation logic
    return True

if __name__ == "__main__":
    data = json.load(sys.stdin)
    result = validate_canvas(data)
    print(json.dumps({"valid": result}))
```

---

### 3.7 templates/ Directory (OPTIONAL - Anthropic Official)

Location: plugin root / templates/
Format: JSON, YAML, Markdown, or other formats

Purpose: Provides starting templates, examples, or boilerplate

Example:
```
templates/
├── blank-template.json        ← Empty/default template
├── success-example.json       ← Real success case
└── failure-example.json       ← Common mistakes example
```

---

### 3.8 .mcp.json (OPTIONAL - Anthropic Official)

Location: plugin root / .mcp.json
Format: JSON array of MCP server configurations

Purpose: External tool integration (Notion, Google Sheets, GitHub, etc.)

**Template**:

```json
[
  {
    "name": "[service-name]",
    "type": "http",
    "url": "[https://api.service.com/v1]",
    "auth": "[oauth2/api_key/none]",
    "description": "[What this integration enables]"
  }
]
```

---

## 4. UNIVERSAL LEARNING LAYER / ユニバーサル学習層
================================================================================

### 4.1 references/ Directory (UNIVERSAL - Independent of Use Case)

Location: plugin root / references/
Purpose: Multilingual learning materials (NOT loaded by Claude Code)
Structure: Identical across all languages
Cost: 0 tokens (completely outside context)

**Protocol**:
```
references/
├── ja/                       ← Japanese
│   ├── README.md
│   ├── 01-concept.md
│   ├── 02-step-by-step.md
│   ├── 03-case-studies.md
│   └── 04-advanced.md
│
├── en/                       ← English (template language)
│   └── (same 5 files)
│
├── zh-CN/                    ← Simplified Chinese
│   └── (same 5 files)
│
├── zh-TW/                    ← Traditional Chinese
│   └── (same 5 files)
│
├── ko/                       ← Korean
│   └── (same 5 files)
│
├── es/                       ← Spanish (future)
│   └── (same 5 files)
│
└── [lang-code]/              ← Any language you want
    └── (same 5 files)
```

### 4.2 references/[lang]/README.md (Language Guide)

**Purpose**: Overview of learning materials for that language

**Template** (ja example):

```markdown
---
title: "学習ガイド - 日本語"
language: ja
---

# [Plugin Name] 学習ガイド

このフォルダは [Plugin Name] の日本語学習資料です。

## 推奨学習パス

### 初級者向け（初めての方）
1. 01-concept.md - 背景・なぜこれが必要か
2. 02-step-by-step.md - 実装方法・実践ガイド

### 中級者向け（実運用・改善）
1. 01-concept.md （復習）
2. 03-case-studies.md （失敗事例から学ぶ）
3. 02-step-by-step.md （改善実装）

### 上級者向け（カスタマイズ・応用）
1. 04-advanced.md （応用テクニック）
2. 03-case-studies.md （パターン認識）

## ファイル説明

| ファイル | 内容 | 読む時期 |
|---------|------|---------|
| 01-concept.md | 背景・理論・なぜ必要か | 最初 |
| 02-step-by-step.md | 実装ガイド・ステップバイステップ | 次 |
| 03-case-studies.md | 失敗事例・成功パターン | 実装後 |
| 04-advanced.md | 応用テクニック・深掘り | 経験者向け |

```

### 4.3 references/[lang]/01-concept.md (Concept & Theory)

**Purpose**: Explain WHAT, WHY, and WHEN

**Length**: 1000-1500 words

**Content Structure**:

```markdown
# [Feature] の背景・理論

## はじめに

[このセクションが何について書かれているか簡潔に説明]

## [Concept Name] とは？

[定義・説明・図解可]

## なぜ必要か？

[ビジネス的理由・効果・メリット]

## 歴史と進化

[誕生背景・流行の変遷]

## 実例

### 成功事例
- [Company A]: [何をしたか・結果]
- [Company B]: [何をしたか・結果]

### 失敗事例
- [Company C]: [何が違ったか]

## よくある質問

- Q: [質問]
  A: [回答]

```

### 4.4 references/[lang]/02-step-by-step.md (Implementation Guide)

**Purpose**: HOW-TO guide with detailed instructions

**Length**: 2000-3000 words

**Content Structure**:

```markdown
# ステップバイステップ実装ガイド

## 準備

[必要な環境・前提知識・ツール]

## プロセス

### ステップ 1: [Action]

[詳細な手順]

**質問リスト**
- [質問 1]
- [質問 2]

**NG例**
```
[悪い例]
```

**OK例**
```
[良い例]
```

### ステップ 2: [Action]

[同じ構造で繰り返す]

...

## よくある間違い

- [間違い 1]: [なぜそうなるか・対策]
- [間違い 2]: [なぜそうなるか・対策]

## 便利なテンプレート

[テンプレートまたはチェックリスト]

```

### 4.5 references/[lang]/03-case-studies.md (Real-World Examples)

**Purpose**: Learn from actual success/failure cases

**Length**: 1500-2000 words

**Content Structure**:

```markdown
# ケーススタディ：実例から学ぶ

## 成功事例

### ケース 1: [Company Name]

**背景**: [状況説明]

**実施内容**: [何をしたか]

**結果**: [成果]

**学べる点**: [このケースから学べること]

### ケース 2: [Company Name]

[同じ構造]

## 失敗事例

### ケース 3: [Company Name]

**背景**: [状況説明]

**失敗点**: [何が上手くいかなかったか]

**原因**: [なぜそうなったか]

**教訓**: [学べる教訓]

### ケース 4: [Company Name]

[同じ構造]

## パターン分析

### 成功企業の共通点
- [パターン 1]
- [パターン 2]

### 失敗パターン
- [パターン 1]
- [パターン 2]

```

### 4.6 references/[lang]/04-advanced.md (Advanced Techniques)

**Purpose**: Deep dive for experienced users

**Length**: 1000-1500 words

**Content Structure**:

```markdown
# 応用テクニック・深掘り

## 高度な活用方法

### テクニック 1: [Name]

[詳細説明・使い時・注意点]

### テクニック 2: [Name]

[詳細説明・使い時・注意点]

## 他のフレームワークとの組み合わせ

- [Framework A] との連携方法
- [Framework B] との使い分け

## よくある質問 (FAQ)

- Q: [質問]
  A: [詳細回答]

## まとめ

[最後のアドバイス・推奨される進め方]

```

================================================================================
## 5. LINKING PROTOCOL / リンク仕様
================================================================================

### 5.1 SKILL.md から references/ へのリンク

In SKILL.md (Execution Layer):

```markdown
## Learning Resources

For learning and detailed guidance in your preferred language:
- **日本語**: See references/ja/
- **English**: See references/en/
- **中文（简体）**: See references/zh-CN/
- **中文（繁體）**: See references/zh-TW/
- **한국어**: See references/ko/
```

In command.md:

```markdown
For detailed examples and case studies:
See references/en/03-case-studies.md
```

### 5.2 Main README.md から references/ へのリンク

```markdown
# Plugin Name

[Brief description]

## Learning Materials

Learn in your preferred language:

| Language | Guide |
|----------|-------|
| 日本語 | [Learning Guide](references/ja/README.md) |
| English | [Learning Guide](references/en/README.md) |
| 简体中文 | [Learning Guide](references/zh-CN/README.md) |
| 繁體中文 | [Learning Guide](references/zh-TW/README.md) |
| 한국어 | [Learning Guide](references/ko/README.md) |

```

================================================================================
## 6. LANGUAGE SUPPORT ROADMAP / 言語対応ロードマップ
================================================================================

### 6.1 Phase-Based Rollout

**Phase 0: Core Languages** (Month 1)
- ja (日本語) - Native
- en (English) - Required

**Phase 1: Asian Markets** (Month 2)
- zh-CN (简体中文) - Simplified Chinese
- zh-TW (繁體中文) - Traditional Chinese

**Phase 2: East Asia** (Month 3)
- ko (한국어) - Korean

**Phase 3: Global** (Month 4+)
- es (Español) - Spanish
- pt-BR (Português) - Brazilian Portuguese
- th (ไทย) - Thai
- vi (Tiếng Việt) - Vietnamese

### 6.2 Adding a New Language (Standard Procedure)

**Effort**: 4-6 hours (translation + testing)

**Step 1**: Create folder
```bash
mkdir -p references/[lang-code]
```

**Step 2**: Create 5 files (translate from en)
```bash
cp references/en/README.md references/[lang-code]/README.md
cp references/en/01-concept.md references/[lang-code]/01-concept.md
cp references/en/02-step-by-step.md references/[lang-code]/02-step-by-step.md
cp references/en/03-case-studies.md references/[lang-code]/03-case-studies.md
cp references/en/04-advanced.md references/[lang-code]/04-advanced.md
```

**Step 3**: Translate content (professional translator or Claude API)

**Step 4**: Update plugin README.md
```markdown
- [Language Name](references/[lang-code]/)
```

**Step 5**: Commit and push
```bash
git add references/[lang-code]/
git commit -m "Add [Language Name] support"
git push
```

**Impact on Plugin**:
- Context cost: +0 tokens (references/ outside context)
- Plugin size: +50-100 KB
- Execution layer: No changes (SKILL.md, commands/, etc. untouched)

================================================================================
## 7. USE CASE EXAMPLES / ユースケース例
================================================================================

### 7.1 Example 1: Business Template Plugin

Plugin Name: `startup-templates-jp`

Skills:
- lean-canvas-jp
- persona-builder-jp
- value-prop-gen-jp

Commands:
- review-canvas
- compare-canvases
- export-canvas

Structure: ✅ Follows UMPA exactly
(See earlier specification for details)

---

### 7.2 Example 2: Code Generation Plugin

Plugin Name: `react-component-generator`

Skills:
- react-button-generator
- react-form-generator
- react-modal-generator

Commands:
- review-component-quality
- optimize-performance
- export-to-repo

references/ structure (same):
- ja/01-concept.md (What is component design?)
- ja/02-step-by-step.md (How to generate components)
- ja/03-case-studies.md (Component patterns from real projects)
- ja/04-advanced.md (Custom styling, accessibility, testing)

---

### 7.3 Example 3: Writing Assistant Plugin

Plugin Name: `content-assistant-jp`

Skills:
- blog-post-generator
- marketing-copy-generator
- documentation-writer

Commands:
- review-content-quality
- improve-tone-consistency
- export-to-markdown

references/ structure (same):
- ja/01-concept.md (Writing principles)
- ja/02-step-by-step.md (Content creation process)
- ja/03-case-studies.md (Successful content examples)
- ja/04-advanced.md (SEO, accessibility, localization)

---

### 7.4 Example 4: Data Analysis Plugin

Plugin Name: `data-analyst-pro`

Skills:
- chart-generator
- statistical-analyzer
- report-builder

Commands:
- validate-data-quality
- benchmark-analysis
- export-findings

references/ structure (same):
- ja/01-concept.md (Data analysis fundamentals)
- ja/02-step-by-step.md (Analysis workflow)
- ja/03-case-studies.md (Real-world analysis examples)
- ja/04-advanced.md (Advanced statistical methods, visualization)

================================================================================
## 8. CONTEXT EFFICIENCY GUARANTEE / コンテキスト効率保証
================================================================================

### 8.1 Token Budget Guarantee

**Fixed Costs** (always loaded):
- plugin.json: ~100 tokens
- SKILL.md (per skill): ~350-400 tokens
- commands/: ~200 tokens
- agents/ (if used): ~300-500 tokens per agent
- hooks/: ~50 tokens

**Variable Costs** (on-demand):
- scripts/: Executed, not loaded (0 tokens)
- templates/: User-referenced, not auto-loaded (0 tokens)
- references/: User-read manually, not auto-loaded (0 tokens)

**Total Initial Context**: ~1,100-1,500 tokens (regardless of language count)

**Language Addition Impact**: +0 tokens per language

### 8.2 Progressive Disclosure Verification

| Timeline | Component | Action | Context Impact |
|----------|-----------|--------|-----------------|
| T0 | plugin.json | Plugin init | +100 tokens |
| T1 | SKILL.md | Skill triggered | +350 tokens |
| T2 | references/ | User reads manually | +0 tokens |
| T3 | scripts/ | Executed | +0 tokens (output only) |
| T4 | Additional language | User switches to ja | +0 tokens |

**Result**: Context efficiency maintained across all languages and skills.

================================================================================
## 9. TEMPLATE GENERATION WORKFLOW / テンプレート生成ワークフロー
================================================================================

### 9.1 How to Use This UMPA as a Template

**Scenario**: You want to create a new multilingual plugin

**Step 1**: Clone/copy the UMPA structure
```bash
cp -r universal-plugin-template/ my-new-plugin/
cd my-new-plugin/
```

**Step 2**: Customize plugin.json
```json
{
  "name": "my-plugin-name",
  "description": "My custom plugin",
  "version": "1.0.0"
}
```

**Step 3**: Create your SKILL.md
```
skills/
└── my-skill/
    └── SKILL.md    ← Write English process here
```

**Step 4**: Create references/ (use UMPA templates)
```
references/
├── ja/
│   ├── 01-concept.md        ← Adapted from template
│   ├── 02-step-by-step.md   ← Adapted from template
│   └── ...
└── en/
    └── (same structure)
```

**Step 5**: Test with Claude
```bash
claude --plugin-dir .
```

**Step 6**: Iterate and improve

### 9.2 Using Claude as Your Template Copilot

**Wallball Strategy** (Prompt Claude to help build templates):

```
You: I want to create a new plugin for [PURPOSE].

Based on the Universal Multilingual Plugin Architecture (UMPA),
help me design:

1. What skills should I create?
2. What commands would be useful?
3. What should each references/ file contain?
4. What example structure fits my use case?

Here's the UMPA spec: [paste entire spec]
Here's my plugin idea: [describe plugin idea]

Help me scaffold the plugin structure.
```

Claude will:
- ✅ Suggest skill names and purposes
- ✅ Design the SKILL.md structure
- ✅ Outline references/ content
- ✅ Propose commands/agents
- ✅ Create template files

**Then you follow the structure and expand with content.**

================================================================================
## 10. SCALABILITY ANALYSIS / スケーラビリティ分析
================================================================================

### 10.1 Growth Projections

| Timeline | Skills | Languages | Context | Effort |
|----------|--------|-----------|---------|--------|
| Month 1 | 3 | 2 (ja, en) | 1,200t | ~40h |
| Month 2 | 3 | 4 (+zh-CN, zh-TW) | 1,200t | +20h |
| Month 3 | 3 | 5 (+ko) | 1,200t | +15h |
| Month 6 | 5 | 7 (+es, pt-BR) | 1,300t | +60h |
| Month 12 | 10 | 10 | 1,500t | +200h |

**Key Insight**: Context cost remains fixed. Only translation effort scales.

### 10.2 Maintenance Cost Model

**Fixed Costs** (one-time):
- Plugin creation: 20-40 hours
- Core SKILL.md writing: 5-10 hours per skill
- English references/: 15-20 hours

**Variable Costs** (per language):
- Translation: 4-6 hours × number of languages
- Localization review: 2-3 hours per language

**Monthly Maintenance**:
- Bug fixes: 5-10 hours
- New features: 10-20 hours
- Language support: 2-3 hours per new language

================================================================================
## 11. BEST PRACTICES & GUIDELINES / ベストプラクティス
================================================================================

### 11.1 SKILL.md Writing Best Practices

✅ DO:
- Write in clear, procedural English
- Use numbered steps for clarity
- Include input/output format specification
- Link to references/ for depth
- Keep it under 600 words
- Use examples sparingly (detailed examples go in references/)

❌ DON'T:
- Include philosophy (references/ is for that)
- Explain WHY in detail (references/01-concept.md is for that)
- Make it too long
- Duplicate content from references/
- Use technical jargon without explanation

### 11.2 references/ Writing Best Practices

✅ DO:
- Write in the target language fluently
- Use cultural context appropriate to audience
- Include real-world examples from that market
- Provide detailed explanations
- Use visuals/diagrams where helpful
- Proofread carefully

❌ DON'T:
- Machine-translate without review
- Copy execution layer content
- Skip cultural localization
- Leave references to non-existent resources
- Make files too long

### 11.3 Testing Checklist

Before releasing:

- [ ] All SKILL.md files load without error
- [ ] Each skill is invokable: /plugin-name:skill-name
- [ ] All commands work
- [ ] All links in references/ are correct
- [ ] No broken Markdown syntax
- [ ] references/ files are readable
- [ ] plugin.json is valid JSON
- [ ] Token count verified (< 1,500 initial)
- [ ] Language links in README.md work
- [ ] Each language structure is consistent

================================================================================
## 12. QUICK START: Creating Your First Plugin
================================================================================

### Step 1: Use UMPA Template

```bash
# Clone universal template
git clone https://github.com/ynobufumi/umpa-universal-plugin-template.git
cd umpa-universal-plugin-template
```

### Step 2: Customize for Your Use Case

```bash
# Rename plugin
mv universal-plugin-template my-awesome-plugin
cd my-awesome-plugin

# Edit plugin.json
vim .claude-plugin/plugin.json
# Change: name, description, author
```

### Step 3: Create Your First Skill

```bash
# Create skill folder
mkdir skills/my-first-skill

# Write SKILL.md (use template from Section 3.2)
vim skills/my-first-skill/SKILL.md
```

### Step 4: Test Locally

```bash
# Start Claude Code with your plugin
claude --plugin-dir .

# Test skill
/my-awesome-plugin:my-first-skill
```

### Step 5: Create English references/

```bash
# Create basic structure
mkdir -p references/en
vim references/en/01-concept.md        # Use template from Section 4.3
vim references/en/02-step-by-step.md   # Use template from Section 4.4
vim references/en/03-case-studies.md   # Use template from Section 4.5
vim references/en/04-advanced.md       # Use template from Section 4.6
```

### Step 6: Add Japanese

```bash
# Copy English as template
cp -r references/en references/ja

# Translate (use Claude API or translator)
# All 5 files → Japanese

# Test that links work
```

### Step 7: Publish

```bash
# Push to GitHub
git push origin main

# Submit to plugin marketplace
# (Instructions: https://code.claude.com/docs/en/plugins)
```

**Congratulations!** You now have a multilingual plugin following UMPA.

================================================================================
## 13. TEMPLATE REPOSITORY / テンプレートリポジトリ
================================================================================

### 13.1 Recommended Repository Structure

```
umpa-universal-plugin-template/
│
├── README.md                    ← How to use this template
├── SPECIFICATION.md             ← Full UMPA specification
├── QUICKSTART.md                ← 10-minute setup guide
│
├── .claude-plugin/
│   └── plugin.json              ← Example (edit this)
│
├── skills/
│   └── example-skill/
│       └── SKILL.md             ← Template (replace content)
│
├── commands/
│   └── example-command.md       ← Template (delete or edit)
│
├── agents/
│   └── example-agent.md         ← Template (delete or edit)
│
├── references/
│   ├── en/
│   │   ├── README.md            ← Template language
│   │   ├── 01-concept.md        ← Template
│   │   ├── 02-step-by-step.md   ← Template
│   │   ├── 03-case-studies.md   ← Template
│   │   └── 04-advanced.md       ← Template
│   └── ja/
│       └── (translated templates)
│
├── scripts/
│   └── example-script.py        ← Example script
│
├── templates/
│   └── example.json             ← Example template
│
├── LICENSE
└── .github/
    └── ISSUE_TEMPLATE/
        └── ...
```

### 13.2 Using the Template Repository

For users wanting to create their own plugin:

```bash
# Use as GitHub template
# Option 1: GitHub "Use this template" button
# Option 2: Clone and customize
git clone https://github.com/ynobufumi/umpa-universal-plugin-template.git
cd umpa-universal-plugin-template
rm -rf .git
git init
# ... customize and commit your version
```

================================================================================
## 14. DOCUMENT HISTORY & VERSIONING
================================================================================

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-04-24 | Nobufumi Yoshida | Initial UMPA specification |
| | | | Universal multilingual architecture |
| | | | Generic use case templates |
| | | | Plugin scaffolding guide |

================================================================================
## APPENDIX A: COMPLETE SKILL.MD TEMPLATE
================================================================================

```markdown
---
name: [skill-identifier-kebab-case]
description: [One-line description that tells users when Claude will use this]
version: 1.0.0
---

# [Skill Display Name]

## Overview

[1-2 sentences: What does this skill do? When/why would Claude use it?]

## Learning Resources

For learning and detailed guidance in your preferred language:
- **日本語**: See references/ja/
- **English**: See references/en/
- **中文（简体）**: See references/zh-CN/
- **中文（繁體）**: See references/zh-TW/
- **한국어**: See references/ko/

## Process

[Main instructions for Claude. 400-600 words total.]

### Step 1: [Action Name]

[Detailed instruction for this step]

Example:
```
[If applicable, show an example]
```

### Step 2: [Action Name]

[Detailed instruction]

... (Continue for each main step)

## Input Format

[Describe what Claude should expect as input]

Example:
```
{
  "field1": "value",
  "field2": "value"
}
```

## Output Format

[Describe the expected output format]

Example:
```
{
  "result": "...",
  "analysis": "..."
}
```

## Best Practices

- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

## Common Pitfalls

- [Pitfall 1]: [How to avoid]
- [Pitfall 2]: [How to avoid]

```

================================================================================
END OF UMPA SPECIFICATION V1.0.0
================================================================================

This Universal Multilingual Plugin Architecture (UMPA) is designed to scale
from 1 plugin to 1,000 plugins, from 2 languages to 20+ languages, while
maintaining zero changes to the execution layer and preserving context
efficiency at 96%+.

Use this specification as a blueprint for creating multilingual Claude Code
plugins that can serve global audiences without reinventing the wheel.

================================================================================
