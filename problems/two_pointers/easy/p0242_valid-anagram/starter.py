"""
LeetCode Problem #242: Valid Anagram
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/valid-anagram/

Problem:
--------
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

Constraints:
-----------
- `1
- s` and `t` consist of lowercase English letters.

Examples:
---------
Example 1:
Input: s = "anagram", t = "nagaram"

Output: true

Example 2:
Input: s = "rat", t = "car"

Output: false
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #242: Valid Anagram

    Approach: Character Frequency Count
    Time Complexity: O(n) where n is the length of the strings
    Space Complexity: O(1) - at most 26 lowercase letters

    Key Insights:
    - Anagrams have the same character frequencies
    - Use Counter or a frequency array to count characters
    - Compare the counts - if equal, they're anagrams
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if t is an anagram of s.

        Args:
            s: First string
            t: Second string

        Returns:
            True if t is an anagram of s
        """
        pass



PROBLEM_METADATA = {
    "number": 242,
    "name": "Valid Anagram",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Hash Table', 'String', 'Sorting'],
    "url": "https://leetcode.com/problems/valid-anagram/",
    "companies": ['Amazon', 'Google', 'Microsoft', 'Apple', 'Facebook'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}