# プラグイン公開ガイド

プラグイン開発後、Claude Code プラグインマーケットプレイスに公開するまでのステップを説明します。

## 📋 公開前チェックリスト

### プラグインの品質確認

- [ ] すべてのスキルが正常に動作するか
- [ ] plugin.json が有効な JSON か
- [ ] SKILL.md が各スキルにあるか
- [ ] コマンドとエージェントが動作するか
- [ ] すべてのリンク（参考資料など）が正しく動作するか

### ドキュメント確認

- [ ] README.md がある
- [ ] CONTRIBUTING.md がある
- [ ] LICENSE ファイルがある（推奨: MIT）
- [ ] SKILL.md に詳細な説明がある
- [ ] references/ フォルダに日本語と英語が揃っているか

### セキュリティ確認

- [ ] API キーやシークレットがコミットされていないか
- [ ] 依存パッケージが最新かつ安全か
- [ ] スクリプトに悪意のあるコードがないか

### テスト確認

```bash
# バリデーション実行
./tools/validate-plugin.py

# Claude Code でテスト
claude --plugin-dir .
```

---

## 🔄 バージョニング

Semantic Versioning （MAJOR.MINOR.PATCH）を使用します。

### バージョン更新ルール

| 変更内容 | 更新部分 | 例 |
|---------|---------|-----|
| 破壊的変更（API変更など） | MAJOR | 1.0.0 → 2.0.0 |
| 新機能追加（後方互換性あり） | MINOR | 1.0.0 → 1.1.0 |
| バグ修正 | PATCH | 1.0.0 → 1.0.1 |

### 更新ファイル

```json
// .claude-plugin/plugin.json
{
  "version": "1.0.0"  ← ここを更新
}
```

---

## 📦 GitHub へのプッシュ

### 1. リポジトリを準備

```bash
# Git リポジトリを初期化（まだの場合）
git init

# GitHub で新しいリポジトリを作成
# https://github.com/new

# リモートを追加
git remote add origin https://github.com/your-username/my-plugin.git

# ブランチを main に設定
git branch -M main
```

### 2. ファイルをコミット

```bash
# すべてのファイルをステージング
git add .

# コミット（初回リリース）
git commit -m "Initial release: v1.0.0"

# タグを作成
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push
git push -u origin main
git push origin v1.0.0
```

### 3. GitHub リリースを作成

1. GitHub リポジトリで **Releases** をクリック
2. **Create a new release** をクリック
3. タグを選択: `v1.0.0`
4. リリース説明を記入：

```markdown
# Lean Canvas プラグイン v1.0.0

## 新機能

- Lean Canvas 自動生成
- 日本語・英語対応
- 9要素の構造化出力

## 改善

- より詳しい学習資料を追加

## インストール

```bash
# プラグインマーケットプレイスで検索: lean-canvas-jp
```

## ドキュメント

- [README](README.md)
- [使用方法](docs/USAGE.md)
```

---

## 🎁 Claude Code プラグインマーケットプレイスに登録

### 1. 提出要件を確認

以下のドキュメントで公式要件を確認：
https://code.claude.com/docs/plugins

チェック項目：
- [ ] plugin.json が正しい形式
- [ ] plugin.json に必須フィールドがすべてある
- [ ] README.md に使用方法が記載
- [ ] ライセンスが明記
- [ ] コードが安全（セキュリティレビュー済み）

### 2. プラグイン情報を準備

**plugin.json の例**:
```json
{
  "name": "lean-canvas-jp",
  "description": "日本語対応 Lean Canvas ビジネステンプレート生成",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "your@email.com"
  },
  "homepage": "https://github.com/your-username/lean-canvas-plugin",
  "repository": "https://github.com/your-username/lean-canvas-plugin",
  "license": "MIT",
  "keywords": ["business", "lean-canvas", "japanese", "multilingual"]
}
```

### 3. GitHub リポジトリをテンプレート化（オプション）

GitHub で、リポジトリを "template repository" として設定すると、他のユーザーが簡単に使用できます。

**設定手順**:
1. リポジトリの **Settings**
2. **Repository template** にチェック

これで、他のユーザーが **"Use this template"** ボタンでプラグインを複製できます。

### 4. プラグインマーケットプレイスに提出

Claude Code 公式ドキュメントの提出フォームから申請：

https://code.claude.com/submit-plugin

または、GitHub Issues で登録リクエスト。

---

## 📢 公開後のマーケティング

### 1. README の充実

```markdown
# プラグイン名

説明

## 特徴

- 特徴1
- 特徴2

## インストール

プラグインマーケットプレイスで「プラグイン名」を検索

## 使用方法

/プラグイン名:スキル名

例：/lean-canvas-jp:lean-canvas-generator

## 学習資料

- [日本語ガイド](references/ja/)
- [English Guide](references/en/)
```

### 2. Social Media での告知

- **X（Twitter）**: `#ClaudeCode #プラグイン #多言語`
- **GitHub Discussions**: コミュニティとの交流
- **技術ブログ**: 作成背景やユースケース記事

### 3. コミュニティフィードバック

- Issues を監視して、ユーザーのフィードバックに対応
- 定期的に改善・更新

---

## 🔄 更新・メンテナンス手順

### マイナー更新（バグ修正や小改善）

```bash
# 1. ファイルを修正

# 2. バージョン更新（PATCH）
# plugin.json の version を更新: 1.0.0 → 1.0.1

# 3. コミット
git add .
git commit -m "Fix: 日本語テンプレートの誤字修正 (v1.0.1)"

# 4. タグと リリース
git tag -a v1.0.1 -m "Patch release: Bug fixes"
git push origin main v1.0.1

# 5. GitHub リリースを作成
```

### メジャー更新（新機能追加）

```bash
# 1. 新しいスキルやコマンドを追加
# 2. references/ に新しい学習資料を追加

# 3. バージョン更新（MINOR）
# plugin.json の version を更新: 1.0.0 → 1.1.0

# 4. CHANGELOG.md を更新
# 5. コミット・タグ・リリース作成
```

---

## 📊 GitHub Actions (CI/CD) 設定

自動テスト・検証を設定（オプション）。

### 1. `.github/workflows/validate.yml` を作成

```yaml
name: Validate Plugin

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Validate Plugin
        run: python tools/validate-plugin.py
```

### 2. ファイルをコミット

```bash
git add .github/workflows/validate.yml
git commit -m "Add CI/CD validation workflow"
git push
```

以降、すべての push で自動的に検証が実行されます。

---

## 📈 バージョン履歴の管理

### CHANGELOG.md を作成

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-04-24

### Added
- Lean Canvas 自動生成スキル
- 日本語・英語の学習資料
- コマンド: review-canvas, export

### Fixed
- テンプレートの初期値を修正

## [0.9.0] - 2026-04-20

### Added
- Initial beta release
```

---

## ✅ 公開チェックリスト（最終確認）

```
公開前の最終チェック：

一般
- [ ] plugin.json が有効か
- [ ] すべてのファイルが正しくコミットされているか
- [ ] .gitignore が設定されているか

ドキュメント
- [ ] README.md が充実しているか
- [ ] CONTRIBUTING.md があるか
- [ ] LICENSE があるか
- [ ] references/ に日本語と英語がそろっているか

テスト
- [ ] すべてのスキルが動作するか
- [ ] validate-plugin.py がエラーを報告していないか

セキュリティ
- [ ] API キーが含まれていないか
- [ ] 依存関係が安全か

バージョン
- [ ] plugin.json の version が正しいか
- [ ] GitHub タグが version に一致しているか
- [ ] CHANGELOG.md が更新されているか
```

---

次のステップ: [メンテナンスガイド](MAINTENANCE.md)
