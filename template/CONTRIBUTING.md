# Contributing to [Plugin Name]

[Plugin Name] へのコントリビューションを歓迎します！

## 貢献方法

### 1. バグ報告

バグを見つけた場合は、GitHub Issues で報告してください。

### 2. 機能提案

新機能について提案する場合は、Issues でディスカッション後に PR をサブミット。

### 3. 翻訳協力

新言語への翻訳に協力できます。

#### 翻訳手順

```bash
# 新言語フォルダを作成
./tools/add-language.sh [lang-code]

# ファイルを翻訳
vim references/[lang-code]/README.md
vim references/[lang-code]/01-concept.md
# ... 他のファイル

# PR をサブミット
git add references/[lang-code]/
git commit -m "Add [Language] translation"
git push origin translate/[lang-code]
```

### 4. ドキュメント改善

README、学習資料、ガイドの改善・誤字修正。

---

## PR サブミット手順

1. Fork してブランチを作成
2. 変更をコミット
3. PR を作成
4. レビューを待つ

詳細は [../../docs/CONTRIBUTION.md](../../docs/CONTRIBUTION.md) を参照。

---

## コミュニティガイドライン

- すべてのコントリビューターを尊重してください
- 建設的なフィードバックをしてください
- 多言語・多文化を尊重してください

---

## ライセンス

このプラグインに貢献することで、MIT ライセンスの下で公開されることに同意します。

---

ご協力ありがとうございます！ 🙏
