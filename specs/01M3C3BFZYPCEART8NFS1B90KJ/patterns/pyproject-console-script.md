---
name: pyproject-console-script
applies_to: "pyproject.toml"
apply_with: fast_apply
---

## Intent

Add the setuptools pyproject that installs console script `hello` from `hello_cli.cli:main`.

## Before

File does not exist in commit `e416e60`.

## After

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "hello-cli"
version = "0.1.0"
description = "Tiny hello CLI"
requires-python = ">=3.12"
readme = "README.md"

[project.optional-dependencies]
dev = ["pytest>=8", "pytest-cov>=5"]

[project.scripts]
hello = "hello_cli.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

## Instruction for writer

1. Create `pyproject.toml` at the repo root of this worktree with the After block only.
2. Create `src/hello_cli/__init__.py` containing exactly:

```python
"""Tiny hello CLI."""

__version__ = "0.1.0"
```

3. Do not add `[project.dependencies]`, a `packages =` list, or a `setup.py`.

## Do not

- Use Poetry, Hatchling, Flit, or PDM as the build backend.
- Name the import package `hello` or `hello-cli`.
- Add ruff/mypy/coverage `fail_under` tool tables.
- Edit `README.md`.
