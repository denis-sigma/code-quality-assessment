import sys
from src.report import generate_report

if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        code = f.read()

    generate_report(code)
