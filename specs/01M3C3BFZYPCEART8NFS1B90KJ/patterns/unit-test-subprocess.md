---
name: unit-test-subprocess
applies_to: "tests/test_cli.py"
apply_with: fast_apply
---

## Intent

Add the single unit test the intent requires: installed `hello --name Alice` prints `Hello, Alice!`.

## Before

File does not exist in commit `e416e60`. There is no `tests/` directory.

## After

```python
"""One unit test: installed console script prints the judge greeting."""

from __future__ import annotations

import subprocess


def test_hello_name_alice() -> None:
    proc = subprocess.run(
        ["hello", "--name", "Alice"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert proc.stdout == "Hello, Alice!\n"
```

## Instruction for writer

1. Create `tests/test_cli.py` with the After block only.
2. Do not add `tests/__init__.py` unless import fails without it (prefer no `__init__.py`).
3. Do not add a second test function.

## Do not

- Use `pytest` fixtures, `capsys`, or import `greeting` instead of the console script.
- Assert a translation of «приветствие».
- Touch `src/`, `pyproject.toml`, `docs/intent.md`, or `.github/workflows/ci.yml`.
- Add tox, coverage fail-under, or parametrize.
