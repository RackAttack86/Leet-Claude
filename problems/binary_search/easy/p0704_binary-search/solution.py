"""
LeetCode Problem #704: Binary Search
Difficulty: Easy
Pattern: Binary Search
Link: https://leetcode.com/problems/binary-search/

Problem:
--------
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

Constraints:
-----------
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique
- nums is sorted in ascending order

Examples:
---------
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #704: Binary Search

    Approach: Standard binary search
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Key Insights:
    - Classic binary search implementation
    - Compare mid with target
    - Adjust left or right pointer
    - Template for all binary search problems
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 704,
    "name": "Binary Search",
    "difficulty": "Easy",
    "pattern": "Binary Search",
    "topics": ["Array", "Binary Search"],
    "url": "https://leetcode.com/problems/binary-search/",
    "companies": ["Amazon", "Google", "Microsoft"],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
