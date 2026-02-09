"""
LeetCode Problem #101: Symmetric Tree
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/symmetric-tree/

Problem:
--------
Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Constraints:
-----------
- The number of nodes in the tree is in the range `[1, 1000]`.
- 100

Examples:
---------
Example 1:
```

Input: root = [1,2,2,3,4,4,3]
Output: true

```

Example 2:
```

Input: root = [1,2,2,null,3,null,3]
Output: false

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
    Solution to LeetCode Problem #101: Symmetric Tree

    Approach: Recursive comparison of mirror nodes
    - A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
    - Two trees are mirrors if:
      1. Their root values are equal
      2. Left subtree of one is a mirror of right subtree of the other
    - Use a helper function to compare two nodes at mirror positions.

    Time Complexity: O(n) - visit each node once
    Space Complexity: O(h) - recursion stack, where h is tree height (O(n) worst case for skewed tree)

    Key Insights:
    - Compare left.left with right.right AND left.right with right.left (mirror comparison)
    - Both nodes being None is symmetric (base case returns True)
    - One None and one non-None is not symmetric
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is symmetric (mirror of itself).
        """
        if not root:
            return True
        return self._isMirror(root.left, root.right)

    def _isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """Helper function to check if two subtrees are mirrors of each other."""
        # Both None - symmetric
        if not left and not right:
            return True
        # One None, one not - not symmetric
        if not left or not right:
            return False
        # Both exist - check values and recursively check mirror children
        return (left.val == right.val and
                self._isMirror(left.left, right.right) and
                self._isMirror(left.right, right.left))


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 101,
    "name": "Symmetric Tree",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Breadth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/symmetric-tree/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Bloomberg", "LinkedIn", "Apple", "Google"],
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
}
