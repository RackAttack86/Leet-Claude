"""
LeetCode Problem #117: Populating Next Right Pointers in Each Node II
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Problem:
--------
Given a binary tree

```

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

Constraints:
-----------
- The number of nodes in the tree is in the range `[0, 6000]`.
- 100

Examples:
---------
Example 1:
```

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

```

Example 2:
```

Input: root = []
Output: []

```
"""

from typing import List, Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """
    Solution to LeetCode Problem #117: Populating Next Right Pointers in Each Node II

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        """
        [TODO: Implement]
        """
        pass

    def connect(self, root: 'Node') -> 'Node':
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 117,
    "name": "Populating Next Right Pointers in Each Node II",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Linked List', 'Tree', 'Depth-First Search', 'Breadth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
