"""
LeetCode Problem #213: House Robber II
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/house-robber-ii/

Problem:
--------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
-----------
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Examples:
---------
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #213: House Robber II

    Approach: Dynamic Programming (House Robber with circle)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Cannot rob both first and last house
    - Run House Robber I twice: [0:n-1] and [1:n]
    - Take maximum of both results
    - Reduces to House Robber I problem
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 213,
    "name": "House Robber II",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/house-robber-ii/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}