"""位置引数、キーワード引数、デフォルト引数を確認するサンプル。"""


def create_user_summary(name: str, age: int, city: str) -> str:
    """名前、年齢、都市からユーザー概要を作る。"""
    # この関数は3つの引数を受け取る。
    # 呼び出し側では、位置引数でもキーワード引数でも渡せる。
    return f"{name} is {age} years old and lives in {city}."


def format_price(price: int, tax_rate: float = 0.1) -> str:
    """税込金額を文字列として返す。"""
    # tax_rate にはデフォルト引数がある。
    # 呼び出し側が tax_rate を省略すると、0.1 が使われる。
    tax_included = int(price * (1 + tax_rate))
    return f"{tax_included} yen"


def build_label(name: str, *, category: str, enabled: bool = True) -> str:
    """キーワード専用引数を使ってラベル文字列を作る。"""
    # * より後ろの引数は、キーワード引数として渡す必要がある。
    # 呼び出し側の意味を明確にしたい場合に使える。
    status = "enabled" if enabled else "disabled"
    return f"{category}:{name}({status})"


def run_argument_patterns() -> None:
    """位置引数、キーワード引数、デフォルト引数を確認する。"""

    # 位置引数は、引数の順番で値が対応する。
    positional_summary = create_user_summary("Sora", 20, "Tokyo")
    print(f"位置引数の結果: {positional_summary}")

    # キーワード引数は、引数名を指定して値を渡す。
    # 順番に依存しにくく、呼び出しの意味が読みやすくなる。
    keyword_summary = create_user_summary(
        city="Osaka",
        age=21,
        name="Mio",
    )
    print(f"キーワード引数の結果: {keyword_summary}")

    # デフォルト引数を省略した場合は、関数定義側の値が使われる。
    default_tax_price = format_price(1000)
    custom_tax_price = format_price(1000, tax_rate=0.08)

    print(f"デフォルト税率の価格: {default_tax_price}")
    print(f"指定した税率の価格: {custom_tax_price}")

    # category はキーワード専用引数。
    # build_label("Python", "language") のような渡し方はできない。
    default_label = build_label("Python", category="language")
    disabled_label = build_label("Draft", category="article", enabled=False)

    print(f"既定状態のラベル: {default_label}")
    print(f"無効状態のラベル: {disabled_label}")

    assert positional_summary == "Sora is 20 years old and lives in Tokyo."
    assert keyword_summary == "Mio is 21 years old and lives in Osaka."
    assert default_tax_price == "1100 yen"
    assert custom_tax_price == "1080 yen"
    assert default_label == "language:Python(enabled)"
    assert disabled_label == "article:Draft(disabled)"
