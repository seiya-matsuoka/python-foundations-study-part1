# 01. Pythonの基本構文・値・文字列

## 1. 学習対象

この単位では、Pythonのコードを読み始めるための最小限の基礎を扱う。

- 変数
- 数値型
- 文字列
- 真偽値
- `None`
- 基本演算
- 型変換
- f文字列
- コメント
- 標準出力の基本
- スクリプト実行の基本

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- Pythonでは変数宣言に型名を書かない
- 値には型があり、`type()` で確認できる
- 同じ変数名に別の型の値を再代入できる
- 数値型には主に `int` と `float` がある
- `/` と `//` は意味が異なる
- 文字列は `str` 型の値として扱う
- f文字列を使うと、値を文字列に埋め込める
- `True` / `False` は `bool` 型の値となる
- `None` は「値がない」ことを表す特別な値となる
- `print()` は標準出力に値を表示する基本的な関数となる
- コメントと docstring はコードを読む補助として使う
- Pythonファイルはスクリプトとして実行できる

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/01_basic_syntax_values_and_strings/
  main.py
  values_and_variables.py
  numbers_and_operations.py
  strings_and_output.py
  booleans_none_and_conversion.py
  comments_and_execution.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 01 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `values_and_variables.py`
  - 値、変数、動的型付けの基本を扱う
- `numbers_and_operations.py`
  - 数値型、算術演算、数値変換を扱う
- `strings_and_output.py`
  - 文字列、f文字列、標準出力を扱う
- `booleans_none_and_conversion.py`
  - 真偽値、`None`、基本的な型変換を扱う
- `comments_and_execution.py`
  - コメント、docstring、スクリプト実行の入口を扱う

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/01_basic_syntax_values_and_strings/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/01_basic_syntax_values_and_strings/main.py
```

Ruff の確認は次のコマンドで行う。

```bash
python -m ruff check .
python -m ruff format --check .
```

必要に応じてフォーマットを実行する。

```bash
python -m ruff format .
```

## 5. コードを読む順番

次の順番で読むと、内容を追いやすい。

1. `main.py`
2. `values_and_variables.py`
3. `numbers_and_operations.py`
4. `strings_and_output.py`
5. `booleans_none_and_conversion.py`
6. `comments_and_execution.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、各テーマ別ファイルを読んで、個別の文法や値の扱いを確認する。

## 6. 処理の流れ

Unit 01 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. 値と変数のサンプルを実行する
5. 数値型と演算のサンプルを実行する
6. 文字列と標準出力のサンプルを実行する
7. 真偽値、`None`、型変換のサンプルを実行する
8. コメントとスクリプト実行のサンプルを実行する
9. 各ファイル内の `assert` により、軽い期待値確認を行う

## 7. 注目ポイント

### 7-1. Pythonは変数宣言に型名を書かない

Javaでは変数宣言時に型名を書くが、Pythonでは次のように値を代入する。

```python
user_name = "Matsuoka"
years_of_experience = 2
```

ただし、型が存在しないわけではない。  
値には型があり、`type()` で確認できる。

### 7-2. 動的型付けの感覚

Pythonでは同じ変数名に別の型の値を再代入できる。

```python
value = "text"
value = 100
```

ただし、読みやすいコードでは、同じ変数名に意味の異なる値を入れ直しすぎない方がよい。

### 7-3. `/` と `//` の違い

Pythonでは `/` は通常の割り算で、結果は `float` になる。  
`//` は切り捨て除算となる。

```python
17 / 5   # 3.4
17 // 5  # 3
```

### 7-4. f文字列

f文字列は、文字列の中に値や式を埋め込むための基本的な書き方。

```python
language = "Python"
unit_number = 1
print(f"Unit {unit_number}: {language}")
```

この書き方は今後も頻繁に使う。

### 7-5. `None` の扱い

`None` は「値がない」ことを表す特別な値。  
`None` かどうかを確認するときは、基本的に `is None` を使う。

```python
selected_book = None

if selected_book is None:
    print("未選択")
```

### 7-6. `assert` の位置づけ

この単位では、軽い確認として `assert` を使っている。  
本格的なテストは Unit 12 で `unittest` として扱う。

## 8. 引っかかりやすい点

### 8-1. 変数に型がないわけではない

Pythonでは変数宣言に型を書かないが、値には型がある。  
「変数に型を書く言語」ではなく、「値の型を実行時に扱う言語」として捉えると理解しやすい。

### 8-2. `/` の結果は整数とは限らない

`10 / 2` のように割り切れる場合でも、結果は `5.0` のような `float` になる。  
整数の商がほしい場合は `//` を使う。

### 8-3. 文字列と数値は `+` で直接連結できない

次のような書き方はエラーになる。

```python
"Unit " + 1
```

この場合は f文字列を使う。

```python
f"Unit {1}"
```

### 8-4. `None` 判定では `is None` を使う

`== None` でも動く場合はあるが、Pythonでは `is None` が定番の書き方となる。

### 8-5. `print()` の戻り値は表示内容ではない

`print()` は表示を行う関数であり、表示した文字列を戻り値として返すわけではない。  
戻り値の考え方は、関数の単位で改めて扱う。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- `type()` で値の型を確認できる
- `int`、`float`、`str`、`bool`、`NoneType` の違いを大まかに説明できる
- `/`、`//`、`%`、`**` の違いを読める
- f文字列の基本形を読める
- `None` が値の未設定や不在を表すことを理解できる
- `is None` の形を読める
- `main.py` から別ファイルの関数が呼び出される流れを追える
- `assert` が軽い期待値確認として使われていることを理解できる
