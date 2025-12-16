---

# Code Quality Assessment

![Python](https://img.shields.io/badge/python-3.12-blue?logo=python\&logoColor=white)
![Build Status](https://img.shields.io/github/actions/workflow/status/<OWNER>/<REPO>/code-quality.yml?branch=main)
![Flake8](https://img.shields.io/badge/flake8-compliant-green)

Серийный номер тома: **7EC9-95E2**

## 📖 Описание проекта

Проект **Code Quality Assessment** предназначен для анализа качества Python-кода с использованием:

* **Flake8** — проверка стиля и ошибок
* **Pytest** — запуск тестов и проверка функционала

Проект помогает поддерживать стандарты качества кода и снижать количество ошибок на ранних этапах разработки.

## 🗂 Структура проекта

```text
code-quality-assessment/
├── .github/workflows/        # GitHub Actions workflows
├── data/                     # Исходные данные
├── docs/                     # Документация
├── scripts/                  # Вспомогательные скрипты
├── src/                      # Исходный код
├── tests/                    # Тесты
└── venv/                     # Виртуальное окружение
```

## ⚙️ Установка

```bash
git clone <URL репозитория>
cd code-quality-assessment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
pip install -r requirements.txt
```

## 🧪 Использование

### Проверка качества кода

```bash
flake8 src/ --statistics
```

Пример вывода flake8:

```
src/module.py:12:1: F401 'os' imported but unused
src/module.py:45:5: E303 too many blank lines (2)
2     F401 'os' imported but unused
1     E303 too many blank lines (2)
```

### Запуск тестов

```bash
pytest tests/ --maxfail=1 --disable-warnings -q
```

Пример вывода pytest:

```
============================= test session starts =============================
platform linux -- Python 3.12.0, pytest-9.0.2
collected 5 items

tests/test_module.py .....                                             [100%]

============================== 5 passed in 0.12s ==============================
```

### Пример использования функций из `src`

```python
from src.module import function_name

result = function_name(arg1, arg2)
print(result)
```

## 🤖 GitHub Actions Workflow

Workflow запускается автоматически:

* **По расписанию:** каждое воскресенье в 00:00
* **При пуше** в ветку `main`

Пример файла `.github/workflows/code-quality.yml`:

```yaml
name: Code Quality

on:
  push:
    branches: [ main ]
  schedule:
    - cron: "0 0 * * 0"

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.12
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest
      - name: Run flake8
        run: flake8 src/ --exit-zero --statistics
      - name: Run tests
        run: pytest tests/ --maxfail=1 --disable-warnings -q
      - name: Upload Artifacts
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: tests/results/
```

## 📄 Лицензия

Проект распространяется под лицензией **MIT License**.

---
