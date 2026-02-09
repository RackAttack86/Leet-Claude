# Problem 392: Is Subsequence

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/is-subsequence/)

## Problem Description

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

## Constraints

- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- `s` and `t` consist only of lowercase English letters.

## Examples

Example 1:
```
Input: s = "abc", t = "ahbgdc"
Output: true
```

Example 2:
```
Input: s = "axc", t = "ahbgdc"
Output: false
```

## Approaches

### 1. Two Pointers

**Time Complexity:** O(n) where n is the length of t
**Space Complexity:** O(1)

```python
def isSubsequence(self, s: str, t: str) -> bool:
    if not s:
        return True

    s_ptr = 0

    for char in t:
        if char == s[s_ptr]:
            s_ptr += 1
            if s_ptr == len(s):
                return True

    return False
```

**Why this works:**
Use two pointers, one for each string. Move through t, advancing s pointer only when characters match. If s pointer reaches end of s, all characters were found in order.

## Key Insights

- Use two pointers, one for each string
- Move through t, advancing s pointer only when characters match
- If s pointer reaches end of s, all characters were found in order

## Common Mistakes

- Not handling empty s (should return True)
- Confusing subsequence with substring
- Not checking if we've matched all characters of s

## Related Problems

- Number of Matching Subsequences
- Shortest Way to Form String
