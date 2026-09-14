# Localization Metrics Summary

Generated from the v0.2 manual pilot evaluation.

## General Results

| Metric | Result |
|---|---:|
| Total test cases | 20 |
| Passed | 16 |
| Failed | 4 |
| Pass rate | 80.00% |
| Open defects | 4 |
| High severity defects | 3 |
| Medium severity defects | 1 |
| Low severity defects | 0 |

## Average Scores

| Dimension | Average |
|---|---:|
| Meaning Preservation | 4.80 |
| PT-BR Naturalness | 4.55 |
| Tone / Register | 4.80 |
| Terminology Accuracy | 4.65 |
| Cultural Fit | 4.50 |
| Clarity | 4.85 |
| Instruction Following | 4.90 |

## Defect Distribution

| Category | Count |
|---|---:|
| Portuguese-from-Portugal wording | 2 |
| False friend / meaning shift | 1 |
| Date and time localization | 1 |

## Readiness Signal

The pilot response set is **not ready for pt-BR localization release**.

Reason:

- pass rate is below the target threshold;
- three High severity localization defects remain open;
- one billing-related date format issue could directly affect user understanding;
- recurring Portugal-oriented wording suggests the need for a pt-BR glossary and retest cycle.

## Notes

These metrics represent a controlled manual pilot response set. They demonstrate the evaluation workflow and should not be presented as an official benchmark of a named model without reproducible collection details.
