"""
LeetCode Problem #252: Meeting Rooms
Difficulty: Easy
Pattern: Intervals
Link: https://leetcode.com/problems/meeting-rooms/

Problem:
--------
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Constraints:
-----------
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti < endi <= 10^6

Examples:
---------
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Input: intervals = [[7,10],[2,4]]
Output: true
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #252: Meeting Rooms

    Approach: Sort and check consecutive overlaps
    Time Complexity: O(n log n)
    Space Complexity: O(1)

    Key Insights:
    - Sort intervals by start time
    - Check if any consecutive intervals overlap
    - Overlap if prev.end > curr.start
    - Simple one-pass after sorting
    """

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        # Check for overlaps
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 252,
    "name": "Meeting Rooms",
    "difficulty": "Easy",
    "pattern": "Intervals",
    "topics": ['Array', 'Sorting'],
    "url": "https://leetcode.com/problems/meeting-rooms/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
}
