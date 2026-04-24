# Lean Canvas プラグイン

UMPA テンプレートに基づいた、Lean Canvas ビジネステンプレート生成プラグインの実装例です。

## このプラグインについて

このプラグインは、ビジネスアイデアをもとに **Lean Canvas** を自動生成します。

Lean Canvas は、スタートアップやビジネス企画に最適な、1ページのビジネスモデルテンプレートです。

## スキル

### `/lean-canvas-jp:lean-canvas-generator`

ビジネスアイデアを入力すると、Lean Canvas を JSON形式で生成します。

**入力例**:
```json
{
  "productName": "TODO管理アプリ",
  "customerSegment": "フリーランスや個人起業家",
  "problems": ["タスク管理が複雑", "優先度の判断が難しい"],
  "solution": "AI により優先度を自動提案",
  "keyFeatures": ["AI優先度提案", "チーム共有", "進捗レポート"],
  "competitiveAdvantage": "日本語特化の AI アルゴリズム"
}
```

**出力例**:
```json
{
  "leanCanvas": {
    "problem": {...},
    "customerSegments": {...},
    "uniqueValueProposition": {...},
    ...
  }
}
```

## ディレクトリ構造

```
lean-canvas-plugin/
├── .claude-plugin/
│   └── plugin.json                    ← プラグイン定義
├── skills/
│   └── lean-canvas-generator/
│       └── SKILL.md                   ← スキル定義（英語のプロセス）
├── references/
│   ├── ja/                            ← 日本語学習資料
│   │   ├── README.md
│   │   ├── 01-concept.md
│   │   ├── 02-step-by-step.md
│   │   ├── 03-case-studies.md
│   │   └── 04-advanced.md
│   └── en/                            ← 英語学習資料
│       └── (same structure)
├── README.md                          ← このファイル
└── LICENSE
```

## UMPA から何を学べるか

このプラグインは、以下のベストプラクティスを示しています：

### 1. 構造の簡潔性

- **実行層**: `SKILL.md` のみで、プロセスを完全に定義
- **学習層**: 複数言語の学習資料を、コンテキスト外で提供

### 2. スケーラビリティ

- 言語追加は **フォルダ追加だけ** — コード変更ゼロ
- 新しいスキル追加も、同じ構造で対応可能

### 3. ユーザー体験

- SKILL.md — Claude へのプロセス指示（英語、簡潔）
- references/ — ユーザーの学習資料（多言語、詳細）

## 使用方法

### 1. Claude Code でプラグインを読み込み

```bash
claude --plugin-dir .
```

### 2. スキルを実行

```
/lean-canvas-jp:lean-canvas-generator
```

ビジネスアイデアの詳細を説明してください。

### 3. Lean Canvas を取得

Claude が JSON形式で Lean Canvas を生成します。

これを Markdown や Excel に変換したり、さらに詳細化することができます。

## 参考資料

- **UMPA 仕様書**: [../../docs/SPECIFICATION.md](../../docs/SPECIFICATION.md)
- **通用テンプレート**: [../../template/](../../template/)
- **学習資料 (日本語)**: [references/ja/](references/ja/)
- **Learning Materials (English)**: [references/en/](references/en/)

## ライセンス

MIT License

---

**このプラグインは UMPA テンプレートの実装例です。**

あなた自身のプラグインを作成する際の参考にしてください。

