"""
LeetCode Problem #297: Serialize and Deserialize Binary Tree
Difficulty: Hard
Pattern: Trees
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Problem:
--------
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Constraints:
-----------
- The number of nodes in the tree is in the range [0, 10^4]
- -1000 <= Node.val <= 1000

Examples:
---------
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

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


class Codec:
    """
    Solution to LeetCode Problem #297: Serialize and Deserialize Binary Tree

    Approach: BFS or DFS with delimiter
    Time Complexity: O(n) for both serialize and deserialize
    Space Complexity: O(n)

    Key Insights:
    - Use preorder DFS or level-order BFS
    - Encode null nodes explicitly
    - Use delimiter to separate values
    - Deserialize using queue or recursion
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            if i < len(values) and values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root


class Solution:
    """Wrapper for LeetCode compatibility."""
    pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 297,
    "name": "Serialize and Deserialize Binary Tree",
    "difficulty": "Hard",
    "pattern": "Trees",
    "topics": ['String', 'Tree', 'Depth-First Search', 'Breadth-First Search', 'Design', 'Binary Tree'],
    "url": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Bloomberg'],
    "time_complexity": "O(n) for both serialize and deserialize",
    "space_complexity": "O(n)",
}
