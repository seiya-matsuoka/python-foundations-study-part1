"""def、戻り値、複数戻り値、docstring を確認するサンプル。"""


def greet(name: str) -> str:
    """名前を受け取り、あいさつ文を返す。"""
    # def は関数を定義するためのキーワード。
    # Python では型ヒントを書けるが、実行時に型が強制されるわけではない。
    return f"Hello, {name}!"


def calculate_total(price: int, quantity: int) -> int:
    """単価と数量を受け取り、合計金額を返す。"""
    # return は関数の結果を呼び出し元へ返す。
    # return に到達すると、その関数の処理はそこで終了する。
    total = price * quantity
    return total


def split_full_name(full_name: str) -> tuple[str, str]:
    """氏名を空白で分割し、姓と名を返す。"""
    # Python では複数の値をカンマ区切りで返せる。
    # 実際には tuple として返される。
    family_name, given_name = full_name.split()
    return family_name, given_name


def build_profile(name: str, age: int) -> dict[str, str | int]:
    """名前と年齢を受け取り、プロフィール情報を dict で返す。"""
    # 関数の中で作った値を return すると、呼び出し元で利用できる。
    # この関数では、複数の情報を dict にまとめて返している。
    profile = {
        "name": name,
        "age": age,
    }
    return profile


def run_function_basics() -> None:
    """関数定義、戻り値、複数戻り値、docstring を確認する。"""

    message = greet("Sora")
    print(f"greet の戻り値: {message}")

    total = calculate_total(1200, 3)
    print(f"calculate_total の戻り値: {total}")

    family_name, given_name = split_full_name("Yamada Taro")
    print(f"family_name: {family_name}")
    print(f"given_name: {given_name}")

    profile = build_profile("Mio", 22)
    print(f"build_profile の戻り値: {profile}")

    # docstring は、関数定義直下に書く文字列。
    # 関数の __doc__ から参照できる。
    greet_doc = greet.__doc__
    print(f"greet の docstring: {greet_doc}")

    assert message == "Hello, Sora!"
    assert total == 3600
    assert family_name == "Yamada"
    assert given_name == "Taro"
    assert profile == {"name": "Mio", "age": 22}
    assert greet_doc == "名前を受け取り、あいさつ文を返す。"
