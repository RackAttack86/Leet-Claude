"""
LeetCode Problem #58: Length of Last Word
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/length-of-last-word/

Problem:
--------
Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Constraints:
-----------
- `1
- s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

Examples:
---------
Example 1:
```

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

```

Example 2:
```

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

```

Example 3:
```

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #58: Length of Last Word

    Approach: Reverse Traversal
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) - only using pointers

    Key Insights:
    - Start from the end and skip trailing spaces
    - Count characters until we hit a space or reach the beginning
    - Using strip() and split() works but uses O(n) extra space
    """

    def lengthOfLastWord(self, s: str) -> int:
        """
        Return the length of the last word in the string.

        Args:
            s: Input string with words and spaces

        Returns:
            Length of the last word
        """
        # Start from the end
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count the last word
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 58,
    "name": "Length of Last Word",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['String'],
    "url": "https://leetcode.com/problems/length-of-last-word/",
    "companies": ['Amazon', 'Google', 'Microsoft'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
