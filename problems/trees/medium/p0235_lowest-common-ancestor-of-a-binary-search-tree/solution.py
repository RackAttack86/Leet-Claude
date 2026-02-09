"""
LeetCode Problem #235: Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Problem:
--------
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).

Constraints:
-----------
- The number of nodes in the tree is in the range [2, 10^5]
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q
- p and q will exist in the BST

Examples:
---------
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution to LeetCode Problem #235: Lowest Common Ancestor of a Binary Search Tree

    Approach: BST property traversal
    Time Complexity: O(h) where h is height
    Space Complexity: O(1) for iterative, O(h) for recursive

    Key Insights:
    - Use BST property for direction
    - If both < root, go left
    - If both > root, go right
    - Otherwise, root is LCA
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Find lowest common ancestor in a BST using BST properties.

        Since it's a BST, we can use the ordering property:
        - If both p and q are smaller than root, LCA is in left subtree
        - If both p and q are larger than root, LCA is in right subtree
        - Otherwise, root is the LCA (split point or one equals root)

        Using iterative approach for O(1) space complexity.
        """
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                # Both nodes are in left subtree
                current = current.left
            elif p.val > current.val and q.val > current.val:
                # Both nodes are in right subtree
                current = current.right
            else:
                # Split point found - current is the LCA
                # This handles: p < current < q, q < current < p,
                # or one of p/q equals current
                return current

        return None


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 235,
    "name": "Lowest Common Ancestor of a Binary Search Tree",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Binary Search Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(h) where h is height",
    "space_complexity": "O(1) for iterative, O(h) for recursive",
}
