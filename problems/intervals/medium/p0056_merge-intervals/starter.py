"""
LeetCode Problem #56: Merge Intervals
Difficulty: Medium
Pattern: Intervals
Link: https://leetcode.com/problems/merge-intervals/

Problem:
--------
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Constraints:
-----------
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

Examples:
---------
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #56: Merge Intervals

    Approach: Sort and merge
    Time Complexity: O(n log n)
    Space Complexity: O(n) for output

    Key Insights:
    - Sort intervals by start time
    - Merge if current.start <= prev.end
    - Track end of current merged interval
    - Classic interval merge pattern
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 56,
    "name": "Merge Intervals",
    "difficulty": "Medium",
    "pattern": "Intervals",
    "topics": ["Array", "Sorting"],
    "url": "https://leetcode.com/problems/merge-intervals/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Bloomberg", "Apple"],
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
}