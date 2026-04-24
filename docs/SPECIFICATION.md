# UMPA - Universal Multilingual Plugin Architecture

**仕様書 完全ガイド** | **Specification Complete Guide**

Document Version: 1.0.0  
Last Updated: 2026-04-24  
Author: Nobufumi Yoshida (@nobufumi-tego)

---

## 📚 目次 / Table of Contents

### 日本語版

1. **[概要・基本概念](spec/01-overview.md)** — UMPA とは、3層アーキテクチャ、メリット
2. **[ディレクトリ構造](spec/02-directory-structure.md)** — プラグインの完全な構成例
3. **[クイックスタート](spec/06-quickstart.md)** ⭐ — 10分でプラグイン開発を始める方法
4. **[プラグイン作成実践ガイド](spec/07-plugin-creation.md)** ⭐ — 実際にプラグインを作成する手順
5. **[コアコンポーネント仕様](spec/03-components.md)** — plugin.json、SKILL.md、commands/、agents/ の詳細
6. **[学習層（References）](spec/04-learning-layer.md)** — 多言語学習資料の構造と書き方
7. **[ベストプラクティス](spec/05-best-practices.md)** — SKILL.md 作成時の注意点、テストチェックリスト

### English Version

1. **[Overview & Architecture](spec/01-overview-en.md)** — What is UMPA, 3-layer architecture, benefits
2. **[Directory Structure](spec/02-directory-structure-en.md)** — Complete plugin composition
3. **[Quick Start](spec/06-quickstart-en.md)** ⭐ — Get started with plugin development in 10 minutes
4. **[Plugin Creation Guide](spec/07-plugin-creation-en.md)** ⭐ — Step-by-step guide to create your first plugin
5. **[Core Components](spec/03-components-en.md)** — Details of plugin.json, SKILL.md, commands/, agents/
6. **[Learning Layer (References)](spec/04-learning-layer-en.md)** — Multilingual learning materials structure
7. **[Best Practices](spec/05-best-practices-en.md)** — Guidelines for SKILL.md, testing checklist

---

## 🎯 このドキュメントを選ぶ

### あなたが知りたいことは？

| 質問 | 参照ドキュメント |
|------|-----------------|
| すぐにプラグイン作成を始めたい | [07-plugin-creation.md](spec/07-plugin-creation.md) ⭐ |
| 10分で概要を理解したい | [06-quickstart.md](spec/06-quickstart.md) ⭐ |
| UMPA の仕組みを理解したい | [01-overview.md](spec/01-overview.md) |
| プラグインの構造を知りたい | [02-directory-structure.md](spec/02-directory-structure.md) |
| plugin.json や SKILL.md の書き方 | [03-components.md](spec/03-components.md) |
| 多言語対応のやり方 | [04-learning-layer.md](spec/04-learning-layer.md) |
| 開発時の注意点 | [05-best-practices.md](spec/05-best-practices.md) |

---

## ⚡ 5分で分かる UMPA

### 3層構造

```
実行層（English, Claude向け）
├── skills/          → スキル定義
├── commands/        → スラッシュコマンド
└── agents/          → カスタムエージェント
    ↓
学習層（多言語、人間向け）
├── references/ja/   → 日本語学習資料
├── references/en/   → 英語学習資料
└── references/xx/   → その他言語
    ↓
設定層
├── plugin.json      → プラグインメタデータ
└── .mcp.json        → MCP統合
```

### コアメリット

✅ **スキルは英語で1回書くだけ**  
✅ **言語を追加してもコンテキストトークンは増えない** (references/ は外)  
✅ **言語追加はフォルダ追加だけ、コード変更ゼロ**  
✅ **1プラグイン → 1000プラグインまでスケール**

---

## 🚀 はじめに

### 初心者向け推奨パス

```
1. このページで全体像を把握
2. spec/06-quickstart.md で10分で開発開始
3. template/ フォルダでテンプレートをコピー
4. 不明な部分があれば、各仕様書を参照
```

### 詳しく学びたい方

```
1. spec/01-overview.md で基本概念を理解
2. spec/02-directory-structure.md で構造を把握
3. spec/03-components.md で各ファイルの詳細を学ぶ
4. spec/04-learning-layer.md で多言語対応を学ぶ
5. spec/05-best-practices.md でベストプラクティスを確認
```

---

## 📊 仕様書の統計

| 項目 | 内容 |
|------|------|
| **総ドキュメント数** | 12（日本語6 + 英語6） |
| **総ページ数** | 約50ページ相当 |
| **読了時間** | クイックスタート: 10分 / 完全版: 2-3時間 |
| **対応言語** | 日本語、英語 |

---

## 🔗 関連ドキュメント

### 開発ガイド

- **[ローカル開発セットアップ](../LOCAL_SETUP.md)** — プラグイン開発環境の構築
- **[テンプレートガイド](../../template/README.md)** — テンプレートの使用方法

### 公開・メンテナンス

- **[公開ガイド](../PLUGIN_RELEASE.md)** — マーケットプレイス登録方法
- **[メンテナンスガイド](../MAINTENANCE.md)** — 継続的なメンテナンス
- **[コントリビューションガイド](../CONTRIBUTION.md)** — 翻訳・協力方法

### 実装例

- **[Lean Canvas プラグイン例](../../examples/lean-canvas-plugin/)** — 完全な実装例
- **[テンプレート](../../template/)** — 汎用テンプレート

---

## 💡 仕様書の使い方

### パターン別ガイド

**パターン1: すぐにプラグイン開発を始めたい**  
→ [クイックスタート](spec/06-quickstart.md) を読む（10分）

**パターン2: UMPA の考え方を理解したい**  
→ [概要](spec/01-overview.md) と [ディレクトリ構造](spec/02-directory-structure.md) を読む（30分）

**パターン3: 詳しく全部学びたい**  
→ 全ドキュメントを順番に読む（2-3時間）

**パターン4: 特定の部分だけ知りたい**  
→ 上の「目次」から該当部分をクリック

---

## ❓ FAQ

**Q: 仕様書を全部読む必要がありますか？**  
A: いいえ。クイックスタートだけで開発を始められます。わからないことがあれば、該当部分を読んでください。

**Q: 日本語と英語、どちらを読むべき？**  
A: 日本語版と英語版は同じ内容です。お好みの言語をお選びください。

**Q: 実装例を先に見た方がいい？**  
A: はい。[Lean Canvas プラグイン](../../examples/lean-canvas-plugin/) を見てから仕様書を読むと、より理解しやすいです。

---

## 📝 ドキュメント更新履歴

| 版 | 日付 | 更新内容 |
|----|------|---------|
| 1.0.0 | 2026-04-24 | 初版リリース、日本語・英語対応、モジュール化 |

---

## 🎯 次のステップ

1. **クイックスタート（推奨）** → [spec/06-quickstart.md](spec/06-quickstart.md)
2. **完全に学ぶ** → [spec/01-overview.md](spec/01-overview.md) から順番に
3. **すぐに始める** → [../../template/README.md](../../template/README.md) をコピー
4. **実装例を見る** → [../../examples/lean-canvas-plugin/](../../examples/lean-canvas-plugin/)

---

**Made with ❤️ by UMPA Contributors**

[プロジェクトホーム](../../README.md) | [GitHub](https://github.com/nobufumi-tego/umpa-universal-plugin-template)
