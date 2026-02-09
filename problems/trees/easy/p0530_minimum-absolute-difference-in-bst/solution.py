"""
LeetCode Problem #530: Minimum Absolute Difference in BST
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Problem:
--------
Given the `root` of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Constraints:
-----------
- The number of nodes in the tree is in the range `[2, 10^4]`.

Examples:
---------
Example 1:
```

Input: root = [4,2,6,1,3]
Output: 1

```

Example 2:
```

Input: root = [1,0,48,null,null,12,49]
Output: 1

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
    Solution to LeetCode Problem #530: Minimum Absolute Difference in BST

    Approach: In-order traversal to get sorted sequence
    - BST in-order traversal produces nodes in sorted (ascending) order.
    - Minimum difference must be between adjacent nodes in sorted order.
    - Track previous node value and update minimum difference during traversal.
    - Use instance variables to maintain state across recursive calls.

    Time Complexity: O(n) - visit each node exactly once
    Space Complexity: O(h) - recursion stack, where h is tree height

    Key Insights:
    - In a BST, in-order traversal gives sorted values
    - Minimum absolute difference is always between consecutive sorted values
    - No need to store all values; just track previous value during traversal
    - This is equivalent to problem #783 (Minimum Distance Between BST Nodes)
    """

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Find the minimum absolute difference between any two nodes in BST.
        """
        self.min_diff = float('inf')
        self.prev = None

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return

            # Visit left subtree
            inorder(node.left)

            # Process current node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            # Visit right subtree
            inorder(node.right)

        inorder(root)
        return self.min_diff


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 530,
    "name": "Minimum Absolute Difference in BST",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Breadth-First Search', 'Binary Search Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/minimum-absolute-difference-in-bst/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Bloomberg", "Oracle"],
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
}
