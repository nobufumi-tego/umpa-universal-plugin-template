# コントリビューション・翻訳ガイド

プラグイン開発者や翻訳者がコントリビューションする方法を説明します。

## 🌍 コントリビューションの種類

### 1. バグ修正

バグを見つけた場合、Issue を報告するか、PR で修正をサブミットしてください。

### 2. 機能追加

新しいスキルやコマンドを提案する場合は、Issue でディスカッション後に PR をサブミット。

### 3. 翻訳・言語追加

新しい言語への翻訳、または既存言語の改善。

### 4. ドキュメント改善

README、学習資料、ガイドの改善・誤字修正。

### 5. テスト・検証

バグ報告、テストケース作成、パフォーマンス測定。

---

## 📝 翻訳ガイド

### サポートしている言語

| 言語 | コード | Status | 対応者 |
|------|-------|--------|-------|
| 日本語 | ja | ✅ Complete | @author |
| English | en | ✅ Complete | @author |
| 簡体字中国語 | zh-CN | 📝 In Progress | @contributor1 |
| 繁體字中国語 | zh-TW | 📝 Planned | - |
| 韓国語 | ko | 📝 Planned | - |
| スペイン語 | es | 📝 Future | - |

### 新言語への翻訳手順

#### Step 1: 翻訳を開始する前に

GitHub Issues で「[Translation] Language Name」という Issue を作成：

```markdown
Title: [Translation] Simplified Chinese (zh-CN)

## 言語
簡体字中国語（Simplified Chinese）

## 翻訳内容
- references/zh-CN/README.md
- references/zh-CN/01-concept.md
- references/zh-CN/02-step-by-step.md
- references/zh-CN/03-case-studies.md
- references/zh-CN/04-advanced.md

## タイムライン
予想完了日: 2026-06-30

## 翻訳の品質保証
ネイティブスピーカーによるレビュー予定
```

これにより、重複した翻訳作業を避けられます。

#### Step 2: 言語フォルダを作成

```bash
# Fork したリポジトリでブランチを作成
git checkout -b translate/zh-CN

# 言語フォルダを自動作成
./tools/add-language.sh zh-CN
```

#### Step 3: ファイルを翻訳

各ファイルを対象言語に翻訳します。

**翻訳品質ガイドライン**:

- ✅ **ネイティブレベルの品質**: 文法、表現が自然
- ✅ **文化的配慮**: その言語圏の文化・ビジネス慣習を反映
- ✅ **一貫性**: 専門用語の翻訳を一貫させる（用語集参照）
- ✅ **実例の現地化**: 日本企業の例→対象国の企業に変更（可能な場合）

**ファイル別翻訳ガイド**:

##### README.md
- プラグインの説明と使用方法
- 対象言語圏のユーザーが理解できるように

##### 01-concept.md
- **背景・理論部分**: 正確な翻訳が重要
- **実例部分**: 対象国の企業・ケーススタディに変更推奨
- **よくある質問**: 対象市場の質問に修正

##### 02-step-by-step.md
- ステップバイステップの手順は正確に翻訳
- スクリーンショット・コード例は言語に合わせて修正
- テンプレートは対象言語でカスタマイズ

##### 03-case-studies.md
- **成功事例・失敗事例**: 対象国の企業に置き換え推奨
- パターン分析は汎用的で問題なし

##### 04-advanced.md
- 技術的内容は正確に
- 参照や引用は対象言語のリソースに置き換え

#### Step 4: 用語集を確認

重要な用語を統一するため、用語集を確認します。

**用語集の例** (`references/GLOSSARY.md`):

```markdown
# 用語集

## 日本語 → 簡体字中国語

| 日本語 | 中文 | 説明 |
|-------|------|------|
| Lean Canvas | 精益画布 / 精益画布 | ビジネステンプレート |
| 顧客セグメント | 客户细分 | ターゲット顧客 |
| 独自の価値提案 | 独特的价值主张 | 競争優位性 |
```

#### Step 5: ローカルテスト

```bash
# ファイルが正しく保存されているか確認
ls references/zh-CN/
# 出力:
# 01-concept.md
# 02-step-by-step.md
# 03-case-studies.md
# 04-advanced.md
# README.md

# テキストエンコーディングが正しいか確認（UTF-8）
file references/zh-CN/*.md
```

#### Step 6: PR をサブミット

```bash
# ブランチにコミット
git add references/zh-CN/
git commit -m "Add Simplified Chinese translation (zh-CN)"

# GitHub にプッシュ
git push origin translate/zh-CN
```

GitHub で **Pull Request** を作成：

```markdown
## 翻訳内容

簡体字中国語（zh-CN）対応を追加しました。

## 翻訳ファイル

- [x] README.md
- [x] 01-concept.md
- [x] 02-step-by-step.md
- [x] 03-case-studies.md
- [x] 04-advanced.md

## 品質チェック

- [x] ネイティブスピーカーのレビュー済み
- [x] 用語集に準拠
- [x] デッドリンク確認

## レビュアー

@contributor-reviewer にレビューをお願いします。
```

#### Step 7: レビュー・マージ

メンテナーが翻訳をレビューし、問題がなければマージします。

### 既存言語の改善

翻訳に誤りや改善点を見つけた場合：

1. GitHub Issues で報告
2. PR で修正をサブミット

```bash
# ブランチを作成
git checkout -b fix/ja-typo

# 誤字を修正
vim references/ja/02-step-by-step.md

# コミット
git commit -m "Fix: typo in ja/02-step-by-step.md"
git push origin fix/ja-typo
```

---

## 🔧 バグ修正 PR

### Issue からの修正フロー

1. GitHub Issues でバグを見つける
2. 修正 Issue を作成・割り当て
3. ブランチを作成

```bash
git checkout -b fix/issue-123
```

4. ファイルを修正

```bash
# 修正対象ファイルを編集
vim skills/lean-canvas-generator/SKILL.md

# テスト
./tools/validate-plugin.py
```

5. PR をサブミット

```bash
git add .
git commit -m "Fix: 日本語入力時の文字化け (fixes #123)"
git push origin fix/issue-123
```

PR で Issue を自動クローズ：

```markdown
Fixes #123

## 修正内容

SKILL.md に UTF-8 エンコーディング指定を追加し、日本語入力時の文字化け問題を解決。

## テスト済み

- [x] ローカルで再現・修正を確認
- [x] validate-plugin.py で検証
- [x] Claude Code で動作確認
```

---

## ✨ 機能追加 PR

### 新機能の提案フロー

1. Issue で機能提案をディスカッション

```markdown
Title: [Feature] Canvas 比較機能

## 説明
複数の Lean Canvas を比較し、差別化ポイントを分析する機能

## ユースケース
同じセグメント向けの複数案を比較したい場合に便利

## 実装案
新しいスキル: /my-plugin:compare-canvases
```

2. メンテナーからの OK を得たら実装開始

3. 機能を実装

```bash
git checkout -b feature/compare-canvases

# 新スキルを追加
mkdir skills/compare-canvases
vim skills/compare-canvases/SKILL.md

# ドキュメントを更新
vim references/ja/02-step-by-step.md
vim references/en/02-step-by-step.md
```

4. テスト

```bash
./tools/validate-plugin.py
claude --plugin-dir .
# /my-plugin:compare-canvases でテスト
```

5. PR をサブミット

```bash
git add .
git commit -m "Feature: Canvas 比較機能を追加(#456)"
git push origin feature/compare-canvases
```

---

## 📋 PR チェックリスト

### サブミット前に必ず確認

```
一般
- [ ] ブランチが最新の main から作成されているか
- [ ] コミットメッセージが明確か
- [ ] 関連する Issue があればリンクしているか

コード・ドキュメント
- [ ] ファイルが正しくエンコードされているか（UTF-8）
- [ ] デッドリンク確認
- [ ] 誤字・脱字確認

テスト
- [ ] validate-plugin.py で検証済み
- [ ] Claude Code でテスト済み

翻訳
- [ ] 日本語と英語の両方を更新したか
- [ ] 用語の一貫性確認

バージョン
- [ ] 必要に応じて plugin.json の version を更新したか
- [ ] CHANGELOG.md を更新したか
```

---

## 🎯 コントリビューション報酬

### 認識・クレジット

- GitHub の Contributors に記載
- README.md のコントリビューター欄に記載
- リリースノートで感謝

### レビュー対象

- バグ修正 PR
- 機能追加 PR
- 翻訳 PR
- ドキュメント改善 PR

---

## 💬 コミュニケーション

### GitHub Discussions

機能提案や一般的な質問は Discussions で：

```
Category: Translations
Title: 新しい言語対応について

質問や提案をシェアしてください。
```

### Issues

バグ報告や機能リクエスト：

```
Label: bug, enhancement, language, documentation
```

---

## ❓ よくある質問

**Q: 小さな修正（誤字など）でも PR は必要？**  
A: はい。ただし、1つの PR に複数の小さな修正をまとめても OK です。

**Q: PR がマージされるまでどのくらい待つ？**  
A: 通常 1-2週間。複雑な PR は時間がかかる場合があります。

**Q: レビューでの修正要求は何回まで？**  
A: 制限なし。品質を高めるための協力をお願いします。

---

ご協力ありがとうございます！ 🙏

コントリビューション関連で質問があれば、GitHub Issues で質問してください。
