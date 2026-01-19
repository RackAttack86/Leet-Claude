"""
LeetCode Problem #347: Top K Frequent Elements
Difficulty: Medium
Pattern: Heaps
Link: https://leetcode.com/problems/top-k-frequent-elements/

Problem:
--------
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Constraints:
-----------
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array]
- It is guaranteed that the answer is unique

Examples:
---------
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
"""

from typing import List, Optional
from collections import Counter
import heapq


class Solution:
    """
    Solution to LeetCode Problem #347: Top K Frequent Elements

    Approach: Hash map + heap or bucket sort
    Time Complexity: O(n log k) for heap, O(n) for bucket sort
    Space Complexity: O(n)

    Key Insights:
    - Count frequencies with hash map
    - Use min heap of size k for top k
    - Bucket sort: group by frequency
    - Heap approach is more general
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        min_heap = []
        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return [num for freq, num in min_heap]
    
    # Alternate solution that does not use a heap. *One Liner*
    # return [key for key, _ in Counter(nums).most_common(k)]


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 347,
    "name": "Top K Frequent Elements",
    "difficulty": "Medium",
    "pattern": "Heaps",
    "topics": ["Array", "Hash Table", "Heap", "Bucket Sort"],
    "url": "https://leetcode.com/problems/top-k-frequent-elements/",
    "companies": ["Amazon", "Facebook", "Google", "Uber"],
    "time_complexity": "O(n log k)",
    "space_complexity": "O(n)",
}
