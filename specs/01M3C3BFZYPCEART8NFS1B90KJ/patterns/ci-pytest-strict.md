---
name: ci-pytest-strict
applies_to: ".github/workflows/ci.yml"
apply_with: fast_apply
---

## Intent

Make CI install the package with dev extras and fail when pytest fails.

## Before

```yaml
name: ci
on:
  push:
    branches: [main]
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install
        run: |
          if [ -f pyproject.toml ]; then
            pip install -e ".[dev]" 2>/dev/null || pip install -e . || true
          fi
          pip install pytest || true
      - name: Test
        run: |
          if [ -d tests ] || ls test_*.py >/dev/null 2>&1; then
            pytest -q
          else
            echo "no tests yet — ok for bootstrap"
          fi
```

## After

```yaml
name: ci
on:
  push:
    branches: [main]
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install
        run: pip install -e ".[dev]"
      - name: Test
        run: pytest -q
```

## Instruction for writer

1. Replace `.github/workflows/ci.yml` entirely with the After block.
2. Keep `actions/checkout@v4`, `actions/setup-python@v5`, and Python 3.12.
3. Do not add extra jobs, caches, or coverage upload.

## Do not

- Restore `|| true`.
- Restore the missing-test `echo` branch.
- Add a GitHub workflow for `agent` labels or auto-merge.
- Change `on:` triggers.
