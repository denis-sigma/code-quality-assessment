import ast


def has_docstring(tree: ast.AST) -> bool:
    return ast.get_docstring(tree) is not None


def count_functions(tree: ast.AST) -> int:
    return len(
        [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    )
