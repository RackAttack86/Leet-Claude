"""
LeetCode Problem #226: Invert Binary Tree
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/invert-binary-tree/

Problem:
--------
Given the root of a binary tree, invert the tree, and return its root.

Constraints:
-----------
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

Examples:
---------
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #226: Invert Binary Tree

    Approach: Recursive DFS
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Key Insights:
    - Swap left and right children recursively
    - Base case: null node returns null
    - Simple recursive pattern
    - Can also use BFS
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 226,
    "name": "Invert Binary Tree",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ["Tree", "Depth-First Search", "Breadth-First Search", "Binary Tree"],
    "url": "https://leetcode.com/problems/invert-binary-tree/",
    "companies": ["Google", "Amazon", "Microsoft", "Facebook", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
}