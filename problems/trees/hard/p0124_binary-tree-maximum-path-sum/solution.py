"""
LeetCode Problem #124: Binary Tree Maximum Path Sum
Difficulty: Hard
Pattern: Trees
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Problem:
--------
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

Constraints:
-----------
- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- 1000

Examples:
---------
Example 1:
```

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

```

Example 2:
```

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

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
    Solution to LeetCode Problem #124: Binary Tree Maximum Path Sum

    Approach: DFS with Global Maximum Tracking
    - At each node, compute max path sum that can be extended to parent
    - Also compute max path sum that goes through current node (left + node + right)
    - Track global maximum across all possible paths
    - Return to parent only the best single-direction path (can't split at parent)

    Time Complexity: O(n) - visit each node once
    Space Complexity: O(h) - recursion stack where h is tree height

    Key Insights:
    - Path can start/end anywhere - doesn't need to pass through root
    - At each node, we have two choices:
      1. Path going through node (left path + node + right path) - update global max
      2. Path extending to parent (node + max(left, right)) - return to parent
    - Negative paths should be treated as 0 (don't include them)
    - A node itself can be a valid path (important for all-negative trees)
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node: TreeNode) -> int:
            """
            Returns maximum path sum starting from this node going down (one direction).
            Also updates global max_sum if path through this node is better.
            """
            if not node:
                return 0

            # Get maximum gain from left and right subtrees
            # Use max with 0 to ignore negative paths
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Path sum going through current node (potential global max)
            path_through_node = node.val + left_gain + right_gain

            # Update global maximum if this path is better
            self.max_sum = max(self.max_sum, path_through_node)

            # Return max gain if we extend path to parent
            # Can only go one direction (either left or right, not both)
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 124,
    "name": "Binary Tree Maximum Path Sum",
    "difficulty": "Hard",
    "pattern": "Trees",
    "topics": ['Dynamic Programming', 'Tree', 'Depth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/binary-tree-maximum-path-sum/",
    "companies": ["Facebook", "Amazon", "Microsoft", "Google", "Bloomberg", "Apple", "DoorDash", "ByteDance", "Uber"],
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
}
