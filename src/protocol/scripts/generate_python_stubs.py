#!/usr/bin/env python3
"""Generate Python gRPC stubs from canonical hardware protocol."""

from __future__ import annotations

import subprocess
import sys
from importlib import resources
from pathlib import Path


def _ensure_init_files(base: Path, rel_pkg_path: Path) -> None:
    current = base
    for part in rel_pkg_path.parts:
        current = current / part
        current.mkdir(parents=True, exist_ok=True)
        init_file = current / "__init__.py"
        if not init_file.exists():
            init_file.write_text("")


def _run_protoc(proto_file: Path, include_dirs: list[Path], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable,
        "-m",
        "grpc_tools.protoc",
        *(f"-I{inc}" for inc in include_dirs),
        f"--python_out={out_dir}",
        f"--grpc_python_out={out_dir}",
        str(proto_file),
    ]
    subprocess.run(cmd, check=True)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    proto_file = repo_root / "src/protocol/hub/v1/hub.proto"

    try:
        grpc_include = Path(str(resources.files("grpc_tools") / "_proto"))
    except Exception as exc:  # pragma: no cover - depends on environment
        print(f"grpc_tools is required to generate stubs: {exc}", file=sys.stderr)
        return 2

    include_dirs = [repo_root / "src/protocol", grpc_include]

    generated_root = repo_root / "src/protocol/generated"
    _run_protoc(proto_file, include_dirs, generated_root)
    _ensure_init_files(generated_root, Path("hub/v1"))

    print("Generated Python stubs from canonical protocol")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
