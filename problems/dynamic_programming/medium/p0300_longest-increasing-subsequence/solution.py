"""
LeetCode Problem #300: Longest Increasing Subsequence
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Problem:
--------
Given an integer array nums, return the length of the longest strictly increasing
subsequence.

Constraints:
-----------
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

Examples:
---------
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101]

Input: nums = [0,1,0,3,2,3]
Output: 4
"""

from typing import List, Optional
import bisect


class Solution:
    """
    Solution to LeetCode Problem #300: Longest Increasing Subsequence

    Approach: Dynamic Programming or Binary Search
    Time Complexity: O(n^2) for DP, O(n log n) for binary search
    Space Complexity: O(n)

    Key Insights:
    - DP: dp[i] = max length ending at i
    - For each i, check all j < i where nums[j] < nums[i]
    - Binary search: maintain array of smallest tail for each length
    - Patience sorting algorithm for O(n log n)
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n log n) solution using binary search
        tails = []

        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 300,
    "name": "Longest Increasing Subsequence",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ["Array", "Binary Search", "Dynamic Programming"],
    "url": "https://leetcode.com/problems/longest-increasing-subsequence/",
    "companies": ["Microsoft", "Amazon", "Google"],
    "time_complexity": "O(n^2) or O(n log n)",
    "space_complexity": "O(n)",
}
