import json
from src.analyzer import analyze_code


def generate_report(code: str, output_path: str = "report.json"):
    result = analyze_code(code)
    score = 0

    if result["has_docstring"]:
        score += 1
    if result["functions"] >= 1:
        score += 1

    report = {
        "metrics": result,
        "score": score,
        "max_score": 2,
    }

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
