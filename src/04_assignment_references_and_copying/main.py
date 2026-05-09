"""Unit 04 の実行入口。

このファイルは、Unit 04 に含まれる各サンプルを順番に呼び出す。
代入、参照、再束縛、コピーの違いを一通り確認するための入口となる。
"""

from assignment_and_rebinding import run_assignment_and_rebinding
from deep_copy_examples import run_deep_copy_examples
from identity_and_equality import run_identity_and_equality
from shallow_copy_examples import run_shallow_copy_examples
from shared_references import run_shared_references


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
    """Unit 04 全体を順番に実行する。

    この単位では、代入は値そのもののコピーではないことを確認する。
    参照の共有、再束縛、浅いコピー、深いコピーを順番に読む。
    """
    print_section("1. 代入と再束縛")
    run_assignment_and_rebinding()

    print_section("2. 参照の共有")
    run_shared_references()

    print_section("3. is と == の違い")
    run_identity_and_equality()

    print_section("4. 浅いコピー")
    run_shallow_copy_examples()

    print_section("5. 深いコピー")
    run_deep_copy_examples()


# この条件式は、main.py を直接実行したときだけ main を呼び出すための書き方。
# import されたときに自動実行されないようにするための基本形となる。
if __name__ == "__main__":
    main()
