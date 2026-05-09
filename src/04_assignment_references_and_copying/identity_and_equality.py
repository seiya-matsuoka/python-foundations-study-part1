"""is と == の違いを確認するサンプル。"""


def run_identity_and_equality() -> None:
    """同一性と等価性の違いを確認する。"""

    # == は、値として等しいかを確認する。
    # is は、同じオブジェクトを指しているかを確認する。
    first_numbers = [1, 2, 3]
    second_numbers = [1, 2, 3]
    shared_numbers = first_numbers

    print(f"first_numbers == second_numbers: {first_numbers == second_numbers}")
    print(f"first_numbers is second_numbers: {first_numbers is second_numbers}")
    print(f"first_numbers is shared_numbers: {first_numbers is shared_numbers}")

    # 値が同じでも、別々に作った list は別のオブジェクト。
    # そのため == は True でも、is は False になる。
    first_numbers.append(4)

    print(f"変更後の first_numbers: {first_numbers}")
    print(f"変更後の second_numbers: {second_numbers}")
    print(f"変更後の shared_numbers: {shared_numbers}")

    # None の確認には is を使うのが一般的。
    # None は「値がない」ことを表す特別なオブジェクト。
    selected_user = None
    fallback_user = "guest"

    if selected_user is None:  # noqa: SIM108
        display_user = fallback_user
    else:
        display_user = selected_user

    print(f"display_user: {display_user}")

    # 小さい整数や短い文字列では、is が True に見える場合がある。
    # ただし、それを前提にした比較は避ける。
    first_text = "Python"
    second_text = "Python"

    print(f"first_text == second_text: {first_text == second_text}")
    print(f"first_text is second_text: {first_text is second_text}")

    assert first_numbers == [1, 2, 3, 4]
    assert second_numbers == [1, 2, 3]
    assert shared_numbers == [1, 2, 3, 4]
    assert first_numbers == shared_numbers
    assert first_numbers is shared_numbers
    assert first_numbers is not second_numbers
    assert display_user == "guest"
    assert first_text == second_text
