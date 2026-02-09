"""
LeetCode Problem #374: Guess Number Higher or Lower
Difficulty: Easy
Pattern: Binary Search
Link: https://leetcode.com/problems/guess-number-higher-or-lower/

Problem:
--------
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Constraints:
-----------
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n

Examples:
---------
Input: n = 10, pick = 6
Output: 6

Input: n = 1, pick = 1
Output: 1

Input: n = 2, pick = 1
Output: 1
"""

from typing import List, Optional


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass  # This is provided by LeetCode


class Solution:
    """
    Solution to LeetCode Problem #374: Guess Number Higher or Lower

    Approach: Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Key Insights:
    - Standard binary search
    - Use guess() API to adjust search range
    - Similar to finding target in sorted array
    """

    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:  # Mid is too high
                right = mid - 1
            else:  # result == 1, Mid is too low
                left = mid + 1
        return left


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 374,
    "name": "Guess Number Higher or Lower",
    "difficulty": "Easy",
    "pattern": "Binary Search",
    "topics": ['Binary Search', 'Interactive'],
    "url": "https://leetcode.com/problems/guess-number-higher-or-lower/",
    "companies": ['Google', 'Amazon', 'Microsoft'],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
