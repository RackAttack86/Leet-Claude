"""
LeetCode Problem #14: Longest Common Prefix
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/longest-common-prefix/

Problem:
--------
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

Constraints:
-----------
- `1
- strs[i]` consists of only lowercase English letters if it is non-empty.

Examples:
---------
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
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #14: Longest Common Prefix

    Approach: Vertical Scanning
    Time Complexity: O(S) where S is sum of all characters in all strings
    Space Complexity: O(1) - only using a few variables

    Key Insights:
    - Compare characters at each position across all strings
    - Stop when we find a mismatch or reach end of any string
    - Use the first string as reference and compare others against it
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix among an array of strings.

        Args:
            strs: List of strings

        Returns:
            The longest common prefix string
        """
        pass



PROBLEM_METADATA = {
    "number": 14,
    "name": "Longest Common Prefix",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Array', 'String', 'Trie'],
    "url": "https://leetcode.com/problems/longest-common-prefix/",
    "companies": ['Amazon', 'Google', 'Facebook', 'Microsoft', 'Apple'],
    "time_complexity": "O(S)",
    "space_complexity": "O(1)",
}