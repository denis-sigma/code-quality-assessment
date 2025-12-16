
---

**`docs/usage.md`**

````markdown
# Использование проекта

В этом документе описано, как настроить и использовать проект для оценки качества кода.

## 1. Установка

### Требования
- Python 3.8 или выше
- pip

### Настройка
```bash
# Клонируем репозиторий
git clone <URL вашего репозитория>
cd code-quality-assessment

# Создаем виртуальное окружение
python -m venv venv

# Для Windows
venv\Scripts\activate
# Для macOS/Linux
source venv/bin/activate

# Устанавливаем зависимости
pip install -r requirements.txt
````

## 2. Запуск анализа кода

Для проверки соответствия кода стандартам PEP 8 используйте:

```bash
flake8 src/
```

## 3. Запуск тестов

Запуск всех тестов проекта:

```bash
pytest tests/
```

С генерацией отчета о покрытии кода:

```bash
pytest --cov=src tests/
```

## 4. Пример использования функций

```python
# src/main.py
def add(a, b):
    """Складывает два числа"""
    return a + b

result = add(3, 5)
print(result)  # Вывод: 8
```

## 5. Артефакты CI/CD

* Отчеты о тестах (`results.xml`) и о проверке кода (`flake8-report.txt`) сохраняются как артефакты workflow.

```

---
```
