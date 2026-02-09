"""
LeetCode Problem #148: Sort List
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/sort-list/

Problem:
--------
Given the `head` of a linked list, return the list after sorting it in ascending order.

Constraints:
-----------
- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- 10^5

Examples:
---------
Example 1:
```

Input: head = [4,2,1,3]
Output: [1,2,3,4]

```

Example 2:
```

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

```

Example 3:
```

Input: head = []
Output: []

```
"""

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """
    Solution to LeetCode Problem #148: Sort List

    Approach: Merge Sort (Top-Down or Bottom-Up)
    - Use merge sort which is optimal for linked lists
    - Top-down: Recursively split list in half, sort each half, merge
    - Bottom-up: Iteratively merge sublists of increasing sizes (O(1) space)

    Top-Down Implementation (shown here):
    - Find middle using slow/fast pointers
    - Recursively sort left and right halves
    - Merge the sorted halves

    Time Complexity: O(n log n) - merge sort
    Space Complexity: O(log n) for recursion stack (O(1) for bottom-up approach)

    Key Insights:
    - Merge sort is ideal for linked lists (no random access needed, no shifting elements)
    - Quick sort is less efficient for linked lists due to lack of random access
    - Finding middle with slow/fast pointers is a classic linked list technique
    - When splitting, we must break the list by setting mid.next = None
    """

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort the linked list in ascending order using merge sort.
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head

        # Split the list into two halves
        mid = self._getMid(head)
        left = head
        right = mid.next
        mid.next = None  # Break the list

        # Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge the sorted halves
        return self._merge(left, right)

    def _getMid(self, head: ListNode) -> ListNode:
        """
        Find the middle node using slow/fast pointer technique.
        For even length, returns the first of the two middle nodes.
        """
        slow = head
        fast = head.next  # Start fast one ahead to get left middle for even length

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left: ListNode, right: ListNode) -> ListNode:
        """
        Merge two sorted linked lists into one sorted list.
        """
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Attach remaining nodes
        current.next = left if left else right

        return dummy.next


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 148,
    "name": "Sort List",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers', 'Divide and Conquer', 'Sorting', 'Merge Sort'],
    "url": "https://leetcode.com/problems/sort-list/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Adobe", "Bloomberg"],
    "time_complexity": "O(n log n)",
    "space_complexity": "O(log n)",
}
