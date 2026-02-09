# Problem 105: Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## Problem Description

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

## Constraints

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- `preorder` and `inorder` consist of unique values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be the preorder traversal of the tree.
- `inorder` is guaranteed to be the inorder traversal of the tree.

## Examples

Example 1:
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

Example 2:
```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

## Approaches

### 1. Divide and Conquer with Hash Map

**Time Complexity:** O(n) - visit each node once, O(1) lookup with hash map
**Space Complexity:** O(n) - hash map and recursion stack (O(h) where h is height)

```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # Build hash map for O(1) lookup of root position in inorder
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None

        # Root is the first element in preorder range
        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        # Find root position in inorder
        root_idx = inorder_map[root_val]

        # Number of nodes in left subtree
        left_size = root_idx - in_start

        # Build left and right subtrees
        root.left = build(pre_start + 1, pre_start + left_size,
                         in_start, root_idx - 1)
        root.right = build(pre_start + left_size + 1, pre_end,
                          root_idx + 1, in_end)

        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)
```

**Why this works:**

- Preorder: [root, left subtree, right subtree]
- Inorder: [left subtree, root, right subtree]
- First element of preorder is always the root
- Find root position in inorder to determine left/right subtree sizes
- Use hash map for O(1) lookup of root position in inorder

## Key Insights

- Preorder's first element is the root
- Inorder splits into left subtree, root, right subtree
- Number of elements to the left of root in inorder = left subtree size
- Use this size to partition preorder into left/right subtrees
- Hash map avoids O(n) search for root in inorder each time

## Common Mistakes

- Off-by-one errors in index calculations
- Not using hash map (leads to O(n^2) time)
- Confusing preorder and inorder partitioning

## Related Problems

- 106 - Construct Binary Tree from Inorder and Postorder Traversal
- 889 - Construct Binary Tree from Preorder and Postorder Traversal
