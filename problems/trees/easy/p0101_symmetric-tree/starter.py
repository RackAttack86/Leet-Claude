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
        pass

class Node:
    def __init__(self, val=0, neighbors=None):
        pass

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
        pass

    def _isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """Helper function to check if two subtrees are mirrors of each other."""
        pass



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