# 04. 代入・参照・コピー

## 1. 学習対象

この単位では、Pythonにおける代入、参照、コピーの基本を扱う。

- 変数への代入の意味
- 参照の共有
- 再束縛
- `is` と参照の関係
- 浅いコピー
- 深いコピー
- `copy.copy`
- `copy.deepcopy`

## 2. この単位で扱う論点

この単位の主な論点は次の通り。

- 変数への代入は、値そのものを常にコピーする操作ではない
- 変数はオブジェクトに名前を付けるものとして考えると理解しやすい
- 再束縛は、変数名を別のオブジェクトに結び直す操作である
- 複数の変数が同じミュータブルな値を指すと、変更が共有される
- `==` は値として等しいかを確認する
- `is` は同じオブジェクトを指しているかを確認する
- 浅いコピーは外側のコレクションだけを新しく作る
- 深いコピーは内側のミュータブルな値も再帰的にコピーする

## 3. ファイル構成

この単位のファイル構成は次の通り。

```text
src/04_assignment_references_and_copying/
  main.py
  assignment_and_rebinding.py
  shared_references.py
  identity_and_equality.py
  shallow_copy_examples.py
  deep_copy_examples.py
```

各ファイルの役割は次の通り。

- `main.py`
  - Unit 04 の実行入口
  - 各テーマ別ファイルの関数を順番に呼び出す
- `assignment_and_rebinding.py`
  - 変数への代入、再束縛、ミュータブルな値の変更を扱う
- `shared_references.py`
  - 同じオブジェクトを複数の変数から参照する例を扱う
- `identity_and_equality.py`
  - `is` と `==` の違い、`None` 判定を扱う
- `shallow_copy_examples.py`
  - スライス、`list()`、`copy.copy()`、`dict.copy()` による浅いコピーを扱う
- `deep_copy_examples.py`
  - `copy.deepcopy()` による深いコピーと浅いコピーの違いを扱う

## 4. 実行方法

リポジトリ直下で仮想環境を有効化してから実行する。

PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
python src/04_assignment_references_and_copying/main.py
```

Git Bash の場合:

```bash
source .venv/Scripts/activate
python src/04_assignment_references_and_copying/main.py
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
2. `assignment_and_rebinding.py`
3. `shared_references.py`
4. `identity_and_equality.py`
5. `shallow_copy_examples.py`
6. `deep_copy_examples.py`

最初に `main.py` を読むことで、この単位全体の実行順序を把握できる。  
その後、代入と再束縛、参照の共有、同一性、浅いコピー、深いコピーの順番で読む。

## 6. 処理の流れ

Unit 04 全体の処理の流れは次の通り。

1. `main.py` が実行される
2. `main()` が呼び出される
3. 表示用の見出しを出す
4. 代入と再束縛のサンプルを実行する
5. 参照の共有のサンプルを実行する
6. `is` と `==` の違いを確認する
7. 浅いコピーのサンプルを実行する
8. 深いコピーのサンプルを実行する
9. 各ファイル内の `assert` により、軽い期待値確認を行う

この単位では、変数名とオブジェクトの関係を主題にしている。  
各ファイルの `run_...()` 関数は、テーマ別サンプルをまとめて実行するための入口として使う。

## 7. 注目ポイント

### 7-1. 再束縛は既存の値の変更ではない

`assignment_and_rebinding.py` では、文字列を使って再束縛を確認する。

```python
language = "Python"
same_language = language

same_language = "Java"
```

最初の `same_language = language` では、`same_language` は `language` と同じ文字列を指す。  
その後の `same_language = "Java"` は、`same_language` という名前を別の文字列に結び直している。

この操作は、`language` の値そのものを変更しているわけではない。  
そのため、再束縛後も `language` は `"Python"` のままとなる。

### 7-2. ミュータブルな値は参照共有の影響が見えやすい

`assignment_and_rebinding.py` では、`list` に対する変更を扱う。

```python
scores = [80, 90]
same_scores = scores

same_scores.append(100)
```

`scores` と `same_scores` は同じ `list` を指している。  
そのため、`same_scores.append(100)` を行うと、`scores` から見ても値が追加されている。

代入は自動的に `list` の中身をコピーしない。  
この感覚は、Pythonのコレクションを扱う上で重要となる。

### 7-3. `is` と `==` は確認している内容が違う

`identity_and_equality.py` では、同じ値を持つ2つの `list` を比較する。

```python
first_numbers = [1, 2, 3]
second_numbers = [1, 2, 3]
shared_numbers = first_numbers
```

`first_numbers == second_numbers` は `True` になる。  
これは、2つの `list` が値として等しいためである。

一方、`first_numbers is second_numbers` は `False` になる。  
別々に作成した `list` なので、同じオブジェクトではないためである。

### 7-4. 浅いコピーは内側の値を共有することがある

`shallow_copy_examples.py` では、ネストした `list` の浅いコピーを扱う。

```python
original_scores = [["Sora", 80], ["Mio", 90]]

copied_by_slice = original_scores[:]
copied_by_slice[0][1] = 100
```

`original_scores[:]` は、外側の `list` を新しく作る。  
ただし、内側の `["Sora", 80]` まではコピーしない。

そのため、`copied_by_slice[0][1] = 100` を行うと、元の `original_scores` 側にも変化が見える。

### 7-5. 深いコピーはネストした値もコピーする

`deep_copy_examples.py` では、`copy.deepcopy()` を使う。

```python
copied_user = copy.deepcopy(original_user)

copied_user["scores"].append(100)
copied_user["profile"]["level"] = "intermediate"
```

`copy.deepcopy()` は、外側の `dict` だけでなく、内側の `list` や `dict` もコピーする。  
そのため、コピー側の `scores` や `profile` を変更しても、元の値には影響しない。

ネストしたデータを安全に複製したい場合は、浅いコピーとの違いを意識する必要がある。

## 8. 引っかかりやすい点

### 8-1. 代入は常にコピーではない

`shared_references.py` では、`list` を別の変数に代入する例を扱う。

```python
users = ["Sora", "Mio"]
active_users = users

active_users.append("Ren")
```

`active_users = users` は、`users` の中身をコピーしているわけではない。  
`active_users` と `users` は、同じ `list` を指している。

そのため、`active_users.append("Ren")` を行うと、`users` 側から見ても `"Ren"` が追加されている。

### 8-2. `is` を値の比較に使わない

`identity_and_equality.py` では、値の比較と同一性の比較を分けている。

```python
first_numbers = [1, 2, 3]
second_numbers = [1, 2, 3]

first_numbers == second_numbers
first_numbers is second_numbers
```

`==` は値として等しいかを見る。  
`is` は同じオブジェクトを指しているかを見る。

値が同じかどうかを確認したい場合は、基本的に `==` を使う。  
`is` は `None` 判定や同じオブジェクトかどうかを確認したい場面で使う。

### 8-3. 浅いコピーはネストした値まで独立しない

`shallow_copy_examples.py` では、浅いコピー後に内側の `list` を変更している。

```python
copied_by_slice = original_scores[:]
copied_by_slice[0][1] = 100
```

`copied_by_slice` は外側の `list` としては `original_scores` とは別物である。  
しかし、内側の `list` は共有されている。

そのため、ネストしたデータを扱うときは、浅いコピーだけで十分かを確認する必要がある。

### 8-4. `dict.copy()` も浅いコピーである

`shallow_copy_examples.py` では、`dict.copy()` の例も扱う。

```python
original_user = {
    "name": "Sora",
    "skills": ["Python", "SQL"],
}
copied_user = original_user.copy()

copied_user["skills"].append("Git")
```

`original_user.copy()` は、新しい `dict` を作る。  
ただし、値として入っている `skills` の `list` は共有されたままとなる。

そのため、`copied_user["skills"].append("Git")` を行うと、`original_user` の `skills` にも `"Git"` が追加される。

### 8-5. 深いコピーは万能ではなく、必要な場面で使う

`deep_copy_examples.py` では、浅いコピーと深いコピーの違いを比較している。

```python
copied_user = copy.deepcopy(original_user)
shallow_user = copy.copy(original_user)
```

`copy.deepcopy()` は、ネストした値もコピーするため安全に見える。  
ただし、データが大きい場合や複雑なオブジェクトを含む場合は、処理コストや意図しない挙動にも注意が必要となる。

今回の単位では、まず浅いコピーと深いコピーの違いを読めることを重視する。

## 9. 確認観点

この単位を読んだ後、次の内容を確認する。

- 変数への代入が常にコピーではないことを説明できる
- 再束縛とミュータブルな値の変更の違いを説明できる
- 複数の変数が同じ `list` を指す例を読める
- `==` と `is` の違いを説明できる
- `None` 判定で `is None` を使う理由を説明できる
- 浅いコピーが外側だけを新しく作ることを説明できる
- ネストした値では浅いコピーの影響が残ることを説明できる
- `copy.copy()` と `dict.copy()` が浅いコピーであることを説明できる
- `copy.deepcopy()` がネストした値もコピーすることを説明できる
