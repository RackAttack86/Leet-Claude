# Problem 236: Lowest Common Ancestor of a Binary Tree

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Problem Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself)."

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- -10^9 <= Node.val <= 10^9
- All `Node.val` are unique.
- p != q
- `p` and `q` will exist in the tree.

## Examples

Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

Example 2:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

Example 3:
```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## Approaches

### 1. Recursive DFS with Propagation

**Time Complexity:** O(n) - visit each node once in worst case
**Space Complexity:** O(h) - recursion stack where h is tree height

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # Base case: if root is None, or we found p or q
    if not root or root == p or root == q:
        return root

    # Search in left and right subtrees
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    # If both subtrees return non-null, root is the LCA
    if left and right:
        return root

    # Otherwise, return the non-null result (or None if both are null)
    return left if left else right
```

**Why this works:**

- Base case: if node is None, p, or q, return node
- Recursively search left and right subtrees
- If both left and right return non-null, current node is LCA
- If only one side returns non-null, propagate that result up

## Key Insights

- If node == p or node == q, that node might be the LCA
- LCA is the node where p and q are found in different subtrees
- If p is ancestor of q (or vice versa), the ancestor is the LCA
- Propagate found nodes up the recursion stack

## Common Mistakes

- Not handling the case where one node is ancestor of the other
- Incorrect propagation of results up the tree

## Related Problems

- 235 - Lowest Common Ancestor of a Binary Search Tree
- 1644 - Lowest Common Ancestor of a Binary Tree II
- 1650 - Lowest Common Ancestor of a Binary Tree III
