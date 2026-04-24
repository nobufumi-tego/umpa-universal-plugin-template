---
name: lean-canvas-generator
description: ビジネスアイデアをもとに Lean Canvas を生成します。プロダクト、顧客、課題、解決策などを定義し、わかりやすい Lean Canvas テンプレートを作成します。
version: 1.0.0
---

# Lean Canvas ジェネレーター

## 概要

ビジネスアイデアに基づいて、Lean Canvas（ビジネスモデルキャンバス）を自動生成します。スタートアップやビジネス企画に必要な9つの要素を、構造化されたフォーマットで作成し、わかりやすく整理します。

## 学習リソース

詳細な学習資料をお好みの言語で参照してください：

- **日本語**: See `references/ja/`
- **English**: See `references/en/`

## プロセス

### ステップ 1: ビジネスアイデアを理解

ユーザーから以下の情報を収集します：

- **プロダクト名**: 何を提供するのか
- **対象顧客**: 誰に売るのか
- **主な課題**: 顧客が抱える課題は何か
- **解決策**: どのように解決するのか
- **主な機能**: 最小限必要な機能は何か

### ステップ 2: Lean Canvas の要素を定義

以下の9つの要素を、ユーザーの入力をもとに作成します：

1. **問題（Problem）**: 顧客が抱える課題（最大3つ）
2. **顧客セグメント（Customer Segments）**: ターゲット顧客
3. **独自の価値提案（Unique Value Proposition）**: 競争優位性
4. **解決策（Solution）**: 問題を解決する方法
5. **チャネル（Channels）**: 顧客への到達方法
6. **収益の流れ（Revenue Streams）**: マネタイズ方法
7. **コスト構造（Cost Structure）**: 主な費用項目
8. **主要メトリクス（Key Metrics）**: 成功を測る指標
9. **圧倒的な利点（Unfair Advantage）**: 他では真似できない優位性

### ステップ 3: Lean Canvas を出力

JSON形式で構造化された Lean Canvas を出力します。

## 入力形式

```json
{
  "productName": "プロダクト名",
  "customerSegment": "対象顧客の説明",
  "problems": ["課題1", "課題2", "課題3"],
  "solution": "解決策の説明",
  "keyFeatures": ["機能1", "機能2"],
  "competitiveAdvantage": "競争優位性の説明"
}
```

## 出力形式

```json
{
  "leanCanvas": {
    "problem": {
      "description": "顧客が抱える課題",
      "items": ["課題1", "課題2", "課題3"]
    },
    "customerSegments": {
      "description": "ターゲット顧客",
      "target": "具体的な顧客セグメント"
    },
    "uniqueValueProposition": {
      "description": "独自の価値提案",
      "statement": "簡潔な説明"
    },
    "solution": {
      "description": "問題を解決する方法",
      "keyFeatures": ["機能1", "機能2"]
    },
    "channels": {
      "description": "顧客への到達方法",
      "methods": ["チャネル1", "チャネル2"]
    },
    "revenueStreams": {
      "description": "マネタイズ方法",
      "model": "ビジネスモデル説明"
    },
    "costStructure": {
      "description": "主な費用項目",
      "costs": ["費用1", "費用2"]
    },
    "keyMetrics": {
      "description": "成功を測る指標",
      "metrics": ["メトリクス1", "メトリクス2"]
    },
    "unfairAdvantage": {
      "description": "圧倒的な利点",
      "advantage": "他では真似できない優位性"
    }
  }
}
```

## ベストプラクティス

- **顧客中心**: 常に顧客視点で考える
- **シンプルさ**: 複雑すぎず、わかりやすく
- **実現可能性**: 理想ではなく、実現可能なプランを立てる
- **定期的な見直し**: 3ヶ月ごとに見直す

## よくあるピットフォール

- **問題の定義が曖昧**: 顧客が実際に感じている課題を定義する
- **ソリューションが不明確**: 具体的な解決方法を説明する
- **ターゲット顧客が広すぎる**: 最初は限定的なセグメントに絞る
