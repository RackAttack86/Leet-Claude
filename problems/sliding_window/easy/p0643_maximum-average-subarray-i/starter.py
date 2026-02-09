"""
LeetCode Problem #643: Maximum Average Subarray I
Difficulty: Easy
Pattern: Sliding Window
Link: https://leetcode.com/problems/maximum-average-subarray-i/

Problem:
--------
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

Constraints:
-----------
- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

Examples:
---------
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Input: nums = [5], k = 1
Output: 5.00000
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #643: Maximum Average Subarray I

    Approach: Sliding Window
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Fixed window size k
    - Calculate initial sum of first k elements
    - Slide window: add new element, remove old element
    - Track maximum sum
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 643,
    "name": "Maximum Average Subarray I",
    "difficulty": "Easy",
    "pattern": "Sliding Window",
    "topics": ['Array', 'Sliding Window'],
    "url": "https://leetcode.com/problems/maximum-average-subarray-i/",
    "companies": ['Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}