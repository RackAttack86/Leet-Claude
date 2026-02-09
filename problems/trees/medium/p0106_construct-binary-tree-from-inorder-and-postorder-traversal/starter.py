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
        pass

class Node:
    def __init__(self, val=0, neighbors=None):
        pass

class Solution:
    """
    Solution to LeetCode Problem #106: Construct Binary Tree from Inorder and Postorder Traversal

    Approach: Divide and Conquer with Hash Map
    - Postorder: [left subtree, right subtree, root]
    - Inorder: [left subtree, root, right subtree]
    - Last element of postorder is always the root
    - Find root position in inorder to determine left/right subtree sizes
    - Use hash map for O(1) lookup of root position in inorder

    Time Complexity: O(n) - visit each node once, O(1) lookup with hash map
    Space Complexity: O(n) - hash map and recursion stack (O(h) where h is height)

    Key Insights:
    - Postorder's last element is the root (unlike preorder where first is root)
    - Build right subtree before left subtree when processing postorder from end
    - Inorder splits into left subtree, root, right subtree
    - Number of elements to the left of root in inorder = left subtree size
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pass



PROBLEM_METADATA = {
    "number": 106,
    "name": "Construct Binary Tree from Inorder and Postorder Traversal",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Array', 'Hash Table', 'Divide and Conquer', 'Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Bloomberg", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}