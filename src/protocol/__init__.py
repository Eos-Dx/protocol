"""Helpers for locating bundled protocol definitions."""

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent


def package_root() -> Path:
    return PACKAGE_ROOT


def commands_dir(version: str = "v1") -> Path:
    return PACKAGE_ROOT / "commands" / str(version)


def hub_dir(version: str = "v1") -> Path:
    return PACKAGE_ROOT / "hub" / str(version)


__all__ = ["PACKAGE_ROOT", "package_root", "commands_dir", "hub_dir"]
