"""
LeetCode Problem #83: Remove Duplicates from Sorted List
Difficulty: Easy
Pattern: Linked Lists
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Problem:
--------
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Constraints:
-----------
- The number of nodes in the list is in the range [0, 300]
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order

Examples:
---------
Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #83: Remove Duplicates from Sorted List

    Approach: Single pointer traversal
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Compare current with next node
    - Skip duplicates by updating next pointer
    - Continue until end of list
    - Simple one-pass solution
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 83,
    "name": "Remove Duplicates from Sorted List",
    "difficulty": "Easy",
    "pattern": "Linked Lists",
    "topics": ['Linked List'],
    "url": "https://leetcode.com/problems/remove-duplicates-from-sorted-list/",
    "companies": ['Amazon', 'Microsoft', 'Facebook'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
