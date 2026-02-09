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

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.

        Sort by start time, then iterate through and merge overlapping intervals.
        Two intervals overlap if current.start <= previous.end.
        """
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            last = result[-1]

            # If current interval overlaps with last merged interval
            if current[0] <= last[1]:
                # Merge by extending the end time
                last[1] = max(last[1], current[1])
            else:
                # No overlap, add current interval
                result.append(current)

        return result


# Metadata for tracking
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
