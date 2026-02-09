"""
LeetCode Problem #141: Linked List Cycle
Difficulty: Easy
Pattern: Linked Lists
Link: https://leetcode.com/problems/linked-list-cycle/

Problem:
--------
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:
-----------
- The number of the nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list

Examples:
---------
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution to LeetCode Problem #141: Linked List Cycle

    Approach: Floyd's Cycle Detection (fast and slow pointers)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Use fast and slow pointers
    - Fast moves 2 steps, slow moves 1 step
    - If cycle exists, they will meet
    - Classic tortoise and hare algorithm
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 141,
    "name": "Linked List Cycle",
    "difficulty": "Easy",
    "pattern": "Linked Lists",
    "topics": ["Hash Table", "Linked List", "Two Pointers"],
    "url": "https://leetcode.com/problems/linked-list-cycle/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Apple", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
