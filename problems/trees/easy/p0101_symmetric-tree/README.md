# Problem 101: Symmetric Tree

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/symmetric-tree/)

## Problem Description

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.
- -100 <= Node.val <= 100

## Examples

Example 1:
```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

Example 2:
```
Input: root = [1,2,2,null,3,null,3]
Output: false
```

## Approaches

### 1. Recursive Comparison of Mirror Nodes

**Time Complexity:** O(n) - visit each node once
**Space Complexity:** O(h) - recursion stack, where h is tree height (O(n) worst case for skewed tree)

```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    return self._isMirror(root.left, root.right)

def _isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    # Both None - symmetric
    if not left and not right:
        return True
    # One None, one not - not symmetric
    if not left or not right:
        return False
    # Both exist - check values and recursively check mirror children
    return (left.val == right.val and
            self._isMirror(left.left, right.right) and
            self._isMirror(left.right, right.left))
```

**Why this works:**

A tree is symmetric if the left subtree is a mirror reflection of the right subtree. Two trees are mirrors if:
1. Their root values are equal
2. Left subtree of one is a mirror of right subtree of the other

The helper function compares two nodes at mirror positions.

## Key Insights

- Compare left.left with right.right AND left.right with right.left (mirror comparison)
- Both nodes being None is symmetric (base case returns True)
- One None and one non-None is not symmetric

## Common Mistakes

- Comparing left.left with right.left instead of right.right (not a mirror comparison)
- Forgetting to handle null nodes properly

## Related Problems

- 100 - Same Tree
- 226 - Invert Binary Tree
