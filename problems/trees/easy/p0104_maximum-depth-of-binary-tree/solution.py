"""
LeetCode Problem #104: Maximum Depth of Binary Tree
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem:
--------
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Constraints:
-----------
- The number of nodes in the tree is in the range [0, 10^4]
- -100 <= Node.val <= 100

Examples:
---------
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #104: Maximum Depth of Binary Tree

    Approach: Recursive DFS
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Key Insights:
    - Base case: null node has depth 0
    - Depth = 1 + max(left_depth, right_depth)
    - Simple recursive solution
    - Can also use BFS
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 104,
    "name": "Maximum Depth of Binary Tree",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ["Tree", "Depth-First Search", "Breadth-First Search", "Binary Tree"],
    "url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Apple", "LinkedIn"],
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
}
