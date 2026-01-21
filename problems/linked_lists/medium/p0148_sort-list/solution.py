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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 148,
    "name": "Sort List",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers', 'Divide and Conquer', 'Sorting', 'Merge Sort'],
    "url": "https://leetcode.com/problems/sort-list/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
