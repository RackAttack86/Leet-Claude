"""
LeetCode Problem #82: Remove Duplicates from Sorted List II
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Problem:
--------
Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Constraints:
-----------
- The number of nodes in the list is in the range `[0, 300]`.
- 100
- The list is guaranteed to be sorted in ascending order.

Examples:
---------
Example 1:
```

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

```

Example 2:
```

Input: head = [1,1,1,2,3]
Output: [2,3]

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
    Solution to LeetCode Problem #82: Remove Duplicates from Sorted List II

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def __init__(self, val=0: Any, next=None: Any):
        """
        [TODO: Implement]
        """
        pass

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 82,
    "name": "Remove Duplicates from Sorted List II",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers'],
    "url": "https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
