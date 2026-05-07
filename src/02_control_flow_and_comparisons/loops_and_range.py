"""for / while / range の基本を確認するサンプル。"""


def run_loops_and_range() -> None:
    """繰り返し処理と range の基本を確認する。"""

    # for は、リストや range などの反復可能な値から順番に値を取り出す。
    languages = ["Python", "Java", "JavaScript"]

    for language in languages:
        print(f"学習候補: {language}")

    # range(5) は 0 から 4 までの値を順番に作る。
    # 終了値の 5 は含まれない点に注意する。
    zero_to_four = []

    for number in range(5):
        zero_to_four.append(number)

    print(f"range(5): {zero_to_four}")

    # range(start, stop) は start から stop の手前までを表す。
    one_to_five = []

    for number in range(1, 6):
        one_to_five.append(number)

    print(f"range(1, 6): {one_to_five}")

    # range(start, stop, step) では増減幅を指定できる。
    even_numbers = []

    for number in range(2, 11, 2):
        even_numbers.append(number)

    print(f"range(2, 11, 2): {even_numbers}")

    # while は、条件が True の間だけ繰り返す。
    # カウンターを更新し忘れると無限ループになるため注意する。
    count = 0
    counted_values = []

    while count < 3:
        counted_values.append(count)
        count += 1

    print(f"while count < 3: {counted_values}")

    assert zero_to_four == [0, 1, 2, 3, 4]
    assert one_to_five == [1, 2, 3, 4, 5]
    assert even_numbers == [2, 4, 6, 8, 10]
    assert counted_values == [0, 1, 2]
