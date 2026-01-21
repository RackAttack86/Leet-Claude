"""
LeetCode Problem #120: Triangle
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/triangle/

Problem:
--------
Given a `triangle` array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

Constraints:
-----------
- `1
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- 10^4

Examples:
---------
Example 1:
```

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

```

Example 2:
```

Input: triangle = [[-10]]
Output: -10

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #120: Triangle

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 120,
    "name": "Triangle",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/triangle/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
