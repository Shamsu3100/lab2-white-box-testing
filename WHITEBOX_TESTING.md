# White-Box Test Suite: check_task()

Testers (pair): <name 1>, <name 2>
Date: <date>
File under test: `whitebox_target.py`, function `check_task(priority, hours)`

## 1. Control flow

List every decision point (every `if`) in the order it appears. A decision
with `and` / `or` still counts as one decision point for this lab.

| # | Line (approx.) | Condition | True branch leads to | False branch leads to |
|---|---|---|---|---|
| D1 | | `priority is None or hours is None` | | |
| D2 | | | | |
| D3 | | | | |
| D4 | | | | |
| D5 | | | | |

## 2. Coverage target

- **Statement coverage**: every line of code executes at least once across your test suite.
- **Decision (branch) coverage**: every decision point takes both True and False at least once across your test suite.

Decision coverage is stronger. If you hit every branch, you also hit every
statement, so design for branch coverage first.

## 3. Test cases

Type: **Positive** = follows the intended success path. **Negative** =
should be rejected.
"Covers" = which decision(s) this case exercises, and whether it takes the
True or False branch, e.g. `D3-True`.

| ID | Type | Preconditions | Test Steps | Test Data | Covers | Expected Result | Actual Result (trace) | Status |
|---|---|---|---|---|---|---|---|---|
| TC-01 | Positive | None | Call `check_task` with the given data | priority=3, hours=5 | D1-F, D2-F, D3-F, D4-F, D5-F | `(True, "Valid.")` | | |
| TC-02 | Negative | None | Call `check_task` with the given data | priority=None, hours=5 | D1-T | `(False, "Missing required field.")` | | |
| TC-03 | | | | | | | | |

Add rows until every decision point has appeared as both True and False at
least once. Check off the table in section 1 as you go.

## 4. How to trace (no interpreter)

For each test case: start at the top of the function, evaluate each `if` in
order using your test data, follow the branch it takes, and stop at the
first `return` you reach. Write that return value as your Actual Result.
Compare it with your Expected Result (based on the business rule, not the
code) and mark Status as Pass or Fail.

## 5. Defects found

Where Actual and Expected disagree, that is a candidate defect. File it as
a GitHub issue using the bug report template, then list it here.

| Issue link | Linked test case | Short title | Severity | Priority |
|---|---|---|---|---|
| | | | | |
