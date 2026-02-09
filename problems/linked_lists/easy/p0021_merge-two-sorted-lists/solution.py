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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution to LeetCode Problem #21: Merge Two Sorted Lists

    Approach: Two pointers merge
    Time Complexity: O(m + n)
    Space Complexity: O(1)

    Key Insights:
    - Use dummy node to simplify
    - Compare values and link smaller node
    - Handle remaining nodes in either list
    - Classic merge pattern
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next


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
