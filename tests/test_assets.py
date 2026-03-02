from protocol import commands_dir, hub_dir


def test_bundled_assets_exist():
    assert commands_dir("v1").is_dir()
    assert (commands_dir("v1") / "move_to.toml").is_file()
    assert (hub_dir("v1") / "hub.proto").is_file()
