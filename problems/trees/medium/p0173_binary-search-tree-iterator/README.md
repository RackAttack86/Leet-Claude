# Problem 173: Binary Search Tree Iterator

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator/)

## Problem Description

Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST):

- `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.
- `int next()` Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to `next()` will return the smallest element in the BST.

You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.

## Constraints

- The number of nodes in the tree is in the range `[1, 10^5]`.
- 0 <= Node.val <= 10^6
- At most `10^5` calls will be made to `hasNext`, and `next`.

## Examples

Example 1:
```
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]
```

## Approaches

### 1. Controlled Recursion Using Stack

**Time Complexity:** O(1) average for next() and hasNext()
**Space Complexity:** O(h) - stack stores at most h nodes (height of tree)

```python
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left_nodes(root)

    def _push_left_nodes(self, node: TreeNode) -> None:
        """Helper to push current node and all its left descendants onto stack."""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the next smallest element
        node = self.stack.pop()

        # If node has right child, push its left path
        if node.right:
            self._push_left_nodes(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
```

**Why this works:**

- Use stack to simulate in-order traversal iteratively
- Push all left children to stack initially
- For next(), pop from stack and push all left children of right subtree
- Stack always contains the path to the next smallest unvisited element

## Key Insights

- In-order traversal: left -> root -> right
- Stack stores the path from root to leftmost unvisited node
- After visiting a node, explore its right subtree's leftmost path
- While worst case for next() is O(h), amortized over n calls is O(1)

## Common Mistakes

- Flattening the entire tree upfront (uses O(n) space)
- Not properly handling the right subtree after popping

## Related Problems

- 94 - Binary Tree Inorder Traversal
- 230 - Kth Smallest Element in a BST
- 285 - Inorder Successor in BST
