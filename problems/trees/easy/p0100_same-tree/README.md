# Problem 100: Same Tree

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/same-tree/)

## Problem Description

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have
the same value.

## Constraints

- The number of nodes in both trees is in the range [0, 100]
- -10^4 <= Node.val <= 10^4

## Examples

Example 1:
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

Example 2:
```
Input: p = [1,2], q = [1,null,2]
Output: false
```

Example 3:
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## Approaches

### 1. Recursive DFS

**Time Complexity:** O(n)
**Space Complexity:** O(h) where h is height

```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

**Why this works:**

The algorithm uses a simple recursive approach. At each step, we check:
1. If both nodes are null, they are the same (base case returns true)
2. If one is null and the other isn't, they are different (return false)
3. If the values differ, they are different (return false)
4. Recursively check left and right subtrees - both must be the same

## Key Insights

- Base case: both null returns true
- If one null or values differ, return false
- Recursively check left and right subtrees
- Simple recursive pattern

## Common Mistakes

- Forgetting to handle the case where one node is null and the other is not
- Not checking both left and right subtrees

## Related Problems

- 101 - Symmetric Tree
- 572 - Subtree of Another Tree

## Tags

Tree, Depth-First Search, Breadth-First Search, Binary Tree
