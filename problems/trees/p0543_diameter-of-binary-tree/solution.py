"""
LeetCode Problem #543: Diameter of Binary Tree
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/diameter-of-binary-tree/

Problem:
--------
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Constraints:
-----------
- The number of nodes in the tree is in the range [1, 10^4]
- -100 <= Node.val <= 100

Examples:
---------
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Input: root = [1,2]
Output: 1
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #543: Diameter of Binary Tree

    Approach: DFS with height calculation
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Key Insights:
    - Diameter at node = left_height + right_height
    - Track maximum diameter globally
    - Return height to parent
    - Path doesn't need to go through root
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 543,
    "name": "Diameter of Binary Tree",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Binary Tree'],
    "url": "https://leetcode.com/problems/diameter-of-binary-tree/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Apple'],
    "time_complexity": "O(n)",
    "space_complexity": "O(h) where h is height",
}
