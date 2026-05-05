"""コメント、docstring、スクリプト実行の基本を確認するサンプル。"""


def run_comments_and_execution():
    """コメントの役割と、スクリプトとして実行する入口を確認する。"""

    # これは行コメント。
    # 「なぜその処理をするのか」「どこに注目するのか」を補足する。
    learning_unit = "Unit 01"

    # コメントは多ければよいわけではない。
    # 今回はコードリーディング学習のため、あえて厚めに書く。
    print(f"現在の学習単位: {learning_unit}")

    # docstring は、関数やモジュールの先頭に置く説明用の文字列。
    # help 関数などからも参照できる。
    description = run_comments_and_execution.__doc__ or ""
    print(f"run_comments_and_execution の説明: {description.strip()}")

    # Python ファイルは、上から順番に実行される。
    # 関数定義そのものは「処理を登録する」だけとなる。
    # 関数の中身は、呼び出すまで実行されない。
    message = build_message("Python")
    print(message)

    # __name__ は、モジュールの実行され方を表す特別な変数。
    # 直接実行されたファイルでは "__main__" になる。
    # このファイルは main.py から import される。
    # そのため、通常はファイル名相当の値になる。
    print(f"comments_and_execution.py の __name__: {__name__}")

    # main.py 側にある if __name__ == "__main__": は、
    # 「そのファイルが直接実行されたときだけ main を呼び出す」ための定番形。
    # 詳細は Unit 08 で改めて扱う。

    assert build_message("Python") == "Python の基本を読む"


def build_message(language):
    """指定された学習言語名を使って表示用メッセージを作る。"""
    return f"{language} の基本を読む"
