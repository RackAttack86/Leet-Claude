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

    Approach: Morris Traversal-like O(1) space approach
    - For each node, if it has a left child:
      1. Find the rightmost node in the left subtree (predecessor in preorder)
      2. Connect that rightmost node's right to current node's right child
      3. Move left subtree to right, set left to None
    - Move to the right child and repeat

    Time Complexity: O(n) - each node visited at most twice
    Space Complexity: O(1) - no recursion stack, constant extra space

    Key Insights:
    - Pre-order: root -> left -> right
    - To flatten: left subtree should come before right subtree
    - Find rightmost of left subtree and link it to right subtree
    - This avoids recursion stack overhead
    - Alternative: reverse postorder (right, left, root) with prev pointer
    """

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root

        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right

                # Connect rightmost to current's right subtree
                rightmost.right = current.right

                # Move left subtree to right
                current.right = current.left
                current.left = None

            # Move to the next node (which is now on the right)
            current = current.right


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 114,
    "name": "Flatten Binary Tree to Linked List",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Linked List', 'Stack', 'Tree', 'Depth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/flatten-binary-tree-to-linked-list/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg", "Apple", "Adobe", "ByteDance"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
