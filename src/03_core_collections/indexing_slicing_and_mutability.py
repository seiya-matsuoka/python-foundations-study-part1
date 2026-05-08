"""インデックス、スライス、ミュータブル性を確認するサンプル。"""


def run_indexing_slicing_and_mutability() -> None:
    """参照位置、範囲取得、変更できる値とできない値を確認する。"""

    # list、tuple、文字列のように順序を持つ値は、
    # インデックスで位置を指定できる。
    letters = ["a", "b", "c", "d", "e"]
    word = "Python"
    point = (10, 20, 30)

    first_letter = letters[0]
    last_letter = letters[-1]
    first_char = word[0]
    last_point = point[-1]

    print(f"letters の先頭: {first_letter}")
    print(f"letters の末尾: {last_letter}")
    print(f"word の先頭文字: {first_char}")
    print(f"point の末尾: {last_point}")

    # スライスは start:stop:step の形で範囲を取り出す。
    # stop の位置にある要素は含まれない。
    middle_letters = letters[1:4]
    every_second_letter = letters[::2]
    reversed_letters = letters[::-1]

    print(f"letters[1:4]: {middle_letters}")
    print(f"letters[::2]: {every_second_letter}")
    print(f"letters[::-1]: {reversed_letters}")

    # list はミュータブルなので、要素や一部範囲を変更できる。
    mutable_numbers = [1, 2, 3, 4]
    mutable_numbers[0] = 100
    mutable_numbers[1:3] = [200, 300]

    print(f"変更後の mutable_numbers: {mutable_numbers}")

    # 文字列や tuple はイミュータブル。
    # 既存の値を直接変更するのではなく、新しい値を作る。
    new_word = "J" + word[1:]
    moved_point = (99,) + point[1:]

    print(f"新しく作った文字列: {new_word}")
    print(f"新しく作った tuple: {moved_point}")

    # list のスライスは、新しい list を作る。
    # コピー側を変更しても、元の list は変わらない。
    copied_letters = letters[:]
    copied_letters.append("z")

    print(f"元の letters: {letters}")
    print(f"コピーした letters: {copied_letters}")

    # 変数への代入は、値そのもののコピーとは限らない。
    # list のようなミュータブルな値では、同じ list を指すことがある。
    shared_letters = letters
    shared_letters.append("f")

    print(f"共有後の letters: {letters}")
    print(f"共有後の shared_letters: {shared_letters}")

    assert first_letter == "a"
    assert last_letter == "e"
    assert first_char == "P"
    assert last_point == 30
    assert middle_letters == ["b", "c", "d"]
    assert every_second_letter == ["a", "c", "e"]
    assert reversed_letters == ["e", "d", "c", "b", "a"]
    assert mutable_numbers == [100, 200, 300, 4]
    assert new_word == "Jython"
    assert moved_point == (99, 20, 30)
    assert copied_letters == ["a", "b", "c", "d", "e", "z"]
    assert letters == ["a", "b", "c", "d", "e", "f"]
    assert shared_letters is letters
