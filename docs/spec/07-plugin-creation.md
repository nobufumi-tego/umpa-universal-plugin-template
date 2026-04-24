# プラグイン作成実践ガイド

## 実際にプラグインを作成する手順

このガイドでは、テンプレートを使用して、**実際に動作するプラグインを作成**します。

**所要時間**: 20-30分

---

## 準備

### 必要なもの

- Git がインストールされている
- Claude Code がインストールされている
- テキストエディタ（VS Code など）

### 確認コマンド

```bash
# Git
git --version

# Claude Code
claude --version
```

---

## Step 1: テンプレートを clone・コピー（5分）

### Option A: 初めての場合

```bash
# UMPA テンプレートをダウンロード
git clone https://github.com/nobufumi-tego/umpa-universal-plugin-template.git
cd umpa-universal-plugin-template

# テンプレートをコピー
cp -r template my-first-plugin
cd my-first-plugin
```

### Option B: すでに clone している場合

```bash
cd umpa-universal-plugin-template
cp -r template ../my-first-plugin
cd ../my-first-plugin
```

---

## Step 2: プラグイン情報を設定（5分）

### 2.1 `.claude-plugin/plugin.json` を編集

```bash
# エディタで開く
code .claude-plugin/plugin.json
```

以下のテンプレートを参考に編集：

```json
{
  "name": "my-first-plugin",
  "description": "My first Claude Code plugin using UMPA template",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  },
  "homepage": "https://github.com/your-username/my-first-plugin",
  "repository": "https://github.com/your-username/my-first-plugin",
  "license": "MIT",
  "keywords": ["first", "plugin", "template", "umpa"]
}
```

**重要な設定**:
- `name`: プラグイン呼び出し時に使用（例: `/my-first-plugin:skill-name`）
- `description`: プラグインマーケットプレイスで表示
- `version`: セマンティックバージョニング（1.0.0 形式）

### 2.2 README.md を編集（オプション）

```bash
code README.md
```

簡潔な説明を追加：

```markdown
# My First Plugin

This is my first Claude Code plugin created with UMPA template.

## Features

- Feature 1
- Feature 2

## Installation

Search "my-first-plugin" in Claude Code plugin marketplace.

## Usage

/my-first-plugin:my-skill

[Learn more](references/ja/README.md)
```

---

## Step 3: スキルを定義（5分）

### 3.1 スキルの概要を決定

```
何をするプラグインか？
例: TODO リスト管理、ブログ記事生成、データ分析、etc.
```

### 3.2 SKILL.md を編集

```bash
code skills/example-skill/SKILL.md
```

**実例: TODO リスト管理プラグイン**

```markdown
---
name: todo-generator
description: ユーザーの要件からTODOリストを自動生成します
version: 1.0.0
---

# TODO リスト生成スキル

## 概要

ユーザーがプロジェクト内容を説明すると、実行可能な TODO リストを生成します。

## 学習リソース

詳細な学習資料は以下を参照してください：

- **日本語**: See `references/ja/`
- **English**: See `references/en/`

## プロセス

### ステップ 1: プロジェクト情報を理解

ユーザーからプロジェクトの以下を確認：
- プロジェクト名
- 目的
- 納期
- チームメンバー数

### ステップ 2: TODO を生成

プロジェクト情報をもとに、実行可能なタスクに分解します。

基準：
- 各タスクは1-2時間で完了可能
- 依存関係を明確に
- 優先度を設定

### ステップ 3: 出力

構造化されたリストで返します。

## 入力形式

```json
{
  "projectName": "新しいウェブサイト構築",
  "purpose": "ユーザー向けポートフォリオサイト",
  "dueDate": "2026-05-31",
  "teamSize": 3
}
```

## 出力形式

```json
{
  "projectName": "新しいウェブサイト構築",
  "todos": [
    {
      "id": 1,
      "title": "デザイン仕様書作成",
      "priority": "高",
      "estimatedHours": 2,
      "dependencies": []
    },
    {
      "id": 2,
      "title": "フロントエンド実装",
      "priority": "高",
      "estimatedHours": 8,
      "dependencies": [1]
    },
    {
      "id": 3,
      "title": "バックエンド実装",
      "priority": "高",
      "estimatedHours": 10,
      "dependencies": [1]
    }
  ],
  "totalHours": 20,
  "suggestedWeeks": 1
}
```

## ベストプラクティス

- タスクは明確で実行可能に
- 見積もり時間は保守的に
- 依存関係を正確に
- プロジェクトの規模に応じてタスク数を調整

## よくあるピットフォール

- **タスク粒度が大きすぎる** → 1-2時間単位に分割
- **依存関係の誤り** → 実装順序を確認
- **見積もりが楽観的** → 25-50%の余裕を加える
```

### 3.3 ファイル名を変更（オプション）

```bash
# example-skill → todo-generator に変更する場合
mv skills/example-skill skills/todo-generator
```

---

## Step 4: Claude Code でテスト（3分）

### 4.1 Claude Code を起動

```bash
# プラグインディレクトリで起動
claude --plugin-dir .
```

出力例：
```
Starting Claude Code with local plugin...
Plugin loaded: my-first-plugin
Ready to use /my-first-plugin:todo-generator
```

### 4.2 スキルをテスト

Claude Code のプロンプトで入力：

```
/my-first-plugin:todo-generator

以下のプロジェクトのTODOリストを作成してください：
- プロジェクト名: モバイルアプリ開発
- 目的: iOS/Android アプリ
- 納期: 2026年7月
- チーム: 5名
```

### 4.3 出力を確認

Claude が JSON 形式で返します：

```json
{
  "projectName": "モバイルアプリ開発",
  "todos": [
    {
      "id": 1,
      "title": "UI/UX デザイン",
      "priority": "高",
      "estimatedHours": 3,
      "dependencies": []
    },
    ...
  ],
  "totalHours": 30,
  "suggestedWeeks": 2
}
```

✅ **動作確認完了！**

---

## Step 5: 学習資料を作成（5分）

### 5.1 日本語ガイドを作成

```bash
code references/ja/README.md
```

テンプレート：

```markdown
---
title: "TODO リスト生成 - 学習ガイド"
language: ja
---

# TODO リスト生成プラグイン 学習ガイド

効率的なプロジェクト管理のための TODO リスト自動生成ツール

## 推奨学習パス

### 初級者向け

1. 01-concept.md - TODO リストの重要性
2. 02-step-by-step.md - 実装方法

### 中級者向け

1. 03-case-studies.md - 実プロジェクトの事例
2. 02-step-by-step.md - 改善方法

## ファイルガイド

| ファイル | 内容 |
|---------|------|
| 01-concept.md | なぜ TODO リストが重要か |
| 02-step-by-step.md | 効果的な TODO 作成方法 |
| 03-case-studies.md | 実例 |
| 04-advanced.md | 応用テクニック |
```

### 5.2 概念説明を追加

```bash
code references/ja/01-concept.md
```

簡潔な説明を追加（300-500行）

### 5.3 実装ガイドを追加

```bash
code references/ja/02-step-by-step.md
```

ステップバイステップで説明

### 5.4 英語版も作成

```bash
cp references/ja/README.md references/en/README.md
# 英語に翻訳
```

---

## Step 6: Git で管理（3分）

### 6.1 Git リポジトリを初期化

```bash
git init
git add .
git commit -m "Initial commit: my-first-plugin v1.0.0

- Add TODO generator skill
- Add Japanese and English learning materials
- Based on UMPA template"
```

### 6.2 GitHub に登録

1. GitHub で新しいリポジトリを作成
2. ローカルで remote を追加

```bash
git remote add origin https://github.com/your-username/my-first-plugin.git
git branch -M main
git push -u origin main
```

---

## Step 7: 改善・拡張（オプション）

### 7.1 新しいスキルを追加

```bash
mkdir skills/task-optimizer
code skills/task-optimizer/SKILL.md
```

### 7.2 新言語を対応させる

```bash
./tools/add-language.sh zh-CN
# references/zh-CN/ が作成されるので、翻訳する
```

### 7.3 コマンドを追加

```bash
code commands/export-to-markdown.md
```

---

## チェックリスト

プラグイン作成時に確認すべき項目：

```
プラグイン設定
- [ ] plugin.json が編集されたか
- [ ] name が正しいか（英数字とハイフンのみ）
- [ ] version が設定されたか

スキル定義
- [ ] SKILL.md が編集されたか
- [ ] 入力形式が定義されたか
- [ ] 出力形式が定義されたか
- [ ] ベストプラクティスが記載されたか

学習資料
- [ ] references/ja/README.md が編集されたか
- [ ] 01-concept.md が作成されたか（オプション）
- [ ] 02-step-by-step.md が作成されたか（オプション）
- [ ] references/en/ に英語版があるか（推奨）

テスト
- [ ] Claude Code で起動できたか
- [ ] スキルが動作するか
- [ ] 出力形式が正しいか

Git
- [ ] .gitignore が設定されたか
- [ ] README.md が更新されたか
- [ ] 初期コミットが完了したか
- [ ] GitHub に push されたか

バリデーション
- [ ] ./tools/validate-plugin.py で検証済みか
- [ ] デッドリンク確認したか
- [ ] 誤字脱字確認したか
```

---

## トラブルシューティング

### プラグインが起動しない

```bash
# エラー: "plugin.json not found"
# 対策: .claude-plugin/plugin.json が存在するか確認

ls -la .claude-plugin/plugin.json

# JSON が有効か確認
python -m json.tool .claude-plugin/plugin.json
```

### スキルが動作しない

```bash
# SKILL.md のフロントマッターを確認
head -10 skills/your-skill/SKILL.md

# 出力形式を JSON でフォーマット
echo '{"test": "value"}' | python -m json.tool
```

### Claude Code が起動しない

```bash
# Claude Code のバージョン確認
claude --version

# 別のディレクトリで試す
mkdir test-plugin
cd test-plugin
cp -r ../my-first-plugin .
claude --plugin-dir my-first-plugin
```

---

## 実装例のパターン

### パターン 1: ジェネレータ型

**例**: Lean Canvas、ペルソナ、マーケティングコピー生成

```
入力 → Claude が生成 → JSON/Markdown で出力
```

### パターン 2: アナライザ型

**例**: テキスト分析、コード品質チェック、データ分析

```
入力（テキスト/コード/データ） → Claude が分析 → 結果を出力
```

### パターン 3: トランスフォーマー型

**例**: テキストの翻訳、フォーマット変換、コード最適化

```
入力 → Claude が変換 → 出力形式で返す
```

---

## 次のステップ

### すぐにやること

1. このガイドに従ってプラグインを作成
2. Claude Code でテスト
3. 学習資料を充実させる
4. GitHub に公開

### 後からやること

1. [プラグイン公開ガイド](../PLUGIN_RELEASE.md) を参照してマーケットプレイスに登録
2. [メンテナンスガイド](../MAINTENANCE.md) に従って更新
3. [コントリビューションガイド](../CONTRIBUTION.md) で翻訳協力を受け入れ

---

## 💡 開発のコツ

### 最初は小さく

```
❌ 複数スキル、複数言語、複数コマンド...
✅ スキル1つ、言語1つ（日本語）、コマンドなし
  → 完成させてから拡張
```

### ユーザーの視点で

```
❌ 技術的に完璧なスキル
✅ ユーザーが理解できるスキル
  → 学習資料を充実させる
```

### 段階的に改善

```
v1.0.0: 基本機能
v1.1.0: 新機能追加
v2.0.0: 大型改善
```

---

## 実装例の確認

実装例を参考にしたい場合：

```bash
# Lean Canvas プラグインを確認
cd examples/lean-canvas-plugin

# SKILL.md の構造を確認
cat skills/lean-canvas-generator/SKILL.md

# 学習資料を確認
ls -la references/ja/
cat references/ja/01-concept.md
```

---

このガイドに従うことで、**20-30分で実際に動作するプラグインを作成**できます！

Happy Plugin Creation! 🚀

---

[← 仕様書ホーム](../SPECIFICATION.md) | [← クイックスタート](06-quickstart.md) | [ローカル開発セットアップ →](../LOCAL_SETUP.md)
