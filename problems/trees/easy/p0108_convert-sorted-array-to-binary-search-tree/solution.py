"""
LeetCode Problem #108: Convert Sorted Array to Binary Search Tree
Difficulty: Easy
Pattern: Trees
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Problem:
--------
Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Constraints:
-----------
- `1
- 10^4
- nums` is sorted in a strictly increasing order.

Examples:
---------
Example 1:
```

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

```

Example 2:
```

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

```
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
    Solution to LeetCode Problem #108: Convert Sorted Array to Binary Search Tree

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

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 108,
    "name": "Convert Sorted Array to Binary Search Tree",
    "difficulty": "Easy",
    "pattern": "Trees",
    "topics": ['Array', 'Divide and Conquer', 'Tree', 'Binary Search Tree', 'Binary Tree'],
    "url": "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
