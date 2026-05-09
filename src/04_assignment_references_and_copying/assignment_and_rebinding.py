"""変数への代入と再束縛を確認するサンプル。"""


def run_assignment_and_rebinding() -> None:
    """変数への代入、再束縛、ミュータブルな値の変更を確認する。"""

    # Python の変数は、値そのものを入れる箱というより、
    # オブジェクトに名前を付けるものとして考えると理解しやすい。
    language = "Python"
    same_language = language

    print(f"language: {language}")
    print(f"same_language: {same_language}")
    print(f"同じ文字列を指すか: {language is same_language}")

    # 再束縛は、変数名を別のオブジェクトに結び直す操作。
    # same_language を変更しても、language の指す先は変わらない。
    same_language = "Java"

    print(f"再束縛後の language: {language}")
    print(f"再束縛後の same_language: {same_language}")

    # list のようなミュータブルな値では、変数を通じて中身を変更できる。
    # ここでは scores という名前が、list オブジェクトを指している。
    scores = [80, 90]
    same_scores = scores

    print(f"変更前の scores: {scores}")
    print(f"変更前の same_scores: {same_scores}")

    # append は list オブジェクト自体を変更する。
    # scores と same_scores は同じ list を指しているため、両方から変化が見える。
    same_scores.append(100)

    print(f"変更後の scores: {scores}")
    print(f"変更後の same_scores: {same_scores}")

    # 変数に新しい list を代入すると、名前の指す先が変わる。
    # これは既存の list を変更する操作とは異なる。
    same_scores = [70, 75]

    print(f"再束縛後の scores: {scores}")
    print(f"再束縛後の same_scores: {same_scores}")

    assert language == "Python"
    assert same_language == "Java"
    assert scores == [80, 90, 100]
    assert same_scores == [70, 75]
    assert scores is not same_scores
