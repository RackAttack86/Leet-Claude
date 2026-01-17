"""
LeetCode Problem #759: Employee Free Time
Difficulty: Hard
Pattern: Intervals
Link: https://leetcode.com/problems/employee-free-time/

Problem:
--------
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Constraints:
-----------
- 1 <= schedule.length, schedule[i].length <= 50
- 0 <= schedule[i].start < schedule[i].end <= 10^8

Examples:
---------
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common free time intervals would be [-inf, 1], [3, 4], [10, inf].

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #759: Employee Free Time

    Approach: Merge all intervals, find gaps
    Time Complexity: O(n log n) where n is total intervals
    Space Complexity: O(n)

    Key Insights:
    - Flatten and sort all intervals
    - Merge overlapping intervals
    - Gaps between merged intervals are free time
    - Similar to merge intervals
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 759,
    "name": "Employee Free Time",
    "difficulty": "Hard",
    "pattern": "Intervals",
    "topics": ['Array', 'Sorting', 'Heap (Priority Queue)'],
    "url": "https://leetcode.com/problems/employee-free-time/",
    "companies": ['Amazon', 'Google', 'Uber'],
    "time_complexity": "O(n log n) where n is total intervals",
    "space_complexity": "O(n)",
}
