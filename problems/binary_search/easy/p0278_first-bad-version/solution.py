"""
LeetCode Problem #278: First Bad Version
Difficulty: Easy
Pattern: Binary Search
Link: https://leetcode.com/problems/first-bad-version/

Problem:
--------
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Constraints:
-----------
- 1 <= bad <= n <= 2^31 - 1

Examples:
---------
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
"""

from typing import List, Optional


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass  # This is provided by LeetCode


class Solution:
    """
    Solution to LeetCode Problem #278: First Bad Version

    Approach: Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Key Insights:
    - Classic binary search for first occurrence
    - If version is bad, search left half
    - If version is good, search right half
    """

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 278,
    "name": "First Bad Version",
    "difficulty": "Easy",
    "pattern": "Binary Search",
    "topics": ['Binary Search', 'Interactive'],
    "url": "https://leetcode.com/problems/first-bad-version/",
    "companies": ['Facebook', 'Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}
