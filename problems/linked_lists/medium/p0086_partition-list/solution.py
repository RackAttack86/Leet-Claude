"""
LeetCode Problem #86: Partition List
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/partition-list/

Problem:
--------
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Constraints:
-----------
- The number of nodes in the list is in the range [0, 200]
- -100 <= Node.val <= 100
- -200 <= x <= 200

Examples:
---------
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input: head = [2,1], x = 2
Output: [1,2]
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution to LeetCode Problem #86: Partition List

    Approach: Two dummy lists
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Create two separate lists: less and greater
    - Traverse and append to appropriate list
    - Connect less list to greater list
    - Use dummy nodes for simplicity
    """

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Partition list so all nodes less than x come before nodes >= x.

        Creates two separate lists (less and greater), then connects them.
        Preserves original relative order within each partition.
        """
        # Create dummy heads for two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        # Traverse and partition nodes
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        # Connect the two partitions
        greater.next = None  # Important: terminate greater list
        less.next = greater_dummy.next

        return less_dummy.next


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 86,
    "name": "Partition List",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers'],
    "url": "https://leetcode.com/problems/partition-list/",
    "companies": ['Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
