"""tuple の基本操作を確認するサンプル。"""


def run_tuple_operations() -> None:
    """tuple の作成、参照、検索、反復、変更できない性質を確認する。"""

    # tuple は、順序を持つコレクション。
    # list と似ているが、作成後に要素を変更できない。
    point = (10, 20)
    print(f"座標を表す point: {point}")

    # tuple もインデックスで要素を参照できる。
    x = point[0]
    y = point[1]

    print(f"x座標: {x}")
    print(f"y座標: {y}")

    # tuple でもスライスを使える。
    # スライスの結果は tuple になる。
    profile = ("Python", 1991, "Guido")
    profile_head = profile[:2]
    print(f"profile の先頭2件: {profile_head}")

    # 要素数が1つの tuple では、末尾のカンマが必要。
    # カンマがない場合、括弧を付けても文字列のままとなる。
    single_item_tuple = ("only-one",)
    not_tuple = "only-one"

    print(f"1要素の tuple: {single_item_tuple}")
    print(f"カンマなしの値: {not_tuple}")

    # tuple はイミュータブル。
    # point[0] = 99 のように、既存の要素を書き換えることはできない。
    # 値を変えたい場合は、新しい tuple を作る。
    moved_point = (99, point[1])
    print(f"新しく作った point: {moved_point}")

    # in による membership 判定は tuple でも使える。
    has_python = "Python" in profile
    has_java = "Java" in profile

    print(f"Python を含むか: {has_python}")
    print(f"Java を含むか: {has_java}")

    # for を使うと、tuple の要素を順番に処理できる。
    profile_items = []

    for item in profile:
        profile_items.append(str(item))

    print(f"文字列化した profile: {profile_items}")

    # sorted は tuple も受け取れる。
    # ただし、結果は tuple ではなく list になる。
    scores = (80, 95, 70)
    sorted_scores = sorted(scores)

    print(f"元の scores: {scores}")
    print(f"sorted の結果: {sorted_scores}")

    assert x == 10
    assert y == 20
    assert profile_head == ("Python", 1991)
    assert single_item_tuple == ("only-one",)
    assert not_tuple == "only-one"
    assert moved_point == (99, 20)
    assert point == (10, 20)
    assert has_python is True
    assert has_java is False
    assert profile_items == ["Python", "1991", "Guido"]
    assert sorted_scores == [70, 80, 95]
