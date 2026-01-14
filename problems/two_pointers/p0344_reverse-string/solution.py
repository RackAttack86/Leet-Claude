"""
LeetCode Problem #344: Reverse String
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/reverse-string/

Problem:
--------
[TODO: Add problem description]

Constraints:
-----------
[TODO: Add constraints]

Examples:
---------
[TODO: Add examples]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #344: Reverse String

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0, len(s)-1
        while l<r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 344,
    "name": "Reverse String",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": [],  # TODO: Add topics
    "url": "https://leetcode.com/problems/reverse-string/",
    "companies": [],  # TODO: Add companies
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
