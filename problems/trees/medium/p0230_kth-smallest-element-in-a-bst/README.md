# Problem 230: Kth Smallest Element in a BST

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Problem Description

Given the `root` of a binary search tree, and an integer `k`, return the `k^th` smallest value (1-indexed) of all the values of the nodes in the tree.

## Constraints

- The number of nodes in the tree is `n`.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

## Examples

Example 1:
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

Example 2:
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## Approaches

### 1. Iterative In-order Traversal with Early Exit

**Time Complexity:** O(H + k) - go to leftmost (H), then visit k nodes
**Space Complexity:** O(H) - stack stores at most H nodes (tree height)

```python
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    current = root
    count = 0

    while stack or current:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process current node
        current = stack.pop()
        count += 1

        # If this is the k-th smallest, return it
        if count == k:
            return current.val

        # Move to right subtree
        current = current.right

    # Should not reach here if k is valid
    return -1
```

**Why this works:**

- In-order traversal of BST visits nodes in ascending order
- Use stack for iterative traversal
- Count nodes visited and return when k-th node is reached
- Early exit avoids traversing entire tree

## Key Insights

- BST in-order traversal = sorted ascending order
- Stop as soon as k-th element is found (no need to complete traversal)
- Iterative approach allows early termination
- For frequent queries: augment tree with subtree sizes

## Common Mistakes

- Traversing entire tree when early exit is possible
- Using recursive approach without ability to terminate early

## Related Problems

- 94 - Binary Tree Inorder Traversal
- 173 - Binary Search Tree Iterator
- 671 - Second Minimum Node In a Binary Tree
