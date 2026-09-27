# Lab 2: White-Box Manual Testing (Test Case Design and Bug Reporting)

**Duration:** 1 hour 45 minutes  **Work mode:** pairs

**Code under test:** `whitebox_target.py`, function `check_task(priority, hours)`

## Objective

Derive test cases directly from source code logic.
Trace the code by hand and design a minimal suite that hits 100% statement
coverage and 100% decision (branch) coverage.

## Key concepts

ISTQB's 7 testing principles, control flow and decision points, statement
coverage, decision/branch coverage, positive vs. negative scenarios, bug
lifecycle and reproducibility (ISTQB CTFL, Ch. 1 and Ch. 4).

## Start here

1. Read this page, then open `whitebox_target.py`.
2. Fill in the control-flow table in `WHITEBOX_TESTING.md`: find every
   decision point in the function.
3. Design test cases until every decision has been True at least once and
   False at least once.
4. Trace each test case by hand against the code (no need to run Python).
   Record the Actual Result.
5. Where Actual and Expected disagree, file a bug using the **Issues** tab.

## Rules

- Work from the code and the business rule stated in the file's docstring.
  Do not guess at intent beyond what is written there.
- No interpreter needed. If you want to check a trace, running the file
  locally is allowed, but your submitted Actual Result must come from your
  own trace, not a printout.
- One bug per issue. Search existing issues in your own repo first.

## Deliverables and assessment

1. `WHITEBOX_TESTING.md` committed, with the control-flow table and full
   test suite.
2. At least 1 GitHub issue per defect found, using the bug report template.

| Criterion | Points |
|---|---|
| Control-flow table: every decision point correctly identified | 20 |
| Test suite reaches 100% decision coverage (every branch, both ways) | 35 |
| Positive/negative labelling and Covers column correct | 10 |
| Traces recorded honestly, Status correct | 15 |
| Bug reports: found, reproducible, correct Severity and Priority | 20 |
