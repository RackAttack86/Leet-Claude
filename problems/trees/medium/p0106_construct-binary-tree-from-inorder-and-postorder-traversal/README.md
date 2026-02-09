# Problem 106: Construct Binary Tree from Inorder and Postorder Traversal

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## Problem Description

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

## Constraints

- 1 <= inorder.length <= 3000
- postorder.length == inorder.length
- -3000 <= inorder[i], postorder[i] <= 3000
- `inorder` and `postorder` consist of unique values.
- Each value of `postorder` also appears in `inorder`.
- `inorder` is guaranteed to be the inorder traversal of the tree.
- `postorder` is guaranteed to be the postorder traversal of the tree.

## Examples

Example 1:
```
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

Example 2:
```
Input: inorder = [-1], postorder = [-1]
Output: [-1]
```

## Approaches

### 1. Divide and Conquer with Hash Map

**Time Complexity:** O(n) - visit each node once, O(1) lookup with hash map
**Space Complexity:** O(n) - hash map and recursion stack (O(h) where h is height)

```python
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    # Build hash map for O(1) lookup of root position in inorder
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    def build(post_start: int, post_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
        if post_start > post_end:
            return None

        # Root is the last element in postorder range
        root_val = postorder[post_end]
        root = TreeNode(root_val)

        # Find root position in inorder
        root_idx = inorder_map[root_val]

        # Number of nodes in left subtree
        left_size = root_idx - in_start

        # Build left and right subtrees
        root.left = build(post_start, post_start + left_size - 1,
                         in_start, root_idx - 1)
        root.right = build(post_start + left_size, post_end - 1,
                          root_idx + 1, in_end)

        return root

    return build(0, len(postorder) - 1, 0, len(inorder) - 1)
```

**Why this works:**

- Postorder: [left subtree, right subtree, root]
- Inorder: [left subtree, root, right subtree]
- Last element of postorder is always the root
- Find root position in inorder to determine left/right subtree sizes
- Use hash map for O(1) lookup of root position in inorder

## Key Insights

- Postorder's last element is the root (unlike preorder where first is root)
- Build right subtree before left subtree when processing postorder from end
- Inorder splits into left subtree, root, right subtree
- Number of elements to the left of root in inorder = left subtree size

## Common Mistakes

- Off-by-one errors in index calculations
- Confusing postorder with preorder partitioning
- Not using hash map (leads to O(n^2) time)

## Related Problems

- 105 - Construct Binary Tree from Preorder and Inorder Traversal
- 889 - Construct Binary Tree from Preorder and Postorder Traversal
