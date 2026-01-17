"""
LeetCode Problem #134: Gas Station
Difficulty: Medium
Pattern: Greedy
Link: https://leetcode.com/problems/gas-station/

Problem:
--------
There are n gas stations along a circular route, where the amount of gas at the ith station
is gas[i]. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from the ith station to its next (i + 1)th station. You begin the journey with an empty
tank at one of the gas stations. Given two integer arrays gas and cost, return the starting
gas station's index if you can travel around the circuit once in the clockwise direction,
otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Constraints:
-----------
- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4

Examples:
---------
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #134: Gas Station

    Approach: Greedy with total and current tank
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - If total gas < total cost, impossible
    - If tank becomes negative, start can't be before current
    - Reset start position when tank negative
    - One pass solution
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 134,
    "name": "Gas Station",
    "difficulty": "Medium",
    "pattern": "Greedy",
    "topics": ["Array", "Greedy"],
    "url": "https://leetcode.com/problems/gas-station/",
    "companies": ["Amazon", "Google"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
