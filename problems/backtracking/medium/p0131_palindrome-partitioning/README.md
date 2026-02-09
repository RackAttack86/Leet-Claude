# Problem 131: Palindrome Partitioning

**Difficulty:** Medium
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/palindrome-partitioning/)

## Problem Description

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

**Constraints:**
- 1 <= s.length <= 16
- s contains only lowercase English letters

**Examples:**

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]
```

## Approaches

### 1. Backtracking with Palindrome Checking

**Time Complexity:** O(n * 2^n)
**Space Complexity:** O(n)

```python
def partition(self, s: str) -> List[List[str]]:
    result = []

    def is_palindrome(string: str) -> bool:
        return string == string[::-1]

    def backtrack(start: int, current: List[str]):
        if start == len(s):
            result.append(current[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                current.append(substring)
                backtrack(end, current)
                current.pop()

    backtrack(0, [])
    return result
```

**Why this works:**

We try all possible partitions using backtracking. At each position, we try substrings of increasing length. If a substring is a palindrome, we add it to our current partition and recurse from the end of that substring. When we reach the end of the string, we've found a valid partition. The key is that we only continue if the current substring is a palindrome.

## Key Insights

- Try all possible partitions using backtracking
- Check if each substring is a palindrome before including it
- Only proceed with valid (palindrome) substrings
- Optimization: precompute palindrome checks using DP

## Common Mistakes

- Not checking palindrome condition before recursing
- Incorrect range for substring end (should be `len(s) + 1` for slicing)
- Not making a copy when adding to result
- Forgetting to handle single characters (always palindromes)

## Related Problems

- Palindrome Partitioning II (#132) - minimum cuts
- Longest Palindromic Substring (#5)
- Valid Palindrome (#125)

## Tags

String, Dynamic Programming, Backtracking
