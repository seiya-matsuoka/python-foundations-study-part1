"""文字列と標準出力の基本を確認するサンプル。"""


def run_strings_and_output():
    """文字列リテラル、f文字列、print の基本を確認する。"""

    # 文字列は str 型の値。
    # シングルクォートとダブルクォートは、基本的にどちらも文字列に使える。
    single_quoted = "single quoted text"
    double_quoted = "double quoted text"

    print(single_quoted)
    print(double_quoted)

    # 文字列の中にクォートを含めたい場合は、外側と内側の種類を変えると読みやすい。
    message = "I'm learning Python."
    print(message)

    # \n は改行を表すエスケープシーケンス。
    line_break_text = "first line\nsecond line"
    print(line_break_text)

    # 三重クォートを使うと、複数行の文字列を書ける。
    # docstring も三重クォートの文字列として書かれる。
    multi_line_text = """Python
foundations
study"""
    print(multi_line_text)

    # + で文字列を連結できる。
    # ただし、数値と文字列を + で直接連結することはできない。
    # 数値を表示に混ぜたい場合は f 文字列を使うと読みやすい。
    first_name = "Seiya"
    last_name = "Matsuoka"
    full_name = first_name + " " + last_name
    print(full_name)

    # f 文字列では、文字列の中に {変数名} や {式} を埋め込める。
    language = "Python"
    unit_number = 1
    print(f"Unit {unit_number}: {language} の基本構文")
    print(f"2 + 3 = {2 + 3}")

    # len 関数は文字数を返す。
    # Python では len(value) のように関数として呼び出す。
    word = "Python"
    print(f"{word} の文字数: {len(word)}")

    # 文字列にもメソッドがある。
    # Unit 09 で詳しく扱うため、ここでは入口として代表例だけ確認する。
    raw_text = "  python basics  "
    print(f"strip: '{raw_text.strip()}'")
    print(f"upper: '{word.upper()}'")
    print(f"replace: '{word.replace('Py', 'My')}'")

    # print は複数の値を受け取れる。
    # sep は値と値の区切り、end は末尾に出力する文字列を指定する。
    print("A", "B", "C", sep="-")
    print("改行しない出力", end=" -> ")
    print("続き")

    assert full_name == "Seiya Matsuoka"
    assert len(word) == 6
    assert raw_text.strip() == "python basics"
