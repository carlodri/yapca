def test_get_logged_in_user(clk_sess, test_settings):
    user = clk_sess.user.get_logged_in_user()
    assert user.id == test_settings.user_id
    assert user.activeWorkspace == test_settings.workspace_id


def test_find_all_users_in_workspace(clk_sess, test_settings):
    users = clk_sess.user.find_all_users_in_workspace(
        workspace_id=test_settings.workspace_id
    )
    assert users[0].id == test_settings.user_id
    assert users[0].activeWorkspace == test_settings.workspace_id


def test_get_member_profile(clk_sess, test_settings):
    member = clk_sess.user.get_member_profile(
        workspace_id=test_settings.workspace_id,
        user_id=test_settings.user_id,
    )
    assert member.name == "Carlo Dri"
