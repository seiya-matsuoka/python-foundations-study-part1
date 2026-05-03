"""値、変数、動的型付けの基本を確認するサンプル。"""

# Python には、値を書き換えられない定数を作るための専用構文はない。
# モジュール直下に大文字名を置くことで、定数として扱う値だと表す。
DEFAULT_LANGUAGE = "Python"


def run_values_and_variables():
    """変数に値を入れ、値の型を確認する。"""

    # Python では、変数宣言のための型名を書かない。
    # 変数名に値を代入すると、その名前から値を参照できるようになる。
    user_name = "Matsuoka"
    learning_language = "Python"
    years_of_experience = 2

    print(f"学習者: {user_name}")
    print(f"学習対象: {learning_language}")
    print(f"エンジニア経験年数: {years_of_experience}")

    # type 関数を使うと、値の型を確認できる。
    # __name__ は型オブジェクトが持つ名前を取り出すために使っている。
    print(f"user_name の型: {type(user_name).__name__}")
    print(f"years_of_experience の型: {type(years_of_experience).__name__}")

    # Python は動的型付けの言語。
    # 同じ変数名に、あとから別の型の値を再代入できる。
    # ただし、読みやすいコードでは同じ変数に意味の違う値を入れ直しすぎない方がよい。
    value = "文字列としての値"
    print(f"value: {value} / type: {type(value).__name__}")

    value = 100
    print(f"value: {value} / type: {type(value).__name__}")

    value = 3.14
    print(f"value: {value} / type: {type(value).__name__}")

    # DEFAULT_LANGUAGE はモジュール直下で定義している。
    # 関数内で大文字の変数を新しく作るより、定数らしい意図が伝わりやすい。
    print(f"既定の学習言語: {DEFAULT_LANGUAGE}")

    # 複数の変数にまとめて代入できる。
    # この書き方は Python ではよく使われる。
    title, level = "Python Foundations", "beginner"
    print(f"title: {title}")
    print(f"level: {level}")

    # assert は「この条件は成り立つはず」という簡易確認に使う。
    # 本格的なテストは Unit 12 で unittest として扱う。
    assert type(user_name).__name__ == "str"
    assert type(years_of_experience).__name__ == "int"
    assert DEFAULT_LANGUAGE == "Python"
