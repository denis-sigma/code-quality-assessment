import ast
from src.analyzer import analyze_code

def test_analyze_code():
    code = """\"\"\"Doc\"\"\"
def f(): pass
"""
    result = analyze_code(code)
    assert isinstance(result, dict)
