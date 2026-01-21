"""
LeetCode Problem #378: Kth Smallest Element in a Sorted Matrix
Difficulty: Medium
Pattern: Heaps
Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Problem:
--------
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Constraints:
-----------
- n == matrix.length == matrix[i].length
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order
- 1 <= k <= n^2

Examples:
---------
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Input: matrix = [[-5]], k = 1
Output: -5
"""

from typing import List, Optional
import heapq


class Solution:
    """
    Solution to LeetCode Problem #378: Kth Smallest Element in a Sorted Matrix

    Approach: Min heap or binary search
    Time Complexity: O(k log n) for heap, O(n log(max-min)) for binary search
    Space Complexity: O(n) for heap

    Key Insights:
    - Heap: Start with first element of each row
    - Binary search on value range
    - Count elements <= mid to find position
    - Both approaches have merits
    """

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
    
        # (value, row, col)
        min_heap = [(matrix[0][0], 0, 0)]
        visited = {(0, 0)}
        
        for _ in range(k):
            val, row, col = heapq.heappop(min_heap)
            
            # Add right neighbor
            if col + 1 < n and (row, col + 1) not in visited:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
                visited.add((row, col + 1))
            
            # Add bottom neighbor
            if row + 1 < n and (row + 1, col) not in visited:
                heapq.heappush(min_heap, (matrix[row + 1][col], row + 1, col))
                visited.add((row + 1, col))
        
        return val




# Metadata for tracking
PROBLEM_METADATA = {
    "number": 378,
    "name": "Kth Smallest Element in a Sorted Matrix",
    "difficulty": "Medium",
    "pattern": "Heaps",
    "topics": ['Array', 'Binary Search', 'Sorting', 'Heap (Priority Queue)', 'Matrix'],
    "url": "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(k log n) for heap, O(n log(max-min)) for binary search",
    "space_complexity": "O(n) for heap",
}
