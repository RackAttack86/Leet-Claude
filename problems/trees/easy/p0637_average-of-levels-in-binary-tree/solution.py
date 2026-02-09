"""
LeetCode Problem #637: Average of Levels in Binary Tree
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

Problem:
--------
Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within `10^-5` of the actual answer will be accepted.

Constraints:
-----------
- The number of nodes in the tree is in the range `[1, 10^4]`.
- 2^31

Examples:
---------
Example 1:
```

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

```

Example 2:
```

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

```
"""

from typing import List, Optional
from collections import deque

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
    Solution to LeetCode Problem #637: Average of Levels in Binary Tree

    Approach: Level-order traversal (BFS) with level sums
    - Use a queue to process nodes level by level.
    - For each level, sum all node values and count nodes.
    - Calculate average as sum / count for each level.
    - Add children to queue for next level processing.

    Time Complexity: O(n) - visit each node exactly once
    Space Complexity: O(w) - queue holds at most one level, w is max width

    Key Insights:
    - BFS naturally processes nodes level by level
    - Process all nodes at current level before moving to next
    - Use queue length at start of each iteration to know level size
    - Be careful with integer overflow for large node values (use float division)
    """

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Calculate the average value of nodes at each level.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate average for this level
            result.append(level_sum / level_size)

        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 637,
    "name": "Average of Levels in Binary Tree",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Breadth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/average-of-levels-in-binary-tree/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(w)",
}
