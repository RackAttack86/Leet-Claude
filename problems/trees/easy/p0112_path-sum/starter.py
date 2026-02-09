"""
LeetCode Problem #112: Path Sum
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/path-sum/

Problem:
--------
Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

A leaf is a node with no children.

Constraints:
-----------
- The number of nodes in the tree is in the range `[0, 5000]`.
- 1000
- 1000

Examples:
---------
Example 1:
```

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

```

Example 2:
```

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

```

Example 3:
```

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

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
    Solution to LeetCode Problem #112: Path Sum

    Approach: Recursive DFS with running sum subtraction
    - Subtract current node's value from targetSum as we traverse.
    - At a leaf node, check if remaining targetSum equals the leaf's value.
    - Recursively check both left and right subtrees.
    - Return True if any path from root to leaf sums to targetSum.

    Time Complexity: O(n) - visit each node once in worst case
    Space Complexity: O(h) - recursion stack, where h is tree height

    Key Insights:
    - Subtract node value from targetSum instead of accumulating sum (cleaner)
    - A leaf is defined as a node with NO children (both left and right are None)
    - Empty tree returns False (no paths exist)
    - Only check sum at leaf nodes, not internal nodes
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Check if there exists a root-to-leaf path with the given sum.
        """
        pass



PROBLEM_METADATA = {
    "number": 112,
    "name": "Path Sum",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Breadth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/path-sum/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Apple", "Bloomberg", "Oracle"],
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
}