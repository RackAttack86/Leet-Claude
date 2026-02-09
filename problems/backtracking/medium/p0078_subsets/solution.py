"""
LeetCode Problem #78: Subsets
Difficulty: Medium
Pattern: Backtracking
Link: https://leetcode.com/problems/subsets/

Problem:
--------
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
-----------
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique

Examples:
---------
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #78: Subsets

    Approach: Backtracking or iterative
    Time Complexity: O(2^n * n)
    Space Complexity: O(n) for recursion

    Key Insights:
    - Each element has two choices: include or exclude
    - Backtrack with start index
    - Add current subset at each step
    - 2^n total subsets
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int, current: List[int]):
            result.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 78,
    "name": "Subsets",
    "difficulty": "Medium",
    "pattern": "Backtracking",
    "topics": ["Array", "Backtracking", "Bit Manipulation"],
    "url": "https://leetcode.com/problems/subsets/",
    "companies": ["Amazon", "Facebook", "Google"],
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
}
