"""深いコピーを確認するサンプル。"""

import copy


def run_deep_copy_examples() -> None:
    """深いコピーが内側のミュータブルな値もコピーすることを確認する。"""

    # deepcopy は、外側だけでなく内側のミュータブルな値もコピーする。
    # ネストした list や dict を安全に複製したいときに使う。
    original_user = {
        "name": "Sora",
        "scores": [80, 90],
        "profile": {
            "language": "Python",
            "level": "beginner",
        },
    }
    copied_user = copy.deepcopy(original_user)

    print(f"original_user: {original_user}")
    print(f"copied_user: {copied_user}")
    print(f"外側の dict が同じか: {original_user is copied_user}")
    print(f"scores が同じか: {original_user['scores'] is copied_user['scores']}")
    print(f"profile が同じか: {original_user['profile'] is copied_user['profile']}")

    # コピー側のネストした値を変更しても、元の値には影響しない。
    copied_user["scores"].append(100)
    copied_user["profile"]["level"] = "intermediate"

    print(f"変更後の original_user: {original_user}")
    print(f"変更後の copied_user: {copied_user}")

    # 比較用に、浅いコピーの挙動も確認する。
    shallow_user = copy.copy(original_user)
    shallow_user["scores"].append(70)
    shallow_user["profile"]["level"] = "advanced"

    print(f"浅いコピー変更後の original_user: {original_user}")
    print(f"浅いコピー変更後の shallow_user: {shallow_user}")

    assert copied_user == {
        "name": "Sora",
        "scores": [80, 90, 100],
        "profile": {
            "language": "Python",
            "level": "intermediate",
        },
    }
    assert original_user == {
        "name": "Sora",
        "scores": [80, 90, 70],
        "profile": {
            "language": "Python",
            "level": "advanced",
        },
    }
    assert shallow_user == {
        "name": "Sora",
        "scores": [80, 90, 70],
        "profile": {
            "language": "Python",
            "level": "advanced",
        },
    }
    assert original_user is not copied_user
    assert original_user["scores"] is not copied_user["scores"]
    assert original_user["profile"] is not copied_user["profile"]
    assert original_user is not shallow_user
    assert original_user["scores"] is shallow_user["scores"]
    assert original_user["profile"] is shallow_user["profile"]
