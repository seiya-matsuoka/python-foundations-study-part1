"""浅いコピーを確認するサンプル。"""

import copy


def run_shallow_copy_examples() -> None:
    """浅いコピーが外側だけを別オブジェクトにすることを確認する。"""

    # 浅いコピーは、外側のコレクションだけを新しく作る。
    # 内側にミュータブルな値がある場合、その中身まではコピーしない。
    original_scores = [["Sora", 80], ["Mio", 90]]

    copied_by_slice = original_scores[:]
    copied_by_list = list(original_scores)
    copied_by_copy = copy.copy(original_scores)

    print(f"original_scores: {original_scores}")
    print(f"copied_by_slice: {copied_by_slice}")
    print(f"copied_by_list: {copied_by_list}")
    print(f"copied_by_copy: {copied_by_copy}")

    print(f"外側が同じか: {original_scores is copied_by_slice}")
    print(f"内側が同じか: {original_scores[0] is copied_by_slice[0]}")

    # 外側の list に要素を追加しても、元の list には影響しない。
    copied_by_slice.append(["Ren", 70])

    print(f"外側追加後の original_scores: {original_scores}")
    print(f"外側追加後の copied_by_slice: {copied_by_slice}")

    # 内側の list は共有されたまま。
    # そのため、内側を変更すると元の list にも変化が見える。
    copied_by_slice[0][1] = 100

    print(f"内側変更後の original_scores: {original_scores}")
    print(f"内側変更後の copied_by_slice: {copied_by_slice}")

    # dict の浅いコピーでも、ネストした list は共有される。
    original_user = {
        "name": "Sora",
        "skills": ["Python", "SQL"],
    }
    copied_user = original_user.copy()

    copied_user["name"] = "Mio"
    copied_user["skills"].append("Git")

    print(f"original_user: {original_user}")
    print(f"copied_user: {copied_user}")

    assert original_scores == [["Sora", 100], ["Mio", 90]]
    assert copied_by_slice == [["Sora", 100], ["Mio", 90], ["Ren", 70]]
    assert copied_by_list == [["Sora", 100], ["Mio", 90]]
    assert copied_by_copy == [["Sora", 100], ["Mio", 90]]
    assert original_scores is not copied_by_slice
    assert original_scores[0] is copied_by_slice[0]
    assert original_user == {
        "name": "Sora",
        "skills": ["Python", "SQL", "Git"],
    }
    assert copied_user == {
        "name": "Mio",
        "skills": ["Python", "SQL", "Git"],
    }
    assert original_user is not copied_user
    assert original_user["skills"] is copied_user["skills"]
