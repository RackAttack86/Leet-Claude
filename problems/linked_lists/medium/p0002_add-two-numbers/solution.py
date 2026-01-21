"""
LeetCode Problem #2: Add Two Numbers
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/add-two-numbers/

Problem:
--------
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
-----------
- The number of nodes in each linked list is in the range `[1, 100]`.
- It is guaranteed that the list represents a number that does not have leading zeros.

Examples:
---------
Example 1:
```

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

```

Example 2:
```

Input: l1 = [0], l2 = [0]
Output: [0]

```

Example 3:
```

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

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
    Solution to LeetCode Problem #2: Add Two Numbers

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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 2,
    "name": "Add Two Numbers",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Math', 'Recursion'],
    "url": "https://leetcode.com/problems/add-two-numbers/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
