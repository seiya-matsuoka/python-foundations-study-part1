"""truthy / falsy と is / == の違いを確認するサンプル。"""


def run_truthy_falsy_and_identity() -> None:
    """真偽値として評価される値と同一性の違いを確認する。"""

    # Python では、bool 型以外の値も条件式の中で評価できる。
    # 空文字、空リスト、0、None などは falsy な値として扱われる。
    values = ["Python", "", [1, 2], [], 1, 0, None]

    for value in values:
        print(f"value={value!r}, bool(value)={bool(value)}")

    # if items: は「items に要素があるか」を読む定番の書き方。
    # len(items) > 0 と書かなくても、空リストは False として扱われる。
    items = ["book", "notebook"]

    if items:
        print("items には要素がある")
    else:
        print("items は空")

    # == は値として等しいかを比較する。
    # is は同じオブジェクトそのものを参照しているかを比較する。
    left = [1, 2, 3]
    right = [1, 2, 3]
    same_reference = left

    print(f"left == right: {left == right}")
    print(f"left is right: {left is right}")
    print(f"left is same_reference: {left is same_reference}")

    # None かどうかを確認するときは、基本的に is None を使う。
    selected_item = None

    if selected_item is None:
        print("selected_item は未選択")

    assert bool("Python") is True
    assert bool("") is False
    assert bool([1, 2]) is True
    assert bool([]) is False
    assert bool(1) is True
    assert bool(0) is False
    assert bool(None) is False
    assert left == right
    assert left is not right
    assert left is same_reference
    assert selected_item is None
