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


def test_hello_name_bob_loud() -> None:
    proc = subprocess.run(
        ["hello", "--name", "Bob", "--loud"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert proc.stdout == "HELLO, BOB!\n"

