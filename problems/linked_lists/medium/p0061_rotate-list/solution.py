"""
LeetCode Problem #61: Rotate List
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/rotate-list/

Problem:
--------
Given the `head` of a linked list, rotate the list to the right by `k` places.

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

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 61,
    "name": "Rotate List",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers'],
    "url": "https://leetcode.com/problems/rotate-list/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
