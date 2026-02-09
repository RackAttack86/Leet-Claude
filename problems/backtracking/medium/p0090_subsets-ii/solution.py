"""
LeetCode Problem #90: Subsets II
Difficulty: Medium
Pattern: Backtracking
Link: https://leetcode.com/problems/subsets-ii/

Problem:
--------
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
-----------
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

Examples:
---------
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input: nums = [0]
Output: [[],[0]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #90: Subsets II

    Approach: Backtracking with duplicate handling
    Time Complexity: O(2^n)
    Space Complexity: O(n)

    Key Insights:
    - Sort array first
    - Skip duplicates at same level
    - Include each subset once
    """

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start: int, current: List[int]):
            result.append(current[:])

            for i in range(start, len(nums)):
                # Skip duplicates at same level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 90,
    "name": "Subsets II",
    "difficulty": "Medium",
    "pattern": "Backtracking",
    "topics": ['Array', 'Backtracking', 'Bit Manipulation'],
    "url": "https://leetcode.com/problems/subsets-ii/",
    "companies": ['Amazon', 'Facebook', 'Microsoft'],
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
}
