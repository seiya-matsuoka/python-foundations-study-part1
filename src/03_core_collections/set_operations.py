"""set の基本操作を確認するサンプル。"""


def run_set_operations() -> None:
    """set の作成、追加、削除、検索、集合演算、反復を確認する。"""

    # set は、重複しない要素の集まり。
    # 順序を前提にせず、membership 判定や集合演算に向く。
    skills = {"Python", "Java", "SQL"}
    print(f"最初の skills: {skills}")

    # 同じ値を複数書いても、set では1つにまとめられる。
    duplicated_numbers = {1, 2, 2, 3, 3, 3}  # noqa: B033
    print(f"重複を含む set: {duplicated_numbers}")

    # add は要素を追加する。
    # 既に存在する値を追加しても、重複は増えない。
    skills.add("Git")
    skills.add("Python")
    print(f"追加後の skills: {skills}")

    # discard は指定した要素を削除する。
    # 要素が存在しない場合でも例外にならない。
    skills.discard("SQL")
    skills.discard("Docker")
    print(f"削除後の skills: {skills}")

    # in は set でよく使う。
    # 値が含まれるかどうかを簡潔に確認できる。
    has_python = "Python" in skills
    has_sql = "SQL" in skills

    print(f"Python を含むか: {has_python}")
    print(f"SQL を含むか: {has_sql}")

    backend_skills = {"Java", "SQL", "Spring"}
    scripting_skills = {"Python", "Shell", "SQL"}

    # | は和集合、& は積集合、- は差集合を表す。
    union_skills = backend_skills | scripting_skills
    common_skills = backend_skills & scripting_skills
    backend_only = backend_skills - scripting_skills

    print(f"和集合: {union_skills}")
    print(f"積集合: {common_skills}")
    print(f"差集合: {backend_only}")

    # set は順序を前提にしない。
    # 表示や比較で順序が必要な場合は sorted を使う。
    sorted_skills = sorted(skills)
    print(f"並び替えた skills: {sorted_skills}")

    # for を使うと set も反復できる。
    # ただし、取り出される順番には意味を持たせない方がよい。
    collected_skills = []

    for skill in skills:
        collected_skills.append(skill)

    print(f"反復で集めた skills: {collected_skills}")

    assert duplicated_numbers == {1, 2, 3}
    assert skills == {"Python", "Java", "Git"}
    assert has_python is True
    assert has_sql is False
    assert union_skills == {"Java", "SQL", "Spring", "Python", "Shell"}
    assert common_skills == {"SQL"}
    assert backend_only == {"Java", "Spring"}
    assert sorted_skills == ["Git", "Java", "Python"]
    assert set(collected_skills) == skills
