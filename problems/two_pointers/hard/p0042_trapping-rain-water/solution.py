"""
LeetCode Problem #42: Trapping Rain Water
Difficulty: Hard
Pattern: Two Pointers
Link: https://leetcode.com/problems/trapping-rain-water/

Problem:
--------
Given n non-negative integers representing an elevation map where the width of each bar
is 1, compute how much water it can trap after raining.

Constraints:
-----------
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

Examples:
---------
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #42: Trapping Rain Water

    Approach: Two Pointers or Dynamic Programming
    Time Complexity: O(n)
    Space Complexity: O(1) for two pointers, O(n) for DP

    Key Insights:
    - Water trapped = min(max_left, max_right) - current_height
    - Two pointers: move from side with smaller max
    - Or precompute max left/right arrays
    """

    def solve(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        total = 0

        while l<r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    total += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    total += right_max - height[r]
                r -= 1
        return total


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 42,
    "name": "Trapping Rain Water",
    "difficulty": "Hard",
    "pattern": "Two Pointers",
    "topics": ["Array", "Two Pointers", "Dynamic Programming", "Stack"],
    "url": "https://leetcode.com/problems/trapping-rain-water/",
    "companies": ["Amazon", "Google", "Apple", "Facebook"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
