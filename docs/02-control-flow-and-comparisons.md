# 02. 条件分岐・繰り返し・比較

## 1. 学習対象

この単位では、Pythonの条件判定、繰り返し、比較の基本を扱う。

- `if / elif / else`
- `for`
- `while`
- `break`
- `continue`
- `range`
- 比較演算子
- 論理演算子
- truthy / falsy
- `is` と `==`

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- Pythonではインデントでブロックを表す
- `elif` は Java の `else if` に近い役割を持つ
- `for` は反復可能な値から順番に要素を取り出す
- `range()` は数値の連続を扱うときによく使う
- `while` は条件が `True` の間だけ繰り返す
- `break` はループを途中で終了する
- `continue` は現在の回をスキップして次の回へ進む
- 比較演算子は `True` または `False` を返す
- `and` / `or` / `not` で条件を組み合わせられる
- Pythonでは空文字、空リスト、`0`、`None` などが falsy になる
- `==` は値の等しさ、`is` は同じオブジェクトかどうかを見る

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/02_control_flow_and_comparisons/
  main.py
  conditionals.py
  loops_and_range.py
  break_continue_examples.py
  comparisons_and_logic.py
  truthy_falsy_and_identity.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 02 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `conditionals.py`
  - `if / elif / else` の基本を扱う
- `loops_and_range.py`
  - `for`、`while`、`range` の基本を扱う
- `break_continue_examples.py`
  - `break` と `continue` によるループ制御を扱う
- `comparisons_and_logic.py`
  - 比較演算子と論理演算子を扱う
- `truthy_falsy_and_identity.py`
  - truthy / falsy、`is` と `==` の違いを扱う

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/02_control_flow_and_comparisons/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/02_control_flow_and_comparisons/main.py
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
2. `conditionals.py`
3. `loops_and_range.py`
4. `break_continue_examples.py`
5. `comparisons_and_logic.py`
6. `truthy_falsy_and_identity.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、各テーマ別ファイルを読んで、条件分岐、繰り返し、比較の基本を確認する。

## 6. 処理の流れ

Unit 02 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. `if / elif / else` のサンプルを実行する
5. `for`、`while`、`range` のサンプルを実行する
6. `break` と `continue` のサンプルを実行する
7. 比較演算子と論理演算子のサンプルを実行する
8. truthy / falsy、`is` と `==` のサンプルを実行する
9. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、関数設計そのものを主題にはしていない。  
各ファイルの `run_...()` 関数は、テーマ別サンプルをまとめて実行するための入口として使う。

## 7. 注目ポイント

### 7-1. `if / elif / else` は上から順に評価される

`conditionals.py` の `describe_temperature()` では、`if / elif / else` を使って気温を分類する。

```python
if temperature >= 30:
    result = "hot"
elif temperature >= 20:
    result = "warm"
elif temperature >= 10:
    result = "cool"
else:
    result = "cold"
```

複数の条件に当てはまりそうな値でも、最初に `True` になった分岐だけが実行される。  
たとえば `35` は `temperature >= 30` に当てはまるため、その下の `elif` は評価されない。

### 7-2. Pythonではインデントがブロックを表す

Pythonでは `{}` ではなく、インデントで処理のまとまりを表す。  
`if`、`for`、`while` の後にあるインデントされた行が、その制御構文の中身となる。

```python
if has_ticket:
    print("チケットがあるため入場できる")
```

インデントがずれると、処理の所属先が変わったり、構文エラーになったりする。

### 7-3. `range()` の終了値は含まれない

`loops_and_range.py` では、`range(1, 6)` を使って `1` から `5` までを作る。

```python
for number in range(1, 6):
    one_to_five.append(number)
```

`range(start, stop)` の `stop` は含まれない。  
そのため、`range(1, 6)` の結果は `[1, 2, 3, 4, 5]` となる。

### 7-4. `break` と `continue` はループの流れを変える

`break_continue_examples.py` では、最初に見つかった偶数を記録した時点で `break` している。

```python
for number in numbers:
    if number % 2 == 0:
        first_even = number
        break
```

`break` はループ全体を終了する。  
一方で `continue` は、その回の残りの処理をスキップして次の回へ進む。

### 7-5. 比較演算子は真偽値を返す

`comparisons_and_logic.py` では、比較結果を変数に入れている。

```python
is_adult = age >= minimum_age
is_not_thirty = age != 30
```

比較演算子の結果は `True` または `False` となる。  
そのため、比較結果をそのまま `if` の条件として使うこともできる。

### 7-6. truthy / falsy はPythonでよく使う感覚

`truthy_falsy_and_identity.py` では、`bool()` を使って値の真偽値評価を確認する。

```python
values = ["Python", "", [1, 2], [], 1, 0, None]

for value in values:
    print(f"value={value!r}, bool(value)={bool(value)}")
```

空文字、空リスト、`0`、`None` は falsy な値として扱われる。  
そのため、`if items:` のように「要素があるか」を直接表す書き方がよく使われる。

### 7-7. `==` と `is` は目的が違う

`truthy_falsy_and_identity.py` では、同じ値を持つ別リストを比較している。

```python
left = [1, 2, 3]
right = [1, 2, 3]
same_reference = left

left == right
left is right
left is same_reference
```

`==` は値として等しいかを比較する。  
`is` は同じオブジェクトそのものを参照しているかを比較する。

## 8. 引っかかりやすい点

### 8-1. `elif` を使うべき場面で `if` を並べすぎない

複数条件から一つだけを選びたい場合は、`if / elif / else` が自然な形となる。  
`return` で早期終了する書き方もあるが、最初の学習では分岐構造が見える形の方が読みやすい。

```python
if temperature >= 30:
    result = "hot"
elif temperature >= 20:
    result = "warm"
else:
    result = "cold"
```

この単位では、`elif` の説明とコードの形が一致するようにしている。

### 8-2. `range()` の終了値を含むと勘違いしやすい

`range(1, 6)` は `1` から `6` までではなく、`1` から `5` までとなる。  
この「終了値を含まない」という考え方は、スライスにもつながる重要な感覚となる。

### 8-3. `while` は更新処理を忘れると無限ループになる

`while count < 3:` のような形では、ループ内で `count` を更新する必要がある。

```python
while count < 3:
    counted_values.append(count)
    count += 1
```

`count += 1` を忘れると、条件がずっと `True` のままになり、ループが終わらない。

### 8-4. `continue` の後ろの処理は実行されない

`continue` が実行されると、その回の残りの処理はスキップされる。  
次の例では、負の値の場合は `valid_scores.append(score)` まで進まない。

```python
for score in raw_scores:
    if score < 0:
        continue

    valid_scores.append(score)
```

### 8-5. truthy / falsy は便利だが、意味を読み取る必要がある

`if items:` は「items に要素があるか」を表す定番の書き方。  
ただし、初見では `items` 自体が真偽値に見えないため、慣れるまでは読み取りに注意する。

```python
if items:
    print("items には要素がある")
```

### 8-6. `is` を値の比較に使わない

`is` は同じオブジェクトを参照しているかを確認するための演算子。  
通常の値の比較では `==` を使う。

```python
left == right  # 値が等しいか
left is right  # 同じオブジェクトか
```

`None` との比較では、例外的に `is None` が定番の書き方となる。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- `if / elif / else` の基本形を読める
- Pythonではインデントでブロックを表すことを理解できる
- `for` でリストや `range()` の値を順番に処理できることを読める
- `range()` の終了値が含まれないことを理解できる
- `while` の条件と更新処理の関係を読める
- `break` と `continue` の違いを説明できる
- 比較演算子の結果が `True` / `False` になることを理解できる
- `and` / `or` / `not` の基本的な意味を読める
- truthy / falsy の基本例を説明できる
- `==` と `is` の違いを説明できる
- `None` 判定では `is None` を使うことを理解できる
