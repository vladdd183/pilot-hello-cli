# Architecture — 01M3C3BFZYPCEART8NFS1B90KJ

Read-only product-code stage. Writers apply this file plus `delta.md` and `patterns/*.md` verbatim. Do not redesign.

Tree: commit `e416e60` (same as `main`). Package, tests, and `pyproject.toml` do not exist. CI still has the bootstrap escape.

## Locked decisions

| Topic | Decision | Source |
| --- | --- | --- |
| Layout | `src/` + setuptools | research/1.md (Typer FAQ, packaging.python.org) |
| Distribution name | `hello-cli` | PEP 621 example in research/1.md |
| Import package | `hello_cli` | research/1.md |
| Console script | `hello = hello_cli.cli:main` | PEP 621 `[project.scripts]` |
| CLI library | `argparse` (stdlib). Not Click. | intent `hello [--name NAME]`; research/1.md |
| `--name` default | `"World"` | research/1.md; omitted `--name` → `Hello, World!` |
| Greeting | `Hello, {name}!` with one trailing newline from `print()` | judge: `Hello, X!`; research/1.md |
| `--help` | `ArgumentParser.parse_args`; exit 0; text mentions `--name` | intent; argparse docs |
| Python | `>=3.12` | existing CI `python-version: "3.12"` |
| Dev extras | `pytest>=8`, `pytest-cov>=5` | research/1.md. No coverage gate. |
| Tests | exactly one unit test | intent «один unit-тест» |
| Test style | `subprocess.run(["hello", "--name", "Alice"], check=True, capture_output=True, text=True)` then `assert proc.stdout == "Hello, Alice!\n"` | research/1.md |
| Intent file | copy `specs/01M3C3BFZYPCEART8NFS1B90KJ/intent.md` → `docs/intent.md` byte-for-byte. No heading, no paraphrase. | recall.md, research/1.md |
| CI | `pip install -e ".[dev]"` then `pytest -q`. Drop `\|\| true` and the missing-test success path. | research/2.md, verify.md |
| Agent → PR | keep README contract; intake is Hermes `mega-intake` outside this repo. No label YAML, no auto-merge workflow file. | research/2.md |
| Merge | polish PRs: `gh pr merge --auto --squash` on green CI (already `deliver.merge: ci`) | research/2.md |

## Modules (create)

```
pyproject.toml                 # build-system setuptools; project.scripts hello
src/hello_cli/__init__.py      # __version__ = "0.1.0"
src/hello_cli/cli.py           # build_parser, greeting, main
docs/intent.md                 # overwrite stub with specs/.../intent.md
.github/workflows/ci.yml       # strict install + pytest
tests/test_cli.py              # one test (polish item)
```

`cli.py` symbols (do not rename):

- `build_parser() -> argparse.ArgumentParser` — `prog="hello"`, `--name` default `"World"`
- `greeting(name: str) -> str` — `f"Hello, {name}!"` with no newline in the string
- `main(argv: list[str] | None = None) -> int` — parse, `print(greeting(args.name))`, return `0`
- `if __name__ == "__main__": raise SystemExit(main())`

## Acceptance map

| Judge item | How it becomes true |
| --- | --- |
| `hello --name X` prints `Hello, X!` | console script + `greeting` + `print` |
| pytest green in CI | one test in `tests/`; CI always runs `pytest -q`; red pytest fails the job |
| `docs/intent.md` stores verbatim intention | byte-for-byte copy of `specs/01M3C3BFZYPCEART8NFS1B90KJ/intent.md` |
| issue label `agent` → PR auto-merge on green CI | README already states it; `mega-intake` + `deliver.merge: ci`. Do not add GitHub workflow for this in S5. |

## Out of scope (MUST NOT)

- Click, Typer, tox, ruff, black, mypy, coverage fail-under, Dependabot, CODEOWNERS
- Second test (`--help`, default name, stdin)
- Russian/translated greeting on stdout
- Extra intent files; editing `specs/.../intent.md`
- SB `work/tech/*`, replicator, Porto, Nix flakes
- GitHub label seed files or `auto-merge` workflow YAML (research/2.md: intake is outside this tree)
- Changing README (already correct)

## Fan-out (items.yaml)

Cap: `plan.parallelism.children` on this card is 6, which is a schema error (D6 F#1 cap is 3). `items.yaml` has **2** items so expand stays under 3.

1. **core** (`kind: core`, `role: brain`) — package, greeting, intent copy, strict CI. One compile/typecheck pass. Do not iterate tests.
2. **polish-tests** (`kind: polish`, `role: polish`) — `tests/test_cli.py` only. Depends on core.

Do not add a third writer on `.github/workflows/ci.yml` (hotspot if split).

## Writer contract

- Apply `delta.md` and every `patterns/*.md` literally (`apply_with: fast_apply`).
- Commit on `wt/01M3C3BFZYPCEART8NFS1B90KJ` inside this worktree.
- Wrong spec → `card_stage(action='replan')`. Do not improvise.
- Later edits to `patterns/` or `items.yaml` → needs-human; do not merge those edits silently.
