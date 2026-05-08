"""Unit 03 の実行入口。

このファイルは、Unit 03 に含まれる各サンプルを順番に呼び出す。
基本コレクションの使い分けと操作を一通り確認するための入口となる。
"""

from dict_operations import run_dict_operations
from indexing_slicing_and_mutability import run_indexing_slicing_and_mutability
from list_operations import run_list_operations
from set_operations import run_set_operations
from tuple_operations import run_tuple_operations


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
    """Unit 03 全体を順番に実行する。

    この単位では、基本コレクションの作成、参照、変更、検索を中心に読む。
    各ファイルは一つのテーマを担当し、main から順番に呼び出す。
    """
    print_section("1. list")
    run_list_operations()

    print_section("2. tuple")
    run_tuple_operations()

    print_section("3. dict")
    run_dict_operations()

    print_section("4. set")
    run_set_operations()

    print_section("5. インデックス・スライス・ミュータブル性")
    run_indexing_slicing_and_mutability()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
