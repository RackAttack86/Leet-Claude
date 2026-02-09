"""
LeetCode Problem #40: Combination Sum II
Difficulty: Medium
Pattern: Backtracking
Link: https://leetcode.com/problems/combination-sum-ii/

Problem:
--------
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations.

Constraints:
-----------
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

Examples:
---------
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #40: Combination Sum II

    Approach: Backtracking with duplicate skipping
    Time Complexity: O(2^n)
    Space Complexity: O(n)

    Key Insights:
    - Sort array first
    - Skip duplicates at same recursion level
    - Each element used at most once
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 40,
    "name": "Combination Sum II",
    "difficulty": "Medium",
    "pattern": "Backtracking",
    "topics": ['Array', 'Backtracking'],
    "url": "https://leetcode.com/problems/combination-sum-ii/",
    "companies": ['Amazon', 'Facebook', 'Microsoft'],
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
}