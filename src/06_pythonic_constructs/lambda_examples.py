"""ラムダ式の基本的な使いどころを確認するサンプル。"""

from collections.abc import Callable


def apply_number_rule(number: int, rule: Callable[[int], int]) -> int:
    """数値と短い処理を受け取り、処理結果を返す。"""
    return rule(number)


def run_lambda_examples() -> None:
    """ラムダ式を key 関数などで使う例を確認する。"""

    # lambda は、短い無名関数を書くための構文。
    # 複雑な処理を書く場所ではなく、短い変換や key 指定に向く。
    doubled = apply_number_rule(5, lambda number: number * 2)
    print(f"doubled: {doubled}")

    users = [
        {"name": "Sora", "score": 80},
        {"name": "Mio", "score": 95},
        {"name": "Ren", "score": 70},
    ]

    # sorted の key に lambda を渡すと、並び替えの基準をその場で書ける。
    # ここでは score の値を基準に並び替えている。
    sorted_by_score = sorted(users, key=lambda user: user["score"])
    print(f"sorted_by_score: {sorted_by_score}")

    # reverse=True を使うと降順になる。
    # lambda は短い基準を渡したい場合に読みやすい。
    sorted_by_score_desc = sorted(
        users,
        key=lambda user: user["score"],
        reverse=True,
    )
    print(f"sorted_by_score_desc: {sorted_by_score_desc}")

    # 複数の値を tuple として返すと、複数条件で並び替えられる。
    # ここでは enabled を先に見て、その後 priority を見る。
    tasks = [
        {"title": "write", "enabled": True, "priority": 2},
        {"title": "test", "enabled": False, "priority": 1},
        {"title": "deploy", "enabled": True, "priority": 1},
    ]
    sorted_tasks = sorted(
        tasks,
        key=lambda task: (not task["enabled"], task["priority"]),
    )

    print(f"sorted_tasks: {sorted_tasks}")

    # 名前を付けて再利用したい処理は、def で書く方が読みやすい。
    # lambda は「その場で短く使う」用途に向く。
    assert doubled == 10
    assert sorted_by_score == [
        {"name": "Ren", "score": 70},
        {"name": "Sora", "score": 80},
        {"name": "Mio", "score": 95},
    ]
    assert sorted_by_score_desc == [
        {"name": "Mio", "score": 95},
        {"name": "Sora", "score": 80},
        {"name": "Ren", "score": 70},
    ]
    assert sorted_tasks == [
        {"title": "deploy", "enabled": True, "priority": 1},
        {"title": "write", "enabled": True, "priority": 2},
        {"title": "test", "enabled": False, "priority": 1},
    ]
