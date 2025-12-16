import ast
from src.metrics import has_docstring, count_functions


def analyze_code(code: str) -> dict:
    tree = ast.parse(code)

    return {
        "has_docstring": has_docstring(tree),
        "functions": count_functions(tree),
    }
