# クイックスタート - 10分でプラグイン開発開始

**この手順を完了すると、基本的なプラグインが動作します**

---

## Step 1: テンプレートをコピー（2分）

```bash
# UMPA テンプレートをクローン
git clone https://github.com/nobufumi-tego/umpa-universal-plugin-template.git
cd umpa-universal-plugin-template

# テンプレートをコピー
cp -r template my-awesome-plugin
cd my-awesome-plugin
```

---

## Step 2: プラグイン情報を更新（2分）

`.claude-plugin/plugin.json` を編集：

```json
{
  "name": "my-awesome-plugin",
  "description": "My awesome plugin description",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "your@email.com"
  },
  "homepage": "https://github.com/your-username/my-awesome-plugin",
  "repository": "https://github.com/your-username/my-awesome-plugin",
  "license": "MIT",
  "keywords": ["awesome", "plugin"]
}
```

**重要**: `name` はプラグイン呼び出し時に使用されます。

---

## Step 3: スキルを編集（3分）

`skills/example-skill/SKILL.md` を編集：

```markdown
---
name: example-skill
description: 何をするスキルか、簡潔に説明
version: 1.0.0
---

# スキルの表示名

## 概要

このスキルが何をするか、1-2文で説明してください。

## 学習リソース

- **日本語**: See references/ja/
- **English**: See references/en/

## プロセス

### ステップ 1: [アクション名]

詳細な手順を説明してください。

### ステップ 2: [アクション名]

次のステップを説明してください。

## 入力形式

例:
```json
{
  "input": "value"
}
```

## 出力形式

例:
```json
{
  "result": "output"
}
```
```

**最小限の内容**で OK です。詳しくは後で追加。

---

## Step 4: ローカルでテスト（2分）

```bash
# Claude Code を起動
claude --plugin-dir .

# スキルをテスト
# プロンプトで:
/my-awesome-plugin:example-skill
```

**これでプラグインが動作します！** ✅

---

## Step 5: 学習資料を追加（1分）

`references/ja/README.md` を編集：

```markdown
---
title: "学習ガイド - 日本語"
language: ja
---

# プラグイン名 学習ガイド

このプラグインについての学習資料です。

## 推奨学習パス

### 初級者向け

1. 01-concept.md - 背景・理論
2. 02-step-by-step.md - 実装ガイド

...
```

テンプレートから適切な部分をコピーして、カスタマイズするだけ。

---

## Step 6: Git に登録（1分）

```bash
# Git リポジトリを初期化
git init

# ファイルを追加
git add .

# 初期コミット
git commit -m "Initial commit: my-awesome-plugin v1.0.0"

# リモートを追加（GitHub での リポジトリ作成後）
git remote add origin https://github.com/your-username/my-awesome-plugin.git
git branch -M main
git push -u origin main
```

---

## ✅ 完成！

これで基本的なプラグインができました。

### あなたのプラグインは：

✅ Claude Code で動作  
✅ GitHub に公開  
✅ 日本語と英語のガイド付き  
✅ 拡張可能な構造  

---

## 📚 次のステップ

### すぐにやること

1. **スキルを改善** - `skills/example-skill/SKILL.md` を充実させる
2. **学習資料を作成** - `references/ja/` と `references/en/` に内容を追加
3. **言語を追加** - 中国語など

### 後からやること

1. **コマンドを追加** - `commands/` フォルダにコマンドを追加
2. **マーケットプレイスに登録** - [公開ガイド](../PLUGIN_RELEASE.md)を参照
3. **翻訳協力を受け入れる** - [コントリビューションガイド](../CONTRIBUTION.md)を参照

---

## 🔧 便利なコマンド

### プラグイン検証

```bash
python ../tools/validate-plugin.py .
```

### 言語を追加

```bash
../tools/add-language.sh zh-CN
```

---

## 💡 よくある質問

**Q: SKILL.md の最小内容は？**

A:
```markdown
---
name: skill-name
description: 説明
version: 1.0.0
---

# スキル名

## 概要
簡潔に説明（1-2文）

## プロセス
詳細な手順

## 入力形式
例

## 出力形式
例
```

**Q: references/ を省略できる？**

A: はい。最初は `references/ja/README.md` だけあれば OK。

**Q: スキルを複数追加したい**

A:
```bash
mkdir skills/skill-2
cp skills/example-skill/SKILL.md skills/skill-2/SKILL.md
# 編集
```

**Q: 他の言語を対応させたい**

A:
```bash
./tools/add-language.sh ko
# references/ko/ が作成されるので、翻訳する
```

---

## ⏱️ 11分で完成するプラグイン

実は：

```
テンプレートコピー: 1分
plugin.json編集: 1分
SKILL.md編集: 2分
ローカルテスト: 1分
GitHub登録: 2分
学習資料修正: 2分
テスト・修正: 2分

= 11分で完全なプラグイン！
```

---

## 🎯 このガイドの後に

### 詳しく学びたい場合

各ドキュメントを読む：

1. [概要](01-overview.md) - UMPA の考え方
2. [ディレクトリ構造](02-directory-structure.md) - プラグイン構成
3. [コアコンポーネント](03-components.md) - plugin.json、SKILL.md 詳細
4. [学習層](04-learning-layer.md) - references/ の書き方
5. [ベストプラクティス](05-best-practices.md) - 質の高いプラグイン

### すぐに改善したい場合

1. SKILL.md を充実させる（100-200行）
2. references/ja/ に学習資料を追加
3. references/en/ に翻訳を追加
4. マーケットプレイスに登録

---

## 🚀 実装例で学ぶ

実装例を参考にするのも有効：

```bash
# Lean Canvas プラグイン（完全版）
cd examples/lean-canvas-plugin

# ファイル構成を確認
find . -type f -name "*.md" | head -20

# SKILL.md を参考に
cat skills/lean-canvas-generator/SKILL.md

# references/ を参考に
ls -la references/ja/
```

---

これでプラグイン開発の第一歩は完了です！

質問があれば、関連ドキュメントを参照するか、GitHub Issues で相談してください。

Happy Plugin Development! 🎉

---

[← 仕様書ホーム](../SPECIFICATION.md) | [← 概要](01-overview.md) | [ベストプラクティス →](05-best-practices.md)
