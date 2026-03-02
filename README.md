# eosdx-protocol

Primary standalone protocol-definition repository for Eos-Dx.

This repo is the source of truth for the shared hardware control contract used
by DiFRA and related services.

## Repository Role

- `protocol` ships versioned command definitions and gRPC assets.
- It can be consumed as an installed Python package.
- `difra` uses it to discover command schemas and protocol files at runtime.

## Contents

- `src/protocol/commands/v1/*.toml`: canonical command schemas
- `src/protocol/hub/v1/hub.proto`: canonical gRPC protocol definition
- `src/protocol/scripts/`: helper utilities for stub generation
- `src/protocol/__init__.py`: small API for locating bundled assets

Public helper functions:

- `protocol.package_root()`
- `protocol.commands_dir("v1")`
- `protocol.hub_dir("v1")`

## Layout

- `src/protocol/` contains the installable package and bundled assets.
- `tests/` contains guardrail checks to keep the asset bundle complete.

## Development

Install in editable mode and run the guardrail tests:

```bash
pip install -e .
pytest
```

Minimal usage:

```python
from protocol import commands_dir, hub_dir

command_root = commands_dir("v1")
proto_root = hub_dir("v1")
```
