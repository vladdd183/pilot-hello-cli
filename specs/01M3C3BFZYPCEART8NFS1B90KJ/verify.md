# Verify — research (stage verify)

Spec: `01M3C3BFZYPCEART8NFS1B90KJ`  
Worktree: `bf5ce801` @ `/var/lib/hermes/workspace/mega/pilot-hello-cli/.worktrees/01M3C3BFZYPCEART8NFS1B90KJ`  
Verifier: `t_39bfd702` · 2026-09-25

## Verdict

| Area | Result |
|------|--------|
| Research URLs (HTTP) | **ok** — 9/9 return 200 (curl -L, 2026-09-25) |
| `questions.yaml` q1 coverage | **ok** |
| `questions.yaml` q2 coverage | **ok** |
| Card acceptance (repo implementation) | **fail** — expected pre–S5; documented below for downstream judge |

Research is sufficient to unblock **architect** (`t_afa8fb4c`). Implementation acceptance remains for core/polish/integrate.

---

## URL checks

| URL | HTTP | Cited in |
|-----|------|----------|
| packaging.python.org … `#creating-executable-scripts` | 200 | research/1.md |
| docs.python.org/3/library/argparse.html | 200 | research/1.md |
| docs.python.org/3/library/functions.html#print | 200 | research/1.md |
| docs.pytest.org … capture-stdout-stderr | 200 | research/1.md |
| docs.github.com … workflow-syntax … `#jobsjob_idsteps` | 200 | research/2.md |
| docs.pytest.org … reference … `#command-line-flags` | 200 | research/2.md |
| docs.github.com … protected-branches … `#require-status-checks-before-merging` | 200 | research/2.md |
| docs.github.com … automatically-merging-a-pull-request | 200 | research/2.md |
| cli.github.com/manual/gh_pr_merge | 200 | research/2.md |

---

## Question coverage

### q1 — Python `hello` CLI (`research/1.md`)

| Item (from `questions.yaml` q1) | Result | Evidence |
|-----------------------------------|--------|----------|
| `hello --name X` → exactly `Hello, X!` | ok | research/1.md §5–6; ties to card acceptance |
| `--help` | ok | research/1.md §4 (argparse default) |
| `pyproject.toml` + console script `hello` | ok | research/1.md §3, PEP 621 table + PyPA quote |
| One unit test for greeting | ok | research/1.md §7 (subprocess / capsys) |
| Stdout when `--name` omitted | ok | research/1.md §5 — default `World` → `Hello, World!` |
| argparse vs click | ok | research/1.md §4 — recommends argparse |
| Trailing newline | ok | research/1.md §6 — `print()` → `\n` |
| Copy `specs/…/intent.md` → `docs/intent.md` byte-for-byte | ok | research/1.md §1, §8; **repo still stub** (see acceptance) |
| Hints: spec intent, recall, docs, PEP 621, argparse | ok | All referenced in research/1.md |

### q2 — CI + `agent` → PR (`research/2.md`)

| Item (from `questions.yaml` q2) | Result | Evidence |
|-----------------------------------|--------|----------|
| CI must fail when pytest fails / install fails | ok | research/2.md §1–2 quotes `.github/workflows/ci.yml` L14–26 |
| Remove bootstrap “no tests yet” success path | ok | research/2.md §2 table |
| Issue label `agent` → PR + auto-merge on green CI | ok | research/2.md §3–4 (README + mega-intake + AGENTS.md) |
| No SB `work/tech` / replicator import | ok | research/2.md §6 |
| Hints: ci.yml, README, mega-intake, auto-merge, `pytest -q` | ok | research/2.md §1–5 |
| Label seed / workflow absent in tree | ok | research/2.md §4, recall.md L18–19 |

---

## Card acceptance (implementation snapshot)

Judge criteria from wb-card; **not** required to pass at research-verify.

| Acceptance | Result | Evidence |
|------------|--------|----------|
| CLI `hello --name X` prints `Hello, X!` | **fail** | No `pyproject.toml`, no package, no `hello` on PATH (`test -f pyproject.toml` → absent) |
| pytest green in CI | **fail** | No `tests/`; `.github/workflows/ci.yml` L22–25 exits 0 with “no tests yet — ok for bootstrap” |
| `docs/intent.md` holds verbatim intention | **fail** | Stub L1–3 vs `specs/…/intent.md` Russian text (`diff` 2026-09-25) |
| issue label `agent` → PR auto-merge on green CI | **fail** | README documents process; no label workflow in repo; intake is Hermes ops (research/2.md §4) |

---

## Artifacts checked

- `specs/01M3C3BFZYPCEART8NFS1B90KJ/questions.yaml` — q1, q2 present (`verify: true`)
- `specs/01M3C3BFZYPCEART8NFS1B90KJ/research/1.md`, `research/2.md` — present
- `.github/workflows/ci.yml` — bootstrap behavior confirmed on worktree
