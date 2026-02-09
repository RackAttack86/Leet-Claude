# Problem 572: Subtree of Another Tree

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)

## Problem Description

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

## Constraints

- The number of nodes in the root tree is in the range [1, 2000]
- The number of nodes in the subRoot tree is in the range [1, 1000]
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4

## Examples

Example 1:
```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

Example 2:
```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

## Approaches

### 1. DFS with Subtree Matching

**Time Complexity:** O(m * n) where m and n are tree sizes
**Space Complexity:** O(h) where h is height

```python
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSameTree(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

**Why this works:**

At each node in the root tree, we check if the subtree rooted at that node is identical to subRoot. We use the isSameTree helper function to compare two trees for equality.

## Key Insights

- Check if trees are same at each node
- Use isSameTree helper function
- Recursively check all nodes in root
- Can optimize with tree hashing or serialization

## Common Mistakes

- Not checking all nodes in the main tree
- Confusing subtree check with same tree check

## Related Problems

- 100 - Same Tree
- 101 - Symmetric Tree

## Tags

Tree, Depth-First Search, Binary Tree, String Matching, Hash Function
