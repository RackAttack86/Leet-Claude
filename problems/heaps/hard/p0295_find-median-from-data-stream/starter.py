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
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



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