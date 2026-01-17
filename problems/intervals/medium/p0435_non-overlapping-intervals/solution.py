"""
LeetCode Problem #435: Non-overlapping Intervals
Difficulty: Medium
Pattern: Intervals
Link: https://leetcode.com/problems/non-overlapping-intervals/

Problem:
--------
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Constraints:
-----------
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4

Examples:
---------
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #435: Non-overlapping Intervals

    Approach: Greedy: sort by end time
    Time Complexity: O(n log n)
    Space Complexity: O(1)

    Key Insights:
    - Sort by end time
    - Greedily keep intervals with earliest end
    - Count intervals that don't overlap
    - Answer = total - kept
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 435,
    "name": "Non-overlapping Intervals",
    "difficulty": "Medium",
    "pattern": "Intervals",
    "topics": ['Array', 'Dynamic Programming', 'Greedy', 'Sorting'],
    "url": "https://leetcode.com/problems/non-overlapping-intervals/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
}
