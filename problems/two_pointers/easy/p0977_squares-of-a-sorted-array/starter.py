"""
LeetCode Problem #977: Squares of a Sorted Array
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/squares-of-a-sorted-array/

Problem:
--------
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints:
-----------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order

Examples:
---------
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, [16,1,0,9,100]. After sorting, [0,1,9,16,100]

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #977: Squares of a Sorted Array

    Approach: Two Pointers (from both ends)
    Time Complexity: O(n)
    Space Complexity: O(n)

    Key Insights:
    - Largest squares come from either end (most negative or most positive)
    - Use two pointers to compare absolute values
    - Fill result array from right to left with larger values
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pass



PROBLEM_METADATA = {
    "number": 977,
    "name": "Squares of a Sorted Array",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Two Pointers', 'Sorting'],
    "url": "https://leetcode.com/problems/squares-of-a-sorted-array/",
    "companies": ['Facebook', 'Amazon', 'Microsoft'],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}