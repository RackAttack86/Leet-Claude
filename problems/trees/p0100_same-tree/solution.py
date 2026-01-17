"""
LeetCode Problem #100: Same Tree
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/same-tree/

Problem:
--------
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have
the same value.

Constraints:
-----------
- The number of nodes in both trees is in the range [0, 100]
- -10^4 <= Node.val <= 10^4

Examples:
---------
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #100: Same Tree

    Approach: Recursive DFS
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height

    Key Insights:
    - Base case: both null returns true
    - If one null or values differ, return false
    - Recursively check left and right subtrees
    - Simple recursive pattern
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 100,
    "name": "Same Tree",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ["Tree", "Depth-First Search", "Breadth-First Search", "Binary Tree"],
    "url": "https://leetcode.com/problems/same-tree/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
}
