"""
LeetCode Problem #49: Group Anagrams
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/group-anagrams/

Problem:
--------
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

Constraints:
-----------
- `1
- strs[i]` consists of lowercase English letters.

Examples:
---------
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

- There is no string in strs that can be rearranged to form `"bat"`.
	
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
	
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]

Output: [[""]]

Example 3:
Input: strs = ["a"]

Output: [["a"]]
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #49: Group Anagrams

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 49,
    "name": "Group Anagrams",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Hash Table', 'String', 'Sorting'],
    "url": "https://leetcode.com/problems/group-anagrams/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
