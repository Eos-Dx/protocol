# eosdx-protocol

Standalone `protocol` assets extracted from `xrd-analysis`.

## Layout

- `src/` contains protocol assets and helper functions.
- `tests/` contains basic checks for bundled command and proto definitions.

## Contents

- command definitions in `commands/v1/*.toml`
- protocol hub definition in `hub/v1/hub.proto`
- helper script in `scripts/`

## Development

Install in editable mode:

```bash
pip install -e .
pytest
```
