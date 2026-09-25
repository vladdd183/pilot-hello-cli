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
