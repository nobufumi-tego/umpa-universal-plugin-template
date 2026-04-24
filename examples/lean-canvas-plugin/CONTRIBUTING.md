# Contributing to Lean Canvas Plugin

Lean Canvas プラグインへのコントリビューションを歓迎します！

## 貢献方法

### バグ報告

バグを見つけた場合は、[GitHub Issues](../../issues) で報告してください。

### 翻訳協力

現在サポートしている言語：
- 日本語 (ja)
- 英語 (en)

新言語への翻訳に協力できます。

#### 新言語対応例

```bash
# 例: 中国語（簡体字）を追加
./tools/add-language.sh zh-CN

# ファイルを翻訳
vim references/zh-CN/01-concept.md
# ... 他のファイル

# PR をサブミット
git add references/zh-CN/
git commit -m "Add Simplified Chinese support"
```

### 機能提案

新しいスキルやコマンドを提案したい場合は、Issues でディスカッションしてください。

---

## テンプレートの参考

このプラグインは UMPA テンプレートに基づいています。

詳細は以下を参照：
- [UMPA 仕様書](../../docs/SPECIFICATION.md)
- [コントリビューションガイド](../../docs/CONTRIBUTION.md)
- [メンテナンスガイド](../../docs/MAINTENANCE.md)

---

ご協力ありがとうございます！ 🙏
