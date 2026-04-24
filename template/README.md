# テンプレートプラグイン

このフォルダは、UMPA（汎用多言語プラグイン・メタアーキテクチャ）に従った新しいプラグインを作成するための骨組みテンプレートです。

## セットアップ手順

### 1. プラグイン情報を更新

`.claude-plugin/plugin.json` を編集して、以下を変更してください：

```json
{
  "name": "your-plugin-name",
  "description": "あなたのプラグインの説明",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  },
  "homepage": "https://github.com/your-username/your-plugin-name",
  "repository": "https://github.com/your-username/your-plugin-name"
}
```

### 2. スキルを作成

`skills/` フォルダ内に、あなたのプラグインのスキルを追加してください。

```bash
mkdir skills/your-skill-name
vim skills/your-skill-name/SKILL.md
```

**SKILL.md テンプレート** は `example-skill/SKILL.md` を参照してください。

### 3. 学習資料を作成

`references/` フォルダで、日本語と英語の学習資料を作成してください。

```bash
mkdir -p references/ja references/en
```

各言語フォルダに以下を作成します：
- `README.md` — 学習ガイド
- `01-concept.md` — 背景・理論
- `02-step-by-step.md` — 実装ガイド
- `03-case-studies.md` — ケーススタディ
- `04-advanced.md` — 応用テクニック

テンプレートは `references/ja/` と `references/en/` を参照してください。

### 4. テスト

```bash
claude --plugin-dir .
```

テストコマンド：
```
/your-plugin-name:your-skill-name
```

## ディレクトリ構造

```
your-plugin-name/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── your-skill-name/
│       └── SKILL.md
├── commands/ (optional)
├── agents/ (optional)
├── references/
│   ├── ja/
│   │   ├── README.md
│   │   ├── 01-concept.md
│   │   ├── 02-step-by-step.md
│   │   ├── 03-case-studies.md
│   │   └── 04-advanced.md
│   └── en/
│       └── (same structure)
├── scripts/ (optional)
├── templates/ (optional)
├── README.md
├── LICENSE
└── .github/
    └── ISSUE_TEMPLATE/
```

## 参考資料

- **UMPA 仕様書**: `../../docs/SPECIFICATION.md`
- **実装例**: `../../examples/`
  - Lean Canvas プラグイン
  - コード生成プラグイン

## 次のステップ

1. このテンプレートをコピーしてカスタマイズ
2. プラグイン情報を更新
3. スキルと学習資料を作成
4. GitHub に push
5. Claude Code プラグインマーケットプレイスに登録

詳細は [UMPA 仕様書](../../docs/SPECIFICATION.md) を参照してください。
