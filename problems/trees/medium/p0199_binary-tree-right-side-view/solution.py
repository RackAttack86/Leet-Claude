"""
LeetCode Problem #199: Binary Tree Right Side View
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/binary-tree-right-side-view/

Problem:
--------
Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Constraints:
-----------
- The number of nodes in the tree is in the range `[0, 100]`.
- 100

Examples:
---------
Example 1:
Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

Example 2:
Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

Example 3:
Input: root = [1,null,3]

Output: [1,3]

Example 4:
Input: root = []

Output: []
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
    Solution to LeetCode Problem #199: Binary Tree Right Side View

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

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 199,
    "name": "Binary Tree Right Side View",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Breadth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/binary-tree-right-side-view/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
