# Python Foundations Study - Part 1

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=ffffff">
  <img alt="Python Study" src="https://img.shields.io/badge/Python-Study-1F6FEB">
  <img alt="pip" src="https://img.shields.io/badge/pip-Dev%20Tools-3775A9?logo=pypi&logoColor=ffffff">
  <img alt="Ruff" src="https://img.shields.io/badge/Ruff-Lint%20%2F%20Format-D7FF64">
</p>

Python の基礎を、コードリーディング中心で学習するためのリポジトリ。  
Part 1 では、**基本構文 / 条件分岐 / 繰り返し / 基本コレクション / 代入・参照・コピー / 関数 / Pythonらしい書き方** を扱う。  
各 Unit ごとにソースコードとドキュメントを用意し、コード、コメント、出力、確認用の `assert` を対応づけながら見返せる形で整理している。

---

## このリポジトリの位置づけ

このリポジトリは、Python基礎学習の前半として作成した `python-foundations-study-part1` である。

今回の Python 学習では、次の2つのリポジトリに分けて進める。

- `python-foundations-study-part1`
  - 前半の学習範囲を扱う
  - 標準寄りの `venv + pip` 構成で環境構築を行う
- `python-foundations-study-part2`
  - 後半の学習範囲を扱う
  - `uv + .venv` 構成で環境構築を行う

Part 1 では、Python の言語基礎と、コードリーディングで頻出する書き方に慣れることを目的とする。  
外部ライブラリは扱わず、Python の言語仕様、組み込み型、組み込み関数、標準的な構文を中心に学習する。

---

## 学習目的

このリポジトリでは、主に次の内容を目的として学習を行う。

- Python の基本構文を読めるようにする
- 変数、値、文字列、真偽値、`None` の基本を理解する
- `if / elif / else`、`for`、`while`、`break`、`continue` を読めるようにする
- truthy / falsy や `is` / `==` の違いを理解する
- `list`、`tuple`、`dict`、`set` の基本操作と違いを理解する
- 代入、参照、再束縛、浅いコピー、深いコピーの違いを理解する
- 関数定義、戻り値、引数、スコープ、docstring の基本を理解する
- 内包表記、`enumerate`、`zip`、`sorted`、`any`、`all` などの Python らしい書き方に慣れる
- ソースコード、コメント、出力結果、`assert` を対応させながら処理を追えるようにする

---

## 学習範囲

このリポジトリで扱う Unit は次の通り。

| Unit | 内容                         |
| ---- | ---------------------------- |
| 01   | Pythonの基本構文・値・文字列 |
| 02   | 条件分岐・繰り返し・比較     |
| 03   | 基本コレクション             |
| 04   | 代入・参照・コピー           |
| 05   | 関数・引数・スコープ         |
| 06   | Pythonらしい書き方           |

### 各 Unit の位置づけ

- **Unit 01: Pythonの基本構文・値・文字列**  
  変数、数値、文字列、真偽値、`None`、型変換、f文字列、標準出力など、Python を読む入口となる基本を確認する

- **Unit 02: 条件分岐・繰り返し・比較**  
  `if / elif / else`、`for`、`while`、`range`、比較演算子、論理演算子、truthy / falsy、`is` と `==` の違いを確認する

- **Unit 03: 基本コレクション**  
  `list`、`tuple`、`dict`、`set` の作成、参照、更新、検索、ソート、反復、membership 判定、ミュータブル / イミュータブルを確認する

- **Unit 04: 代入・参照・コピー**  
  Python における代入の意味、参照の共有、再束縛、浅いコピー、深いコピー、`copy.copy`、`copy.deepcopy` を確認する

- **Unit 05: 関数・引数・スコープ**  
  `def`、戻り値、複数戻り値、位置引数、キーワード引数、デフォルト引数、`*args`、`**kwargs`、スコープ、docstring を確認する

- **Unit 06: Pythonらしい書き方**  
  リスト / 辞書 / 集合内包表記、ジェネレータ式、`enumerate`、`zip`、`sorted`、`reversed`、`any`、`all`、パック / アンパック、ラムダ式を確認する

---

## 学習の進め方

基本的な進め方は次の通り。

1. `docs/` の対象 Unit の Markdown を読む
2. `src/<unit>/main.py` を実行する
3. `main.py` から呼び出される各テーマ別ファイルを読む
4. ソースコード内のコメントと出力結果を対応させながら処理を追う
5. 各ファイル末尾の `assert` で、期待値との対応を確認する
6. 必要に応じて値を書き換え、再実行して挙動を確認する

このリポジトリでは、ソースコード単体でも学習できるようにコメントを多めに記載している。  
ドキュメントは、各 Unit の学習対象、読む順番、処理の流れ、注目ポイント、引っかかりやすい点を確認するための補助資料として使う。

---

## 前提環境

- Python 3.13.13
- VS Code
- Python 拡張機能
- Pylance
- Ruff
- venv
- pip

このリポジトリでは、Python 標準の `venv` と `pip` を使って仮想環境を作成する。  
学習コード自体は外部ライブラリを使わず、標準機能・標準ライブラリの範囲で動作する。  
`requirements-dev.txt` は、Ruff などの開発用ツールをインストールするために使用する。

---

## セットアップ

### 1. 仮想環境を作成

```bash
py -3.13 -m venv .venv
```

### 2. 仮想環境を有効化

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
```

### 3. pip を更新

```bash
python -m pip install --upgrade pip
```

### 4. 開発用ツールをインストール

```bash
python -m pip install -r requirements-dev.txt
```

### 5. Python バージョンを確認

```bash
python --version
```

想定するバージョンは次の通り。

```text
Python 3.13.13
```

---

## 実行方法

### Unit 01: Pythonの基本構文・値・文字列

```bash
python src/01_basic_syntax_values_and_strings/main.py
```

### Unit 02: 条件分岐・繰り返し・比較

```bash
python src/02_control_flow_and_comparisons/main.py
```

### Unit 03: 基本コレクション

```bash
python src/03_core_collections/main.py
```

### Unit 04: 代入・参照・コピー

```bash
python src/04_assignment_references_and_copying/main.py
```

### Unit 05: 関数・引数・スコープ

```bash
python src/05_functions_arguments_and_scope/main.py
```

### Unit 06: Pythonらしい書き方

```bash
python src/06_pythonic_constructs/main.py
```

### Ruff による確認

```bash
python -m ruff check .
python -m ruff format --check .
```

必要に応じてフォーマットを実行する。

```bash
python -m ruff format .
```

---

## リポジトリ構成

主要な構成は次の通り。

```text
.
├─ docs/
│  ├─ 01-basic-syntax-values-and-strings.md
│  ├─ 02-control-flow-and-comparisons.md
│  ├─ 03-core-collections.md
│  ├─ 04-assignment-references-and-copying.md
│  ├─ 05-functions-arguments-and-scope.md
│  └─ 06-pythonic-constructs.md
│
├─ src/
│  ├─ 01_basic_syntax_values_and_strings/
│  ├─ 02_control_flow_and_comparisons/
│  ├─ 03_core_collections/
│  ├─ 04_assignment_references_and_copying/
│  ├─ 05_functions_arguments_and_scope/
│  └─ 06_pythonic_constructs/
│
├─ .vscode/
│  ├─ extensions.json
│  └─ settings.json
│
├─ requirements-dev.txt
├─ pyproject.toml
└─ README.md
```

### 各ディレクトリ・ファイルの役割

- `docs/`  
  各 Unit の学習対象、ファイル構成、実行方法、読む順番、処理の流れ、注目ポイント、引っかかりやすい点、確認観点をまとめた Markdown ドキュメントを置く

- `src/`  
  Unit ごとの Python ソースコードを置く  
  各 Unit はディレクトリ単位で分け、`main.py` を実行入口とする

- `.vscode/`  
  VS Code の推奨拡張機能とワークスペース設定を置く

- `requirements-dev.txt`  
  開発用ツールを `pip` でインストールするためのファイル

- `pyproject.toml`  
  Ruff などのツール設定を管理するファイル

---

## ドキュメント

- Pythonの基本構文・値・文字列: [`docs/01-basic-syntax-values-and-strings.md`](docs/01-basic-syntax-values-and-strings.md)
- 条件分岐・繰り返し・比較: [`docs/02-control-flow-and-comparisons.md`](docs/02-control-flow-and-comparisons.md)
- 基本コレクション: [`docs/03-core-collections.md`](docs/03-core-collections.md)
- 代入・参照・コピー: [`docs/04-assignment-references-and-copying.md`](docs/04-assignment-references-and-copying.md)
- 関数・引数・スコープ: [`docs/05-functions-arguments-and-scope.md`](docs/05-functions-arguments-and-scope.md)
- Pythonらしい書き方: [`docs/06-pythonic-constructs.md`](docs/06-pythonic-constructs.md)

---

## このリポジトリで確認できること

このリポジトリでは、次の内容を確認できる。

- Python の基本的な構文を読める
- 変数、値、文字列、真偽値、`None` の基本を説明できる
- `if / elif / else`、`for`、`while` の基本を読める
- truthy / falsy や `is` / `==` の違いを説明できる
- `list`、`tuple`、`dict`、`set` の違いを説明できる
- インデックス、スライス、membership 判定の基本を説明できる
- 代入、参照、再束縛、浅いコピー、深いコピーの違いを説明できる
- 関数の定義、戻り値、引数、スコープの基本を説明できる
- ミュータブルなデフォルト引数の注意点を説明できる
- 内包表記やジェネレータ式の基本を読める
- `enumerate`、`zip`、`sorted`、`reversed`、`any`、`all` の用途を説明できる
- パック / アンパック、複数代入、ラムダ式の基本を読める
- ソースコード、コメント、出力、`assert` を対応させながら挙動を確認できる
