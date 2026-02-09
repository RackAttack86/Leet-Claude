"""
LeetCode Problem #205: Isomorphic Strings
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/isomorphic-strings/

Problem:
--------
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Constraints:
-----------
- `1
- t.length == s.length
- s` and `t` consist of any valid ascii character.

Examples:
---------
Example 1:
Input: s = "egg", t = "add"

Output: true

Explanation:

The strings `s` and `t` can be made identical by:

- Mapping `'e'` to `'a'`.
	
- Mapping `'g'` to `'d'`.

Example 2:
Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings `s` and `t` can not be made identical as `'o'` needs to be mapped to both `'a'` and `'r'`.

Example 3:
Input: s = "paper", t = "title"

Output: true
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #205: Isomorphic Strings

    Approach: Two Hash Maps for Bidirectional Mapping
    Time Complexity: O(n) where n is the length of the strings
    Space Complexity: O(k) where k is the size of the character set

    Key Insights:
    - Need bidirectional mapping: s->t AND t->s must be consistent
    - Use two hash maps to track both directions
    - If a character in s maps to different chars in t, or vice versa, return False
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determine if two strings are isomorphic.

        Args:
            s: First string
            t: Second string

        Returns:
            True if s and t are isomorphic
        """
        pass



PROBLEM_METADATA = {
    "number": 205,
    "name": "Isomorphic Strings",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Hash Table', 'String'],
    "url": "https://leetcode.com/problems/isomorphic-strings/",
    "companies": ['Amazon', 'Google', 'Microsoft', 'LinkedIn'],
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
}