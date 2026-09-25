---
name: argparse-hello-cli
applies_to: "src/hello_cli/cli.py"
apply_with: fast_apply
---

## Intent

Implement `hello [--name NAME]` with argparse so stdout is `Hello, {name}!` plus a newline.

## Before

File does not exist in commit `e416e60`.

## After

```python
"""hello CLI: print a greeting."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hello", description="Print a greeting.")
    parser.add_argument("--name", default="World", help="Name to greet")
    return parser


def greeting(name: str) -> str:
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(greeting(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Instruction for writer

1. Create `src/hello_cli/cli.py` with the After block only.
2. Keep symbol names `build_parser`, `greeting`, and `main`.
3. `greeting` must not include a newline; `print()` supplies it.

## Do not

- Import click, typer, or docopt.
- Print a Russian greeting.
- Change the default away from `"World"`.
- Add subcommands or positional name arguments.
