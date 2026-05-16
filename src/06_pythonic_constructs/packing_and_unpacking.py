"""パック、アンパック、複数代入を確認するサンプル。"""


def build_profile_tuple() -> tuple[str, int, str]:
    """プロフィール情報を tuple として返す。"""
    # 複数の値をカンマ区切りで返すと、tuple として扱える。
    return "Sora", 20, "Python"


def format_user(name: object, age: object, language: object) -> str:
    """ユーザー情報を文字列に整形する。"""
    return f"{name}({age}) uses {language}."


def run_packing_and_unpacking() -> None:
    """パック、アンパック、複数代入を確認する。"""

    # 右辺に複数の値を書くと、tuple としてまとめられる。
    # これをパックと考えられる。
    packed_profile = "Mio", 21, "Java"
    print(f"packed_profile: {packed_profile}")

    # 左辺に複数の変数を書くと、値を分解して受け取れる。
    # これをアンパックと呼ぶ。
    name, age, language = packed_profile

    print(f"name: {name}")
    print(f"age: {age}")
    print(f"language: {language}")

    # 関数の戻り値が tuple の場合も、同じようにアンパックできる。
    profile_name, profile_age, profile_language = build_profile_tuple()

    print(f"profile_name: {profile_name}")
    print(f"profile_age: {profile_age}")
    print(f"profile_language: {profile_language}")

    # 複数代入を使うと、一時変数なしで値を入れ替えられる。
    left = "left"
    right = "right"

    left, right = right, left
    print(f"left: {left}")
    print(f"right: {right}")

    # * を使うと、残りの値を list として受け取れる。
    first, *middle, last = [10, 20, 30, 40, 50]

    print(f"first: {first}")
    print(f"middle: {middle}")
    print(f"last: {last}")

    # 関数呼び出し時に * を使うと、コレクションを引数に展開できる。
    user_values = ("Ren", 22, "SQL")
    formatted_user = format_user(*user_values)
    print(f"formatted_user: {formatted_user}")

    # ** を使うと、dict をキーワード引数として展開できる。
    user_options = {
        "name": "Aoi",
        "age": 23,
        "language": "Python",
    }
    formatted_user_by_dict = format_user(**user_options)
    print(f"formatted_user_by_dict: {formatted_user_by_dict}")

    assert packed_profile == ("Mio", 21, "Java")
    assert name == "Mio"
    assert age == 21
    assert language == "Java"
    assert profile_name == "Sora"
    assert profile_age == 20
    assert profile_language == "Python"
    assert left == "right"
    assert right == "left"
    assert first == 10
    assert middle == [20, 30, 40]
    assert last == 50
    assert formatted_user == "Ren(22) uses SQL."
    assert formatted_user_by_dict == "Aoi(23) uses Python."
