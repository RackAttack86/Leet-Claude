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

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 530,
    "name": "Minimum Absolute Difference in BST",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Breadth-First Search', 'Binary Search Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/minimum-absolute-difference-in-bst/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
