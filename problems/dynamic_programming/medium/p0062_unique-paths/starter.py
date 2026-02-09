"""
LeetCode Problem #62: Unique Paths
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/unique-paths/

Problem:
--------
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Constraints:
-----------
- 1 <= m, n <= 100

Examples:
---------
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation: From top-left corner, there are 3 ways to reach bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #62: Unique Paths

    Approach: Dynamic Programming or Math (combinations)
    Time Complexity: O(m * n)
    Space Complexity: O(n) with space optimization

    Key Insights:
    - dp[i][j] = dp[i-1][j] + dp[i][j-1]
    - Can optimize to 1D array
    - Math solution: C(m+n-2, m-1)
    - Each cell's paths = sum of paths from top and left
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 62,
    "name": "Unique Paths",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['Math', 'Dynamic Programming', 'Combinatorics'],
    "url": "https://leetcode.com/problems/unique-paths/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(m * n)",
    "space_complexity": "O(n) with space optimization",
}