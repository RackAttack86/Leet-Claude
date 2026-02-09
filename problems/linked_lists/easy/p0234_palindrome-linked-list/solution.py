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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find middle using slow/fast pointers
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second_half = slow.next
        prev = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node

        # Compare first and reversed second half
        first_half = head
        second_half = prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True


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
