# Problem 543: Diameter of Binary Tree

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)

## Problem Description

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

## Constraints

- The number of nodes in the tree is in the range [1, 10^4]
- -100 <= Node.val <= 100

## Examples

Example 1:
```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

Example 2:
```
Input: root = [1,2]
Output: 1
```

## Approaches

### 1. DFS with Height Calculation

**Time Complexity:** O(n)
**Space Complexity:** O(h) where h is height

```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.diameter = 0

    def height(node):
        if not node:
            return 0

        left_h = height(node.left)
        right_h = height(node.right)

        self.diameter = max(self.diameter, left_h + right_h)

        return max(left_h, right_h) + 1

    height(root)
    return self.diameter
```

**Why this works:**

At each node, the diameter passing through that node is the sum of the heights of its left and right subtrees. We calculate heights bottom-up while tracking the maximum diameter seen so far.

## Key Insights

- Diameter at node = left_height + right_height
- Track maximum diameter globally
- Return height to parent
- Path doesn't need to go through root

## Common Mistakes

- Assuming the diameter must pass through the root
- Confusing height with diameter
- Not tracking the global maximum

## Related Problems

- 104 - Maximum Depth of Binary Tree
- 110 - Balanced Binary Tree
- 124 - Binary Tree Maximum Path Sum

## Tags

Tree, Depth-First Search, Binary Tree
