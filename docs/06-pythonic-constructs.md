# 06. Pythonらしい書き方

## 1. 学習対象

この単位では、Pythonらしい簡潔な書き方と定番のコレクション処理を扱う。

- リスト内包表記
- 辞書内包表記
- 集合内包表記
- ジェネレータ式
- `enumerate`
- `zip`
- `sorted`
- `reversed`
- `any`
- `all`
- パック / アンパック
- 複数代入
- ラムダ式

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- 内包表記を使うと、コレクション生成を簡潔に書ける
- リスト内包表記は、変換や絞り込みを1行にまとめられる
- 辞書内包表記は、キーと値を組み立てながら `dict` を作れる
- 集合内包表記は、重複しない値の集まりを作れる
- ジェネレータ式は、必要なタイミングで値を取り出す
- `enumerate` は、インデックスと要素を同時に取り出せる
- `zip` は、複数のコレクションを同時に処理できる
- `sorted` と `reversed` は、並び順を扱うときに使う
- `any` と `all` は、条件を満たす値の有無や全体判定に使う
- パック / アンパックを使うと、複数の値をまとめたり分解したりできる
- ラムダ式は、短い無名関数をその場で渡したいときに使う

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/06_pythonic_constructs/
  main.py
  comprehension_examples.py
  generator_expression_examples.py
  iteration_helper_functions.py
  packing_and_unpacking.py
  lambda_examples.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 06 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `comprehension_examples.py`
  - リスト内包表記、辞書内包表記、集合内包表記を扱う
- `generator_expression_examples.py`
  - ジェネレータ式とリスト内包表記の違いを扱う
- `iteration_helper_functions.py`
  - `enumerate`、`zip`、`sorted`、`reversed`、`any`、`all` を扱う
- `packing_and_unpacking.py`
  - パック、アンパック、複数代入、引数展開を扱う
- `lambda_examples.py`
  - ラムダ式の基本的な利用場面を扱う

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/06_pythonic_constructs/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/06_pythonic_constructs/main.py
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
2. `comprehension_examples.py`
3. `generator_expression_examples.py`
4. `iteration_helper_functions.py`
5. `packing_and_unpacking.py`
6. `lambda_examples.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、内包表記、ジェネレータ式、便利な組み込み関数、アンパック、ラムダ式の順番で読む。

## 6. 処理の流れ

Unit 06 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. 内包表記のサンプルを実行する
5. ジェネレータ式のサンプルを実行する
6. `enumerate`、`zip`、`sorted`、`reversed`、`any`、`all` のサンプルを実行する
7. パック、アンパック、複数代入のサンプルを実行する
8. ラムダ式のサンプルを実行する
9. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、Pythonでよく使われる簡潔な書き方を主題にしている。  
各ファイルの `run_...()` 関数は、テーマ別サンプルをまとめて実行するための入口として使う。

## 7. 注目ポイント

### 7-1. リスト内包表記は変換と絞り込みを短く書ける

`comprehension_examples.py` では、リスト内包表記を使って値を変換している。

```python
squares = [number * number for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]
```

`squares` は、`numbers` の各値を2乗した `list` を作る。  
`even_numbers` は、条件を満たす値だけを集める。

単純な変換や絞り込みでは、内包表記を使うと「何から何を作るか」がまとまりやすい。

### 7-2. 辞書内包表記と集合内包表記も使える

`comprehension_examples.py` では、`dict` と `set` も内包表記で作成している。

```python
name_lengths = {name: len(name) for name in names}
normalized_categories = {category.lower() for category in categories}
```

`name_lengths` は、名前をキー、文字数を値にした `dict` である。  
`normalized_categories` は、小文字化したカテゴリ名を集めた `set` である。

`list` だけではなく、`dict` や `set` も内包表記で作れる点に注目する。

### 7-3. ジェネレータ式は必要なタイミングで値を取り出す

`generator_expression_examples.py` では、ジェネレータ式を作成している。

```python
squares_generator = (number * number for number in numbers)

first_square = next(squares_generator)
second_square = next(squares_generator)
```

ジェネレータ式は、`list` を先に作るのではなく、値を必要なタイミングで取り出す。  
`next()` を呼ぶたびに、次の値が計算される。

一度取り出した値は戻らないため、同じジェネレータを何度も再利用する前提では扱わない。

### 7-4. `enumerate` と `zip` は反復処理を読みやすくする

`iteration_helper_functions.py` では、`enumerate` と `zip` を使っている。

```python
for index, name in enumerate(names, start=1):
    indexed_names.append(f"{index}: {name}")

for name, score in zip(names, scores, strict=True):
    score_rows.append(f"{name}={score}")
```

`enumerate` は、インデックスと要素を同時に取り出す。  
`zip` は、複数のコレクションから対応する値を同時に取り出す。

どちらも、`range(len(...))` や手動のインデックス管理を減らせる。

### 7-5. `any` と `all` は条件判定を短く書ける

`iteration_helper_functions.py` では、`any` と `all` を使っている。

```python
has_high_score = any(score >= 90 for score in scores)
all_passed = all(score >= 60 for score in scores)
```

`any` は、1つでも条件を満たす値があれば `True` を返す。  
`all` は、すべての値が条件を満たす場合に `True` を返す。

条件式とジェネレータ式を組み合わせると、存在確認や全体判定を簡潔に書ける。

### 7-6. アンパックは複数の値を分解して受け取る

`packing_and_unpacking.py` では、tuple のアンパックを扱っている。

```python
packed_profile = "Mio", 21, "Java"
name, age, language = packed_profile
```

`packed_profile` は、複数の値をまとめた tuple として扱える。  
`name, age, language = packed_profile` は、その tuple を分解して変数に受け取る。

複数戻り値や `for` の中でもよく使う考え方である。

### 7-7. ラムダ式は短い関数をその場で渡す

`lambda_examples.py` では、`sorted` の `key` にラムダ式を渡している。

```python
sorted_by_score = sorted(users, key=lambda user: user["score"])
```

`lambda user: user["score"]` は、ユーザー情報から `score` を取り出す短い関数である。  
このように、その場だけで使う短い関数を渡したい場合にラムダ式を使える。

複雑な処理や再利用したい処理は、`def` で名前を付けた方が読みやすい。

## 8. 引っかかりやすい点

### 8-1. 内包表記は短ければ常に良いわけではない

`comprehension_examples.py` では、内包表記と通常の `for` の両方を扱っている。

```python
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

doubled_numbers_by_comprehension = [number * 2 for number in numbers]
```

単純な変換では、内包表記の方がすっきり書ける。  
ただし、処理が複雑になりすぎると、通常の `for` の方が読みやすい場合もある。

短く書くことより、処理の意図が読み取りやすいことを優先する。

### 8-2. ジェネレータは一度消費すると空になる

`generator_expression_examples.py` では、同じジェネレータを2回 `list` にしている。

```python
upper_words_generator = (word.upper() for word in words)

upper_words = list(upper_words_generator)
empty_after_consumed = list(upper_words_generator)
```

1回目の `list(upper_words_generator)` で、ジェネレータの値はすべて取り出される。  
そのため、2回目の `list(upper_words_generator)` は空の `list` になる。

もう一度使いたい場合は、ジェネレータ式を作り直す必要がある。

### 8-3. `zip` は短い方に合わせて止まる

`iteration_helper_functions.py` では、同じ長さの `names` と `scores` を使っている。

```python
for name, score in zip(names, scores, strict=True):
    score_rows.append(f"{name}={score}")
```

通常の `zip` は、複数のコレクションを同時に進める。  
長さが違う場合は、短い方が終わった時点で止まる。

今回のコードでは `strict=True` を付けて、長さの違いをエラーとして検出できる形にしている。

### 8-4. `reversed` は元の list を変更しない

`iteration_helper_functions.py` では、`reversed` の結果を `list` にしている。

```python
reversed_names = list(reversed(names))
```

`reversed(names)` は、逆順に取り出すためのイテレータを返す。  
元の `names` 自体を並び替えるわけではない。

元の `list` を変更したい場合は、別の方法が必要になる。

### 8-5. `*` と `**` は使う場所で意味が変わる

`packing_and_unpacking.py` では、`*` と `**` による引数展開を扱っている。

```python
formatted_user = format_user(*user_values)
formatted_user_by_dict = format_user(**user_options)
```

`*user_values` は、`tuple` の値を位置引数として展開する。  
`**user_options` は、`dict` の値をキーワード引数として展開する。

関数定義側の `*args` / `**kwargs` と、呼び出し側の `*` / `**` は関連しているが、読む位置によって役割が変わる。

### 8-6. ラムダ式は複雑な処理には向かない

`lambda_examples.py` では、短い並び替え基準としてラムダ式を使っている。

```python
sorted_by_score = sorted(users, key=lambda user: user["score"])
```

このように、短い処理をその場で渡す場合はラムダ式が読みやすい。  
一方で、条件分岐や複数行の処理が必要な場合は、`def` で関数として定義した方がよい。

ラムダ式は、短く書ける場面だけで使うと読みやすさを保ちやすい。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- リスト内包表記で変換と絞り込みを書ける
- 辞書内包表記でキーと値を組み立てられる
- 集合内包表記で重複しない値の集まりを作れる
- 内包表記と通常の `for` の使い分けを説明できる
- ジェネレータ式が必要なタイミングで値を取り出すことを説明できる
- ジェネレータが一度消費されると空になることを説明できる
- `enumerate` と `zip` の基本的な使い方を説明できる
- `sorted`、`reversed`、`any`、`all` の用途を説明できる
- パック / アンパックと複数代入を読める
- ラムダ式の基本的な利用場面を説明できる
