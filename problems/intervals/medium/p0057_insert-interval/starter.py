"""
LeetCode Problem #57: Insert Interval
Difficulty: Medium
Pattern: Intervals
Link: https://leetcode.com/problems/insert-interval/

Problem:
--------
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by
starti. You are also given an interval newInterval = [start, end] that represents the start and
end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Constraints:
-----------
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by starti in ascending order
- newInterval.length == 2
- 0 <= start <= end <= 10^5

Examples:
---------
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #57: Insert Interval

    Approach: Three-way split: before, merge, after
    Time Complexity: O(n)
    Space Complexity: O(n) for output

    Key Insights:
    - Add all intervals before newInterval
    - Merge overlapping intervals
    - Add all intervals after newInterval
    - Linear time since already sorted
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 57,
    "name": "Insert Interval",
    "difficulty": "Medium",
    "pattern": "Intervals",
    "topics": ["Array"],
    "url": "https://leetcode.com/problems/insert-interval/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "LinkedIn", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}