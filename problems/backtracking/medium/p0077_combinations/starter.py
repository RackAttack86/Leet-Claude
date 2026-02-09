"""
LeetCode Problem #77: Combinations
Difficulty: Medium
Pattern: Backtracking
Link: https://leetcode.com/problems/combinations/

Problem:
--------
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Constraints:
-----------
- 1 <= n <= 20
- 1 <= k <= n

Examples:
---------
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Input: n = 1, k = 1
Output: [[1]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #77: Combinations

    Approach: Backtracking
    Time Complexity: O(C(n,k) * k) = O(n! / (k! * (n-k)!))
    Space Complexity: O(k)

    Key Insights:
    - Choose k elements from 1 to n
    - Backtrack with start index to avoid duplicates
    - Stop when combination has k elements
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 77,
    "name": "Combinations",
    "difficulty": "Medium",
    "pattern": "Backtracking",
    "topics": ['Backtracking'],
    "url": "https://leetcode.com/problems/combinations/",
    "companies": ['Amazon', 'Facebook', 'Microsoft', 'Google'],
    "time_complexity": "O(C(n,k) * k) = O(n! / (k! * (n-k)!))",
    "space_complexity": "O(k)",
}