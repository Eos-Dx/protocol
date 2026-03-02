from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_protocol_layout_exists():
    assert (REPO_ROOT / "src" / "protocol" / "commands" / "v1").is_dir()
    assert (REPO_ROOT / "src" / "protocol" / "hub" / "v1" / "hub.proto").is_file()


def test_expected_core_commands_exist():
    cmd_dir = REPO_ROOT / "src" / "protocol" / "commands" / "v1"
    expected = {
        "initialize_detector.toml",
        "initialize_motion.toml",
        "get_state.toml",
        "move_to.toml",
        "home.toml",
        "start_exposure.toml",
        "pause.toml",
        "resume.toml",
        "stop.toml",
        "abort.toml",
    }
    found = {p.name for p in cmd_dir.glob("*.toml")}
    assert expected.issubset(found)
