# Problem 14: Longest Common Prefix

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/longest-common-prefix/)

## Problem Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Constraints

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Examples

Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

Example 2:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Approaches

### 1. Vertical Scanning

**Time Complexity:** O(S) where S is sum of all characters in all strings
**Space Complexity:** O(1) - only using a few variables

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    # Use first string as reference
    for i in range(len(strs[0])):
        char = strs[0][i]
        # Check this character against all other strings
        for s in strs[1:]:
            # If we've reached end of this string or chars don't match
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]
```

**Why this works:**
Compare characters at each position across all strings. Stop when we find a mismatch or reach the end of any string. Use the first string as reference and compare others against it.

## Key Insights

- Compare characters at each position across all strings
- Stop when we find a mismatch or reach end of any string
- Use the first string as reference and compare others against it

## Common Mistakes

- Not handling empty input array
- Not handling empty strings in the array
- Forgetting to check array bounds when comparing characters

## Related Problems

- Longest Common Subsequence
