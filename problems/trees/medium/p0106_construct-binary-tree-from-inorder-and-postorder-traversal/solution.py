"""
LeetCode Problem #106: Construct Binary Tree from Inorder and Postorder Traversal
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Problem:
--------
Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

Constraints:
-----------
- `1
- postorder.length == inorder.length
- 3000
- inorder` and `postorder` consist of unique values.
- Each value of `postorder` also appears in `inorder`.
- inorder` is guaranteed to be the inorder traversal of the tree.
- postorder` is guaranteed to be the postorder traversal of the tree.

Examples:
---------
Example 1:
```

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

```

Example 2:
```

Input: inorder = [-1], postorder = [-1]
Output: [-1]

```
"""

from typing import List, Optional
from collections import Counter, defaultdict

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
    Solution to LeetCode Problem #106: Construct Binary Tree from Inorder and Postorder Traversal

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

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 106,
    "name": "Construct Binary Tree from Inorder and Postorder Traversal",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Array', 'Hash Table', 'Divide and Conquer', 'Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
