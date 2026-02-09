"""
LeetCode Problem #295: Find Median from Data Stream
Difficulty: Hard
Pattern: Heaps
Link: https://leetcode.com/problems/find-median-from-data-stream/

Problem:
--------
The median is the middle value in an ordered integer list. Design a data structure that
supports adding integers and finding the median. Implement the MedianFinder class with
addNum and findMedian methods.

Constraints:
-----------
- -10^5 <= num <= 10^5
- There will be at least one element before calling findMedian
- At most 5 * 10^4 calls will be made to addNum and findMedian

Examples:
---------
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
       [[], [1], [2], [], [3], []]
Output: [null, null, null, 1.5, null, 2.0]
"""

from typing import List, Optional
import heapq


class Solution:
    """
    Solution to LeetCode Problem #295: Find Median from Data Stream

    Approach: Two heaps (max heap for smaller half, min heap for larger half)
    Time Complexity: O(log n) for addNum, O(1) for findMedian
    Space Complexity: O(n)

    Key Insights:
    - Max heap stores smaller half
    - Min heap stores larger half
    - Keep heaps balanced (size diff <= 1)
    - Median is top of heap(s)
    """

    def __init__(self):
        # Max heap for smaller half (use negative values for max heap)
        self.small = []
        # Min heap for larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to max heap (small)
        heapq.heappush(self.small, -num)

        # Ensure max of small <= min of large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance heaps - small can have at most 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 295,
    "name": "Find Median from Data Stream",
    "difficulty": "Hard",
    "pattern": "Heaps",
    "topics": ["Heap", "Design", "Two Pointers", "Data Stream"],
    "url": "https://leetcode.com/problems/find-median-from-data-stream/",
    "companies": ["Google", "Amazon", "Facebook", "Microsoft"],
    "time_complexity": "O(log n) for addNum, O(1) for findMedian",
    "space_complexity": "O(n)",
}
