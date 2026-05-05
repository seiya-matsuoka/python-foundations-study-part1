"""真偽値、None、型変換の基本を確認するサンプル。"""


def run_booleans_none_and_conversion():
    """bool、None、基本的な型変換を確認する。"""

    # bool は真偽値を表す型。
    # 値は True または False のどちらかになる。
    is_python_fun = True
    is_finished = False

    print(f"is_python_fun: {is_python_fun} / type: {type(is_python_fun).__name__}")
    print(f"is_finished: {is_finished} / type: {type(is_finished).__name__}")

    # 比較演算の結果は bool になる。
    # 比較演算の詳細は Unit 02 で扱う。
    current_unit = 1
    print(f"current_unit == 1: {current_unit == 1}")
    print(f"current_unit > 3: {current_unit > 3}")

    # None は「値がない」「まだ値が決まっていない」ことを表す特別な値。
    # Java の null と似た場面で使われるが、Python では None という1つの値として扱う。
    selected_book = None
    print(f"selected_book: {selected_book}")
    print(f"selected_book の型: {type(selected_book).__name__}")

    # None かどうかを確認するときは、基本的に is None を使う。
    # == None でも動く場合はあるが、Python では is None が定番の書き方。
    if selected_book is None:
        print("selected_book はまだ選択されていない")

    selected_book = "Python入門"
    if selected_book is not None:
        print(f"selected_book が選択された: {selected_book}")

    # 戻り値を書かない関数は None を返す。
    # この性質は、関数を読むときに重要となる。
    result = do_nothing()
    print(f"do_nothing() の戻り値: {result}")

    # bool 関数を使うと、値を真偽値として評価した結果を確認できる。
    # truthy / falsy は Unit 02 で詳しく扱うため、ここでは入口だけ確認する。
    print(f"bool(0): {bool(0)}")
    print(f"bool(1): {bool(1)}")
    print(f"bool(''): {bool('')}")
    print(f"bool('Python'): {bool('Python')}")
    print(f"bool(None): {bool(None)}")

    # 代表的な型変換。
    # int、float、str、bool は、値を別の型として扱いたいときに使う。
    number_text = "42"
    number = int(number_text)
    ratio = float("0.75")
    label = str(number)
    flag = bool("non-empty text")

    print(f"number: {number} / type: {type(number).__name__}")
    print(f"ratio: {ratio} / type: {type(ratio).__name__}")
    print(f"label: {label} / type: {type(label).__name__}")
    print(f"flag: {flag} / type: {type(flag).__name__}")

    assert result is None
    assert bool(0) is False
    assert bool("Python") is True
    assert number == 42


def do_nothing():
    """明示的な return を持たない関数。

    Python では return を書かない関数も呼び出せる。
    その場合、戻り値は None になる。
    """
    # pass は「何もしない」ことを表す文。
    # 空の関数や、あとで実装する処理の仮置きで使われることがある。
    pass
