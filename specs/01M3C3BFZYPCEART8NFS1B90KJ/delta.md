# Spec delta — card 01M3C3BFZYPCEART8NFS1B90KJ

<!-- OpenSpec form. Writers apply this verbatim. Human may edit before implement. -->

## ADDED Requirements

### Requirement: Hello console script
The system SHALL install a console script named `hello` via PEP 621 `[project.scripts]` as `hello = hello_cli.cli:main` in `pyproject.toml`, using a src-layout package `hello_cli` and setuptools (`[build-system]` requires `setuptools>=68`, `[tool.setuptools.packages.find] where = ["src"]`).

#### Scenario: script is importable after editable install
- WHEN a developer runs `pip install -e ".[dev]"`
- THEN the `hello` executable is on PATH and `hello_cli.cli:main` is the entry point

### Requirement: Greeting stdout
The system SHALL print exactly `Hello, {name}!` followed by a single newline when `hello` runs. `--name` SHALL default to `World`. The greeting string SHALL be produced by `hello_cli.cli.greeting` and written with `print()`.

#### Scenario: named greeting
- WHEN the user runs `hello --name X`
- THEN stdout is exactly `Hello, X!` plus one trailing newline and the process exits 0

#### Scenario: default name
- WHEN the user runs `hello` with `--name` omitted
- THEN stdout is exactly `Hello, World!` plus one trailing newline and the process exits 0

### Requirement: Help flag
The system SHALL use stdlib `argparse.ArgumentParser` (`prog="hello"`) so `--help` works. The parser SHALL define `--name` with default `"World"`.

#### Scenario: help exits zero
- WHEN the user runs `hello --help`
- THEN the process exits 0 and the help text mentions `--name`

### Requirement: One unit test
The system SHALL ship exactly one unit test in `tests/test_cli.py` that runs the installed console script.

#### Scenario: Alice greeting
- WHEN CI or a developer runs `pytest -q`
- THEN `test_hello_name_alice` executes `subprocess.run(["hello", "--name", "Alice"], check=True, capture_output=True, text=True)` and asserts `proc.stdout == "Hello, Alice!\n"`, and pytest is green

### Requirement: Verbatim intent file
The system SHALL store the project intention in `docs/intent.md` as a byte-for-byte copy of `specs/01M3C3BFZYPCEART8NFS1B90KJ/intent.md` (no paraphrase, no extra heading).

#### Scenario: docs/intent.md matches spec intent
- WHEN a reviewer compares `docs/intent.md` to `specs/01M3C3BFZYPCEART8NFS1B90KJ/intent.md`
- THEN the two files are identical

### Requirement: Strict GitHub Actions pytest
The system SHALL run GitHub Actions job `test` on `ubuntu-latest` for `push` to `main` and `pull_request`, using `actions/checkout@v4` and `actions/setup-python@v5` with `python-version: "3.12"`. Install SHALL be `pip install -e ".[dev]"`. Tests SHALL be `pytest -q`. A failing pytest SHALL fail the job.

#### Scenario: pytest failure fails CI
- WHEN pytest returns non-zero
- THEN the GitHub Actions job `test` is red

#### Scenario: pytest green
- WHEN the one unit test passes
- THEN the GitHub Actions job `test` is green

### Requirement: Agent-labeled issues spawn PRs with auto-merge
The system SHALL keep the existing README contract: issues labeled `agent` (or comments with `/agent`) spawn Hermes kanban cards and PRs on `wt/<card>` with auto-merge on green CI. Intake SHALL remain the out-of-repo `mega-intake` skill; this repository MUST NOT add a label YAML or an auto-merge workflow file.

#### Scenario: README still states the contract
- WHEN a reader opens `README.md`
- THEN it still states that `agent` / `/agent` spawn cards → PRs on `wt/<card>` with auto-merge on green CI

#### Scenario: no in-repo intake workflow
- WHEN S5/S6 land
- THEN the tree has no new `.github` workflow whose job is label-intake or auto-merge; merge remains `gh pr merge --auto --squash` from mega-intake / polish

## MODIFIED Requirements

### Requirement: CI install and test steps
The bootstrap CI in `.github/workflows/ci.yml` SHALL be replaced by a strict install and test as specified under "Strict GitHub Actions pytest". Checkout, setup-python, runner, and `on:` triggers SHALL stay as they are.

#### Scenario: no swallowed install failure
- WHEN `pip install -e ".[dev]"` fails
- THEN the job fails (no `|| true` on pip)

## REMOVED Requirements

### Requirement: Bootstrap missing-test success
The system MUST NOT treat a missing `tests/` directory or missing `test_*.py` as a successful CI job and MUST NOT print `no tests yet — ok for bootstrap` as a substitute for pytest.

#### Scenario: tests are required
- WHEN the Test step runs
- THEN it invokes `pytest -q` unconditionally

### Requirement: Swallowed pip install
The system MUST NOT append `|| true` to `pip install` in `.github/workflows/ci.yml`.

#### Scenario: install errors propagate
- WHEN pip exits non-zero
- THEN the Install step is failed

