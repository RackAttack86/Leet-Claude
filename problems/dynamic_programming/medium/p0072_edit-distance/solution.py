"""
LeetCode Problem #72: Edit Distance
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/edit-distance/

Problem:
--------
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

- Insert a character
	
- Delete a character
	
- Replace a character

Constraints:
-----------
- `0
- word1` and `word2` consist of lowercase English letters.

Examples:
---------
Example 1:
```

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

```

Example 2:
```

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #72: Edit Distance

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def minDistance(self, word1: str, word2: str) -> int:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 72,
    "name": "Edit Distance",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['String', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/edit-distance/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
