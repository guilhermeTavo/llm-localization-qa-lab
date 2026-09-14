# Severity Levels

## Purpose

Severity describes the impact of a localization issue on the user, product or business.

Severity is not the same as score. A small grammar issue may have a low score in naturalness but low severity. A mistranslated payment message may have high severity because it affects trust and user action.

## Critical

Use Critical when the issue can cause serious harm, legal risk, security risk or complete user failure.

Examples:

- mistranslating a safety warning;
- telling users to take an unsafe action;
- exposing or requesting private information unnecessarily;
- changing the meaning of legal, medical or security guidance.

## High

Use High when the issue can cause major user confusion, loss of trust or failed completion of an important task.

Examples:

- mistranslating login or account recovery instructions;
- using wrong payment terminology;
- changing refund or subscription meaning;
- sounding rude or dismissive in a support escalation;
- using Portugal-specific terms in a Brazil-only product flow.

## Medium

Use Medium when the issue affects quality but does not block the user.

Examples:

- unnatural but understandable translation;
- tone mismatch in a low-risk support message;
- minor terminology inconsistency;
- localized message is too long for the intended UI context.

## Low

Use Low when the issue is cosmetic or slightly awkward.

Examples:

- minor phrasing issue;
- small punctuation issue;
- wording could be more natural but is acceptable;
- style inconsistency with low user impact.

## Decision Guide

Ask:

1. Does the issue change the meaning?
2. Does it affect a payment, account, security or support-critical flow?
3. Would a Brazilian user immediately notice that it sounds translated?
4. Could the issue reduce trust in the product?
5. Does it block the user's next action?

The more answers are yes, the higher the severity.
