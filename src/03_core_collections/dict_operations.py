"""dict の基本操作を確認するサンプル。"""


def run_dict_operations() -> None:
    """dict の作成、参照、更新、削除、検索、反復を確認する。"""

    # dict は、キーと値の対応を持つコレクション。
    # Java の Map に近い使い方をする。
    student = {
        "name": "Sora",
        "age": 20,
        "language": "Python",
    }
    print(f"最初の student: {student}")

    # キーを指定すると、対応する値を取得できる。
    # 存在しないキーを [] で参照すると KeyError になる。
    name = student["name"]
    language = student["language"]

    print(f"name: {name}")
    print(f"language: {language}")

    # get を使うと、キーが存在しない場合の既定値を指定できる。
    # 存在しない可能性があるキーを読むときに使いやすい。
    city = student.get("city", "unknown")
    print(f"city: {city}")

    # dict はミュータブル。
    # 既存キーの値を変更でき、新しいキーも追加できる。
    student["age"] = 21
    student["city"] = "Tokyo"
    print(f"更新後の student: {student}")

    # pop は、キーに対応する値を取り出しながら削除する。
    removed_city = student.pop("city")

    print(f"削除した city: {removed_city}")
    print(f"削除後の student: {student}")

    # dict に対する in は、キーの存在確認になる。
    # 値の中を探しているわけではない点に注意する。
    has_name_key = "name" in student
    has_sora_value_as_key = "Sora" in student

    print(f"name キーを持つか: {has_name_key}")
    print(f"Sora をキーとして持つか: {has_sora_value_as_key}")

    # keys、values、items で dict の中身の見方を変えられる。
    keys = list(student.keys())
    values = list(student.values())
    items = list(student.items())

    print(f"keys: {keys}")
    print(f"values: {values}")
    print(f"items: {items}")

    # dict をそのまま for で回すと、キーを順番に取り出す。
    descriptions = []

    for key in student:
        descriptions.append(f"{key}={student[key]}")

    print(f"dict の反復結果: {descriptions}")

    # sorted に dict を渡すと、キーを並び替えた list が返る。
    sorted_keys = sorted(student)
    print(f"並び替えたキー: {sorted_keys}")

    assert name == "Sora"
    assert language == "Python"
    assert city == "unknown"
    assert removed_city == "Tokyo"
    assert student == {
        "name": "Sora",
        "age": 21,
        "language": "Python",
    }
    assert has_name_key is True
    assert has_sora_value_as_key is False
    assert keys == ["name", "age", "language"]
    assert values == ["Sora", 21, "Python"]
    assert items == [
        ("name", "Sora"),
        ("age", 21),
        ("language", "Python"),
    ]
    assert descriptions == [
        "name=Sora",
        "age=21",
        "language=Python",
    ]
    assert sorted_keys == ["age", "language", "name"]
