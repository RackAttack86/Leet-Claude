# Problem 22: Generate Parentheses

**Difficulty:** Medium
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/generate-parentheses/)

## Problem Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Constraints:**
- 1 <= n <= 8

**Examples:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
```

## Approaches

### 1. Backtracking with Constraints

**Time Complexity:** O(4^n / sqrt(n)) - Catalan number
**Space Complexity:** O(n)

```python
def generateParenthesis(self, n: int) -> List[str]:
    result = []

    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result
```

**Why this works:**

We use backtracking with two key constraints to ensure we only generate valid parentheses:
1. We can add an opening parenthesis '(' if the count of open parentheses is less than n
2. We can add a closing parenthesis ')' only if the count of closing parentheses is less than the count of opening ones (ensuring we always have a matching open paren)

This naturally prunes invalid combinations and builds all valid sequences.

## Key Insights

- Add '(' if count < n
- Add ')' if ')' count < '(' count (ensures valid pairing)
- Backtrack to build all valid combinations
- The number of valid combinations is the nth Catalan number

## Common Mistakes

- Allowing ')' when there's no matching '(' (close_count should be < open_count)
- Not tracking open and close counts separately
- Generating all combinations first and filtering (inefficient)

## Related Problems

- Letter Combinations of a Phone Number (#17)
- Valid Parentheses (#20)
- Longest Valid Parentheses (#32)

## Tags

String, Dynamic Programming, Backtracking
