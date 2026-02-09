"""
LeetCode Problem #230: Kth Smallest Element in a BST
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Problem:
--------
Given the `root` of a binary search tree, and an integer `k`, return the `k^th` smallest value (1-indexed) of all the values of the nodes in the tree.

Constraints:
-----------
- The number of nodes in the tree is `n`.

Examples:
---------
Example 1:
```

Input: root = [3,1,4,null,2], k = 1
Output: 1

```

Example 2:
```

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

```
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        pass

class Node:
    def __init__(self, val=0, neighbors=None):
        pass

class Solution:
    """
    Solution to LeetCode Problem #230: Kth Smallest Element in a BST

    Approach: Iterative In-order Traversal with Early Exit
    - In-order traversal of BST visits nodes in ascending order
    - Use stack for iterative traversal
    - Count nodes visited and return when k-th node is reached
    - Early exit avoids traversing entire tree

    Time Complexity: O(H + k) - go to leftmost (H), then visit k nodes
    Space Complexity: O(H) - stack stores at most H nodes (tree height)

    Key Insights:
    - BST in-order traversal = sorted ascending order
    - Stop as soon as k-th element is found (no need to complete traversal)
    - Iterative approach allows early termination
    - For frequent queries: augment tree with subtree sizes
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pass



PROBLEM_METADATA = {
    "number": 230,
    "name": "Kth Smallest Element in a BST",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Tree', 'Depth-First Search', 'Binary Search Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/kth-smallest-element-in-a-bst/",
    "companies": ["Amazon", "Facebook", "Microsoft", "Google", "Bloomberg", "Apple", "Uber", "LinkedIn"],
    "time_complexity": "O(H + k)",
    "space_complexity": "O(H)",
}