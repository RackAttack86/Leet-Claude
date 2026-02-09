# Problem 104: Maximum Depth of Binary Tree

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Problem Description

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Constraints

- The number of nodes in the tree is in the range [0, 10^4]
- -100 <= Node.val <= 100

## Examples

Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

Example 2:
```
Input: root = [1,null,2]
Output: 2
```

## Approaches

### 1. Recursive DFS

**Time Complexity:** O(n)
**Space Complexity:** O(h) where h is height

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

**Why this works:**

The maximum depth of a tree is 1 (for the current node) plus the maximum depth of either its left or right subtree. The base case is a null node which has depth 0.

## Key Insights

- Base case: null node has depth 0
- Depth = 1 + max(left_depth, right_depth)
- Simple recursive solution
- Can also use BFS (level-order traversal, counting levels)

## Common Mistakes

- Forgetting the base case for null nodes
- Off-by-one errors in counting depth

## Related Problems

- 111 - Minimum Depth of Binary Tree
- 110 - Balanced Binary Tree
- 543 - Diameter of Binary Tree

## Tags

Tree, Depth-First Search, Breadth-First Search, Binary Tree
