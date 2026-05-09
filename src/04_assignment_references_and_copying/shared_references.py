"""参照の共有による値の見え方を確認するサンプル。"""


def run_shared_references() -> None:
    """同じオブジェクトを複数の変数から参照する例を確認する。"""

    # list を代入しても、list の中身が自動でコピーされるわけではない。
    # users と active_users は、同じ list オブジェクトを指す。
    users = ["Sora", "Mio"]
    active_users = users

    print(f"users: {users}")
    print(f"active_users: {active_users}")
    print(f"同じ list を指すか: {users is active_users}")

    # active_users から append しているが、変更されるのは同じ list。
    # そのため users から見ても "Ren" が追加されている。
    active_users.append("Ren")

    print(f"追加後の users: {users}")
    print(f"追加後の active_users: {active_users}")

    # ネストした list でも、参照の共有は起きる。
    # teams の中には、別の list が要素として入っている。
    backend_team = ["Java", "Spring"]
    frontend_team = ["TypeScript", "React"]
    teams = [backend_team, frontend_team]

    # assigned_teams は teams と同じ外側の list を指す。
    assigned_teams = teams
    assigned_teams[0].append("Python")

    print(f"teams: {teams}")
    print(f"assigned_teams: {assigned_teams}")

    # 新しい list を作ると、外側の list は別物になる。
    # ただし、この書き方では内側の list は共有されたままとなる。
    copied_teams = teams[:]
    copied_teams.append(["SQL", "PostgreSQL"])
    copied_teams[0].append("Kotlin")

    print(f"teams after copied_teams change: {teams}")
    print(f"copied_teams: {copied_teams}")
    print(f"外側の list が同じか: {teams is copied_teams}")
    print(f"内側の list が同じか: {teams[0] is copied_teams[0]}")

    assert users == ["Sora", "Mio", "Ren"]
    assert active_users == ["Sora", "Mio", "Ren"]
    assert users is active_users
    assert teams == [
        ["Java", "Spring", "Python", "Kotlin"],
        ["TypeScript", "React"],
    ]
    assert copied_teams == [
        ["Java", "Spring", "Python", "Kotlin"],
        ["TypeScript", "React"],
        ["SQL", "PostgreSQL"],
    ]
    assert teams is not copied_teams
    assert teams[0] is copied_teams[0]
