"""break / continue の基本を確認するサンプル。"""


def run_break_continue_examples() -> None:
    """ループの途中終了とスキップを確認する。"""

    # break は、ループを途中で終了するときに使う。
    # 次の例では、最初に見つかった偶数を記録した時点でループを抜ける。
    numbers = [1, 3, 5, 8, 10]
    first_even = None

    for number in numbers:
        if number % 2 == 0:
            first_even = number
            break

    print(f"最初に見つかった偶数: {first_even}")

    # continue は、その回の残りの処理をスキップして次のループへ進む。
    # 次の例では、負の値を無効な値として集計対象から外す。
    raw_scores = [80, -1, 72, -5, 90]
    valid_scores = []

    for score in raw_scores:
        if score < 0:
            continue

        valid_scores.append(score)

    print(f"有効なスコア: {valid_scores}")

    # while と break を組み合わせると、条件を満たした時点で抜けられる。
    # while True は無限ループの形だが、break の条件がないと危険となる。
    attempts = 0

    while True:
        attempts += 1

        if attempts == 3:
            break

    print(f"break までの試行回数: {attempts}")

    assert first_even == 8
    assert valid_scores == [80, 72, 90]
    assert attempts == 3
