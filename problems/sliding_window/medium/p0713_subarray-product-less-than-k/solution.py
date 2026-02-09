"""
LeetCode Problem #713: Subarray Product Less Than K
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/subarray-product-less-than-k/

Problem:
--------
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Constraints:
-----------
- 1 <= nums.length <= 3 * 10^4
- 1 <= nums[i] <= 1000
- 0 <= k <= 10^6

Examples:
---------
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

Input: nums = [1,2,3], k = 0
Output: 0
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #713: Subarray Product Less Than K

    Approach: Sliding Window
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Expand window while product < k
    - Contract window when product >= k
    - For window [left, right], adds (right - left + 1) subarrays
    - All positive numbers simplify the problem
    """

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Count subarrays where product of all elements is strictly less than k.

        Uses sliding window. For each position right, count subarrays ending at right
        with product < k. When product >= k, shrink window from left.
        """
        if k <= 1:
            return 0

        count = 0
        product = 1
        left = 0

        for right in range(len(nums)):
            product *= nums[right]

            # Shrink window while product >= k
            while product >= k:
                product //= nums[left]
                left += 1

            # All subarrays ending at right with start in [left, right] are valid
            # Number of such subarrays = right - left + 1
            count += right - left + 1

        return count


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 713,
    "name": "Subarray Product Less Than K",
    "difficulty": "Medium",
    "pattern": "Sliding Window",
    "topics": ['Array', 'Sliding Window'],
    "url": "https://leetcode.com/problems/subarray-product-less-than-k/",
    "companies": ['Amazon', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
