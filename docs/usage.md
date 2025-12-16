
---
**`docs/usage.md`**

````markdown
# Использование проекта

## Запуск анализа кода
```bash
flake8 src/
````

## Запуск тестов

```bash
pytest tests/
pytest --cov=src tests/
```

## Пример функции

```python
def add(a, b):
    return a + b
```

````

**`docs/ci_cd.md`**  
```markdown
# CI/CD Workflow

Workflow на GitHub Actions выполняет:
- Проверку кода через flake8 и black
- Запуск тестов через pytest
- Сохранение отчетов как артефакты
- Автоматический запуск каждое воскресенье
````

---

