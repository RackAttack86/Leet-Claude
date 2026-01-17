"""
LeetCode Problem #234: Palindrome Linked List
Difficulty: Easy
Pattern: Linked Lists
Link: https://leetcode.com/problems/palindrome-linked-list/

Problem:
--------
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Constraints:
-----------
- The number of nodes in the list is in the range [1, 10^5]
- 0 <= Node.val <= 9

Examples:
---------
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #234: Palindrome Linked List

    Approach: Find middle, reverse second half, compare
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Find middle using slow/fast pointers
    - Reverse second half
    - Compare first and second halves
    - Can restore list after checking
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 234,
    "name": "Palindrome Linked List",
    "difficulty": "Easy",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers', 'Stack', 'Recursion'],
    "url": "https://leetcode.com/problems/palindrome-linked-list/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Apple'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
