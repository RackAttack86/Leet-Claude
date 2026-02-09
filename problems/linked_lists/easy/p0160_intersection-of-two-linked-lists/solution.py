"""
LeetCode Problem #160: Intersection of Two Linked Lists
Difficulty: Easy
Pattern: Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

Problem:
--------
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Constraints:
-----------
- The number of nodes of listA is in the m
- The number of nodes of listB is in the n
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5
- 0 <= skipA < m
- 0 <= skipB < n

Examples:
---------
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Solution to LeetCode Problem #160: Intersection of Two Linked Lists

    Approach: Two pointers with length alignment
    Time Complexity: O(m + n)
    Space Complexity: O(1)

    Key Insights:
    - Two pointers traverse both lists
    - When reaching end, switch to other list
    - They will meet at intersection or null
    - Clever pointer switching eliminates length difference
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 160,
    "name": "Intersection of Two Linked Lists",
    "difficulty": "Easy",
    "pattern": "Linked Lists",
    "topics": ['Hash Table', 'Linked List', 'Two Pointers'],
    "url": "https://leetcode.com/problems/intersection-of-two-linked-lists/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(m + n)",
    "space_complexity": "O(1)",
}
