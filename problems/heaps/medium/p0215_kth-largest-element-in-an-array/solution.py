"""
LeetCode Problem #215: Kth Largest Element in an Array
Difficulty: Medium
Pattern: Heaps
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem:
--------
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Constraints:
-----------
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Examples:
---------
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

from typing import List, Optional
import heapq


class Solution:
    """
    Solution to LeetCode Problem #215: Kth Largest Element in an Array

    Approach: Min heap of size k or Quickselect
    Time Complexity: O(n log k) for heap, O(n) average for quickselect
    Space Complexity: O(k) for heap, O(1) for quickselect

    Key Insights:
    - Maintain min heap of k largest elements
    - Heap top is kth largest
    - Quickselect is faster but harder to implement
    - Can also sort in O(n log n)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num < heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 215,
    "name": "Kth Largest Element in an Array",
    "difficulty": "Medium",
    "pattern": "Heaps",
    "topics": ["Array", "Heap", "Quickselect", "Divide and Conquer"],
    "url": "https://leetcode.com/problems/kth-largest-element-in-an-array/",
    "companies": ["Facebook", "Amazon", "Microsoft", "Apple"],
    "time_complexity": "O(n log k)",
    "space_complexity": "O(k)",
}
