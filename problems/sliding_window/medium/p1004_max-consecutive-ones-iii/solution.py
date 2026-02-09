"""
LeetCode Problem #1004: Max Consecutive Ones III
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/max-consecutive-ones-iii/

Problem:
--------
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Constraints:
-----------
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
- 0 <= k <= nums.length

Examples:
---------
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #1004: Max Consecutive Ones III

    Approach: Sliding Window
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Track count of zeros in window
    - Expand window with right pointer
    - Contract window when zeros > k
    - Window size gives consecutive 1's after flips
    """

    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Find maximum consecutive 1's if at most k 0's can be flipped.

        Uses sliding window. Track count of zeros in window.
        Shrink window when zeros exceed k.
        """
        max_length = 0
        zero_count = 0
        left = 0

        for right in range(len(nums)):
            # Add element to window
            if nums[right] == 0:
                zero_count += 1

            # Shrink window while zeros exceed k
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 1004,
    "name": "Max Consecutive Ones III",
    "difficulty": "Medium",
    "pattern": "Sliding Window",
    "topics": ['Array', 'Binary Search', 'Sliding Window', 'Prefix Sum'],
    "url": "https://leetcode.com/problems/max-consecutive-ones-iii/",
    "companies": ['Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
