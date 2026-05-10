"""ミュータブルなデフォルト引数の注意点を確認するサンプル。"""


def append_bad(item: str, items: list[str] = []) -> list[str]:  # noqa: B006
    """ミュータブルなデフォルト引数の注意点を確認するための例。"""
    # この書き方は、学習用にあえて用意している。
    # デフォルト引数の list は、関数定義時に一度だけ作られる。
    items.append(item)
    return items


def append_good(item: str, items: list[str] | None = None) -> list[str]:
    """None を使って、呼び出しごとに新しい list を作る例。"""
    # デフォルト値を None にしておくと、呼び出しごとに新しい list を作れる。
    # ミュータブルな値をデフォルト引数に直接置くより安全な書き方となる。
    if items is None:
        items = []

    items.append(item)
    return items


def run_mutable_default_arguments() -> None:
    """ミュータブルなデフォルト引数の注意点を確認する。"""

    # append_bad は、呼び出しをまたいで同じ list を使い続ける。
    # そのため、2回目の呼び出し結果に1回目の値が残る。
    first_bad = append_bad("apple")
    second_bad = append_bad("banana")

    print(f"append_bad 1回目: {first_bad}")
    print(f"append_bad 2回目: {second_bad}")
    print(f"同じ list を指すか: {first_bad is second_bad}")

    # append_good は、引数を省略した呼び出しごとに新しい list を作る。
    first_good = append_good("apple")
    second_good = append_good("banana")

    print(f"append_good 1回目: {first_good}")
    print(f"append_good 2回目: {second_good}")
    print(f"同じ list を指すか: {first_good is second_good}")

    # 呼び出し側が list を渡した場合は、その list に追加する。
    existing_items = ["orange"]
    result_items = append_good("grape", existing_items)

    print(f"渡した list: {existing_items}")
    print(f"戻り値の list: {result_items}")

    assert first_bad == ["apple", "banana"]
    assert second_bad == ["apple", "banana"]
    assert first_bad is second_bad
    assert first_good == ["apple"]
    assert second_good == ["banana"]
    assert first_good is not second_good
    assert existing_items == ["orange", "grape"]
    assert result_items is existing_items
