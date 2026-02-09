"""
LeetCode Problem #253: Meeting Rooms II
Difficulty: Medium
Pattern: Intervals
Link: https://leetcode.com/problems/meeting-rooms-ii/

Problem:
--------
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Constraints:
-----------
- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6

Examples:
---------
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Input: intervals = [[7,10],[2,4]]
Output: 1
"""

from typing import List, Optional
import heapq


class Solution:
    """
    Solution to LeetCode Problem #253: Meeting Rooms II

    Approach: Min heap or chronological ordering
    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Key Insights:
    - Use min heap to track end times
    - Add meeting, remove finished ones
    - Heap size = rooms needed at any time
    - Or use start/end time arrays
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Find minimum number of conference rooms required.

        Use a min-heap to track end times of meetings.
        For each meeting, if it starts after the earliest ending meeting,
        we can reuse that room (pop from heap). Otherwise, we need a new room.
        """
        if not intervals:
            return 0

        # Sort meetings by start time
        intervals.sort(key=lambda x: x[0])

        # Min-heap to track end times of ongoing meetings
        heap = []

        for interval in intervals:
            start, end = interval

            # If current meeting starts after the earliest ending meeting
            if heap and start >= heap[0]:
                # Reuse that room (remove its end time and add new one)
                heapq.heappop(heap)

            # Add current meeting's end time
            heapq.heappush(heap, end)

        # The size of heap is the number of rooms needed
        return len(heap)


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 253,
    "name": "Meeting Rooms II",
    "difficulty": "Medium",
    "pattern": "Intervals",
    "topics": ['Array', 'Two Pointers', 'Greedy', 'Sorting', 'Heap (Priority Queue)', 'Prefix Sum'],
    "url": "https://leetcode.com/problems/meeting-rooms-ii/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
}
