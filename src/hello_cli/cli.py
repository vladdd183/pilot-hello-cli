"""hello CLI: print a greeting."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hello", description="Print a greeting.")
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.add_argument(
        "--loud",
        action="store_true",
        help="Print the greeting in uppercase",
    )
    return parser


def greeting(name: str, loud: bool = False) -> str:
    text = f"Hello, {name}!"
    return text.upper() if loud else text


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(greeting(args.name, loud=args.loud))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

