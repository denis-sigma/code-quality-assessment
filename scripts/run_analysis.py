import sys
import os

# Добавляем корень проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.report import generate_report

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python scripts/run_analysis.py <путь_к_файлу>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"Файл не найден: {file_path}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    generate_report(code)
