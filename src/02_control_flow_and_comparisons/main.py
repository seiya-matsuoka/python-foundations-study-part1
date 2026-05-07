"""Unit 02 の実行入口。

このファイルは、Unit 02 に含まれる各サンプルを順番に呼び出す。
条件分岐、繰り返し、比較の基本を一通り確認するための入口となる。
"""

from break_continue_examples import run_break_continue_examples
from comparisons_and_logic import run_comparisons_and_logic
from conditionals import run_conditionals
from loops_and_range import run_loops_and_range
from truthy_falsy_and_identity import run_truthy_falsy_and_identity


def print_section(title: str) -> None:
    """表示上の区切りを出力する。

    学習用コードのため、処理のまとまりごとに見出しを出す。
    戻り値はなく、標準出力への表示だけを行う。
    """
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def main() -> None:
    """Unit 02 全体を順番に実行する。

    この単位では、条件判定と反復処理を中心に読む。
    各ファイルは一つのテーマを担当し、main から順番に呼び出す。
    """
    print_section("1. if / elif / else")
    run_conditionals()

    print_section("2. for / while / range")
    run_loops_and_range()

    print_section("3. break / continue")
    run_break_continue_examples()

    print_section("4. 比較演算子・論理演算子")
    run_comparisons_and_logic()

    print_section("5. truthy / falsy・is と ==")
    run_truthy_falsy_and_identity()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
