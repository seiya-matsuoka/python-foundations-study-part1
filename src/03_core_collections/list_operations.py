"""list の基本操作を確認するサンプル。"""


def run_list_operations() -> None:
    """list の作成、参照、更新、削除、検索、ソート、反復を確認する。"""

    # list は、順序を持つコレクション。
    # 同じ値を複数入れられ、作成後に要素を変更できる。
    fruits = ["apple", "banana", "orange"]
    print(f"最初の fruits: {fruits}")

    # インデックスは 0 から始まる。
    # -1 を使うと末尾の要素を参照できる。
    first_fruit = fruits[0]
    last_fruit = fruits[-1]

    print(f"先頭の要素: {first_fruit}")
    print(f"末尾の要素: {last_fruit}")

    # append は末尾に要素を追加する。
    # insert は指定した位置に要素を挿入する。
    fruits.append("grape")
    fruits.insert(1, "kiwi")
    print(f"追加後の fruits: {fruits}")

    # list はミュータブル。
    # インデックスを指定して、既存の要素を書き換えられる。
    fruits[0] = "melon"
    print(f"先頭を書き換えた fruits: {fruits}")

    # pop は要素を取り出しながら削除する。
    # remove は指定した値に一致する最初の要素を削除する。
    removed_fruit = fruits.pop()
    fruits.remove("banana")

    print(f"pop で取り出した要素: {removed_fruit}")
    print(f"削除後の fruits: {fruits}")

    # in は membership 判定。
    # 値が含まれるかどうかを True / False で返す。
    has_orange = "orange" in fruits
    has_banana = "banana" in fruits

    print(f"orange を含むか: {has_orange}")
    print(f"banana を含むか: {has_banana}")

    # sorted は並び替えた新しい list を返す。
    # 元の list は変更されない。
    numbers = [3, 1, 4, 1, 5]
    sorted_numbers = sorted(numbers)

    print(f"元の numbers: {numbers}")
    print(f"sorted の結果: {sorted_numbers}")

    # sort は list 自身を並び替える。
    # 元の list が変更される点に注意する。
    numbers.sort()
    print(f"sort 後の numbers: {numbers}")

    # for を使うと、list の要素を先頭から順番に処理できる。
    upper_fruits = []

    for fruit in fruits:
        upper_fruits.append(fruit.upper())

    print(f"大文字に変換した fruits: {upper_fruits}")

    assert first_fruit == "apple"
    assert last_fruit == "orange"
    assert removed_fruit == "grape"
    assert fruits == ["melon", "kiwi", "orange"]
    assert has_orange is True
    assert has_banana is False
    assert sorted_numbers == [1, 1, 3, 4, 5]
    assert numbers == [1, 1, 3, 4, 5]
    assert upper_fruits == ["MELON", "KIWI", "ORANGE"]
