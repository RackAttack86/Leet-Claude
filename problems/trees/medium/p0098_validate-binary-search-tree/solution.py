"""
LeetCode Problem #98: Validate Binary Search Tree
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/validate-binary-search-tree/

Problem:
--------
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Constraints:
-----------
- The number of nodes in the tree is in the range [1, 10^4]
- -2^31 <= Node.val <= 2^31 - 1

Examples:
---------
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution to LeetCode Problem #98: Validate Binary Search Tree

    Approach: Recursive with range validation or Inorder traversal
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Key Insights:
    - Pass valid range (min, max) down recursion
    - Left subtree must be in (min, root.val)
    - Right subtree must be in (root.val, max)
    - Inorder traversal of BST is sorted
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validate if a binary tree is a valid BST using range validation.

        For each node, we track the valid range (min_val, max_val) that its value
        must fall within. Left children must be less than parent, right children
        must be greater than parent.
        """
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True

            # Check if current node's value is within valid range
            if node.val <= min_val or node.val >= max_val:
                return False

            # Left subtree: values must be less than current node
            # Right subtree: values must be greater than current node
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root, float('-inf'), float('inf'))


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 98,
    "name": "Validate Binary Search Tree",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ["Tree", "Depth-First Search", "Binary Search Tree", "Binary Tree"],
    "url": "https://leetcode.com/problems/validate-binary-search-tree/",
    "companies": ["Amazon", "Microsoft", "Facebook", "Google", "Bloomberg", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
}
