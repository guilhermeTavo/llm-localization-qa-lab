# Localization QA Report

## Overview

This report summarizes the first manual pilot run for the LLM Localization QA Lab.

The goal was to evaluate whether a candidate LLM response set was properly localized for Brazilian Portuguese users across support, UI, billing, security, account and product messaging scenarios.

## Current Version

Version: v0.2 manual pilot  
Model label: Candidate LLM B — Manual pilot response set v0.2  
Target locale: Brazilian Portuguese (pt-BR)  
Execution date: 2026-09-13  
Execution status: Completed

## Test Suite

The first suite contains 20 localization test cases covering:

- EN to PT-BR translation;
- customer support replies;
- UI microcopy;
- billing and subscription messages;
- account and login instructions;
- Brazilian date/time formats;
- security warnings;
- tone adaptation;
- false friends;
- Portuguese-from-Portugal avoidance.

## Summary Results

| Metric | Result |
|---|---:|
| Total evaluated cases | 20 |
| Passed | 16 |
| Failed | 4 |
| Pass rate | 80.00% |
| Open defects | 4 |
| High severity defects | 3 |
| Medium severity defects | 1 |

## Main Findings

The pilot found four localization issues:

1. Portuguese-from-Portugal wording in a Brazilian account message.
2. False-friend mistranslation of "eventually" as "eventualmente".
3. US date and time format used in a Brazilian subscription renewal message.
4. Portugal-oriented SaaS terminology such as "subscrição" and "definições".

## Evaluation Method

Each response was reviewed against these dimensions:

- Meaning Preservation
- Brazilian Portuguese Naturalness
- Tone and Register
- Terminology Accuracy
- Cultural Fit
- Clarity
- Instruction Following

Each defect was classified by severity based on user impact, risk and whether the issue could affect account, billing or support workflows.

## Readiness Recommendation

The evaluated response set is **blocked for pt-BR localization release**.

Reason:

- pass rate is below the 90% localization readiness target;
- three High severity defects remain open;
- one issue affects billing date/time clarity;
- the response set shows repeated risk of Portugal-oriented wording.

## Current Conclusion

The pilot successfully demonstrates a realistic Localization QA workflow: test design, response review, scoring, defect logging, severity classification and localization release decision.

Before release, the failed cases should be fixed and retested using a pt-BR glossary and explicit Brazilian formatting rules.
