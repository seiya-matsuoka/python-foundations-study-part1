"""enumerate、zip、sorted、reversed、any、all を確認するサンプル。"""


def run_iteration_helper_functions() -> None:
    """反復処理でよく使う組み込み関数を確認する。"""

    names = ["Sora", "Mio", "Ren"]

    # enumerate は、インデックスと要素を同時に取り出す。
    # range(len(names)) より、何をしているかが読みやすい。
    indexed_names = []

    for index, name in enumerate(names, start=1):
        indexed_names.append(f"{index}: {name}")

    print(f"indexed_names: {indexed_names}")

    # zip は、複数のコレクションを同時に1つずつ取り出す。
    # strict=True を付けると、長さが違う場合にエラーとして検出できる。
    scores = [80, 95, 70]
    score_rows = []

    for name, score in zip(names, scores, strict=True):
        score_rows.append(f"{name}={score}")

    print(f"score_rows: {score_rows}")

    # sorted は、並び替えた新しい list を返す。
    # key を指定すると、並び替えの基準を変えられる。
    words = ["python", "java", "sql", "typescript"]
    sorted_words = sorted(words)
    sorted_by_length = sorted(words, key=len)

    print(f"sorted_words: {sorted_words}")
    print(f"sorted_by_length: {sorted_by_length}")

    # reversed は、逆順に取り出すためのイテレータを返す。
    # list にすると、逆順の list として確認できる。
    reversed_names = list(reversed(names))
    print(f"reversed_names: {reversed_names}")

    # any は、1つでも True 相当の値があれば True を返す。
    # all は、すべて True 相当の値であれば True を返す。
    has_high_score = any(score >= 90 for score in scores)
    all_passed = all(score >= 60 for score in scores)

    print(f"has_high_score: {has_high_score}")
    print(f"all_passed: {all_passed}")

    # any / all は、条件式とジェネレータ式を組み合わせることが多い。
    # 「存在するか」「全て満たすか」を短く書ける。
    has_long_name = any(len(name) >= 4 for name in names)
    all_names_not_empty = all(len(name) > 0 for name in names)

    print(f"has_long_name: {has_long_name}")
    print(f"all_names_not_empty: {all_names_not_empty}")

    assert indexed_names == ["1: Sora", "2: Mio", "3: Ren"]
    assert score_rows == ["Sora=80", "Mio=95", "Ren=70"]
    assert sorted_words == ["java", "python", "sql", "typescript"]
    assert sorted_by_length == ["sql", "java", "python", "typescript"]
    assert reversed_names == ["Ren", "Mio", "Sora"]
    assert has_high_score is True
    assert all_passed is True
    assert has_long_name is True
    assert all_names_not_empty is True
