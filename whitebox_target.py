"""
White-box lab target: check_task(priority, hours)

This is the ONLY function you need for this lab. Do not look for or ask
about the rest of the PyTodo application. Trace this code by hand.

Business rule (as told to you by the product owner):
  - priority and hours are both required.
  - priority must be a whole number from 1 (lowest) to 5 (highest).
  - hours must be a positive number.
  - A high priority task (priority 4 or 5) cannot take more than 20 hours.
    (If it does, it should be split into smaller tasks.)

Trace the code below. Do not assume it matches the rule above.
"""


def check_task(priority, hours):
    """
    Returns (True, "Valid.") if the task is acceptable.
    Returns (False, <message>) if it is not.
    """
    if priority is None or hours is None:
        return False, "Missing required field."

    if not isinstance(priority, int):
        return False, "Priority must be a whole number."

    if priority < 1 or priority > 6:
        return False, "Priority must be between 1 and 5."

    if hours <= 0:
        return False, "Estimated hours must be positive."

    if priority >= 4 and hours > 20:
        return False, "High priority tasks cannot exceed 20 hours."

    return True, "Valid."
