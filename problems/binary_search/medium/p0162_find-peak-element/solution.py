"""
LeetCode Problem #162: Find Peak Element
Difficulty: Medium
Pattern: Binary Search
Link: https://leetcode.com/problems/find-peak-element/

Problem:
--------
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Constraints:
-----------
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i

Examples:
---------
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element.

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: 6 is a peak element.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #162: Find Peak Element

    Approach: Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Key Insights:
    - If mid element is increasing, peak must be on right
    - If mid element is decreasing, peak must be on left or at mid
    - At least one peak always exists
    """

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                # Peak is on left side or at mid
                right = mid
            else:
                # Peak is on right side
                left = mid + 1

        return left


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 162,
    "name": "Find Peak Element",
    "difficulty": "Medium",
    "pattern": "Binary Search",
    "topics": ['Array', 'Binary Search'],
    "url": "https://leetcode.com/problems/find-peak-element/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
