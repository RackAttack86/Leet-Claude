"""
LeetCode Problem #198: House Robber
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/house-robber/

Problem:
--------
You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing each of
them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night. Given an
integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.

Constraints:
-----------
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

Examples:
---------
Input: nums = [1,2,3,1]
Output: 4

Input: nums = [2,7,9,3,1]
Output: 12
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #198: House Robber

    Approach: Dynamic Programming
    Time Complexity: O(n)
    Space Complexity: O(1) with space optimization

    Key Insights:
    - dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    - Either rob current house or skip it
    - Can optimize to O(1) space with two variables
    - Classic DP with non-adjacent constraint
    """

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = 0, 0

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 198,
    "name": "House Robber",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ["Array", "Dynamic Programming"],
    "url": "https://leetcode.com/problems/house-robber/",
    "companies": ["Amazon", "Google", "Airbnb"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
