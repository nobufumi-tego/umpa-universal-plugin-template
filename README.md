# UMPA - Universal Multilingual Plugin Architecture

多言語対応Claude Codeプラグインを、簡単に、スケーラブルに作成するためのテンプレートとガイド。

**Main Concept**: Write once, scale to 10+ languages + unlimited use cases

---

## 📚 What is UMPA?

**UMPA（汎用多言語プラグイン・メタアーキテクチャ）** は、以下を実現するアーキテクチャです：

✅ スキルを一度英語で書く  
✅ 20言語対応しても、コンテキストトークン数は変わらない  
✅ 言語追加はフォルダ追加だけ、コード変更ゼロ  
✅ 1プラグインから1000プラグインまでスケール  

### 3層構造

```
実行層 (英語、Claude向け)
├── skills/
├── commands/
└── agents/
    ↓
学習層 (多言語、人間向け)
├── references/ja/
├── references/en/
├── references/zh-CN/
└── ...
    ↓
設定層
├── plugin.json
└── .mcp.json
```

**重要**: `references/` はClaudeのコンテキストに読み込まれません。つまり、言語を追加してもトークン数が増えません。

---

## 📁 Repository Structure

```
umpa-universal-plugin-template/
│
├── docs/
│   └── SPECIFICATION.md              ← 完全な仕様書
│
├── template/                         ← 汎用テンプレート
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── skills/
│   │   └── example-skill/
│   │       └── SKILL.md
│   ├── commands/ (optional)
│   ├── references/
│   │   ├── ja/
│   │   │   ├── README.md
│   │   │   ├── 01-concept.md
│   │   │   ├── 02-step-by-step.md
│   │   │   ├── 03-case-studies.md
│   │   │   └── 04-advanced.md
│   │   └── en/
│   │       └── (same structure)
│   └── README.md
│
├── examples/                         ← 完全に機能する実装例
│   ├── lean-canvas-plugin/
│   │   └── (完全なプラグイン実装)
│   └── code-generator-plugin/
│       └── (完全なプラグイン実装)
│
├── tools/                            ← 開発支援ツール
│   ├── add-language.sh              ← 言語追加スクリプト
│   └── validate-plugin.py           ← 検証ツール
│
├── README.md                         ← このファイル
├── README_en.md                      ← English version
├── LICENSE
└── .github/
    └── ISSUE_TEMPLATE/
```

---

## 🚀 Quick Start

### 1. テンプレートをコピー

```bash
# リポジトリをクローン
git clone https://github.com/ynobufumi/umpa-universal-plugin-template.git
cd umpa-universal-plugin-template

# template/ をコピーしてカスタマイズ
cp -r template my-awesome-plugin
cd my-awesome-plugin
```

### 2. プラグイン情報を更新

`.claude-plugin/plugin.json` を編集：

```json
{
  "name": "my-awesome-plugin",
  "description": "My awesome plugin description",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  }
}
```

### 3. スキルを作成

`skills/` に新しいスキルを追加：

```bash
mkdir skills/my-skill
vim skills/my-skill/SKILL.md
```

`SKILL.md` テンプレートは `skills/example-skill/SKILL.md` を参照してください。

### 4. 学習資料を作成

`references/` に日本語と英語の学習資料を作成：

```bash
# テンプレートをコピー
cp -r references/ja references/ja
cp -r references/en references/en

# 各言語の5つのファイルを編集
```

### 5. テスト

```bash
claude --plugin-dir .
```

テストコマンド：
```
/my-awesome-plugin:my-skill
```

### 6. GitHub に push

```bash
git add .
git commit -m "Create my-awesome-plugin"
git push
```

---

## 📖 Documentation

### アーキテクチャ・仕様書

- **[UMPA 完全仕様書](docs/SPECIFICATION.md)** — ディレクトリ構造、ファイル仕様、ベストプラクティス

### 開発ガイド

- **[ローカル開発セットアップ](docs/LOCAL_SETUP.md)** — プラグインをローカルで開発・テストする方法
- **[Template ガイド](template/README.md)** — テンプレートを使い始める方法
- **[SKILL.md テンプレート](template/skills/example-skill/SKILL.md)** — スキルの書き方

### 公開・メンテナンスガイド

- **[プラグイン公開ガイド](docs/PLUGIN_RELEASE.md)** — マーケットプレイスへの登録手順
- **[メンテナンスガイド](docs/MAINTENANCE.md)** — バグ対応、新機能追加、翻訳協力
- **[コントリビューション・翻訳ガイド](docs/CONTRIBUTION.md)** — 詳細なコントリビューション方法

### 実装例

実装例を見て学ぶ：

- **[Lean Canvas プラグイン](examples/lean-canvas-plugin/)** — ビジネステンプレート（完全実装例）
- **[Code Generator プラグイン](examples/code-generator-plugin/)** — コード生成（予定）

各例は完全に動作するプラグインで、あなたのプラグイン作成の参考になります。

### 学習資料テンプレート

- **[日本語学習資料テンプレート](template/references/ja/)** — 日本語ユーザー向けガイド
- **[English Learning Materials](template/references/en/)** — English user guide

---

## 🛠️ Tools

開発を効率化するツール：

### 言語追加スクリプト

新しい言語対応を簡単に追加：

```bash
./tools/add-language.sh ja
```

このスクリプトが自動的に：
- `references/ja/` フォルダを作成
- 基本ファイル（README.md など）を生成

### 検証ツール

プラグインの構造を検証：

```bash
./tools/validate-plugin.py
```

チェック項目：
- ✅ plugin.json の有効性
- ✅ SKILL.md の形式
- ✅ references/ フォルダ構造
- ✅ 言語フォルダの一貫性

---

## 💡 How UMPA Works

### コンテキスト効率

| Component | 読み込まれるか | トークン数 |
|-----------|----------|---------|
| plugin.json | ✅ Yes | ~100 |
| skills/ | ✅ Yes | ~350/skill |
| commands/ | ✅ Yes | ~200 |
| references/ | ❌ No | 0 |
| scripts/ | ❌ No | 0 |
| templates/ | ❌ No | 0 |

**初期コンテキスト**: ~1,200トークン（言語数に関わらず固定）

### 言語の追加方法

1. フォルダを作成: `references/[lang]/`
2. 5つのファイルを翻訳
3. 親フォルダの README に言語リンクを追加
4. Commit & Push

**影響**: コンテキストトークン +0、プラグインサイズ +50-100KB

---

## 🌍 Supported Languages

現在テンプレートで対応している言語：

| 言語 | コード | Status |
|------|-------|--------|
| 日本語 | ja | ✅ Complete |
| English | en | ✅ Complete |
| 简体中文 | zh-CN | 📝 Template |
| 繁體中文 | zh-TW | 📝 Template |
| 한국어 | ko | 📝 Template |
| Español | es | 📝 Future |

**Template状態** = フォルダ構造とテンプレートは用意されているが、実装例の翻訳は未実施

---

## 📊 Scalability

UMPAのスケーラビリティ実績：

| 項目 | 最小 | 推奨 | 最大 |
|------|-----|-----|-----|
| Skills per plugin | 1 | 5 | 50+ |
| Languages | 2 | 5 | 20+ |
| Initial context | ~1,200t | ~1,200t | ~1,500t |
| Time to add language | 2h | 4-6h | 8h |

**重要**: スキルを追加してもコンテキストはほぼ変わりません。言語を追加してもコンテキストは増えません。

---

## 🤝 Contributing

UMPAをより良くする方法：

1. **テンプレートの改善提案** - GitHub Issues で提案
2. **新言語対応** - 翻訳をしてPR送付
3. **実装例の追加** - 新しいプラグイン例をサブミット
4. **バグ報告** - Issues で報告
5. **フィードバック** - 使用感をシェア

---

## 📝 License

MIT License - 自由に使用、修正、配布できます。

詳細は [LICENSE](LICENSE) を参照してください。

---

## 🔗 Related Resources

- **Claude Code 公式ドキュメント**: https://code.claude.com
- **プラグイン開発ガイド**: https://code.claude.com/docs/plugins
- **UMPA 仕様書**: [docs/SPECIFICATION.md](docs/SPECIFICATION.md)

---

## 📞 Support

### よくある質問

**Q: 複数の言語を一度に対応させたい**  
A: `template/references/` フォルダをコピーして、各言語フォルダの内容を翻訳してください。

**Q: 既存のプラグインをUMPAに移行したい**  
A: 仕様書の「移行ガイド」セクションを参照するか、GitHub Issues で相談してください。

**Q: 言語の追加以外でカスタマイズしたい**  
A: 仕様書の「カスタマイズガイド」を参照してください。

### フィードバック

- 📧 Email: nobufumi.yoshida@tegosacloud.com
- 🐙 GitHub: [@ynobufumi](https://github.com/ynobufumi)
- 🔗 Issues: [GitHub Issues](https://github.com/ynobufumi/umpa-universal-plugin-template/issues)

---

## 🎯 Next Steps

### プラグイン開発フロー

1. **ローカル開発環境を準備** → [ローカル開発ガイド](docs/LOCAL_SETUP.md)
   ```bash
   cp -r template my-plugin
   cd my-plugin
   claude --plugin-dir .
   ```

2. **仕様書を理解する** → [UMPA 仕様書](docs/SPECIFICATION.md)

3. **実装例を参考にする** → [Lean Canvas プラグイン](examples/lean-canvas-plugin/)

4. **プラグインを開発** → スキル、コマンド、学習資料を作成

5. **ローカルでテスト** → `./tools/validate-plugin.py`

6. **GitHub にプッシュ** → [公開ガイド](docs/PLUGIN_RELEASE.md)

7. **マーケットプレイスに登録** → 公開ガイドに従う

8. **継続メンテナンス** → [メンテナンスガイド](docs/MAINTENANCE.md)

---

**Made with ❤️ by Nobufumi Yoshida**

Last Updated: 2026-04-24
