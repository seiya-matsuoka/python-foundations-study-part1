"""リスト内包表記、辞書内包表記、集合内包表記を確認するサンプル。"""


def run_comprehension_examples() -> None:
    """内包表記によるコレクション生成を確認する。"""

    # リスト内包表記は、for を使った list 生成を短く書くための構文。
    # 単純な変換や絞り込みでは、通常の for より意図がまとまりやすい。
    numbers = [1, 2, 3, 4, 5]

    squares = [number * number for number in numbers]
    even_numbers = [number for number in numbers if number % 2 == 0]

    print(f"squares: {squares}")
    print(f"even_numbers: {even_numbers}")

    # 通常の for で同じ処理を書くと、結果用の list を先に用意する。
    # 内包表記では「何から何を作るか」を1行にまとめられる。
    doubled_numbers = []

    for number in numbers:
        doubled_numbers.append(number * 2)

    doubled_numbers_by_comprehension = [number * 2 for number in numbers]

    print(f"for で作った doubled_numbers: {doubled_numbers}")
    print(f"内包表記で作った doubled_numbers: {doubled_numbers_by_comprehension}")

    # 辞書内包表記は、キーと値を組み立てながら dict を作る。
    # ここでは名前をキー、文字数を値にしている。
    names = ["Sora", "Mio", "Ren"]
    name_lengths = {name: len(name) for name in names}

    print(f"name_lengths: {name_lengths}")

    # 集合内包表記は、重複しない値の集まりを作る。
    # ここでは小文字化したカテゴリ名の set を作る。
    categories = ["Book", "book", "Music", "music", "Game"]
    normalized_categories = {category.lower() for category in categories}

    print(f"normalized_categories: {normalized_categories}")

    # 内包表記の中に if を入れると、条件を満たす値だけを使える。
    # 複雑にしすぎると読みにくくなるため、短い処理に向く。
    long_names = [name for name in names if len(name) >= 4]
    print(f"long_names: {long_names}")

    assert squares == [1, 4, 9, 16, 25]
    assert even_numbers == [2, 4]
    assert doubled_numbers == [2, 4, 6, 8, 10]
    assert doubled_numbers_by_comprehension == [2, 4, 6, 8, 10]
    assert name_lengths == {"Sora": 4, "Mio": 3, "Ren": 3}
    assert normalized_categories == {"book", "music", "game"}
    assert long_names == ["Sora"]
