"""可変長引数 *args と **kwargs を確認するサンプル。"""


def total_scores(*scores: int) -> int:
    """任意個数の点数を受け取り、合計を返す。"""
    # *args の形で受け取ると、複数の位置引数を tuple として扱える。
    # この関数では scores という名前で受け取っている。
    total = 0

    for score in scores:
        total += score

    return total


def join_words(separator: str, *words: str) -> str:
    """任意個数の単語を区切り文字で連結する。"""
    # 通常の引数と *args は組み合わせられる。
    # separator は通常の引数、words は可変長の位置引数となる。
    return separator.join(words)


def build_query(**params: str | int) -> str:
    """任意個数のキーワード引数からクエリ文字列を作る。"""
    # **kwargs の形で受け取ると、複数のキーワード引数を dict として扱える。
    # この関数では params という名前で受け取っている。
    parts = []

    for key, value in params.items():
        parts.append(f"{key}={value}")

    return "&".join(parts)


def build_message(title: str, **options: str | bool) -> str:
    """タイトルと任意のオプションから表示用メッセージを作る。"""
    # 通常の引数と **kwargs も組み合わせられる。
    # options は dict なので、get を使って任意項目を読み取れる。
    prefix = options.get("prefix", "")
    urgent = options.get("urgent", False)

    if urgent:
        return f"{prefix}[URGENT] {title}"

    return f"{prefix}{title}"


def run_variable_arguments() -> None:
    """可変長引数 *args と **kwargs を確認する。"""

    score_total = total_scores(80, 90, 70)
    print(f"total_scores の結果: {score_total}")

    joined_text = join_words("-", "Python", "Java", "SQL")
    print(f"join_words の結果: {joined_text}")

    query = build_query(page=1, size=20, sort="created")
    print(f"build_query の結果: {query}")

    normal_message = build_message("Deploy completed", prefix="INFO: ")
    urgent_message = build_message(
        "Production error",
        prefix="WARN: ",
        urgent=True,
    )

    print(f"通常メッセージ: {normal_message}")
    print(f"緊急メッセージ: {urgent_message}")

    assert score_total == 240
    assert joined_text == "Python-Java-SQL"
    assert query == "page=1&size=20&sort=created"
    assert normal_message == "INFO: Deploy completed"
    assert urgent_message == "WARN: [URGENT] Production error"
