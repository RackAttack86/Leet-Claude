# Problem 226: Invert Binary Tree

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/invert-binary-tree/)

## Problem Description

Given the root of a binary tree, invert the tree, and return its root.

## Constraints

- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

## Examples

Example 1:
```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

Example 2:
```
Input: root = [2,1,3]
Output: [2,3,1]
```

Example 3:
```
Input: root = []
Output: []
```

## Approaches

### 1. Recursive DFS

**Time Complexity:** O(n)
**Space Complexity:** O(h) where h is height

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
```

**Why this works:**

The algorithm swaps the left and right children of each node recursively. By doing this at every node in the tree, we effectively mirror the entire tree around its center.

## Key Insights

- Swap left and right children recursively
- Base case: null node returns null
- Simple recursive pattern
- Can also use BFS (level-order traversal)

## Common Mistakes

- Forgetting to return the root after inversion
- Not handling the null case

## Related Problems

- 101 - Symmetric Tree
- 100 - Same Tree

## Tags

Tree, Depth-First Search, Breadth-First Search, Binary Tree
