# Recall — 01M3C3BFZYPCEART8NFS1B90KJ

Stage recall, read-only. No implementation on this card.

## Already exists

Repo worktree `wt/01M3C3BFZYPCEART8NFS1B90KJ` is commit `e416e60` (2026-09-25, hermes-mega): "chore: megaproject bootstrap (CI, labels seed, intent stub)". Same commit as `main`. Untracked: `specs/01M3C3BFZYPCEART8NFS1B90KJ/` (`intent.md`, empty `delta.md`). No Python package.

- `docs/intent.md` is a stub: "Verbatim intent will be written by /mega / wb-mega start." It does not yet store the intention. Acceptance still requires that file to hold the verbatim text.
- Verbatim intention lives in `specs/01M3C3BFZYPCEART8NFS1B90KJ/intent.md`:

> Сделай маленький CLI на Python: команда `hello [--name NAME]` печатает приветствие, есть `--help`, pyproject.toml, один unit-тест, CI на GitHub Actions (pytest). Репозиторий публичный. После S7 issue с меткой agent должен порождать PR.

- `README.md` — issues labeled `agent` (or `/agent` comments) spawn kanban cards, PRs on `wt/<card>`, auto-merge on green CI.
- `.github/workflows/ci.yml` — `push` to `main` and `pull_request`; ubuntu-latest; Python 3.12; `actions/checkout@v4` + `actions/setup-python@v5`. Install swallows failure (`pip install … || true`). Pytest runs only if `tests/` or `test_*.py` exists; otherwise the job prints "no tests yet — ok for bootstrap" and succeeds. `pytest -q` itself is not masked with `|| true`.
- `.gitignore` — `.worktrees/`, `__pycache__/`, `*.egg-info/`, `.venv/`, `dist/`, `.pytest_cache/`.
- `specs/01M3C3BFZYPCEART8NFS1B90KJ/delta.md` — empty OpenSpec (ADDED/MODIFIED/REMOVED only).
- Commit message says "labels seed". No label file is in the tree. No `hello` entry point, no `pyproject.toml`, no unit test, no auto-merge workflow.

Acceptance the judge reads:

- `hello --name X` prints `Hello, X!`
- pytest green in CI
- `docs/intent.md` stores the verbatim intention (not true yet; stub only)
- issue with label `agent` → PR with auto-merge on green CI

Prior recall `t_aea1cc45` (archived) wrote `specs/01M3C20DEE483A1HPAZTY34KVM/recall.md` on worktree `01M3C20D5X5TRW2VWVNRAHR2ZY` (commit `9217dcd`). That note claimed `docs/intent.md` already held the Russian text. On this tree at `e416e60` it does not. Do not copy that claim.

`code_search` (Relace) returned 401 "No active credentials for provider: relace". Tree is one commit; listing was enough.

## Reuse

- Copy `specs/01M3C3BFZYPCEART8NFS1B90KJ/intent.md` into `docs/intent.md` byte-for-byte. Do not paraphrase.
- Greeting the judge checks is `Hello, X!` (acceptance), not a free translation of "приветствие".
- CI skeleton: checkout v4, setup-python v5, Python 3.12, `pytest -q`. Drop the missing-test success path and the install `|| true` so a red pytest fails the job.
- README contract: label `agent` → card → `wt/<card>` → auto-merge only on green CI.
- Empty spec delta is the OpenSpec form later writers fill. Do not add a second intent file.
- Governance already on the card: `patterns/`, `items.yaml`, `architecture.md`, budget breach → needs-human, do not merge. Stages are already spawned (recall → research_plan `t_e19aa323` → architect → core → integrate). Do not add stages.

## Avoid

- SB `work/tech/` (`/var/lib/hermes/workspace/meta-intent/corpus/sb/work/tech`): agent-os, gost-conveyor, nix-ipfs, nixpkgs-governance-crisis, omniroute-hermes, psychic-paper, swh-ipfs-bridge, tessera. No hello CLI. Do not import those designs. Workspace `SB/` has no `work/tech/`.
- Replicator (`pc-home/Desktop/kwork/replicator`, Hyper-Porto self-evolution, `foxdocs/HANDOFF-NOTES.md`) is not this CLI. Do not reuse Porto, Nix flakes, or that pipeline.
- Hermes sessions (profile mega): no hits for `pilot-hello`, `hello --name`, or megaproject.
- Do not keep the bootstrap escape (skip pytest when tests are missing; `|| true` on pip).
- Do not write `architecture.md`, `patterns/`, or `items.yaml`.
- Card `plan.parallelism.children: 6` exceeds cap 3 (D6 F#1). Do not fan out past 3. This card's budget is `children: 0`.
