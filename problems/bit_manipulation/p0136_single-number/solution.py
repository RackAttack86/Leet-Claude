"""
LeetCode Problem #136: Single Number
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/single-number/

Problem:
--------
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one. You must implement a solution with linear runtime complexity
and use only constant extra space.

Constraints:
-----------
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once

Examples:
---------
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #136: Single Number

    Approach: XOR all elements
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - XOR of two equal numbers is 0
    - XOR of 0 and any number is that number
    - XOR all elements to find single one
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 136,
    "name": "Single Number",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ["Array", "Bit Manipulation"],
    "url": "https://leetcode.com/problems/single-number/",
    "companies": ["Amazon", "Google", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
