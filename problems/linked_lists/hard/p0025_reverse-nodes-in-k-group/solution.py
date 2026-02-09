"""
LeetCode Problem #25: Reverse Nodes in k-Group
Difficulty: Hard
Pattern: Linked Lists
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

Problem:
--------
Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Constraints:
-----------
- The number of nodes in the list is `n`.

Examples:
---------
Example 1:
```

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

```

Example 2:
```

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

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
    Solution to LeetCode Problem #25: Reverse Nodes in k-Group

    Approach: Iterative Group Reversal
    - Process the list in groups of k nodes
    - For each group: check if there are k nodes, then reverse them
    - Keep track of the previous group's tail to connect reversed groups
    - If fewer than k nodes remain, leave them as is

    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(1) - only using constant extra space

    Key Insights:
    - Need to check if k nodes exist before reversing (don't reverse partial groups)
    - After reversing a group, the first node becomes the last (new tail)
    - Use a dummy node to handle the head changing
    - Track group_prev (end of previous group) to connect groups together
    - The original first node of a group becomes the connection point to next group
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes in k-sized groups.
        """
        if not head or k == 1:
            return head

        # Dummy node to handle head changes
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy  # Points to node before current group

        while True:
            # Check if there are k nodes remaining
            kth = self._getKth(group_prev, k)
            if not kth:
                break  # Less than k nodes remaining, leave as is

            group_next = kth.next  # Node after current group

            # Reverse the group
            # prev, curr will reverse k nodes starting from group_prev.next
            prev = group_next  # After reversal, last node points to next group
            curr = group_prev.next

            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Connect the reversed group to the rest of the list
            # After reversal:
            # - prev points to new first node of group (was kth)
            # - group_prev.next still points to old first node (now last in group)
            tmp = group_prev.next  # Old first node (now last in reversed group)
            group_prev.next = kth  # Connect to new first node
            group_prev = tmp  # Move to end of current group for next iteration

        return dummy.next

    def _getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        """
        Get the kth node from curr (exclusive of curr).
        Returns None if there are fewer than k nodes.
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 25,
    "name": "Reverse Nodes in k-Group",
    "difficulty": "Hard",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Recursion'],
    "url": "https://leetcode.com/problems/reverse-nodes-in-k-group/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple", "Bloomberg", "Adobe", "ByteDance"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
