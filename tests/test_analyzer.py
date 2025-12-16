# import ast  # удалил, так как не используется
from src.analyzer import analyze_code


def test_analyze_code():
    code = """\"\"\"Doc\"\"\"
def f(): pass
"""
    result = analyze_code(code)
    assert isinstance(result, dict)
    assert "functions" in result
    assert "has_docstring" in result
