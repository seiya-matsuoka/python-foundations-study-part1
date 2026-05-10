# 05. 関数・引数・スコープ

## 1. 学習対象

この単位では、Pythonの関数定義、引数、戻り値、スコープを扱う。

- `def`
- 戻り値
- 複数戻り値
- 位置引数
- キーワード引数
- デフォルト引数
- 可変長引数
- `*args`
- `**kwargs`
- スコープ
- ローカル変数とグローバル変数
- ミュータブルなデフォルト引数の注意点
- docstring

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- `def` を使って関数を定義する
- `return` を使って呼び出し元に値を返す
- 複数の値を返すと、tuple として扱える
- 位置引数は引数の順番で値を渡す
- キーワード引数は引数名を指定して値を渡す
- デフォルト引数は省略時に使われる値を定義する
- `*args` は複数の位置引数をまとめて受け取る
- `**kwargs` は複数のキーワード引数をまとめて受け取る
- ローカル変数は関数内で使う変数である
- グローバル変数はモジュール直下に定義した変数である
- ミュータブルな値をデフォルト引数に直接置くと共有される
- docstring は関数の説明として利用できる

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/05_functions_arguments_and_scope/
  main.py
  function_basics.py
  argument_patterns.py
  variable_arguments.py
  scope_examples.py
  mutable_default_arguments.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 05 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `function_basics.py`
  - `def`、戻り値、複数戻り値、docstring を扱う
- `argument_patterns.py`
  - 位置引数、キーワード引数、デフォルト引数、キーワード専用引数を扱う
- `variable_arguments.py`
  - `*args` と `**kwargs` を扱う
- `scope_examples.py`
  - スコープ、ローカル変数、グローバル変数を扱う
- `mutable_default_arguments.py`
  - ミュータブルなデフォルト引数の注意点と安全な書き方を扱う

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/05_functions_arguments_and_scope/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/05_functions_arguments_and_scope/main.py
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
2. `function_basics.py`
3. `argument_patterns.py`
4. `variable_arguments.py`
5. `scope_examples.py`
6. `mutable_default_arguments.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、関数の基本、引数の渡し方、可変長引数、スコープ、デフォルト引数の注意点の順番で読む。

## 6. 処理の流れ

Unit 05 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. 関数定義、戻り値、docstring のサンプルを実行する
5. 位置引数、キーワード引数、デフォルト引数のサンプルを実行する
6. `*args` と `**kwargs` のサンプルを実行する
7. スコープ、ローカル変数、グローバル変数のサンプルを実行する
8. ミュータブルなデフォルト引数のサンプルを実行する
9. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、関数の定義と呼び出し方を主題にしている。  
各ファイルの `run_...()` 関数は、テーマ別サンプルをまとめて実行するための入口として使う。

## 7. 注目ポイント

### 7-1. `def` と `return` で関数の入口と出口を作る

`function_basics.py` では、`def` で関数を定義し、`return` で結果を返す。

```python
def calculate_total(price: int, quantity: int) -> int:
    total = price * quantity
    return total
```

`def` は関数を定義するためのキーワードである。  
`calculate_total(1200, 3)` のように呼び出すと、関数内の処理が実行される。

`return` は、関数の結果を呼び出し元に返す。  
この例では、`price * quantity` の計算結果を `int` として返している。

### 7-2. 複数の値は tuple として返せる

`function_basics.py` では、氏名を分割して2つの値を返す。

```python
def split_full_name(full_name: str) -> tuple[str, str]:
    family_name, given_name = full_name.split()
    return family_name, given_name
```

`return family_name, given_name` は、複数の値を返しているように見える。  
Pythonでは、このような戻り値は tuple として扱える。

呼び出し側では、`family_name, given_name = ...` のように受け取れる。  
この書き方は、後のアンパックの学習にもつながる。

### 7-3. キーワード引数は呼び出し側の意味を明確にする

`argument_patterns.py` では、キーワード引数で値を渡す例を扱う。

```python
keyword_summary = create_user_summary(
    city="Osaka",
    age=21,
    name="Mio",
)
```

キーワード引数では、引数名を指定して値を渡す。  
そのため、順番に依存しにくく、どの値が何を表すかを読みやすい。

一方で、位置引数は順番で対応する。  
引数が増えた関数では、キーワード引数の方が意図を読み取りやすい場面がある。

### 7-4. `*args` は複数の位置引数をまとめて受け取る

`variable_arguments.py` では、任意個数の点数を受け取る。

```python
def total_scores(*scores: int) -> int:
    total = 0

    for score in scores:
        total += score

    return total
```

`*scores` は、複数の位置引数をまとめて受け取る。  
関数内では、`scores` は tuple のように扱える。

`total_scores(80, 90, 70)` のように、引数の個数が固定でない場合に使える。

### 7-5. `**kwargs` は複数のキーワード引数をまとめて受け取る

`variable_arguments.py` では、任意個数のキーワード引数を受け取る。

```python
def build_query(**params: str | int) -> str:
    parts = []

    for key, value in params.items():
        parts.append(f"{key}={value}")

    return "&".join(parts)
```

`**params` は、複数のキーワード引数を dict として受け取る。  
関数内では `params.items()` のように、通常の `dict` と同じ感覚で扱える。

キーワードの数が呼び出しごとに変わる場合に使える。

### 7-6. ローカル変数は関数の中だけで使う

`scope_examples.py` では、関数内で `message` を作成している。

```python
def build_local_message(name: str) -> str:
    message = f"Hello, {name}!"
    return message
```

`message` は関数内で作られたローカル変数である。  
そのため、関数の外側から直接参照することはできない。

関数は、必要な値を引数で受け取り、結果を `return` で返すようにすると読みやすくなる。

### 7-7. デフォルト引数は関数定義時に評価される

`mutable_default_arguments.py` では、ミュータブルなデフォルト引数の例を扱う。

```python
def append_bad(item: str, items: list[str] = []) -> list[str]:
    items.append(item)
    return items
```

この `items` の `list` は、関数を呼び出すたびに新しく作られるわけではない。  
関数定義時に一度だけ作られ、呼び出しをまたいで使われる。

そのため、1回目に追加した値が2回目にも残る。  
この挙動は意図しない共有につながりやすい。

## 8. 引っかかりやすい点

### 8-1. return がない関数は `None` を返す

今回のサンプルでは、明示的に `return` を使って値を返す関数を中心にしている。  
一方、Pythonでは `return` がない関数は暗黙的に `None` を返す。

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

値を呼び出し元で使いたい場合は、`return` を書く必要がある。  
`print()` で表示することと、`return` で値を返すことは別の処理である。

### 8-2. 位置引数は順番を間違えると意味が変わる

`argument_patterns.py` では、位置引数とキーワード引数を比較している。

```python
positional_summary = create_user_summary("Sora", 20, "Tokyo")

keyword_summary = create_user_summary(
    city="Osaka",
    age=21,
    name="Mio",
)
```

位置引数では、引数の順番によって値が対応する。  
順番を間違えると、コードとして実行できても意味がずれることがある。

キーワード引数は引数名を指定するため、呼び出し側の意図が読みやすい。

### 8-3. `*args` と `**kwargs` は何でも使えばよいものではない

`variable_arguments.py` では、可変長引数を使っている。

```python
def total_scores(*scores: int) -> int:
    total = 0

    for score in scores:
        total += score

    return total
```

`*args` や `**kwargs` は柔軟だが、使いすぎると関数が何を受け取るのか分かりにくくなる。  
引数の個数や名前が決まっている場合は、通常の引数として定義する方が読みやすい。

可変長引数は、呼び出し側の値の数が自然に変わる場面で使う。

### 8-4. グローバル変数の変更は慎重に扱う

`scope_examples.py` では、モジュール直下の `DEFAULT_LANGUAGE` を参照している。

```python
DEFAULT_LANGUAGE = "Python"


def build_language_message() -> str:
    return f"Learning {DEFAULT_LANGUAGE}"
```

関数内からグローバル変数を読むことはできる。  
ただし、関数内からグローバル変数を書き換える設計は、処理の見通しを悪くしやすい。

今回のサンプルでは、グローバル変数は読み取りだけにしている。  
値を変えたい場合は、引数として渡す方が分かりやすい場面が多い。

### 8-5. ミュータブルなデフォルト引数は共有される

`mutable_default_arguments.py` では、危険な書き方と安全な書き方を比較している。

```python
def append_good(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []

    items.append(item)
    return items
```

デフォルト値に `None` を置き、関数内で新しい `list` を作ると、呼び出しごとの共有を避けられる。  
この書き方は、ミュータブルなデフォルト引数の落とし穴を避ける定番の形である。

`list` や `dict` などをデフォルト値に直接置く場合は、呼び出しをまたいだ共有に注意する。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- `def` を使った関数定義を読める
- `return` で呼び出し元に値を返す流れを説明できる
- 複数戻り値が tuple として扱えることを説明できる
- 位置引数とキーワード引数の違いを説明できる
- デフォルト引数が省略時に使われることを説明できる
- `*args` が複数の位置引数をまとめて受け取ることを説明できる
- `**kwargs` が複数のキーワード引数をまとめて受け取ることを説明できる
- ローカル変数とグローバル変数の違いを説明できる
- docstring の役割を説明できる
- ミュータブルなデフォルト引数の注意点を説明できる
