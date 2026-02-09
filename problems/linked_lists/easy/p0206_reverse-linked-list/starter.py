"""
LeetCode Problem #206: Reverse Linked List
Difficulty: Easy
Pattern: Linked Lists
Link: https://leetcode.com/problems/reverse-linked-list/

Problem:
--------
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
-----------
- The number of nodes in the list is the range [0, 5000]
- -5000 <= Node.val <= 5000

Examples:
---------
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #206: Reverse Linked List

    Approach: Iterative with three pointers
    Time Complexity: O(n)
    Space Complexity: O(1) for iterative, O(n) for recursive

    Key Insights:
    - Use prev, curr, next pointers
    - Reverse links one by one
    - Can also solve recursively
    - Classic linked list problem
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 206,
    "name": "Reverse Linked List",
    "difficulty": "Easy",
    "pattern": "Linked Lists",
    "topics": ["Linked List", "Recursion"],
    "url": "https://leetcode.com/problems/reverse-linked-list/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Apple", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}