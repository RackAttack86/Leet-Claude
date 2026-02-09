"""
LeetCode Problem #55: Jump Game
Difficulty: Medium
Pattern: Greedy
Link: https://leetcode.com/problems/jump-game/

Problem:
--------
You are given an integer array nums. You are initially positioned at the array's first
index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Constraints:
-----------
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

Examples:
---------
Input: nums = [2,3,1,1,4]
Output: true

Input: nums = [3,2,1,0,4]
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #55: Jump Game

    Approach: Greedy tracking max reach
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Track maximum reachable position
    - If current index > max reach, return false
    - Update max reach at each step
    - Simple one-pass solution
    """

    def canJump(self, nums: List[int]) -> bool:
        """
        Determine if you can reach the last index.

        Args:
            nums: Array where nums[i] is max jump length from index i

        Returns:
            True if you can reach the last index, False otherwise
        """
        max_reach = 0
        n = len(nums)

        for i in range(n):
            # If current position is beyond max reach, we can't get here
            if i > max_reach:
                return False

            # Update the farthest position we can reach
            max_reach = max(max_reach, i + nums[i])

            # Early termination if we can already reach the end
            if max_reach >= n - 1:
                return True

        return True


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 55,
    "name": "Jump Game",
    "difficulty": "Medium",
    "pattern": "Greedy",
    "topics": ["Array", "Dynamic Programming", "Greedy"],
    "url": "https://leetcode.com/problems/jump-game/",
    "companies": ["Amazon", "Microsoft", "Google"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
