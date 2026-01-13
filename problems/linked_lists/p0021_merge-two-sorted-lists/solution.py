"""
LeetCode Problem #21: Merge Two Sorted Lists
Difficulty: Easy
Pattern: Linked Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Problem:
--------
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes
of the first two lists.
Return the head of the merged linked list.

Constraints:
-----------
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

Examples:
---------
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #21: Merge Two Sorted Lists

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 21,
    "name": "Merge Two Sorted Lists",
    "difficulty": "Easy",
    "pattern": "Linked Lists",
    "topics": ["Linked List", "Recursion"],
    "url": "https://leetcode.com/problems/merge-two-sorted-lists/",
    "companies": ["Amazon", "Microsoft", "Apple", "Facebook", "Google", "Adobe"],
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
}
