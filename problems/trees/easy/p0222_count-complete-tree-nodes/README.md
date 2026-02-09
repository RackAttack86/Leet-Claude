# Problem 222: Count Complete Tree Nodes

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/count-complete-tree-nodes/)

## Problem Description

Given the `root` of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between `1` and `2^h` nodes inclusive at the last level `h`.

Design an algorithm that runs in less than O(n) time complexity.

## Constraints

- The number of nodes in the tree is in the range `[0, 5 * 10^4]`.
- The tree is guaranteed to be complete.

## Examples

Example 1:
```
Input: root = [1,2,3,4,5,6]
Output: 6
```

Example 2:
```
Input: root = []
Output: 0
```

Example 3:
```
Input: root = [1]
Output: 1
```

## Approaches

### 1. Leverage Complete Binary Tree Property with Binary Search

**Time Complexity:** O(log^2 n) - O(log n) height calculations, each O(log n) depth
**Space Complexity:** O(log n) - recursion stack depth

```python
def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_height = self._getLeftHeight(root)
    right_height = self._getRightHeight(root)

    # If left and right heights are equal, tree is perfect
    if left_height == right_height:
        return (1 << left_height) - 1  # 2^h - 1

    # Otherwise, recursively count nodes
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)

def _getLeftHeight(self, node: Optional[TreeNode]) -> int:
    """Get height by traversing left edge."""
    height = 0
    while node:
        height += 1
        node = node.left
    return height

def _getRightHeight(self, node: Optional[TreeNode]) -> int:
    """Get height by traversing right edge."""
    height = 0
    while node:
        height += 1
        node = node.right
    return height
```

**Why this works:**

- Compare left and right subtree heights
- If heights are equal, left subtree is a perfect binary tree. Count it as 2^h - 1 + 1 (root) and recurse on right
- If heights differ, right subtree is perfect (one level shorter). Count it as 2^(h-1) - 1 + 1 (root) and recurse on left
- This avoids visiting all nodes by skipping perfect subtrees

## Key Insights

- In a complete tree, at least one subtree is always a perfect binary tree
- Perfect binary tree with height h has 2^h - 1 nodes
- Computing left/right height only traverses leftmost/rightmost path: O(log n)
- We recurse on only ONE subtree each time, giving O(log n) recursive calls

## Common Mistakes

- Using O(n) traversal when O(log^2 n) is possible
- Not leveraging the complete binary tree property

## Related Problems

- 104 - Maximum Depth of Binary Tree
- 110 - Balanced Binary Tree
