"""
LeetCode Problem #392: Is Subsequence
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/is-subsequence/

Problem:
--------
Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

Constraints:
-----------
- `0
- s` and `t` consist only of lowercase English letters.

Examples:
---------
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
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #392: Is Subsequence

    Approach: Two Pointers
    Time Complexity: O(n) where n is the length of t
    Space Complexity: O(1)

    Key Insights:
    - Use two pointers, one for each string
    - Move through t, advancing s pointer only when characters match
    - If s pointer reaches end of s, all characters were found in order
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Check if s is a subsequence of t.

        Args:
            s: Potential subsequence
            t: Original string

        Returns:
            True if s is a subsequence of t
        """
        pass



PROBLEM_METADATA = {
    "number": 392,
    "name": "Is Subsequence",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Two Pointers', 'String', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/is-subsequence/",
    "companies": ['Amazon', 'Google', 'Microsoft', 'Apple'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}