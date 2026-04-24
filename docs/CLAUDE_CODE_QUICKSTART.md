# Claude Code でプラグイン開発を始める（クイックスタート）

**Claude Code アシストを使用して、10分でプラグインを作成します**

---

## 準備

### 必要なもの

- Claude Code（Web / Desktop / IDE拡張）
- Git がインストールされている
- GitHub アカウント（オプション、公開する場合）

### 確認

```bash
git --version
```

---

## ステップ 1: Claude Code でプロジェクトを開く

### 1.1 テンプレートリポジトリをクローン

Claude Code のターミナルで実行：

```bash
git clone https://github.com/nobufumi-tego/umpa-universal-plugin-template.git
cd umpa-universal-plugin-template
```

### 1.2 Claude Code でフォルダを開く

Claude Code で：
- **File → Open Folder** → `umpa-universal-plugin-template` を選択
- または、ターミナルで `code .` を実行

---

## ステップ 2: テンプレートをコピー

### 2.1 ファイルエクスプローラーで操作

Claude Code のファイルエクスプローラー（左パネル）で：

1. `template/` フォルダを右クリック
2. **Copy** → **Paste** を選択
3. フォルダ名を `my-awesome-plugin` に変更

または、Claude Code のターミナルで：

```bash
cp -r template my-awesome-plugin
cd my-awesome-plugin
```

---

## ステップ 3: プラグイン情報を編集

### 3.1 `.claude-plugin/plugin.json` を開く

Claude Code で：
1. ファイルエクスプローラーから `.claude-plugin/plugin.json` をクリック
2. エディタでファイルが開きます

### 3.2 プラグイン情報を入力

以下の部分を編集：

```json
{
  "name": "my-awesome-plugin",
  "description": "My awesome plugin description",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  },
  "homepage": "https://github.com/your-username/my-awesome-plugin",
  "repository": "https://github.com/your-username/my-awesome-plugin",
  "license": "MIT",
  "keywords": ["awesome", "plugin"]
}
```

**入力のコツ:**
- `name`: プラグイン呼び出し時に使用（例：`/my-awesome-plugin:skill-name`）
- `description`: マーケットプレイスで表示される説明
- `version`: セマンティックバージョニング（`1.0.0` 形式）

### 3.3 保存

**Ctrl+S** (Windows/Linux) または **Cmd+S** (Mac)

---

## ステップ 4: スキルを定義

### 4.1 `skills/example-skill/SKILL.md` を開く

Claude Code のファイルエクスプローラーから開きます：
1. `skills/` → `example-skill/` → `SKILL.md`

### 4.2 スキル情報を編集

例：TODO リスト生成スキル

```markdown
---
name: todo-generator
description: プロジェクト情報から TODO リストを生成します
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

ユーザーから以下を確認：
- プロジェクト名
- 目的
- 納期
- チームメンバー数

### ステップ 2: TODO を生成

プロジェクト情報をもとに、実行可能なタスクに分解します。

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
      "estimatedHours": 2
    }
  ],
  "totalHours": 20
}
```
```

### 4.3 スキルフォルダの名前変更（オプション）

`example-skill` を別の名前に変更する場合：

1. Claude Code のファイルエクスプローラーで `example-skill/` を右クリック
2. **Rename** を選択
3. 新しい名前を入力（例：`todo-generator`）

**注意**: 変更した場合、step 6 でテスト時に新しい名前を使用します

### 4.4 保存

**Ctrl+S** または **Cmd+S**

---

## ステップ 5: Claude Code でテスト

### 5.1 ローカルプラグインとして起動

Claude Code のターミナルで：

```bash
# プロジェクトのルートに移動
cd ..

# ローカルプラグインとして起動
claude --plugin-dir my-awesome-plugin
```

**出力例:**
```
Starting Claude Code with local plugin...
Plugin loaded: my-awesome-plugin
Ready to use /my-awesome-plugin:example-skill
```

### 5.2 スキルをテスト

Claude Code のプロンプトで入力：

```
/my-awesome-plugin:example-skill

以下のプロジェクトのTODOリストを作成してください：
- プロジェクト名: モバイルアプリ開発
- 目的: iOS/Android アプリ
- 納期: 2026年7月
- チーム: 5名
```

### 5.3 出力を確認

Claude が JSON 形式で返します。形式が正しければ成功！

---

## ステップ 6: 学習資料を作成（オプション）

### 6.1 `references/ja/README.md` を編集

Claude Code で開いて編集：

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

## ファイルガイド

| ファイル | 内容 |
|---------|------|
| 01-concept.md | なぜ TODO リストが重要か |
| 02-step-by-step.md | 効果的な TODO 作成方法 |
```

### 6.2 英語版も作成

`references/en/README.md` も同様に編集

---

## ステップ 7: Git で管理

### 7.1 Git リポジトリを初期化

Claude Code のターミナルで：

```bash
# my-awesome-plugin に移動
cd my-awesome-plugin

# Git 初期化
git init
git add .
git commit -m "Initial commit: my-awesome-plugin v1.0.0"
```

### 7.2 GitHub に登録（オプション）

1. **GitHub で新しいリポジトリを作成**
   - `my-awesome-plugin` という名前で作成
   - Public を選択

2. **Claude Code のターミナルで実行:**

```bash
git remote add origin https://github.com/your-username/my-awesome-plugin.git
git branch -M main
git push -u origin main
```

---

## ✅ 完成！

プラグインが完成しました！

### あなたのプラグインは：

✅ Claude Code で動作  
✅ GitHub に公開（オプション）  
✅ 日本語と英語のガイド付き  
✅ 拡張可能な構造  

---

## 次のステップ

### すぐにやること

1. **スキルを改善** - SKILL.md を充実させる（100-200行）
2. **学習資料を作成** - `references/` に内容を追加
3. **テストする** - `claude --plugin-dir my-awesome-plugin` で動作確認

### 後からやること

1. **コマンドを追加** - `commands/` フォルダにコマンドを追加
2. **マーケットプレイスに登録** - [プラグイン公開ガイド](PLUGIN_RELEASE.md) を参照
3. **翻訳協力を受け入れる** - [コントリビューションガイド](CONTRIBUTION.md) を参照

---

## 🔧 便利なコマンド

### プラグイン検証

```bash
cd my-awesome-plugin
python ../tools/validate-plugin.py .
```

### 言語を追加

```bash
cd my-awesome-plugin
../tools/add-language.sh zh-CN
```

---

## 💡 Claude Code での操作のコツ

### ファイルエクスプローラーの使用

- **左クリック**: ファイルを開く
- **右クリック**: コピー、削除、リネームなど
- **ドラッグ&ドロップ**: ファイルを移動

### エディタのショートカット

| 操作 | Windows/Linux | Mac |
|------|---------------|-----|
| 保存 | Ctrl+S | Cmd+S |
| すべて選択 | Ctrl+A | Cmd+A |
| コピー | Ctrl+C | Cmd+C |
| ペースト | Ctrl+V | Cmd+V |
| 検索 | Ctrl+F | Cmd+F |
| 置換 | Ctrl+H | Cmd+H |

### ターミナルの使用

Claude Code で：
- **View → Terminal** でターミナルを開く
- または **Ctrl+`** (バッククォート)

---

## ❓ よくある質問

**Q: スキルファイルの最小内容は？**

A: SKILL.md に以下を記述：
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

**Q: プラグイン名に特殊文字を使えますか？**

A: いいえ。英数字とハイフン（-）のみ使用可。例：`my-awesome-plugin`、`todo-generator`

**Q: 複数のスキルを追加したい**

A: `skills/` に新しいフォルダを作成：
```bash
mkdir skills/skill-2
cp skills/example-skill/SKILL.md skills/skill-2/SKILL.md
# 編集
```

**Q: ローカルテスト後に GitHub に公開したい**

A: [プラグイン公開ガイド](PLUGIN_RELEASE.md) を参照してください。

---

## 📚 関連ドキュメント

- **[仕様書](SPECIFICATION.md)** - 完全な仕様書
- **[プラグイン公開ガイド](PLUGIN_RELEASE.md)** - マーケットプレイス登録方法
- **[ローカル開発ガイド](LOCAL_SETUP.md)** - 詳細な開発手順
- **[メンテナンスガイド](MAINTENANCE.md)** - 継続的なメンテナンス

---

これでプラグイン開発の第一歩は完了です！

Happy Plugin Development! 🎉

---

[← README に戻る](../README.md) | [プラグイン公開ガイド →](PLUGIN_RELEASE.md)
