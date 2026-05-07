"""比較演算子と論理演算子を確認するサンプル。"""


def run_comparisons_and_logic() -> None:
    """比較と論理条件の基本を確認する。"""

    # 比較演算子は、比較結果として True または False を返す。
    age = 25
    minimum_age = 18

    is_adult = age >= minimum_age
    is_child = age < minimum_age
    is_exactly_twenty_five = age == 25
    is_not_thirty = age != 30

    print(f"age >= minimum_age: {is_adult}")
    print(f"age < minimum_age: {is_child}")
    print(f"age == 25: {is_exactly_twenty_five}")
    print(f"age != 30: {is_not_thirty}")

    # Python では、比較をつなげて書ける。
    # 18 <= age and age < 65 と近い意味だが、より自然に読める。
    is_working_age = 18 <= age < 65
    print(f"18 <= age < 65: {is_working_age}")

    # and は両方 True のときだけ True になる。
    # or はどちらか一方でも True であれば True になる。
    has_account = True
    password_is_valid = True
    is_admin = False

    can_sign_in = has_account and password_is_valid
    can_open_admin_page = can_sign_in and is_admin
    can_open_help_page = can_sign_in or is_admin

    print(f"ログイン可能: {can_sign_in}")
    print(f"管理画面を開ける: {can_open_admin_page}")
    print(f"ヘルプページを開ける: {can_open_help_page}")

    # not は真偽値を反転する。
    is_guest = not has_account
    print(f"ゲストユーザー: {is_guest}")

    assert is_adult is True
    assert is_child is False
    assert is_exactly_twenty_five is True
    assert is_not_thirty is True
    assert is_working_age is True
    assert can_sign_in is True
    assert can_open_admin_page is False
    assert can_open_help_page is True
    assert is_guest is False
