# Problem 5: Longest Palindromic Substring

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)

## Problem Description

Given a string s, return the longest palindromic substring in s.

### Constraints

- 1 <= s.length <= 1000
- s consist of only digits and English letters

### Examples

**Example 1:**
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**
```
Input: s = "cbbd"
Output: "bb"
```

## Approaches

### 1. Expand Around Center

**Time Complexity:** O(n^2)
**Space Complexity:** O(1)

```python
def longestPalindrome(self, s: str) -> str:
    if not s:
        return ""

    start, max_len = 0, 1

    def expandAroundCenter(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        # Odd length palindrome
        len1 = expandAroundCenter(i, i)
        # Even length palindrome
        len2 = expandAroundCenter(i, i + 1)

        length = max(len1, len2)
        if length > max_len:
            max_len = length
            start = i - (length - 1) // 2

    return s[start:start + max_len]
```

**Why this works:**

The expand around center approach treats each position (and each pair of adjacent positions) as a potential center of a palindrome. From each center, we expand outward as long as the characters on both sides match. This efficiently finds the longest palindrome centered at each position.

## Key Insights

1. Each center can expand to form palindrome
2. Check both odd and even length palindromes
3. DP approach: dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
4. Manacher's algorithm achieves O(n) but is more complex

## Common Mistakes

1. Forgetting to check both odd-length and even-length palindromes
2. Off-by-one errors when calculating the start index from the center
3. Not handling single character strings correctly

## Related Problems

- Palindromic Substrings
- Longest Palindromic Subsequence
- Valid Palindrome

## Tags

String, Dynamic Programming
