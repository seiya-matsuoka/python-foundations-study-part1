"""Unit 05 の実行入口。

このファイルは、Unit 05 に含まれる各サンプルを順番に呼び出す。
関数定義、引数、戻り値、スコープの基本を一通り確認する入口となる。
"""

from argument_patterns import run_argument_patterns
from function_basics import run_function_basics
from mutable_default_arguments import run_mutable_default_arguments
from scope_examples import run_scope_examples
from variable_arguments import run_variable_arguments


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
    """Unit 05 全体を順番に実行する。

    この単位では、関数の定義、戻り値、引数の受け取り方を確認する。
    その後、スコープとミュータブルなデフォルト引数の注意点を読む。
    """
    print_section("1. def・戻り値・docstring")
    run_function_basics()

    print_section("2. 位置引数・キーワード引数・デフォルト引数")
    run_argument_patterns()

    print_section("3. 可変長引数 args・kwargs")
    run_variable_arguments()

    print_section("4. スコープ")
    run_scope_examples()

    print_section("5. ミュータブルなデフォルト引数")
    run_mutable_default_arguments()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
