# ローカルプラグイン開発・インストールガイド

Claude Code でプラグインをローカル環境で開発・テストする方法を説明します。

## 📍 2つのプラグイン利用方法

### 1. マーケットプレイス版（推奨・公開版）

Claude Code プラグインマーケットプレイスからインストール。

- ✅ 一度インストールすれば、どのプロジェクトからでも使用可能
- ✅ 自動更新
- ✅ 公式サポート対象

### 2. ローカル版（開発用）

プラグインフォルダをローカルで指定して読み込む。

- ✅ 開発中のテストに最適
- ✅ カスタマイズ版を即座に試せる
- ✅ CI/CD 前の検証に便利

---

## 🛠️ ローカルプラグインの開発・テスト

### Step 1: プラグインディレクトリを準備

**方法A: テンプレートをコピー**

```bash
# UMPA テンプレートから新プラグインを作成
cp -r template my-awesome-plugin
cd my-awesome-plugin
```

**方法B: 既存プラグインをコピー**

```bash
# 既存プラグインをローカルで修正・テスト
cp -r ../existing-plugin my-modified-plugin
cd my-modified-plugin
```

### Step 2: プラグイン情報を更新

```bash
# plugin.json を編集
vim .claude-plugin/plugin.json
```

**例**:
```json
{
  "name": "my-awesome-plugin",
  "description": "My custom plugin for testing",
  "version": "0.1.0",
  "author": {
    "name": "Your Name",
    "email": "your@email.com"
  }
}
```

### Step 3: スキルを作成・カスタマイズ

```bash
# example-skill をカスタマイズ、または新しいスキルを追加
vim skills/example-skill/SKILL.md
```

### Step 4: ローカルプラグインで Claude Code を起動

```bash
# プラグインフォルダで Claude Code を起動
# 方法1: コマンドライン
cd my-awesome-plugin
claude --plugin-dir .

# 方法2: 親フォルダから指定
claude --plugin-dir ./my-awesome-plugin
```

### Step 5: プラグインをテスト

Claude Code が起動したら、スキルを実行：

```
/my-awesome-plugin:example-skill
```

または、フルパスで指定：

```
/example-skill
```

### Step 6: 修正・改善

```bash
# ファイルを修正
vim skills/example-skill/SKILL.md

# Claude Code を再起動（変更を反映）
# CLI を終了: Ctrl+C
# 再度起動: claude --plugin-dir .
```

---

## 📂 ローカルプラグインのディレクトリ構成

Claude Code がプラグインを認識するために必要なファイル構成：

```
my-awesome-plugin/
├── .claude-plugin/
│   └── plugin.json              ← 必須：プラグインメタデータ
├── skills/
│   └── [skill-name]/
│       └── SKILL.md             ← 各スキルの定義
├── commands/                    ← オプション：スラッシュコマンド
├── agents/                      ← オプション：カスタムエージェント
├── references/                  ← オプション：学習資料（ローカル非読み込み）
└── README.md
```

**重要**: `.claude-plugin/plugin.json` がないと認識されません。

---

## 🔧 ローカル開発の便利なコマンド

### プラグイン検証

開発中のプラグインが仕様を満たしているか確認：

```bash
# UMPA テンプレートのツール使用
cd my-awesome-plugin
python ../tools/validate-plugin.py .

# 出力例:
# ✅ plugin.json valid
# ✅ Found skill: example-skill/SKILL.md
# ✅ Found languages: ja, en
```

### 言語を追加

開発中のプラグインに新言語を追加：

```bash
cd my-awesome-plugin

# 中国語（簡体字）を追加
../tools/add-language.sh zh-CN

# references/zh-CN が自動作成されます
```

### ローカル版とマーケットプレイス版の共存

同じプラグインでも、異なるバージョンを使い分けられます：

```bash
# ローカル開発版（最新機能）
claude --plugin-dir ./my-awesome-plugin-dev

# またはマーケットプレイス版（安定版）
# （Claude Code の設定から選択）
```

---

## 🔄 開発ワークフロー例

### シナリオ: 新しいスキルを追加したい

```bash
# ステップ 1: ローカルプラグインで開発開始
cd my-awesome-plugin

# ステップ 2: 新しいスキルを作成
mkdir skills/new-skill
vim skills/new-skill/SKILL.md

# ステップ 3: テスト
claude --plugin-dir .
# → /my-awesome-plugin:new-skill でテスト

# ステップ 4: 改善を繰り返す
# ファイル編集 → Claude Code 再起動 → テスト

# ステップ 5: 完成したら GitHub にコミット・プッシュ
git add skills/new-skill/SKILL.md
git commit -m "Add new-skill"
git push
```

---

## 🎯 ローカル開発 vs マーケットプレイス版

| 観点 | ローカル開発版 | マーケットプレイス版 |
|------|----------|-----------|
| インストール | `claude --plugin-dir .` | マーケットプレイスから |
| 更新頻度 | 手動（毎回再起動時） | 自動 |
| 複数プロジェクト | そのプロジェクトだけ有効 | 全プロジェクトで使用可 |
| バージョン管理 | ローカルで管理 | マーケットプレイスが管理 |
| 用途 | 開発・テスト | 本運用 |

---

## 💾 複数プラグインの同時開発

複数のプラグインを同時に開発する場合：

### 方法1: スイッチして実行

```bash
# プラグイン A で テスト
claude --plugin-dir ./plugin-a

# （終了して）プラグイン B で テスト
claude --plugin-dir ./plugin-b
```

### 方法2: IDE で複数フォルダを開く

VS Code などで複数フォルダをワークスペースで開く：

```json
{
  "folders": [
    { "path": "plugin-a" },
    { "path": "plugin-b" },
    { "path": "plugin-c" }
  ]
}
```

その後、各プラグインを個別にテスト。

---

## 🧪 自動テスト・検証セットアップ

### Git Hooks でテスト自動実行

プッシュ前に自動的に検証するように設定：

**`.git/hooks/pre-push`** を作成：

```bash
#!/bin/bash

echo "Validating plugin before push..."

# プラグイン検証を実行
python tools/validate-plugin.py

# エラーがあれば push を中止
if [ $? -ne 0 ]; then
    echo "❌ Plugin validation failed. Push cancelled."
    exit 1
fi

echo "✅ Plugin validation passed. Proceeding with push."
exit 0
```

実行権限を付与：

```bash
chmod +x .git/hooks/pre-push
```

---

## 📊 ローカルプラグイン開発チェックリスト

開発中に確認すべき項目：

```
プラグイン構造
- [ ] .claude-plugin/plugin.json が存在するか
- [ ] plugin.json が有効な JSON か
- [ ] skills/ フォルダに SKILL.md があるか

機能テスト
- [ ] すべてのスキルが動作するか
- [ ] 入出力形式が正しいか
- [ ] エラーハンドリングが適切か

ドキュメント
- [ ] README.md が充実しているか
- [ ] references/ に日本語と英語があるか
- [ ] デッドリンク確認

セキュリティ
- [ ] API キーが含まれていないか
- [ ] 秘密情報がコミットされていないか

バージョン管理
- [ ] plugin.json の version が正しいか
- [ ] CHANGELOG.md が更新されているか
```

---

## 🆘 トラブルシューティング

### Q: プラグインが認識されない

**A:** `.claude-plugin/plugin.json` が存在するか確認

```bash
# 確認コマンド
ls -la .claude-plugin/plugin.json

# JSON が有効か確認
python -m json.tool .claude-plugin/plugin.json
```

### Q: スキルが動作しない

**A:** SKILL.md の形式を確認

```bash
# テンプレートと比較
diff skills/my-skill/SKILL.md skills/example-skill/SKILL.md

# またはローカルで検証
python ../tools/validate-plugin.py .
```

### Q: ローカル版とマーケットプレイス版が競合する

**A:** `--plugin-dir` で明示的に指定

```bash
# ローカル版を優先
claude --plugin-dir ./my-plugin

# マーケットプレイス版のみ使用
claude  # オプションなし
```

### Q: 変更が反映されない

**A:** Claude Code を再起動

```bash
# CLI を終了
Ctrl+C

# 再度起動（変更が反映される）
claude --plugin-dir .
```

---

## 🚀 ローカル開発から公開まで

### フロー図

```
1. ローカルで開発
   ↓
2. validate-plugin.py で検証
   ↓
3. Claude Code でテスト
   ↓
4. GitHub にプッシュ
   ↓
5. マーケットプレイスに登録
   ↓
6. ユーザーがマーケットプレイスからインストール
```

### バージョン進行例

```
v0.1.0  ← ローカル開発版（初期）
v0.2.0  ← 機能追加（まだ開発中）
v0.9.0  ← ベータ版（GitHub で公開）
v1.0.0  ← 正式版（マーケットプレイス登録）
```

---

## 📚 関連ドキュメント

- [テンプレートセットアップ](../template/README.md)
- [プラグイン公開ガイド](PLUGIN_RELEASE.md)
- [メンテナンスガイド](MAINTENANCE.md)
- [UMPA 仕様書](SPECIFICATION.md)

---

**ローカル開発で十分テストしてから、マーケットプレイスに公開してください！** 🚀
