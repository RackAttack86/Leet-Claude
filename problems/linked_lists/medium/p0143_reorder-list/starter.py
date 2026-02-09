"""
LeetCode Problem #143: Reorder List
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/reorder-list/

Problem:
--------
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Constraints:
-----------
- The number of nodes in the list is in the range [1, 5 * 10^4]
- 1 <= Node.val <= 1000

Examples:
---------
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #143: Reorder List

    Approach: Find middle, reverse second half, merge
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Find middle using slow/fast pointers
    - Reverse second half of list
    - Merge two halves alternately
    - Three-step approach
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 143,
    "name": "Reorder List",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers', 'Stack', 'Recursion'],
    "url": "https://leetcode.com/problems/reorder-list/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}