"""
LeetCode Problem #92: Reverse Linked List II
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/reverse-linked-list-ii/

Problem:
--------
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Constraints:
-----------
- The number of nodes in the list is n
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

Examples:
---------
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #92: Reverse Linked List II

    Approach: Iterative reversal with markers
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Find node before left position
    - Reverse nodes between left and right
    - Reconnect reversed portion
    - Use dummy node for edge cases
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 92,
    "name": "Reverse Linked List II",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List'],
    "url": "https://leetcode.com/problems/reverse-linked-list-ii/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
