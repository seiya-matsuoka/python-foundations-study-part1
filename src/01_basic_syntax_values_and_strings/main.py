"""Unit 01 の実行入口。

このファイルは、Unit 01 に含まれる各サンプルを順番に呼び出す。
個別ファイルを直接読む前に、まずこのファイルを見ると全体の流れを追いやすい。
"""

from booleans_none_and_conversion import run_booleans_none_and_conversion
from comments_and_execution import run_comments_and_execution
from numbers_and_operations import run_numbers_and_operations
from strings_and_output import run_strings_and_output
from values_and_variables import run_values_and_variables


def print_section(title):
    """表示上の区切りを出力する。

    今回は学習用コードのため、処理のまとまりごとに見出しを出す。
    戻り値はなく、標準出力への表示だけを行う。
    """
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def main():
    """Unit 01 全体を順番に実行する。

    main 関数に処理をまとめると、実行入口が分かりやすくなる。
    今回は次の順番で読むことを想定する。

    1. 値と変数
    2. 数値型と演算
    3. 文字列と標準出力
    4. 真偽値、None、型変換
    5. コメントとスクリプト実行
    """
    print_section("1. 値と変数")
    run_values_and_variables()

    print_section("2. 数値型と演算")
    run_numbers_and_operations()

    print_section("3. 文字列と標準出力")
    run_strings_and_output()

    print_section("4. 真偽値・None・型変換")
    run_booleans_none_and_conversion()

    print_section("5. コメントとスクリプト実行")
    run_comments_and_execution()


# この条件式は「このファイルが直接実行されたときだけ main を呼び出す」ための書き方。
# 詳細は Unit 08 のモジュール・import・コード分割で改めて扱う。
if __name__ == "__main__":
    main()
