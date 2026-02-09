"""
LeetCode Problem #102: Binary Tree Level Order Traversal
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem:
--------
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Constraints:
-----------
- The number of nodes in the tree is in the range [0, 2000]
- -1000 <= Node.val <= 1000

Examples:
---------
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution to LeetCode Problem #102: Binary Tree Level Order Traversal

    Approach: BFS with queue
    Time Complexity: O(n)
    Space Complexity: O(n)

    Key Insights:
    - Use queue for BFS
    - Process level by level
    - Track level size before processing
    - Classic BFS pattern
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return level order traversal of binary tree using BFS.

        Use a queue to process nodes level by level. For each level,
        we know how many nodes to process (current queue size) before
        moving to the next level.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)

        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 102,
    "name": "Binary Tree Level Order Traversal",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ["Tree", "Breadth-First Search", "Binary Tree"],
    "url": "https://leetcode.com/problems/binary-tree-level-order-traversal/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Google", "LinkedIn", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}
