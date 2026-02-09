"""
LeetCode Problem #153: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Pattern: Binary Search
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Problem:
--------
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums of unique elements, return the minimum element of
this array. You must write an algorithm that runs in O(log n) time.

Constraints:
-----------
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique
- nums is sorted and rotated between 1 and n times

Examples:
---------
Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]
Output: 0
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #153: Find Minimum in Rotated Sorted Array

    Approach: Binary search
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Key Insights:
    - Compare mid with right
    - If mid > right, minimum is in right half
    - If mid < right, minimum is in left half or mid
    - Minimum is at rotation point
    """

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum is in right half
                left = mid + 1
            else:
                # Minimum is in left half or at mid
                right = mid

        return nums[left]


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 153,
    "name": "Find Minimum in Rotated Sorted Array",
    "difficulty": "Medium",
    "pattern": "Binary Search",
    "topics": ["Array", "Binary Search"],
    "url": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/",
    "companies": ["Amazon", "Microsoft", "Bloomberg"],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
