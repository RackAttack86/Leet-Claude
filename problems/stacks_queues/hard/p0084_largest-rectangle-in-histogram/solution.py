"""
LeetCode Problem #84: Largest Rectangle in Histogram
Difficulty: Hard
Pattern: Stacks Queues
Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

Problem:
--------
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Constraints:
-----------
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

Examples:
---------
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Input: heights = [2,4]
Output: 4
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #84: Largest Rectangle in Histogram

    Approach: Monotonic stack
    Time Complexity: O(n)
    Space Complexity: O(n)

    Key Insights:
    - Use stack to track indices
    - Maintain increasing heights in stack
    - Calculate area when popping
    - Classic monotonic stack problem
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack of indices
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        # Process remaining bars in stack
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 84,
    "name": "Largest Rectangle in Histogram",
    "difficulty": "Hard",
    "pattern": "Stacks Queues",
    "topics": ['Array', 'Stack', 'Monotonic Stack'],
    "url": "https://leetcode.com/problems/largest-rectangle-in-histogram/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}
