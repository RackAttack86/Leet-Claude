"""
LeetCode Problem #74: Search a 2D Matrix
Difficulty: Medium
Pattern: Binary Search
Link: https://leetcode.com/problems/search-a-2d-matrix/

Problem:
--------
You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
	
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

Constraints:
-----------
- `m == matrix.length
- n == matrix[i].length
- 10^4

Examples:
---------
Example 1:
```

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

```

Example 2:
```

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #74: Search a 2D Matrix

    Approach: Treat 2D Matrix as 1D Sorted Array
    Since each row is sorted and the first element of each row is greater than
    the last element of the previous row, the entire matrix can be treated as
    a single sorted array of length m*n.

    We perform standard binary search where:
    - Virtual index i maps to matrix[i // n][i % n]
    - Search space is 0 to m*n - 1

    Time Complexity: O(log(m*n)) - Single binary search over m*n elements
    Space Complexity: O(1) - Only using constant extra space

    Key Insights:
    1. The 2D matrix with given properties is essentially a flattened sorted array
    2. Convert 1D index to 2D coordinates: row = idx // cols, col = idx % cols
    3. Single binary search is more efficient than two binary searches
    4. Handle empty matrix edge case
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass



PROBLEM_METADATA = {
    "number": 74,
    "name": "Search a 2D Matrix",
    "difficulty": "Medium",
    "pattern": "Binary Search",
    "topics": ['Array', 'Binary Search', 'Matrix'],
    "url": "https://leetcode.com/problems/search-a-2d-matrix/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Apple", "Bloomberg", "Google", "Oracle", "Uber"],
    "time_complexity": "O(log(m*n))",
    "space_complexity": "O(1)",
}