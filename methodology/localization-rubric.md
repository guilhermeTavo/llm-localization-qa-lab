# Localization Evaluation Rubric

## Goal

This rubric evaluates whether an LLM response is properly localized for Brazilian Portuguese users.

A good localized answer should preserve meaning, sound natural, fit the context and avoid literal translation artifacts.

## Scoring Scale

| Score | Meaning |
|---:|---|
| 5 | Excellent: natural, accurate and appropriate for Brazilian users. |
| 4 | Good: minor wording issues, but meaning and tone are strong. |
| 3 | Acceptable: understandable, but noticeably awkward or partially localized. |
| 2 | Poor: meaning, tone or terminology problems affect user experience. |
| 1 | Failure: wrong meaning, wrong language variety, unsafe wording or unusable output. |
| N/A | Dimension does not apply to the test case. |

## Dimensions

### 1. Meaning Preservation

Checks whether the localized response keeps the original meaning.

Common failures:

- mistranslating the source;
- adding unsupported information;
- removing important details;
- changing the user's intent.

### 2. Brazilian Portuguese Naturalness

Checks whether the answer sounds natural to a Brazilian user.

Common failures:

- literal translation;
- unnatural sentence structure;
- Portuguese-from-Portugal expressions;
- excessive formality for a simple support context;
- mixed English and Portuguese without need.

### 3. Tone and Register

Checks whether the response uses the right level of formality and emotional tone.

Common failures:

- sounding cold to an angry customer;
- sounding too casual for payment or security issues;
- over-apologizing;
- using robotic support language.

### 4. Terminology Accuracy

Checks whether product, support and technical terms are translated correctly.

Common failures:

- translating established technical terms too literally;
- confusing login, sign up, sign in and account recovery;
- mistranslating billing, refund, charge, invoice or subscription terms.

### 5. Cultural and Regional Fit

Checks whether the answer fits Brazilian context.

Common failures:

- using Portugal-specific terms;
- using date, currency or address formats that do not fit Brazil;
- ignoring common Brazilian support/payment terms such as Pix when context requires it.

### 6. Clarity and Usefulness

Checks whether the final answer is easy to understand and actionable.

Common failures:

- vague troubleshooting;
- long response when user asked for short copy;
- unclear next step;
- unnecessary explanation.

### 7. Instruction Following

Checks whether the model respected explicit constraints.

Common failures:

- wrong language;
- wrong number of options or bullets;
- ignoring tone requirements;
- adding content that was explicitly forbidden.

## Overall Result

Use PASS when the response meets the expected behavior and no critical dimension fails.

Use FAIL when:

- a critical dimension scores 1 or 2;
- the meaning changes;
- the answer does not sound like Brazilian Portuguese;
- the tone is inappropriate for the user situation;
- important instructions are ignored.
