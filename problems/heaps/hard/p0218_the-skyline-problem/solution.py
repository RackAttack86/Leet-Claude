"""
LeetCode Problem #218: The Skyline Problem
Difficulty: Hard
Pattern: Heaps
Link: https://leetcode.com/problems/the-skyline-problem/

Problem:
--------
A city's skyline is the outer contour of the silhouette formed by all the buildings
when viewed from a distance. Given the locations and heights of all buildings as
buildings[i] = [left, right, height], return the skyline formed as a list of key points.

Each key point is the left endpoint of a horizontal segment in the skyline.
The last point has y=0 marking the termination of the skyline.

Constraints:
-----------
- 1 <= buildings.length <= 10^4
- 0 <= left < right <= 2^31 - 1
- 1 <= height <= 2^31 - 1
- buildings is sorted by left in non-decreasing order

Examples:
---------
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
"""

from typing import List, Optional
import heapq


class Solution:
    """
    Solution to LeetCode Problem #218: The Skyline Problem

    Approach: Event-based line sweep with max heap
    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Key Insights:
    - Convert buildings to events (start/end)
    - Use max heap to track active building heights
    - Key point occurs when max height changes
    - Use negative heights for max heap simulation in Python
    """

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events: (x, type, height, end)
        # type: 0 = start (we use negative height for sorting), 1 = end
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # Start event
            events.append((right, height, 0))  # End event (height positive, no end needed)

        # Sort events: by x, then by height (negative for start, positive for end)
        events.sort()

        result = []
        # Max heap: (-height, end_x) - use negative for max heap simulation
        heap = [(0, float('inf'))]  # Ground level that never ends

        for x, neg_height, end in events:
            # Remove buildings that have ended
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_height < 0:  # Start of building
                # Add building to heap
                heapq.heappush(heap, (neg_height, end))

            # Get current max height
            max_height = -heap[0][0]

            # If height changed, add key point
            if not result or result[-1][1] != max_height:
                result.append([x, max_height])

        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 218,
    "name": "The Skyline Problem",
    "difficulty": "Hard",
    "pattern": "Heaps",
    "topics": ["Heap", "Divide and Conquer", "Line Sweep", "Segment Tree"],
    "url": "https://leetcode.com/problems/the-skyline-problem/",
    "companies": ["Google", "Microsoft", "Facebook", "Amazon", "Twitter"],
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
}
