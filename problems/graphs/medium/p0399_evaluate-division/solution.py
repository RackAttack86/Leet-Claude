"""
LeetCode Problem #399: Evaluate Division
Difficulty: Medium
Pattern: Graphs
Link: https://leetcode.com/problems/evaluate-division/

Problem:
--------
You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the `j^th` query where you must find the answer for `Cj / Dj = ?`.

Return the answers to all queries. If a single answer cannot be determined, return `-1.0`.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Constraints:
-----------
- `1
- equations[i].length == 2
- 1 i.length, Bi.length
- values.length == equations.length
- 0.0
- queries[i].length == 2
- 1 j.length, Dj.length
- Ai, Bi, Cj, Dj` consist of lower case English letters and digits.

Examples:
---------
Example 1:
```

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
```

Example 2:
```

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

```

Example 3:
```

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #399: Evaluate Division

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 399,
    "name": "Evaluate Division",
    "difficulty": "Medium",
    "pattern": "Graphs",
    "topics": ['Array', 'String', 'Depth-First Search', 'Breadth-First Search', 'Union-Find', 'Graph Theory', 'Shortest Path'],
    "url": "https://leetcode.com/problems/evaluate-division/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
