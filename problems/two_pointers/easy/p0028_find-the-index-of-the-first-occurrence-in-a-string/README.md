# Problem 28: Find the Index of the First Occurrence in a String

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Problem Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Constraints

- 1 <= haystack.length, needle.length <= 10^4
- `haystack` and `needle` consist of only lowercase English characters.

## Examples

Example 1:
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

Example 2:
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

## Approaches

### 1. Sliding Window

**Time Complexity:** O(n * m) where n is haystack length, m is needle length
**Space Complexity:** O(1)

```python
def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0

    n, m = len(haystack), len(needle)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1
```

**Why this works:**
Slide a window of size len(needle) across haystack. At each position, check if the substring matches needle. Can also use built-in find() or KMP for O(n + m) time.

## Key Insights

- Slide a window of size len(needle) across haystack
- At each position, check if the substring matches needle
- Can also use built-in find() or KMP for O(n + m) time

## Common Mistakes

- Not handling empty needle case
- Off-by-one error in the loop range
- Using inefficient string comparison methods

## Related Problems

- Implement strStr()
- Repeated Substring Pattern
