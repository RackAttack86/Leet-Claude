"""
LeetCode Problem #15: 3Sum
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/3sum/

Problem:
--------
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the
solution set must not contain duplicate triplets.

Constraints:
-----------
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Examples:
---------
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = [0,1,1]
Output: []
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #15: 3Sum

    Approach: Sort the array, then use two pointers technique. For each element,
    fix it as the first number and use two pointers to find pairs that sum to
    the negative of that number. Skip duplicates to avoid duplicate triplets.

    Time Complexity: O(n^2) - O(n log n) sorting + O(n) outer loop * O(n) two-pointer scan
    Space Complexity: O(1) - excluding the output array, only constant extra space used

    Key Insights:
    - Sorting enables efficient duplicate skipping and two-pointer technique
    - Converting 3Sum to 2Sum problem by fixing one element
    - Skip duplicates at all three positions (i, left, right) to avoid duplicate triplets
    - Two pointers converge based on whether sum is too small or too large
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass



PROBLEM_METADATA = {
    "number": 15,
    "name": "3Sum",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ["Array", "Two Pointers", "Sorting"],
    "url": "https://leetcode.com/problems/3sum/",
    "companies": ["Facebook", "Amazon", "Microsoft", "Google"],
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
}