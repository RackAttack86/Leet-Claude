# Problem 91: Decode Ways

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/decode-ways/)

## Problem Description

A message containing letters from A-Z can be encoded into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

- "AAJF" with the grouping (1 1 10 6)
- "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

### Constraints

- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s)

### Examples

**Example 1:**
```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**
```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

## Approaches

### 1. Dynamic Programming

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def numDecodings(self, s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    # prev2 = dp[i-2], prev1 = dp[i-1]
    prev2, prev1 = 1, 1

    for i in range(1, n):
        current = 0

        # Single digit
        if s[i] != '0':
            current += prev1

        # Two digits
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            current += prev2

        prev2, prev1 = prev1, current

    return prev1
```

**Why this works:**

Similar to climbing stairs, but with conditions. dp[i] depends on whether we can decode a single digit (dp[i-1]) and whether we can decode two digits (dp[i-2]). A single digit is valid if it's not '0', and a two-digit number is valid if it's between 10 and 26.

## Key Insights

1. Similar to climbing stairs with conditions
2. dp[i] depends on single digit (dp[i-1]) and two digits (dp[i-2])
3. Handle leading zeros and invalid two-digit numbers
4. Two-digit valid if 10 <= num <= 26

## Common Mistakes

1. Not handling leading zeros ('0' cannot be decoded alone)
2. Allowing invalid two-digit numbers like "00", "01", "09"
3. Forgetting that two-digit numbers must be between 10 and 26

## Related Problems

- Climbing Stairs
- Decode Ways II

## Tags

String, Dynamic Programming
