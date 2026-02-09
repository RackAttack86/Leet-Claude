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
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



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