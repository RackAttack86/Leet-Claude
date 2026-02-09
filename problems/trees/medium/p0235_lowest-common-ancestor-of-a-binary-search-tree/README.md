# Problem 235: Lowest Common Ancestor of a Binary Search Tree

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Problem Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).

## Constraints

- The number of nodes in the tree is in the range [2, 10^5]
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q
- p and q will exist in the BST

## Examples

Example 1:
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

Example 2:
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself.
```

## Approaches

### 1. BST Property Traversal

**Time Complexity:** O(h) where h is height
**Space Complexity:** O(1) for iterative, O(h) for recursive

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    current = root

    while current:
        if p.val < current.val and q.val < current.val:
            # Both nodes are in left subtree
            current = current.left
        elif p.val > current.val and q.val > current.val:
            # Both nodes are in right subtree
            current = current.right
        else:
            # Split point found - current is the LCA
            return current

    return None
```

**Why this works:**

Since it's a BST, we can use the ordering property:
- If both p and q are smaller than root, LCA is in left subtree
- If both p and q are larger than root, LCA is in right subtree
- Otherwise, root is the LCA (split point or one equals root)

## Key Insights

- Use BST property for direction
- If both < root, go left
- If both > root, go right
- Otherwise, root is LCA

## Common Mistakes

- Not leveraging BST property (using general binary tree approach)
- Using recursion when iterative O(1) space is possible

## Related Problems

- 236 - Lowest Common Ancestor of a Binary Tree
- 1650 - Lowest Common Ancestor of a Binary Tree III

## Tags

Tree, Depth-First Search, Binary Search Tree, Binary Tree
