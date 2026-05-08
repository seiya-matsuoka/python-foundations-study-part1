# 03. 基本コレクション

## 1. 学習対象

この単位では、Pythonで頻出する基本コレクションを扱う。

- `list`
- `tuple`
- `dict`
- `set`
- インデックス
- スライス
- 要素の追加・削除・更新
- 検索
- ソート
- 反復処理
- membership 判定
- ミュータブル / イミュータブル

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- `list` は順序を持ち、要素の追加・変更・削除ができる
- `tuple` は順序を持つが、作成後に要素を変更できない
- `dict` はキーと値の対応を持つ
- `set` は重複しない値の集まりを表す
- インデックスは順序を持つ値から特定位置の要素を取り出す
- スライスは順序を持つ値から範囲を取り出す
- `in` は membership 判定として使える
- `sorted()` は並び替えた新しい `list` を返す
- ミュータブルな値は作成後に変更できる
- イミュータブルな値は作成後に変更できない

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/03_core_collections/
  main.py
  list_operations.py
  tuple_operations.py
  dict_operations.py
  set_operations.py
  indexing_slicing_and_mutability.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 03 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `list_operations.py`
  - `list` の作成、参照、追加、更新、削除、検索、ソート、反復を扱う
- `tuple_operations.py`
  - `tuple` の作成、参照、検索、反復、変更できない性質を扱う
- `dict_operations.py`
  - `dict` のキーと値、参照、更新、削除、検索、反復を扱う
- `set_operations.py`
  - `set` の重複排除、追加、削除、membership 判定、集合演算を扱う
- `indexing_slicing_and_mutability.py`
  - インデックス、スライス、ミュータブル / イミュータブルを扱う

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/03_core_collections/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/03_core_collections/main.py
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
2. `list_operations.py`
3. `tuple_operations.py`
4. `dict_operations.py`
5. `set_operations.py`
6. `indexing_slicing_and_mutability.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、各テーマ別ファイルを読んで、基本コレクションの特徴と操作を確認する。

## 6. 処理の流れ

Unit 03 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. `list` のサンプルを実行する
5. `tuple` のサンプルを実行する
6. `dict` のサンプルを実行する
7. `set` のサンプルを実行する
8. インデックス、スライス、ミュータブル性のサンプルを実行する
9. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、コレクションごとの使い分けと基本操作を主題にしている。  
各ファイルの `run_...()` 関数は、テーマ別サンプルをまとめて実行するための入口として使う。

## 7. 注目ポイント

### 7-1. `list` は順序を持ち、作成後に変更できる

`list_operations.py` では、`list` の追加、更新、削除を扱う。

```python
fruits.append("grape")
fruits.insert(1, "kiwi")
fruits[0] = "melon"
```

`append` は末尾に要素を追加する。  
`insert` は指定した位置に要素を挿入する。  
`fruits[0] = "melon"` は、既存の要素を別の値に書き換えている。

このように、`list` はミュータブルなコレクションであり、作成後に中身を変えられる。

### 7-2. `sorted()` と `sort()` は結果の持ち方が違う

`list_operations.py` では、`sorted()` と `sort()` の違いを確認する。

```python
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)

numbers.sort()
```

`sorted(numbers)` は、並び替えた新しい `list` を返す。  
そのため、元の `numbers` はこの時点では変更されない。

一方で、`numbers.sort()` は `numbers` 自体を並び替える。  
同じソートでも、元の値を変更するかどうかが違う点に注目する。

### 7-3. `tuple` は順序を持つが変更できない

`tuple_operations.py` では、`tuple` の参照と新しい値の作成を扱う。

```python
point = (10, 20)
x = point[0]
y = point[1]

moved_point = (99, point[1])
```

`tuple` はインデックス参照できるため、`list` と似た感覚で読める。  
ただし、`point[0] = 99` のように既存の要素を書き換えることはできない。

値を変えたい場合は、`moved_point` のように新しい `tuple` を作る。

### 7-4. `dict` はキーと値の対応を持つ

`dict_operations.py` では、キーを使って値を取り出す例を扱う。

```python
student = {
    "name": "Sora",
    "age": 20,
    "language": "Python",
}

name = student["name"]
city = student.get("city", "unknown")
```

`student["name"]` は、`"name"` キーに対応する値を取得する。  
`get` を使うと、キーが存在しない場合の既定値を指定できる。

存在しない可能性があるキーを読むときは、`get` の方が扱いやすい場面がある。

### 7-5. `set` は重複しない値の集まりを表す

`set_operations.py` では、重複した値を含む `set` を作成する。

```python
duplicated_numbers = {1, 2, 2, 3, 3, 3}
```

この値は、実際には `{1, 2, 3}` として扱われる。  
`set` は同じ値を複数持たないため、重複を取り除きたい場面でも使える。

また、`set` は順序を前提にしない。  
順序が必要な場合は `sorted(skills)` のように明示的に並び替える。

### 7-6. スライスは範囲を取り出す

`indexing_slicing_and_mutability.py` では、複数のスライスを扱う。

```python
middle_letters = letters[1:4]
every_second_letter = letters[::2]
reversed_letters = letters[::-1]
```

`letters[1:4]` は、インデックス `1` から `4` の手前までを取り出す。  
`letters[::2]` は、2つおきに値を取り出す。  
`letters[::-1]` は、逆順の `list` を作る。

スライスの基本形は `start:stop:step` として読む。

## 8. 引っかかりやすい点

### 8-1. `list` と `tuple` は似ているが変更可否が違う

`list` と `tuple` は、どちらも順序を持つコレクションとして使える。

```python
fruits = ["apple", "banana", "orange"]
point = (10, 20)
```

どちらもインデックス参照ができるため、読み方が似ている。  
ただし、`list` はミュータブルで、`tuple` はイミュータブルである。

後から要素を変更したい場合は `list` を使う。  
作成後に値の組み合わせを変えたくない場合は `tuple` を使う。

### 8-2. 1要素の `tuple` にはカンマが必要

`tuple_operations.py` では、1要素の `tuple` と文字列を比較している。

```python
single_item_tuple = ("only-one",)
not_tuple = ("only-one")
```

`("only-one",)` は `tuple` になる。  
一方、`("only-one")` は括弧があっても文字列のままである。

1要素の `tuple` を作る場合は、カンマが必要になる。

### 8-3. `dict` の `in` はキーを見る

`dict_operations.py` では、`dict` に対する membership 判定を扱う。

```python
has_name_key = "name" in student
has_sora_value_as_key = "Sora" in student
```

`"name" in student` は、`"name"` というキーがあるかを見る。  
`"Sora"` は値としては存在するが、キーではないため `False` になる。

`dict` の `in` は値ではなくキーを見る、という点に注意する。

### 8-4. `set` はインデックスで取り出せない

`set` は順序を前提にしないコレクションである。

```python
skills = {"Python", "Java", "SQL"}
sorted_skills = sorted(skills)
```

`skills[0]` のように、インデックスで要素を取り出すことはできない。  
順番が必要な場合は、`sorted(skills)` のように `list` として並び替えて扱う。

`set` は「何番目の要素か」ではなく、「その値が含まれているか」を確認する用途に向く。

### 8-5. スライスコピーと代入は同じではない

`indexing_slicing_and_mutability.py` では、スライスコピーと代入の違いを扱う。

```python
copied_letters = letters[:]
copied_letters.append("z")

shared_letters = letters
shared_letters.append("f")
```

`copied_letters = letters[:]` は、新しい `list` を作る。  
そのため、`copied_letters` に要素を追加しても、元の `letters` は変わらない。

一方で、`shared_letters = letters` は、同じ `list` を指す。  
そのため、`shared_letters.append("f")` を行うと、`letters` 側にも変化が見える。

この内容は Unit 04「代入・参照・コピー」でさらに詳しく扱う。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- `list` の追加、更新、削除の基本を読める
- `sorted()` と `sort()` の違いを説明できる
- `tuple` が作成後に変更できないことを説明できる
- 1要素の `tuple` にカンマが必要なことを理解できる
- `dict` がキーと値の対応を持つことを説明できる
- `dict` の `in` がキーを確認することを説明できる
- `set` が重複しない値の集まりであることを説明できる
- `set` が順序を前提にしないことを説明できる
- インデックスとスライスの基本形を読める
- ミュータブル / イミュータブルの違いを説明できる
