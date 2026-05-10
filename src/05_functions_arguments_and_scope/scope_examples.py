"""スコープ、ローカル変数、グローバル変数を確認するサンプル。"""

DEFAULT_LANGUAGE = "Python"


def build_local_message(name: str) -> str:
    """ローカル変数を使ってメッセージを作る。"""
    # message はこの関数の中だけで使えるローカル変数。
    # 関数の外側から直接参照することはできない。
    message = f"Hello, {name}!"
    return message


def build_language_message() -> str:
    """モジュールレベルの変数を参照してメッセージを作る。"""
    # DEFAULT_LANGUAGE はモジュール直下で定義した変数。
    # 関数の中から読み取ることができる。
    return f"Learning {DEFAULT_LANGUAGE}"


def shadow_global_language() -> str:
    """同じ名前のローカル変数が優先されることを確認する。"""
    # 関数内で同じ名前の変数を定義すると、ローカル変数として扱われる。
    # これはモジュール直下の DEFAULT_LANGUAGE を変更しているわけではない。
    default_language = "Java"
    return f"Local language is {default_language}"


def count_active_users(users: list[dict[str, bool]]) -> int:
    """ユーザー一覧から active が True の人数を数える。"""
    # count はこの関数の中だけで使うローカル変数。
    # for の中で更新しているが、関数の外には漏れない。
    count = 0

    for user in users:
        if user["active"]:
            count += 1

    return count


def run_scope_examples() -> None:
    """スコープ、ローカル変数、グローバル変数を確認する。"""

    local_message = build_local_message("Sora")
    language_message = build_language_message()
    shadow_message = shadow_global_language()

    users = [
        {"active": True},
        {"active": False},
        {"active": True},
    ]
    active_count = count_active_users(users)

    print(f"ローカル変数を使った結果: {local_message}")
    print(f"グローバル変数を参照した結果: {language_message}")
    print(f"同名ローカル変数を使った結果: {shadow_message}")
    print(f"active なユーザー数: {active_count}")
    print(f"DEFAULT_LANGUAGE: {DEFAULT_LANGUAGE}")

    assert local_message == "Hello, Sora!"
    assert language_message == "Learning Python"
    assert shadow_message == "Local language is Java"
    assert active_count == 2
    assert DEFAULT_LANGUAGE == "Python"
