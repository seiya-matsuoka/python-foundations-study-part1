"""ジェネレータ式を確認するサンプル。"""


def run_generator_expression_examples() -> None:
    """ジェネレータ式とリスト内包表記の違いを確認する。"""

    numbers = [1, 2, 3, 4, 5]

    # リスト内包表記は、その場で list を作る。
    # 作られた list は何度でも繰り返し参照できる。
    squares_list = [number * number for number in numbers]
    print(f"squares_list: {squares_list}")

    # ジェネレータ式は、必要になったタイミングで値を取り出す。
    # list そのものを先に作るわけではない。
    squares_generator = (number * number for number in numbers)
    print(f"squares_generator: {squares_generator}")

    # next を使うと、ジェネレータから値を1つずつ取り出せる。
    first_square = next(squares_generator)
    second_square = next(squares_generator)

    print(f"first_square: {first_square}")
    print(f"second_square: {second_square}")

    # 残りの値を list にすると、まだ取り出していない値だけが得られる。
    remaining_squares = list(squares_generator)
    print(f"remaining_squares: {remaining_squares}")

    # sum のような関数には、ジェネレータ式をそのまま渡せる。
    # 全要素を list にしてから渡すより、途中の list を作らずに済む。
    total_even_square = sum(number * number for number in numbers if number % 2 == 0)
    print(f"total_even_square: {total_even_square}")

    # ジェネレータは一度取り出した値を戻せない。
    # もう一度使いたい場合は、ジェネレータ式を作り直す。
    words = ["Python", "Java", "SQL"]
    upper_words_generator = (word.upper() for word in words)

    upper_words = list(upper_words_generator)
    empty_after_consumed = list(upper_words_generator)

    print(f"upper_words: {upper_words}")
    print(f"empty_after_consumed: {empty_after_consumed}")

    assert squares_list == [1, 4, 9, 16, 25]
    assert first_square == 1
    assert second_square == 4
    assert remaining_squares == [9, 16, 25]
    assert total_even_square == 20
    assert upper_words == ["PYTHON", "JAVA", "SQL"]
    assert empty_after_consumed == []
