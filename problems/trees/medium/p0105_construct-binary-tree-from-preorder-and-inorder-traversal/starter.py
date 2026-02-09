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
        pass

class Node:
    def __init__(self, val=0, neighbors=None):
        pass

class Solution:
    """
    Solution to LeetCode Problem #105: Construct Binary Tree from Preorder and Inorder Traversal

    Approach: Divide and Conquer with Hash Map
    - Preorder: [root, left subtree, right subtree]
    - Inorder: [left subtree, root, right subtree]
    - First element of preorder is always the root
    - Find root position in inorder to determine left/right subtree sizes
    - Use hash map for O(1) lookup of root position in inorder

    Time Complexity: O(n) - visit each node once, O(1) lookup with hash map
    Space Complexity: O(n) - hash map and recursion stack (O(h) where h is height)

    Key Insights:
    - Preorder's first element is the root
    - Inorder splits into left subtree, root, right subtree
    - Number of elements to the left of root in inorder = left subtree size
    - Use this size to partition preorder into left/right subtrees
    - Hash map avoids O(n) search for root in inorder each time
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass



PROBLEM_METADATA = {
    "number": 105,
    "name": "Construct Binary Tree from Preorder and Inorder Traversal",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Array', 'Hash Table', 'Divide and Conquer', 'Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Bloomberg", "Apple", "ByteDance", "Uber"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}