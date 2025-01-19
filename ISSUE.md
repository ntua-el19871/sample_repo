# Issue: Bug in add_numbers function
**Description**: The `add_numbers` function in `src/math_operations.py` is not returning the correct result.

**Steps to Reproduce**:
1. Call `add_numbers(2, 3)`; expected result is `5`, but the function returns `-1`.

**Expected Behavior**: The function should return the sum of two numbers.

**Suggested Fix**: Update the function to return `a + b` instead of `a - b`.
