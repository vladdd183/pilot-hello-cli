# Ревизия структур, паттернов и библиотек

Ответ на issue #4: обзор текущего состояния репозитория `pilot-hello-cli` на ветке `main` (после PR #1 и #3).

## Структура репозитория

| Путь | Назначение |
| --- | --- |
| `src/hello_cli/` | Пакет приложения (layout `src/`) |
| `src/hello_cli/cli.py` | Точка входа CLI: парсер, приветствие, `main` |
| `src/hello_cli/__init__.py` | Версия пакета |
| `tests/test_cli.py` | Интеграционные тесты через `subprocess` и консольный скрипт `hello` |
| `docs/intent.md` | Дословный интент проекта (не перефразировать) |
| `pyproject.toml` | Метаданные PEP 621, `[project.scripts]`, dev-зависимости |
| `.github/workflows/ci.yml` | CI: `pip install -e ".[dev]"`, затем `pytest -q` |
| `specs/` | Артефакты мегапроекта (архитектура, паттерны, verify); не меняются intake-PR без needs-human |

Дерево соответствует зафиксированной архитектуре в `specs/01M3C3BFZYPCEART8NFS1B90KJ/architecture.md`: один модуль CLI, один тестовый файл (сейчас два теста после флага `--loud`).

## Паттерны (megaproject `patterns/`)

Паттерны в `specs/01M3C3BFZYPCEART8NFS1B90KJ/patterns/` описывают, как собирался скелет. Соответствие коду:

| Паттерн | Файл | Статус |
| --- | --- | --- |
| `argparse-hello-cli` | `src/hello_cli/cli.py` | Соблюдён: `argparse`, `--name` (default `World`), `greeting` без `\n`, `print()` даёт перевод строки. Добавлен `--loud` (PR #3) — расширение поверх базового паттерна, uppercase через `greeting(..., loud=True)`. |
| `pyproject-console-script` | `pyproject.toml` | Соблюдён: `hello = "hello_cli.cli:main"`, пакеты из `src/`. |
| `unit-test-subprocess` | `tests/test_cli.py` | Соблюдён: вызов установленного `hello`, проверка `stdout` с `\n`. |
| `ci-pytest-strict` | `.github/workflows/ci.yml` | Соблюдён: установка editable + dev extras, строгий `pytest -q` без `|| true`. |
| `verbatim-intent` | `docs/intent.md` | Соблюдён: файл интента не переписывается произвольно. |

Вывод: базовые паттерны S5 соблюдены; единственное продуктовое отклонение от исходного «один unit-тест» — второй тест для `--loud` (осознанное расширение в PR #3).

## Используемые библиотеки

| Компонент | Библиотека | Роль |
| --- | --- | --- |
| CLI | **stdlib `argparse`** | Парсинг `--name`, `--loud`, `--help`. Click/Typer/docopt не используются (по архитектуре). |
| Сборка | **setuptools** (`build-backend` в `pyproject.toml`) | Установка пакета и консольного скрипта `hello`. |
| Тесты (dev) | **pytest** (≥8), **pytest-cov** (≥5, в extras без fail-under) | CI и локальный прогон. |
| Runtime | Только **Python ≥3.12** (stdlib) | Нет сторонних runtime-зависимостей. |

Внешних зависимостей в `[project.dependencies]` нет — минимальная поверхность поставки.

## Поведение CLI (кратко)

- `hello --name Alice` → `Hello, Alice!\n`
- `hello --name Bob --loud` → `HELLO, BOB!\n`
- `hello` (без `--name`) → `Hello, World!\n`
- `hello --help` — стандартная справка `argparse`

Приветствие на stdout остаётся **английским** (архитектура: «Russian/translated greeting on stdout» вне scope). Документация и ответы агентов по issue #4 — **на русском**.

## Рекомендации (без изменения архитектуры в этом PR)

1. Держать `docs/intent.md` синхронным с `specs/.../intent.md` при правках интента.
2. Новые флаги CLI — отдельные issue + тесты subprocess, как для `--loud`.
3. Правки `specs/*/patterns/` или `architecture.md` — только с меткой `needs-human`, не auto-merge.

---
*Документ добавлен по запросу issue #4; CI не менялся.*
