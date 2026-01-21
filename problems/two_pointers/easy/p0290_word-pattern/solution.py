"""
LeetCode Problem #290: Word Pattern
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/word-pattern/

Problem:
--------
Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`. Specifically:

- Each letter in `pattern` maps to exactly one unique word in `s`.
	
- Each unique word in `s` maps to exactly one letter in `pattern`.
	
- No two letters map to the same word, and no two words map to the same letter.

Constraints:
-----------
- `1
- pattern` contains only lower-case English letters.
- s` contains only lowercase English letters and spaces `' '`.
- s` does not contain any leading or trailing spaces.
- All the words in `s` are separated by a single space.

Examples:
---------
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

- `'a'` maps to `"dog"`.
	
- `'b'` maps to `"cat"`.

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #290: Word Pattern

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 290,
    "name": "Word Pattern",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Hash Table', 'String'],
    "url": "https://leetcode.com/problems/word-pattern/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
