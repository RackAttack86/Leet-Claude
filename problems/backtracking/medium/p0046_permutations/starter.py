"""
LeetCode Problem #46: Permutations
Difficulty: Medium
Pattern: Backtracking
Link: https://leetcode.com/problems/permutations/

Problem:
--------
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Constraints:
-----------
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique

Examples:
---------
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #46: Permutations

    Approach: Backtracking with swapping or used array
    Time Complexity: O(n! * n)
    Space Complexity: O(n)

    Key Insights:
    - Use backtracking to generate permutations
    - Track used elements or use swapping
    - Add to result when permutation complete
    - Classic backtracking problem
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 46,
    "name": "Permutations",
    "difficulty": "Medium",
    "pattern": "Backtracking",
    "topics": ["Array", "Backtracking"],
    "url": "https://leetcode.com/problems/permutations/",
    "companies": ["Microsoft", "Amazon", "LinkedIn"],
    "time_complexity": "O(n!)",
    "space_complexity": "O(n!)",
}