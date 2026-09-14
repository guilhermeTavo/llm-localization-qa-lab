import argparse
import csv
from collections import Counter
from pathlib import Path

SCORE_COLUMNS = [
    "meaning_preservation",
    "ptbr_naturalness",
    "tone_register",
    "terminology_accuracy",
    "cultural_fit",
    "clarity",
    "instruction_following",
]


def read_rows(input_path: Path) -> list[dict[str, str]]:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with input_path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def average_score(rows: list[dict[str, str]], column: str) -> float:
    scores: list[float] = []
    for row in rows:
        value = row.get(column, "").strip()
        if value:
            scores.append(float(value))
    return sum(scores) / len(scores) if scores else 0.0


def build_report(rows: list[dict[str, str]]) -> str:
    total = len(rows)
    result_counts = Counter(row.get("overall_result", "UNKNOWN") for row in rows)
    severity_counts = Counter(row.get("severity", "Unknown") for row in rows)
    failed_rows = [row for row in rows if row.get("overall_result") == "FAIL"]

    pass_count = result_counts.get("PASS", 0)
    fail_count = result_counts.get("FAIL", 0)
    pass_rate = (pass_count / total * 100) if total else 0

    lines = [
        "# Localization Metrics Summary",
        "",
        "Generated from `results/evaluation-results.csv`.",
        "",
        "## General Results",
        "",
        "| Metric | Result |",
        "|---|---:|",
        f"| Total test cases | {total} |",
        f"| Passed | {pass_count} |",
        f"| Failed | {fail_count} |",
        f"| Pass rate | {pass_rate:.2f}% |",
        "",
        "## Average Scores",
        "",
        "| Dimension | Average |",
        "|---|---:|",
    ]

    for column in SCORE_COLUMNS:
        label = column.replace("_", " ").title()
        lines.append(f"| {label} | {average_score(rows, column):.2f} |")

    lines.extend([
        "",
        "## Severity Distribution",
        "",
        "| Severity | Count |",
        "|---|---:|",
    ])

    for severity in ["Critical", "High", "Medium", "Low", "None"]:
        lines.append(f"| {severity} | {severity_counts.get(severity, 0)} |")

    lines.extend([
        "",
        "## Failed Cases",
        "",
    ])

    if failed_rows:
        lines.extend([
            "| Test Case | Severity | Notes |",
            "|---|---|---|",
        ])
        for row in failed_rows:
            lines.append(
                f"| {row.get('test_case_id', '')} | {row.get('severity', '')} | {row.get('evaluator_notes', '')} |"
            )
    else:
        lines.append("No failed cases recorded.")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze LLM localization QA results.")
    parser.add_argument("--input", default="results/evaluation-results.csv")
    parser.add_argument("--output", default="results/metrics-summary.md")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    rows = read_rows(input_path)
    report = build_report(rows)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"Metrics report written to: {output_path}")


if __name__ == "__main__":
    main()
