"""
LeetCode Problem #110: Balanced Binary Tree
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/balanced-binary-tree/

Problem:
--------
Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Constraints:
-----------
- The number of nodes in the tree is in the range [0, 5000]
- -10^4 <= Node.val <= 10^4

Examples:
---------
Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #110: Balanced Binary Tree

    Approach: Recursive DFS with height calculation
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Key Insights:
    - Calculate height while checking balance
    - Return -1 if unbalanced for early exit
    - Check |left_height - right_height| <= 1
    - Bottom-up approach more efficient
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 110,
    "name": "Balanced Binary Tree",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/balanced-binary-tree/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(h) where h is height",
}
