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

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Find minimum number of intervals to remove to make the rest non-overlapping.

        Args:
            intervals: List of intervals [start, end]

        Returns:
            Minimum number of intervals to remove
        """
        if not intervals:
            return 0

        # Sort by end time - greedy approach keeps intervals that end earliest
        intervals.sort(key=lambda x: x[1])

        count = 0  # Number of intervals to remove
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                # Overlapping - remove this interval (increment count)
                count += 1
            else:
                # Non-overlapping - keep this interval, update prev_end
                prev_end = end

        return count


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
