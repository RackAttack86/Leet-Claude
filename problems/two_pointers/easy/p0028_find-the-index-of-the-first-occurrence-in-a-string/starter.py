"""
LeetCode Problem #28: Find the Index of the First Occurrence in a String
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Problem:
--------
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

Constraints:
-----------
- `1
- haystack` and `needle` consist of only lowercase English characters.

Examples:
---------
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
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #28: Find the Index of the First Occurrence in a String

    Approach: Sliding Window
    Time Complexity: O(n * m) where n is haystack length, m is needle length
    Space Complexity: O(1)

    Key Insights:
    - Slide a window of size len(needle) across haystack
    - At each position, check if the substring matches needle
    - Can also use built-in find() or KMP for O(n + m) time
    """
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Find the first occurrence of needle in haystack.

        Args:
            haystack: The string to search in
            needle: The string to search for

        Returns:
            Index of first occurrence, or -1 if not found
        """
        pass



PROBLEM_METADATA = {
    "number": 28,
    "name": "Find the Index of the First Occurrence in a String",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Two Pointers', 'String', 'String Matching'],
    "url": "https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Apple'],
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
}