# プラグインメンテナンスガイド

プラグイン公開後の継続的なメンテナンスと改善について説明します。

## 📅 定期メンテナンススケジュール

### 週次

- [ ] GitHub Issues を確認
- [ ] ユーザーのバグ報告に返信
- [ ] Analytics を確認（ダウンロード数など）

### 月次

- [ ] 依存関係を更新
- [ ] セキュリティパッチを適用
- [ ] バグ修正を集約してマイナーリリース準備

### 四半期（3ヶ月）

- [ ] ユーザーフィードバックをレビュー
- [ ] 新機能の要望を集約
- [ ] 新言語対応の優先順位を決定
- [ ] CHANGELOG.md を更新してリリース準備

### 年次

- [ ] 大きな機能追加（メジャーリリース）を計画
- [ ] パフォーマンス改善を検討
- [ ] ドキュメント全体を見直し

---

## 🐛 バグ対応フロー

### Step 1: バグ報告を受け取る

GitHub Issues で報告されたバグを確認：

```
Title: [BUG] Lean Canvas 生成時に日本語が文字化けする
Labels: bug
```

### Step 2: バグを再現

```bash
# バグの条件を確認
# 再現手順: /lean-canvas-jp:lean-canvas-generator で日本語を入力

# ローカルで再現できるか確認
cd my-plugin
claude --plugin-dir .
```

### Step 3: バグを修正

```bash
# 修正内容に応じてファイルを変更
# skills/lean-canvas-generator/SKILL.md を修正

# テストして確認
```

### Step 4: コミット・リリース

```bash
# コミット
git add .
git commit -m "Fix: 日本語入力時の文字化け問題を修正 (#123)"

# バージョン更新（PATCH）
# plugin.json: version を 1.0.0 → 1.0.1 に

# タグ・リリース
git tag -a v1.0.1 -m "Fix: Japanese character encoding issue"
git push origin main v1.0.1
```

### Step 5: Issue にコメント

```markdown
# Fixed in v1.0.1

この問題は v1.0.1 で修正されました。

修正内容: SKILL.md に UTF-8 エンコーディング指定を追加

プラグインマーケットプレイスで最新バージョンを確認してください。
```

---

## ✨ 新機能追加フロー

### Step 1: 要件を定義

```markdown
# 新機能: Canvas 比較機能

## 概要
複数の Lean Canvas を比較し、差別化ポイントを分析する機能

## スキル
/my-plugin:compare-canvases

## 入力
Canvas 2つの JSON ファイル

## 出力
比較結果の JSON
```

### Step 2: テンプレートに追加

```bash
# 新しいスキルを作成
mkdir skills/compare-canvases
vim skills/compare-canvases/SKILL.md
```

### Step 3: 学習資料を更新

```bash
# references/ja/02-step-by-step.md に新機能の説明を追加
vim references/ja/02-step-by-step.md

# references/en/ も同様に更新
vim references/en/02-step-by-step.md
```

### Step 4: テスト

```bash
# 新機能をテスト
claude --plugin-dir .
/my-plugin:compare-canvases
```

### Step 5: バージョン更新・リリース

```bash
# plugin.json の version を更新（MINOR）
# 1.0.0 → 1.1.0

# CHANGELOG.md を更新
vim CHANGELOG.md

# コミット・タグ・リリース
git add .
git commit -m "Feature: Canvas 比較機能を追加 (v1.1.0)"
git tag -a v1.1.0 -m "Add compare-canvases skill"
git push origin main v1.1.0
```

---

## 🌍 新言語対応フロー

### Step 1: 言語サポート要望を受け取る

```
Issue: 中国語（簡体字）対応をお願いします
Labels: enhancement, language
```

### Step 2: 言語を追加

```bash
# スクリプトで言語フォルダを自動作成
./tools/add-language.sh zh-CN

# コントリビューターに翻訳を依頼
# または、Claude API で半自動翻訳
```

### Step 3: 翻訳を確認

- 翻訳の品質をチェック
- 文化的なカスタマイズを確認
- ネイティブスピーカーにレビュー依頼

### Step 4: マージ・リリース

```bash
# PR をマージ
git add references/zh-CN/
git commit -m "Add Simplified Chinese support (v1.2.0)"
git tag -a v1.2.0 -m "Add zh-CN language support"
git push
```

### Step 5: 公開

- README.md に新言語を追加
- マーケットプレイスで言語対応を更新

---

## 📊 パフォーマンス監視

### メトリクス確認

- **ダウンロード数**: マーケットプレイスで確認
- **Star 数**: GitHub で確認
- **Issue 数**: 品質指標

### パフォーマンス改善

```markdown
## パフォーマンス最適化 (v1.3.0)

- Canvas 生成速度を 50% 高速化
- メモリ使用量を削減
- API レスポンス時間を改善
```

---

## 🔄 依存関係の更新

### 月次セキュリティ確認

```bash
# セキュリティの脆弱性をチェック
# 使用している外部ライブラリ（Python、Node.js など）を更新

# 例: Python の場合
pip list --outdated
pip install --upgrade <package>
```

### 更新後のテスト

```bash
# すべてのテストを実行
./tools/validate-plugin.py

# Claude Code でテスト
claude --plugin-dir .
```

---

## 📝 ドキュメント管理

### README.md の更新

- 新機能追加時に更新
- ユーザーフィードバックに基づく改善
- デッドリンク確認

### Learning Materials（references/）の更新

```bash
# 新機能に関する説明を追加
vim references/ja/02-step-by-step.md
vim references/en/02-step-by-step.md

# ケーススタディを追加
vim references/ja/03-case-studies.md
```

### CHANGELOG.md の管理

```markdown
# Changelog

## [Unreleased]

### Added
- Canvas 比較機能（開発中）

## [1.1.0] - 2026-05-15

### Added
- Canvas 比較機能を追加

### Fixed
- 日本語の文字化けを修正
```

---

## 💬 コミュニティ管理

### Issue テンプレート（例）

`.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
## 説明
バグについて簡潔に説明してください

## 再現手順
1. ...
2. ...
3. ...

## 期待される動作
何が起こるべきだったか

## 実際の動作
何が起こったか

## 環境
- Claude Code バージョン:
- OS:
```

### コントリビューション方針

`CONTRIBUTING.md`:

```markdown
# コントリビューションガイド

## Bug 報告

GitHub Issues で報告してください。

## 機能提案

Issues で機能提案のディスカッション。

## 翻訳協力

references/ フォルダで新言語対応に協力できます。

## Pull Request

1. Fork してブランチを作成
2. 変更をコミット
3. PR を作成
4. レビューを待つ
```

---

## 🚨 クリティカルバグへの対応

### 緊急対応フロー

```
1. Issue が報告される（例: セキュリティ脆弱性）
   ↓
2. 直ちに対応チーム内でディスカッション
   ↓
3. パッチ修正を進める（1-2日以内）
   ↓
4. セキュリティレビュー
   ↓
5. 緊急リリース（パッチバージョン）
   ↓
6. ユーザーに通知
```

### 通知方法

- GitHub Issues にアナウンス
- README.md に警告を追加
- SNS で告知

---

## 📈 ユーザーサポート

### Issue/Discussion への返信テンプレート

**バグ報告に対して**:
```markdown
ご報告ありがとうございます。

確認したところ、[原因]が原因のようです。

v1.0.1 で修正予定です。
当面の回避方法: [回避方法]
```

**機能提案に対して**:
```markdown
提案ありがとうございます。

[理由]により、今後の検討の対象にさせていただきます。

実装されるまでの間、現在の機能で代替する方法: [代替案]
```

---

## ✅ メンテナンスチェックリスト

毎月実施：

```
定期メンテナンス
- [ ] Issues を確認・返信
- [ ] セキュリティ更新を確認
- [ ] ドキュメントのデッドリンク確認
- [ ] バグ修正をまとめてリリース準備

四半期ごと
- [ ] ユーザーフィードバックをまとめる
- [ ] 新言語対応の優先順位を確認
- [ ] パフォーマンス改善の検討
- [ ] major.minor バージョンリリース準備

年次
- [ ] 大型機能追加の計画
- [ ] メジャーバージョンリリース検討
- [ ] コミュニティからのコントリビューション管理
```

---

次のステップ: [コントリビューションガイド](CONTRIBUTION.md)
