"""Unit 06 の実行入口。

このファイルは、Unit 06 に含まれる各サンプルを順番に呼び出す。
Pythonらしいコレクション処理や値の受け渡しを確認する入口となる。
"""

from comprehension_examples import run_comprehension_examples
from generator_expression_examples import run_generator_expression_examples
from iteration_helper_functions import run_iteration_helper_functions
from lambda_examples import run_lambda_examples
from packing_and_unpacking import run_packing_and_unpacking


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
    """Unit 06 全体を順番に実行する。

    この単位では、Pythonらしい簡潔な書き方を確認する。
    内包表記、ジェネレータ式、便利な組み込み関数、アンパックを読む。
    """
    print_section("1. 内包表記")
    run_comprehension_examples()

    print_section("2. ジェネレータ式")
    run_generator_expression_examples()

    print_section("3. enumerate・zip・sorted・reversed・any・all")
    run_iteration_helper_functions()

    print_section("4. パック・アンパック・複数代入")
    run_packing_and_unpacking()

    print_section("5. ラムダ式")
    run_lambda_examples()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
