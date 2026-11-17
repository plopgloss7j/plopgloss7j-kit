# plopgloss7j-kit

Summarize numeric CSV columns (n / min / max / mean).

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m plopgloss7j_kit.cli --help
```

```python
from plopgloss7j_kit.core import Plopgloss7jTool

tool = Plopgloss7jTool()
print(tool)
```

## Layout

```
plopgloss7j_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 plopgloss7j
