"""
LeetCode Problem #11: Container With Most Water
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/container-with-most-water/

Problem:
--------
You are given an integer array height of length n. There are n vertical lines drawn such
that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines
that together with the x-axis form a container, such that the container contains the most
water. Return the maximum amount of water a container can store.

Constraints:
-----------
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Examples:
---------
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1

width = j-i
height = min(i_value, j_value)
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #11: Container With Most Water

    Approach: Two Pointers (greedy)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Start with widest container
    - Move pointer with smaller height inward
    - Width decreases so need taller heights to improve
    """
    def bruteForce(self, heights: List[int]) -> int:
        pass

    def maxArea(self, height: List[int]) -> int:
        pass



PROBLEM_METADATA = {
    "number": 11,
    "name": "Container With Most Water",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ["Array", "Two Pointers", "Greedy"],
    "url": "https://leetcode.com/problems/container-with-most-water/",
    "companies": ["Amazon", "Facebook", "Google", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}