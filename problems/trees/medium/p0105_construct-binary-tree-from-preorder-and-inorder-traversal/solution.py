"""
LeetCode Problem #105: Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Problem:
--------
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

Constraints:
-----------
- `1
- inorder.length == preorder.length
- 3000
- preorder` and `inorder` consist of unique values.
- Each value of `inorder` also appears in `preorder`.
- preorder` is guaranteed to be the preorder traversal of the tree.
- inorder` is guaranteed to be the inorder traversal of the tree.

Examples:
---------
Example 1:
```

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

```

Example 2:
```

Input: preorder = [-1], inorder = [-1]
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
    Solution to LeetCode Problem #105: Construct Binary Tree from Preorder and Inorder Traversal

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

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 105,
    "name": "Construct Binary Tree from Preorder and Inorder Traversal",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Array', 'Hash Table', 'Divide and Conquer', 'Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
