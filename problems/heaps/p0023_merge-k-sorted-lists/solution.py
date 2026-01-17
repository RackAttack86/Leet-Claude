"""
LeetCode Problem #23: Merge k Sorted Lists
Difficulty: Hard
Pattern: Heaps
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Problem:
--------
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Constraints:
-----------
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order
- The sum of lists[i].length will not exceed 10^4

Examples:
---------
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Input: lists = []
Output: []
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #23: Merge k Sorted Lists

    Approach: Min heap with k pointers
    Time Complexity: O(N log k) where N is total nodes
    Space Complexity: O(k) for heap

    Key Insights:
    - Use min heap to track smallest elements
    - Add head of each list to heap
    - Pop min, add next node from that list
    - More efficient than merging pairs
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 23,
    "name": "Merge k Sorted Lists",
    "difficulty": "Hard",
    "pattern": "Heaps",
    "topics": ['Linked List', 'Divide and Conquer', 'Heap (Priority Queue)', 'Merge Sort'],
    "url": "https://leetcode.com/problems/merge-k-sorted-lists/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Apple'],
    "time_complexity": "O(N log k) where N is total nodes",
    "space_complexity": "O(k) for heap",
}
