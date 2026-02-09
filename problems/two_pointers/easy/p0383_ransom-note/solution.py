"""
LeetCode Problem #383: Ransom Note
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/ransom-note/

Problem:
--------
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

Constraints:
-----------
- `1
- ransomNote` and `magazine` consist of lowercase English letters.

Examples:
---------
Example 1:
```
Input: ransomNote = "a", magazine = "b"
Output: false

```

Example 2:
```
Input: ransomNote = "aa", magazine = "ab"
Output: false

```

Example 3:
```
Input: ransomNote = "aa", magazine = "aab"
Output: true

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #383: Ransom Note

    Approach: Character Frequency Count
    Time Complexity: O(m + n) where m and n are lengths of ransomNote and magazine
    Space Complexity: O(1) - at most 26 lowercase letters

    Key Insights:
    - Count character frequencies in magazine
    - Check if ransomNote can be constructed from those frequencies
    - Each magazine letter can only be used once
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Check if ransomNote can be constructed from magazine letters.

        Args:
            ransomNote: The note to construct
            magazine: Source of letters

        Returns:
            True if ransomNote can be constructed
        """
        magazine_count = Counter(magazine)

        for char in ransomNote:
            if magazine_count[char] <= 0:
                return False
            magazine_count[char] -= 1

        return True


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 383,
    "name": "Ransom Note",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Hash Table', 'String', 'Counting'],
    "url": "https://leetcode.com/problems/ransom-note/",
    "companies": ['Amazon', 'Microsoft', 'Apple'],
    "time_complexity": "O(m + n)",
    "space_complexity": "O(1)",
}
