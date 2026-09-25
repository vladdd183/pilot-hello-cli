---
name: verbatim-intent
applies_to: "docs/intent.md"
apply_with: fast_apply
---

## Intent

Overwrite the bootstrap stub so `docs/intent.md` is a byte-for-byte copy of `specs/01M3C3BFZYPCEART8NFS1B90KJ/intent.md`.

## Before

```markdown
# Intent — pilot-hello-cli

_Verbatim intent will be written by /mega / wb-mega start._
```

## After

```text
Сделай маленький CLI на Python: команда `hello [--name NAME]` печатает
приветствие, есть `--help`, pyproject.toml, один unit-тест, CI на GitHub
Actions (pytest). Репозиторий публичный. После S7 issue с меткой agent
должен порождать PR.
```

## Instruction for writer

1. Open `docs/intent.md` in the worktree.
2. Replace the entire file with the After block (four lines of Russian, no `#` heading).
3. Copy from `specs/01M3C3BFZYPCEART8NFS1B90KJ/intent.md` if anything looks different — those bytes win.
4. Do not wrap the text in quotes or add a trailing English translation.

## Do not

- Paraphrase.
- Keep the markdown title or italic stub.
- Edit `specs/01M3C3BFZYPCEART8NFS1B90KJ/intent.md`.
- Create a second intent file.
