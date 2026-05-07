"""if / elif / else の基本を確認するサンプル。"""


def describe_temperature(temperature: int) -> str:
    """気温を大まかな体感に分類する。"""
    # if / elif / else は、複数条件のうち一つを選ぶときに使う。
    # 上から順番に条件を評価し、最初に True になった枝だけを実行する。
    if temperature >= 30:
        result = "hot"
    elif temperature >= 20:
        result = "warm"
    elif temperature >= 10:
        result = "cool"
    else:
        result = "cold"

    return result


def run_conditionals() -> None:
    """条件分岐の基本形を順番に確認する。"""

    # if だけの形。
    # 条件が True のときだけ、インデントされたブロックが実行される。
    has_ticket = True

    if has_ticket:
        print("チケットがあるため入場できる")

    # if / else の形。
    # 条件が True のときと False のときで、実行する処理を分ける。
    score = 68
    passing_score = 70

    if score >= passing_score:  # noqa: SIM108
        score_message = "合格"
    else:
        score_message = "再確認"

    print(f"score={score}: {score_message}")

    # if / elif / else の形。
    # Java の else if に近いものが、Python では elif となる。
    temperatures = [35, 24, 15, 5]

    for temperature in temperatures:
        label = describe_temperature(temperature)
        print(f"{temperature}度: {label}")

    # 条件式の結果を変数に入れると、判定の意味が読みやすくなる。
    login_count = 3
    is_locked = False
    can_login = login_count < 5 and not is_locked

    if can_login:
        print("ログイン可能")
    else:
        print("ログイン不可")

    assert describe_temperature(35) == "hot"
    assert describe_temperature(24) == "warm"
    assert describe_temperature(15) == "cool"
    assert describe_temperature(5) == "cold"
    assert score_message == "再確認"
    assert can_login is True
