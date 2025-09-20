# Как вносить изменения

## Ветки
- Основная: `main` (защищена), рабочая: `dev`.
- Фичи: `feature/<кратко>`, багфиксы: `fix/<кратко>`, техдолг: `chore/<кратко>`.

## Коммиты (Conventional Commits)
- `feat: ...` — новая фича
- `fix: ...` — исправление
- `chore: ...` — обслуживание/мелочи
- `docs: ...` — документация
- `test: ...` — тесты
- `refactor: ...` — без изменения поведения

## Процесс
1. Ответвитесь от `dev`: `git checkout dev && git pull && git checkout -b feature/...`
2. Пишите код + тесты.
3. `git commit -m "feat(ingestion): add ws loader"`
4. `git push -u origin feature/...` → создайте PR в `dev`.
5. Дождитесь зелёного CI и 1 ревью.
6. Раз в неделю мержим `dev` → `main` через PR.

## Стандарты
- Тесты: `pytest -q` должны быть зелёные.
- Линтеры: black/ruff (автоформатирование).
- Секреты в git не коммитить (используем .env.sample + keyring).
