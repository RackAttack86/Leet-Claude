"""
LeetCode Problem #19: Remove Nth Node From End of List
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Problem:
--------
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:
-----------
- The number of nodes in the list is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Examples:
---------
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #19: Remove Nth Node From End of List

    Approach: Two pointers with gap of n
    Time Complexity: O(L) where L is list length
    Space Complexity: O(1)

    Key Insights:
    - Use two pointers n steps apart
    - Move both until fast reaches end
    - Slow pointer will be at node before target
    - Use dummy node to handle edge cases
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 19,
    "name": "Remove Nth Node From End of List",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers'],
    "url": "https://leetcode.com/problems/remove-nth-node-from-end-of-list/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Apple'],
    "time_complexity": "O(L) where L is list length",
    "space_complexity": "O(1)",
}
