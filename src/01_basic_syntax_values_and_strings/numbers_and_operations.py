"""数値型と基本演算を確認するサンプル。"""


def run_numbers_and_operations():
    """int、float、基本演算、型変換を確認する。"""

    # int は整数を表す型。
    # Java の int / long のようにサイズを明示して使い分ける書き方ではない。
    book_count = 12
    page_count = 245

    # float は小数を表す型。
    average_score = 82.5

    print(f"book_count: {book_count} / type: {type(book_count).__name__}")
    print(f"average_score: {average_score} / type: {type(average_score).__name__}")

    # 基本的な算術演算子。
    # / は割り算で、結果は float になる。
    # // は切り捨て除算で、商の整数部分を得る。
    total = 17
    group_size = 5

    print(f"加算: {book_count + 3}")
    print(f"減算: {page_count - 45}")
    print(f"乗算: {group_size * 4}")
    print(f"割り算: {total / group_size}")
    print(f"切り捨て除算: {total // group_size}")
    print(f"余り: {total % group_size}")
    print(f"累乗: {2**4}")

    # 演算子には優先順位がある。
    # 読みやすさを優先する場合は、必要に応じて括弧を使う。
    without_parentheses = 10 + 2 * 3
    with_parentheses = (10 + 2) * 3
    print(f"括弧なし: {without_parentheses}")
    print(f"括弧あり: {with_parentheses}")

    # 複合代入演算子を使うと、現在の値を使って更新できる。
    remaining_tasks = 5
    remaining_tasks -= 1
    print(f"残りタスク数: {remaining_tasks}")

    # 型変換は int、float、str などの関数で行う。
    # 変換できない文字列を int にしようとするとエラーになる。
    # 例外処理は Unit 07 で扱うため、ここでは成功する例だけ実行する。
    numeric_text = "123"
    converted_number = int(numeric_text)
    converted_float = float("3.5")
    converted_text = str(456)

    print(f"int への変換: {converted_number} / type: {type(converted_number).__name__}")
    print(f"float への変換: {converted_float} / type: {type(converted_float).__name__}")
    print(f"str への変換: {converted_text} / type: {type(converted_text).__name__}")

    # 小数の計算では、2進数で正確に表せない値がある。
    # ここでは「float には丸め誤差が見える場合がある」とだけ押さえる。
    float_result = 0.1 + 0.2
    print(f"0.1 + 0.2 の結果: {float_result}")

    assert total // group_size == 3
    assert total % group_size == 2
    assert without_parentheses == 16
    assert with_parentheses == 36
    assert converted_number == 123
