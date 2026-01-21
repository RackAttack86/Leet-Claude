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

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 383,
    "name": "Ransom Note",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Hash Table', 'String', 'Counting'],
    "url": "https://leetcode.com/problems/ransom-note/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
