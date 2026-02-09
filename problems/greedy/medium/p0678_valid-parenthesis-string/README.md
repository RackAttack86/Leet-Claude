# Problem 678: Valid Parenthesis String

**Difficulty:** Medium
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/)

## Problem Description

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

## Constraints

- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'

## Examples

Example 1:
```
Input: s = "()"
Output: true
```

Example 2:
```
Input: s = "(*)"
Output: true
```

Example 3:
```
Input: s = "(*))"
Output: true
```

## Approaches

### 1. Greedy with Range Tracking

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def checkValidString(self, s: str) -> bool:
    # Track range of possible open parentheses counts
    low = 0   # Minimum possible open count (treat * as ) or empty)
    high = 0  # Maximum possible open count (treat * as ()

    for char in s:
        if char == '(':
            low += 1
            high += 1
        elif char == ')':
            low -= 1
            high -= 1
        else:  # char == '*'
            low -= 1   # Treat as )
            high += 1  # Treat as (

        # If high becomes negative, too many )
        if high < 0:
            return False

        # low can't go below 0 (we can always choose * as empty)
        low = max(low, 0)

    # Valid if we can reach exactly 0 open parentheses
    return low == 0
```

**Why this works:**
We track a range [low, high] of possible open parenthesis counts. The wildcard '*' expands this range. If at any point high < 0, we have too many closing parentheses. At the end, if 0 is within our range (low == 0), the string is valid.

## Key Insights

1. Track range of possible open parentheses count
2. low = minimum opens, high = maximum opens
3. '*' can be (, ), or empty - affects range
4. Valid if low <= 0 and high >= 0 at end

## Common Mistakes

1. Using stack without considering all possibilities for '*'
2. Not handling the case where low goes negative (reset to 0)
3. Checking high < 0 at wrong point

## Related Problems

- 20. Valid Parentheses
- 32. Longest Valid Parentheses

## Tags

String, Dynamic Programming, Stack, Greedy
