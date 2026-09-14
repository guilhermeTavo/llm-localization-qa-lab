# Interview Guide — LLM Localization QA Lab

This guide helps explain the project clearly in interviews for AI Quality, LLM Evaluation, Localization QA, PT-BR Reviewer and Portuguese AI Trainer roles.

## 30-second version

I built a Localization QA portfolio project focused on evaluating whether LLM outputs are properly adapted for Brazilian Portuguese users.

The project includes 20 structured test cases, a localization rubric, severity levels, manual evaluation results, a defect log, metrics summary and a localization readiness report.

In the pilot run, I identified four localization defects, including Portuguese-from-Portugal wording, a false-friend mistranslation, US date/time formatting and unnatural SaaS terminology. Based on the results, the candidate response set was blocked for PT-BR localization release.

## 2-minute version

This project simulates a real Localization QA workflow for AI-generated content.

I created a test suite with 20 cases covering translation, support tone, UI microcopy, billing messages, account recovery, technical terminology, false friends, Brazilian date/time format and Portuguese-from-Portugal avoidance.

Each response was evaluated using a rubric with dimensions such as meaning preservation, Brazilian Portuguese naturalness, tone and register, terminology accuracy, cultural fit, clarity and instruction following.

The pilot run produced 16 passing cases and 4 failing cases, resulting in an 80% pass rate. The key defects were related to localization quality rather than general grammar: Portugal-oriented wording, literal translation, incorrect regional format and unnatural SaaS vocabulary.

I documented each issue with severity, expected behavior, actual behavior, user impact and remediation guidance. Because the pass rate was below the readiness target and three High severity defects remained open, the final recommendation was to block PT-BR localization release until fixes and retesting.

## STAR answer

**Situation:** AI-generated content can be grammatically correct but still feel unnatural or wrong for Brazilian users.

**Task:** I wanted to create a portfolio project that demonstrates how to evaluate LLM localization quality in a structured way, not just by saying whether a translation sounds good or bad.

**Action:** I designed 20 localization test cases, created a rubric, evaluated sample responses, logged defects, classified severity and wrote a localization readiness report.

**Result:** The pilot found 4 defects, including 3 High severity issues. The response set was blocked for PT-BR release, showing that I can identify localization risk, document evidence and make a QA-style release recommendation.

## How to explain the value

This project is useful because it shows three things at the same time:

1. I understand Brazilian Portuguese quality beyond literal translation.
2. I can apply QA structure to AI-generated content.
3. I can document defects in a way that product, QA and localization teams can act on.

## Strong points to mention

- The goal was not to prove a model is perfect.
- The goal was to simulate how a Localization QA evaluator reviews model output before release.
- I focused on user impact, not only grammar.
- I separated translation accuracy from naturalness, tone and cultural fit.
- I used severity levels to make the findings actionable.
- I produced a release recommendation based on metrics and open defects.

## Key defects to discuss

### Portuguese-from-Portugal wording

A response used wording that may be understandable but does not sound natural for Brazilian users. In localization QA, that can reduce trust and make support content feel poorly adapted.

### False friend: eventually

The word "eventually" was translated as "eventualmente", which often changes the meaning in Brazilian Portuguese. A better translation depends on context, such as "por fim", "mais tarde" or "em algum momento".

### US date/time format

A billing message used an American date/time style instead of Brazilian formatting. In billing or payment contexts, this can create confusion and increase support contacts.

### Unnatural SaaS terms

Terms such as "subscrição" and "definições" are more associated with European Portuguese. For Brazilian SaaS users, terms like "assinatura" and "configurações" are more natural.

## Questions recruiters may ask

### Why did you choose localization QA?

Because many AI evaluation roles need language quality review, especially for non-English markets. As a native Brazilian Portuguese speaker with professional English experience, I can evaluate both meaning transfer and local language quality.

### What makes this different from normal translation?

Translation focuses on transferring meaning. Localization QA also checks tone, user context, regional language, terminology, formatting, cultural fit and whether the content feels natural for the target audience.

### How did you decide severity?

I classified severity based on user impact. A small awkward phrase may be Low, but a billing date format issue or a false-friend translation that changes meaning can become High because it can confuse users or cause wrong decisions.

### Why was the response set blocked?

Because the pass rate was below the readiness target and three High severity localization issues remained open. In QA, a release recommendation should be based on risk, not on whether most cases passed.

### How would you improve the project next?

I would compare two named models using the same test set, add retest results after fixes, expand the suite to 40+ cases and add a glossary for PT-BR SaaS terminology.

## Resume bullet

Built an LLM Localization QA Lab with 20 structured PT-BR test cases, localization rubric, manual evaluation results, defect logging, severity classification, metrics reporting and localization readiness analysis for AI-generated content.

## LinkedIn project summary

LLM Localization QA Lab is a portfolio project focused on evaluating whether AI-generated content is properly localized for Brazilian Portuguese users.

The project includes structured localization test cases, a scoring rubric, manual evaluation results, defect logging, severity classification and a localization readiness report.

The pilot run identified 4 defects, including Portuguese-from-Portugal wording, a false-friend mistranslation, US date/time formatting and unnatural SaaS terminology. The final recommendation was to block the candidate response set for PT-BR localization release pending remediation and retesting.
