"""
LeetCode Problem #1: Two Sum
Difficulty: Easy
Pattern: Two Pointers / Hash Table
Link: https://leetcode.com/problems/two-sum/

Problem:
--------
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Constraints:
-----------
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

Examples:
---------
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


class Solution:
    """
    Solution to LeetCode Problem #1: Two Sum

    Approach: Hash Map (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(n)

    Key Insights:
    - Instead of checking all pairs with nested loops (O(n^2)),
      use a hash map to store complements
    - For each number, check if its complement (target - num) exists
    - Trade space for time: O(n) space for O(n) time
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices where nums[i] + nums[j] = target.

        Args:
            nums: List of integers
            target: Target sum value

        Returns:
            List containing two indices [i, j] where nums[i] + nums[j] = target
        """
        seen = {}  # num -> index mapping

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []  # No solution found (shouldn't happen per constraints)

    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force approach for comparison.
        Time: O(n^2), Space: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 1,
    "name": "Two Sum",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ["Array", "Hash Table"],
    "url": "https://leetcode.com/problems/two-sum/",
    "companies": ["Amazon", "Google", "Facebook", "Microsoft", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}
