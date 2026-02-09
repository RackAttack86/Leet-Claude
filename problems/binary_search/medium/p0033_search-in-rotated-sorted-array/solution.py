"""
LeetCode Problem #33: Search in Rotated Sorted Array
Difficulty: Medium
Pattern: Binary Search
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem:
--------
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot
index. Given the array nums after the possible rotation and an integer target, return
the index of target if it is in nums, or -1 if it is not. You must write an algorithm
with O(log n) runtime complexity.

Constraints:
-----------
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4

Examples:
---------
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #33: Search in Rotated Sorted Array

    Approach: Modified binary search
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Key Insights:
    - One half is always sorted
    - Check which half is sorted
    - Determine if target is in sorted half
    - Adjust search range accordingly
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 33,
    "name": "Search in Rotated Sorted Array",
    "difficulty": "Medium",
    "pattern": "Binary Search",
    "topics": ["Array", "Binary Search"],
    "url": "https://leetcode.com/problems/search-in-rotated-sorted-array/",
    "companies": ["Facebook", "Amazon", "Microsoft", "LinkedIn"],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
