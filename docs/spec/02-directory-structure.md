# プラグイン - ディレクトリ構造

## プラグインの完全構成

### 最小構成

プラグインとして機能するために必須：

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          ← 必須
├── skills/
│   └── my-skill/
│       └── SKILL.md         ← 必須（最低1つ）
└── README.md
```

### 標準構成（推奨）

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          ← プラグインメタデータ
│
├── skills/                  ← 実行層
│   ├── skill-1/
│   │   └── SKILL.md
│   ├── skill-2/
│   │   └── SKILL.md
│   └── skill-N/
│       └── SKILL.md
│
├── commands/                ← オプション
│   ├── command-1.md
│   ├── command-2.md
│   └── command-N.md
│
├── agents/                  ← オプション
│   ├── agent-1.md
│   ├── agent-2.md
│   └── agent-N.md
│
├── references/              ← 学習層（重要）
│   ├── ja/
│   │   ├── README.md
│   │   ├── 01-concept.md
│   │   ├── 02-step-by-step.md
│   │   ├── 03-case-studies.md
│   │   └── 04-advanced.md
│   │
│   └── en/
│       └── (同じ構成)
│
├── README.md                ← ドキュメント
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

### フル構成（大規模プラグイン）

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
│
├── skills/
│   ├── skill-1/SKILL.md
│   └── skill-N/SKILL.md
│
├── commands/
│   ├── command-1.md
│   └── command-N.md
│
├── agents/
│   ├── agent-1.md
│   └── agent-N.md
│
├── hooks/                   ← イベントハンドラ
│   └── hooks.json
│
├── scripts/                 ← ユーティリティ
│   ├── script-1.py
│   ├── script-2.sh
│   └── script-N.js
│
├── templates/               ← テンプレート例
│   ├── template-1.json
│   ├── template-2.yaml
│   └── template-N.md
│
├── .mcp.json                ← MCP統合
│
├── references/
│   ├── ja/
│   ├── en/
│   ├── zh-CN/
│   ├── zh-TW/
│   ├── ko/
│   └── es/
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── .gitignore
│
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   ├── feature_request.md
    │   └── translation_request.md
    │
    ├── pull_request_template.md
    │
    └── workflows/
        └── validate.yml
```

---

## 各ディレクトリの説明

### `.claude-plugin/` - プラグイン定義

**必須**: ✅

```
.claude-plugin/
└── plugin.json
```

プラグインのメタデータ。詳細は [コンポーネント仕様](03-components.md)を参照。

### `skills/` - スキル定義

**必須**: ✅

```
skills/
├── skill-1/
│   └── SKILL.md
├── skill-2/
│   └── SKILL.md
└── skill-N/
    └── SKILL.md
```

各スキルの処理内容を定義（英語のみ）。

**命名規則**:
- ディレクトリ: `[skill-name-lowercase-with-hyphens]/`
- ファイル: `SKILL.md`

**例**:
```
skills/
├── lean-canvas-generator/SKILL.md
├── persona-builder/SKILL.md
└── value-prop-generator/SKILL.md
```

### `commands/` - スラッシュコマンド

**オプション**: ⭕

```
commands/
├── review-canvas.md
├── compare-canvases.md
└── export-to-pdf.md
```

ユーザーが呼び出せるコマンドを定義。

### `agents/` - カスタムエージェント

**オプション**: ⭕

```
agents/
├── analyzer.md
└── reviewer.md
```

複雑な処理を担当する専門エージェント。

### `hooks/` - イベントハンドラ

**オプション**: ⭕

```
hooks/
└── hooks.json
```

プラグインイベント（ツール使用前後など）に反応。

### `scripts/` - ユーティリティ

**オプション**: ⭕

```
scripts/
├── validate.py
├── migrate.sh
└── generate.js
```

Python、Bash、JavaScript などの実行スクリプト。

### `templates/` - テンプレート例

**オプション**: ⭕

```
templates/
├── blank-template.json
├── success-example.json
└── best-practice.md
```

ユーザーが参照するテンプレートやサンプル。

### `.mcp.json` - MCP 統合

**オプション**: ⭕

```
.mcp.json
```

外部ツール（Notion、Google Sheets、GitHub など）の統合。

### `references/` - 多言語学習資料

**重要**: ✅

```
references/
├── ja/
│   ├── README.md
│   ├── 01-concept.md
│   ├── 02-step-by-step.md
│   ├── 03-case-studies.md
│   └── 04-advanced.md
│
├── en/
│   └── (同じ構成)
│
├── zh-CN/
├── zh-TW/
├── ko/
└── es/
```

各言語のユーザーガイド（コンテキスト外なので無制限）。

### `README.md` - ドキュメント

**推奨**: ✅

プラグインの説明、使用方法、インストール方法。

### `CONTRIBUTING.md` - コントリビューション方針

**推奨**: ✅

バグ報告、機能提案、翻訳協力のやり方。

### `LICENSE` - ライセンス

**推奨**: ✅

通常は MIT ライセンス推奨。

### `.github/` - GitHub テンプレート

**推奨**: ✅

```
.github/
├── ISSUE_TEMPLATE/
│   ├── bug_report.md
│   ├── feature_request.md
│   └── translation_request.md
├── pull_request_template.md
└── workflows/
    └── validate.yml
```

Issue/PR テンプレートと CI/CD パイプライン。

---

## ファイルサイズの目安

| ファイル | 行数 | 説明 |
|---------|------|------|
| plugin.json | 10-20 | シンプル |
| SKILL.md | 100-200 | 簡潔に |
| commands/.md | 50-100 | 簡潔に |
| references/01-concept.md | 200-400 | 詳しく |
| references/02-step-by-step.md | 300-500 | 実装ガイド |
| references/03-case-studies.md | 200-300 | 実例 |
| references/04-advanced.md | 200-300 | 応用 |

---

## 命名規則

### ディレクトリ

```
skills/[skill-name-lowercase-with-hyphens]/
commands/ (flat, no subdirs)
agents/ (flat, no subdirs)
references/[lang-code]/
```

### 言語コード

```
ja         → 日本語
en         → 英語
zh-CN      → 簡体字中国語
zh-TW      → 繁體字中国語
ko         → 韓国語
es         → スペイン語
pt-BR      → ブラジルポルトガル語
```

### ファイル名

```
SKILL.md           → スキル定義（必ずこの名前）
[command].md       → コマンド定義
[agent].md         → エージェント定義
README.md          → ガイド
01-concept.md      → 学習資料（01～04の順序固定）
02-step-by-step.md
03-case-studies.md
04-advanced.md
```

---

## コンテキスト効率

### Claude Code に読み込まれるもの

```
plugin.json       ~100 tokens
SKILL.md          ~350 tokens/スキル
commands/         ~200 tokens
agents/           ~300-500 tokens/エージェント
hooks/            ~50 tokens
```

**合計初期**: ~1,200-1,500 tokens（言語数に関わらず固定）

### Claude Code に読み込まれないもの（0 tokens）

```
references/       ← 多言語学習資料（ユーザー用）
scripts/          ← 実行スクリプト（出力のみ）
templates/        ← テンプレート例（手動参照）
.github/          ← GitHub テンプレート
```

**結果**: 言語を追加してもコンテキストは増えない！

---

## ベストプラクティス

✅ **DO**:
- skills/ には SKILL.md だけ
- SKILL.md は簡潔に（400-600 words）
- references/ に詳しく書く
- 言語ごとに references/[lang]/ を作成

❌ **DON'T**:
- skills/[skill]/ に SKILL.md 以外を入れる
- SKILL.md に詳しすぎる説明を書く
- references/ を飛ばす
- 言語対応を実行層で実装する

---

## 実装例（Lean Canvas）

```
lean-canvas-plugin/
├── .claude-plugin/
│   └── plugin.json
│
├── skills/
│   └── lean-canvas-generator/
│       └── SKILL.md
│
├── references/
│   ├── ja/
│   │   ├── README.md
│   │   ├── 01-concept.md
│   │   ├── 02-step-by-step.md
│   │   ├── 03-case-studies.md
│   │   └── 04-advanced.md
│   │
│   └── en/
│       └── (同じ構成)
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

---

次に読むべきドキュメント：

- [コアコンポーネント仕様](03-components.md) - 各ファイルの詳細
- [学習層（References）](04-learning-layer.md) - references/ の書き方
- [クイックスタート](06-quickstart.md) - 10分でプラグイン開発開始

---

[← 仕様書ホーム](../SPECIFICATION.md) | [← 概要](01-overview.md) | [コアコンポーネント →](03-components.md)
