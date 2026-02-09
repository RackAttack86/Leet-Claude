"""
LeetCode Problem #61: Rotate List
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/rotate-list/

Problem:
--------
Given the `head` of a linked list, rotate the list to the right by `k` places.

Constraints:
-----------
- The number of nodes in the list is in the range `[0, 500]`.
- 100

Examples:
---------
Example 1:
```

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

```

Example 2:
```

Input: head = [0,1,2], k = 4
Output: [2,0,1]

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
    Solution to LeetCode Problem #61: Rotate List

    Approach: Close the Circle and Break at New Head
    - First, compute the length of the list and connect tail to head (making it circular)
    - Calculate effective rotation: k % length (to handle k > length)
    - Find the new tail position: (length - k % length) steps from the original head
    - Break the circle at this point to get the rotated list

    Time Complexity: O(n) where n is the length of the list
    Space Complexity: O(1) - only using constant extra space

    Key Insights:
    - Rotating right by k is equivalent to moving the last k nodes to the front
    - k can be larger than list length, so we use k % length
    - Making the list circular simplifies the rotation logic
    - The new head is at position (length - k % length) from original head
    """

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate the list to the right by k places.
        """
        # Handle edge cases
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length and the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Calculate effective rotation
        k = k % length
        if k == 0:
            return head  # No rotation needed

        # Step 3: Connect tail to head (make it circular)
        tail.next = head

        # Step 4: Find the new tail (length - k steps from head)
        # The new head will be right after the new tail
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # Step 5: Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 61,
    "name": "Rotate List",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers'],
    "url": "https://leetcode.com/problems/rotate-list/",
    "companies": ["Amazon", "Microsoft", "LinkedIn", "Facebook", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
