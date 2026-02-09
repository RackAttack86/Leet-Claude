"""
LeetCode Problem #69: Sqrt(x)
Difficulty: Easy
Pattern: Binary Search
Link: https://leetcode.com/problems/sqrt(x)/

Problem:
--------
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

Constraints:
-----------
- 0 <= x <= 2^31 - 1

Examples:
---------
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2.

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., rounded down to 2.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #69: Sqrt(x)

    Approach: Binary Search on answer space
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Key Insights:
    - Search for answer in range [0, x]
    - Use mid * mid <= x to check
    - Be careful with integer overflow
    """

    def mySqrt(self, x: int) -> int:
        """
        Binary search for integer square root.
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 69,
    "name": "Sqrt(x)",
    "difficulty": "Easy",
    "pattern": "Binary Search",
    "topics": ['Math', 'Binary Search'],
    "url": "https://leetcode.com/problems/sqrt(x)/",
    "companies": ['Facebook', 'Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
