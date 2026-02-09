"""
LeetCode Problem #1197: Minimum Knight Moves
Difficulty: Medium
Pattern: Bfs Dfs
Link: https://leetcode.com/problems/minimum-knight-moves/

Problem:
--------
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

Constraints:
-----------
- | x| + |y| <= 300

Examples:
---------
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] -> [2, 1]

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] -> [2, 1] -> [4, 2] -> [3, 4] -> [5, 5]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #1197: Minimum Knight Moves

    Approach: BFS for shortest path
    Time Complexity: O(max(|x|, |y|)^2)
    Space Complexity: O(max(|x|, |y|)^2)

    Key Insights:
    - Use BFS to find shortest path
    - 8 possible knight moves
    - Track visited positions
    - Can optimize with symmetry
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 1197,
    "name": "Minimum Knight Moves",
    "difficulty": "Medium",
    "pattern": "Bfs Dfs",
    "topics": ['Breadth-First Search'],
    "url": "https://leetcode.com/problems/minimum-knight-moves/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(max(|x|, |y|)^2)",
    "space_complexity": "O(max(|x|, |y|)^2)",
}