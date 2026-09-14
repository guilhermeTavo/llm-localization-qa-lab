# LLM Localization QA Lab

**Project page:** https://guilhermetavo.github.io/llm-localization-qa-lab/

A practical AI Quality portfolio project focused on evaluating Large Language Model (LLM) responses for Brazilian Portuguese localization, translation quality, tone, cultural fit, support readiness and regional language accuracy.

## Project Objective

This lab simulates a real Localization QA workflow for AI-generated content.

The project demonstrates how an AI Quality / Localization QA evaluator can:

- design structured localization test cases;
- evaluate whether Portuguese output sounds natural for Brazilian users;
- identify literal translation, Portuguese-from-Portugal wording and unnatural phrasing;
- test tone adaptation for customer support, product messaging and technical content;
- classify localization defects by severity and user impact;
- document findings in a repeatable QA format;
- generate a localization readiness recommendation.

## Current Status — v0.2 Pilot

The current version includes a completed manual pilot evaluation with:

- 20 structured localization test cases;
- manual evaluation results;
- localization defect log;
- metrics summary;
- localization QA report;
- localization readiness report;
- Python script for metrics analysis;
- GitHub Pages-ready landing page;
- project summary for recruiters;
- interview guide for explaining the project.

## Quick Links

- [Project page](https://guilhermetavo.github.io/llm-localization-qa-lab/)
- [Evaluation plan](evaluation-plan.md)
- [Localization rubric](methodology/localization-rubric.md)
- [Localization report](results/localization-report.md)
- [Readiness report](results/localization-readiness-report.md)
- [Defect log](results/defect-log.csv)
- [Recruiter summary](docs/project-summary.md)
- [Interview guide](docs/interview-guide.md)

## Pilot Results

| Metric | Result |
|---|---:|
| Total Tests | 20 |
| Passed | 16 |
| Failed | 4 |
| Pass Rate | 80.00% |
| Open Defects | 4 |
| High Severity Defects | 3 |
| Medium Severity Defects | 1 |
| Localization Verdict | Blocked for PT-BR release |

> Integrity note: this is a controlled manual pilot response set created to demonstrate the evaluation workflow. It should not be presented as an official benchmark of a named model unless future responses are collected directly from named models with reproducible run details.

## Evaluation Areas

This lab focuses on:

- Brazilian Portuguese naturalness;
- translation accuracy;
- tone and register;
- customer support empathy;
- technical terminology;
- regional/cultural fit;
- false friends and literal translation;
- instruction following;
- clarity and usefulness;
- severity classification.

## Key Findings

The v0.2 pilot identified four localization defects:

| ID | Severity | Finding |
|---|---|---|
| LOCBUG-001 | High | Portuguese-from-Portugal wording in a Brazilian account message |
| LOCBUG-002 | High | False-friend mistranslation of "eventually" as "eventualmente" |
| LOCBUG-003 | High | US date and time format used in a Brazilian billing scenario |
| LOCBUG-004 | Medium | Portugal-oriented SaaS terminology such as "subscrição" and "definições" |

These findings are tracked in:

```text
results/defect-log.csv
```

## Localization Readiness

The candidate response set is marked as:

```text
BLOCKED FOR PT-BR LOCALIZATION RELEASE
```

Reason:

- pass rate is below the 90% localization readiness target;
- three High severity defects remain open;
- one billing-related date/time issue could affect user understanding;
- repeated Portugal-oriented wording requires glossary remediation and retesting.

See:

```text
results/localization-readiness-report.md
```

## How to Explain This Project

For interview preparation, see:

```text
docs/interview-guide.md
```

The guide includes a 30-second explanation, a 2-minute explanation, a STAR answer, key defects to discuss and recruiter questions.

## How to Run the Analysis

From the project root, run:

```bash
python scripts/analyze_localization_results.py
```

The script reads:

```text
results/evaluation-results.csv
```

and updates:

```text
results/metrics-summary.md
```

## Project Structure

```text
llm-localization-qa-lab/
│
├── README.md
├── evaluation-plan.md
│
├── methodology/
│   ├── localization-rubric.md
│   └── severity-levels.md
│
├── test-cases/
│   └── localization-tests.csv
│
├── results/
│   ├── evaluation-results-template.csv
│   ├── evaluation-results.csv
│   ├── defect-log-template.csv
│   ├── defect-log.csv
│   ├── localization-report.md
│   ├── localization-readiness-report.md
│   └── metrics-summary.md
│
├── scripts/
│   └── analyze_localization_results.py
│
└── docs/
    ├── index.html
    ├── project-summary.md
    └── interview-guide.md
```

## Test Coverage

The first test suite includes scenarios such as:

- EN → PT-BR translation;
- customer support replies;
- irritated customer handling;
- SaaS error messages;
- app notifications;
- payment and account messaging;
- formal vs informal tone adaptation;
- avoiding Portuguese-from-Portugal expressions;
- localizing technical terms naturally;
- preserving meaning while sounding native.

## What This Project Demonstrates

This project demonstrates practical skills relevant to AI Quality, LLM Evaluation and Localization QA roles:

- LLM localization evaluation;
- Portuguese language quality review;
- prompt evaluation;
- translation QA;
- support content QA;
- defect documentation;
- severity classification;
- test case design;
- human evaluation methodology;
- Python-based metrics reporting;
- localization readiness decision making.

## Next Steps

Planned improvements:

- compare outputs from two different models;
- add retest results after localization fixes;
- expand the suite to 40+ test cases.

## Author

**Guilherme Tavares**

AI Quality Analyst | LLM Evaluator | Localization QA | QA Tester | PT-BR Reviewer

- GitHub: [guilhermeTavo](https://github.com/guilhermeTavo)
- LinkedIn: [Guilherme Tavares](https://www.linkedin.com/in/guilherme-tavares-398563240/)
