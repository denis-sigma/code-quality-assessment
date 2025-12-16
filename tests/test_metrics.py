import ast
from src.metrics import has_docstring

def test_has_docstring():
    code = """\"\"\"Doc\"\"\"
print(1)
"""
    tree = ast.parse(code)
    assert has_docstring(tree) is True
