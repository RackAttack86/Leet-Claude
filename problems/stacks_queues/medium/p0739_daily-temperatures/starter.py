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
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



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