"""
LeetCode Problem #75: Sort Colors
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/sort-colors/

Problem:
--------
Given an array nums with n objects colored red, white, or blue, sort them in-place so
that objects of the same color are adjacent, with the colors in the order red, white,
and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and
blue, respectively. You must solve this problem without using the library's sort function.

Constraints:
-----------
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2

Examples:
---------
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #75: Sort Colors

    Approach: Dutch National Flag (Three Pointers)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Use three pointers: low, mid, high
    - Swap 0s to front, 2s to back
    - One pass solution
    """

    def sortColors(self, nums: List[int]) -> None:
        low, mid = 0, 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 75,
    "name": "Sort Colors",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ["Array", "Two Pointers", "Sorting"],
    "url": "https://leetcode.com/problems/sort-colors/",
    "companies": ["Microsoft", "Facebook", "Amazon"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
