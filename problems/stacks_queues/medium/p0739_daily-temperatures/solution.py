"""
LeetCode Problem #739: Daily Temperatures
Difficulty: Medium
Pattern: Stacks Queues
Link: https://leetcode.com/problems/daily-temperatures/

Problem:
--------
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Constraints:
-----------
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

Examples:
---------
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #739: Daily Temperatures

    Approach: Monotonic stack
    Time Complexity: O(n)
    Space Complexity: O(n)

    Key Insights:
    - Use monotonic decreasing stack
    - Store indices in stack
    - Calculate days difference when finding warmer
    - Classic next greater element variant
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Find days until warmer temperature for each day.

        Use monotonic decreasing stack storing indices.
        When we find a warmer temperature, calculate the difference
        in days for all stack indices with lower temperatures.
        """
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stack of indices

        for i in range(n):
            # While current temp is greater than temp at stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx

            stack.append(i)

        # Remaining indices in stack have no warmer day (stay 0)
        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 739,
    "name": "Daily Temperatures",
    "difficulty": "Medium",
    "pattern": "Stacks Queues",
    "topics": ['Array', 'Stack', 'Monotonic Stack'],
    "url": "https://leetcode.com/problems/daily-temperatures/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}
