# Localization Evaluation Plan

## Objective

Evaluate whether LLM-generated Portuguese content is accurate, natural, useful and appropriate for Brazilian users.

This project focuses on Brazilian Portuguese localization rather than simple word-for-word translation.

## Scope

The v0.1 test suite covers:

- English to Brazilian Portuguese translation;
- Brazilian Portuguese customer support replies;
- technical support messages;
- SaaS and app interface copy;
- tone adaptation;
- false friends;
- cultural and regional fit;
- avoiding Portuguese-from-Portugal expressions;
- clarity and instruction following.

## Out of Scope

This version does not evaluate:

- legal compliance of localized contracts;
- medical translation;
- certified translation;
- full product internationalization engineering;
- automated translation scoring.

## Evaluation Method

Each test case includes:

- test case ID;
- category;
- source prompt;
- expected behavior;
- target user context;
- critical dimensions;
- severity notes.

The evaluator reviews the model output manually and scores it using the localization rubric.

## Quality Dimensions

- Meaning Preservation
- Brazilian Portuguese Naturalness
- Tone and Register
- Terminology Accuracy
- Cultural Fit
- Clarity
- Instruction Following

## Release Readiness Criteria

A localized model response set should not be recommended for release if:

- overall pass rate is below 95%;
- any Critical severity localization issue remains open;
- High severity issues affect user trust, safety, payment, login or support workflows;
- PT-BR output repeatedly sounds translated, unnatural or Portugal-oriented;
- technical terms are mistranslated in a way that changes meaning.

## Evidence Rules

For each failed case, the evaluator should record:

- expected behavior;
- actual behavior;
- localization issue;
- severity;
- user impact;
- suggested fix.

## Integrity Note

This repository is a portfolio project. Results should clearly state whether they are sample evaluations or real runs collected from a named model.
