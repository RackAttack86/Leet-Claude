"""
LeetCode Problem #45: Jump Game II
Difficulty: Medium
Pattern: Greedy
Link: https://leetcode.com/problems/jump-game-ii/

Problem:
--------
You are given a 0-indexed array of integers nums of length n. You are initially positioned
at nums[0]. Each element nums[i] represents the maximum length of a forward jump from index
i. In other words, if you are at nums[i], you can jump to any nums[i + j] where 0 <= j <=
nums[i] and i + j < n. Return the minimum number of jumps to reach nums[n - 1]. The test
cases are generated such that you can reach nums[n - 1].

Constraints:
-----------
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1]

Examples:
---------
Input: nums = [2,3,1,1,4]
Output: 2

Input: nums = [2,3,0,1,4]
Output: 2
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #45: Jump Game II

    Approach: Greedy with range tracking
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Track current jump end and farthest reachable
    - Increment jumps when reaching current end
    - Update farthest as you iterate
    - BFS-like level order traversal
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 45,
    "name": "Jump Game II",
    "difficulty": "Medium",
    "pattern": "Greedy",
    "topics": ["Array", "Dynamic Programming", "Greedy"],
    "url": "https://leetcode.com/problems/jump-game-ii/",
    "companies": ["Amazon", "Adobe", "ByteDance"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}