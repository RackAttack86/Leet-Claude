# Problem 110: Balanced Binary Tree

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/balanced-binary-tree/)

## Problem Description

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Constraints

- The number of nodes in the tree is in the range [0, 5000]
- -10^4 <= Node.val <= 10^4

## Examples

Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

Example 2:
```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

## Approaches

### 1. Recursive DFS with Height Calculation

**Time Complexity:** O(n)
**Space Complexity:** O(h) where h is height

```python
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def check_height(node):
        if not node:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return check_height(root) != -1
```

**Why this works:**

The algorithm calculates the height of each subtree while simultaneously checking if it's balanced. If any subtree is unbalanced, it returns -1 as a signal to propagate up. This bottom-up approach is efficient because:
1. It only visits each node once
2. It short-circuits as soon as an imbalance is detected

## Key Insights

- Calculate height while checking balance
- Return -1 if unbalanced for early exit
- Check |left_height - right_height| <= 1
- Bottom-up approach is more efficient than top-down

## Common Mistakes

- Using a top-down approach that recalculates height multiple times (O(n^2))
- Not properly propagating the unbalanced status up the tree

## Related Problems

- 104 - Maximum Depth of Binary Tree
- 543 - Diameter of Binary Tree

## Tags

Tree, Depth-First Search, Binary Tree
