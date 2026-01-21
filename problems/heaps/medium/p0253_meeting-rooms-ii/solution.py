"""
LeetCode Problem #253: Meeting Rooms II
Difficulty: Medium
Pattern: Heaps
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

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

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

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        heap = []

        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return len(heap) # Number of rooms needed

# Metadata for tracking
PROBLEM_METADATA = {
    "number": 253,
    "name": "Meeting Rooms II",
    "difficulty": "Medium",
    "pattern": "Heaps",
    "topics": ['Array', 'Two Pointers', 'Greedy', 'Sorting', 'Heap (Priority Queue)', 'Prefix Sum'],
    "url": "https://leetcode.com/problems/meeting-rooms-ii/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
}
