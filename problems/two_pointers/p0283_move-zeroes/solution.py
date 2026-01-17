"""
LeetCode Problem #283: Move Zeroes
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/move-zeroes/

Problem:
--------
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements. You must do this in-place without
making a copy of the array.

Constraints:
-----------
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Examples:
---------
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #283: Move Zeroes

    Approach: Two Pointers (in-place)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Keep pointer for next non-zero position
    - Swap non-zero elements forward
    - Two passes: move non-zeros, then fill zeros
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                continue
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 283,
    "name": "Move Zeroes",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ["Array", "Two Pointers"],
    "url": "https://leetcode.com/problems/move-zeroes/",
    "companies": ["Facebook", "Bloomberg", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
