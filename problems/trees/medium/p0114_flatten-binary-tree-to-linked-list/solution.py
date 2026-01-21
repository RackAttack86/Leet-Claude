"""
LeetCode Problem #114: Flatten Binary Tree to Linked List
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Problem:
--------
Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
	
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Constraints:
-----------
- The number of nodes in the tree is in the range `[0, 2000]`.
- 100

Examples:
---------
Example 1:
```

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

```

Example 2:
```

Input: root = []
Output: []

```

Example 3:
```

Input: root = [0]
Output: [0]

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
    Solution to LeetCode Problem #114: Flatten Binary Tree to Linked List

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

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 114,
    "name": "Flatten Binary Tree to Linked List",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Linked List', 'Stack', 'Tree', 'Depth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/flatten-binary-tree-to-linked-list/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
