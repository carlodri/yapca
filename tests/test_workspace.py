def test_get_all_workspaces(clk_sess, test_settings):
    workspaces = clk_sess.workspace.get_all_workspaces()
    assert len(workspaces.root) == 2


def test_get_workspace_info(clk_sess, test_settings):
    workspace = clk_sess.workspace.get_workspace_info(test_settings.workspace_id)
    assert workspace.id == test_settings.workspace_id
