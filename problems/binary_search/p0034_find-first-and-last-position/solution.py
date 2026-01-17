"""
LeetCode Problem #34: Find First and Last Position
Difficulty: Medium
Pattern: Binary Search
Link: https://leetcode.com/problems/find-first-and-last-position/

Problem:
--------
Given an array of integers nums sorted in non-decreasing order, find the starting and
ending position of a given target value. If target is not found in the array, return
[-1, -1]. You must write an algorithm with O(log n) runtime complexity.

Constraints:
-----------
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array
- -10^9 <= target <= 10^9

Examples:
---------
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #34: Find First and Last Position

    Approach: Binary search twice (first and last position)
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Key Insights:
    - Find leftmost position with binary search
    - Find rightmost position with binary search
    - Modify binary search to find boundaries
    - Two separate binary searches
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 34,
    "name": "Find First and Last Position",
    "difficulty": "Medium",
    "pattern": "Binary Search",
    "topics": ["Array", "Binary Search"],
    "url": "https://leetcode.com/problems/find-first-and-last-position/",
    "companies": ["Facebook", "Amazon", "Google"],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
