"""
LeetCode Problem #103: Binary Tree Zigzag Level Order Traversal
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Problem:
--------
Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Constraints:
-----------
- The number of nodes in the tree is in the range `[0, 2000]`.
- 100

Examples:
---------
Example 1:
```

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

```

Example 2:
```

Input: root = [1]
Output: [[1]]

```

Example 3:
```

Input: root = []
Output: []

```
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """
    Solution to LeetCode Problem #103: Binary Tree Zigzag Level Order Traversal

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def __init__(self, val=0: Any, left=None: Any, right=None: Any):
        """
        [TODO: Implement]
        """
        pass

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 103,
    "name": "Binary Tree Zigzag Level Order Traversal",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Tree', 'Breadth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
