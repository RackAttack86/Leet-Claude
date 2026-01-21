"""
LeetCode Problem #230: Kth Smallest Element in a BST
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Problem:
--------
Given the `root` of a binary search tree, and an integer `k`, return the `k^th` smallest value (1-indexed) of all the values of the nodes in the tree.

Constraints:
-----------
- The number of nodes in the tree is `n`.

Examples:
---------
Example 1:
```

Input: root = [3,1,4,null,2], k = 1
Output: 1

```

Example 2:
```

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

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
    Solution to LeetCode Problem #230: Kth Smallest Element in a BST

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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 230,
    "name": "Kth Smallest Element in a BST",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Binary Search Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
