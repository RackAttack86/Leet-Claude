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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the list.

        Uses two pointers with a gap of n nodes between them.
        When fast pointer reaches the end, slow pointer is at the node before the target.
        """
        # Create dummy node to handle edge case of removing head
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from end
        slow.next = slow.next.next

        return dummy.next


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
