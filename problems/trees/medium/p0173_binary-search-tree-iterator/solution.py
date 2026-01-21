"""
LeetCode Problem #173: Binary Search Tree Iterator
Difficulty: Medium
Pattern: Trees
Link: https://leetcode.com/problems/binary-search-tree-iterator/

Problem:
--------
Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST):

- `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
	
- `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.
	
- `int next()` Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to `next()` will return the smallest element in the BST.

You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.

Constraints:
-----------
- The number of nodes in the tree is in the range `[1, 10^5]`.
- At most `10^5` calls will be made to `hasNext`, and `next`.

Examples:
---------
Example 1:
```

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

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
    Solution to LeetCode Problem #173: Binary Search Tree Iterator

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

    def __init__(self, root: Optional[TreeNode]):
        """
        [TODO: Implement]
        """
        pass

    def next(self) -> int:
        """
        [TODO: Implement]
        """
        pass

    def hasNext(self) -> bool:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 173,
    "name": "Binary Search Tree Iterator",
    "difficulty": "Medium",
    "pattern": "Trees",
    "topics": ['Stack', 'Tree', 'Design', 'Binary Search Tree', 'Binary Tree', 'Iterator'],
    "url": "https://leetcode.com/problems/binary-search-tree-iterator/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
