"""
LeetCode Problem #268: Missing Number
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/missing-number/

Problem:
--------
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Constraints:
-----------
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique

Examples:
---------
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in range [0,3]. 2 is missing.

Input: nums = [0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #268: Missing Number

    Approach: XOR or Math (sum)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - XOR all indices and values
    - Missing number remains after XOR
    - Or use expected sum - actual sum
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 268,
    "name": "Missing Number",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ['Array', 'Hash Table', 'Math', 'Binary Search', 'Bit Manipulation', 'Sorting'],
    "url": "https://leetcode.com/problems/missing-number/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
