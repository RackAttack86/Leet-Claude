# Problem 530: Minimum Absolute Difference in BST

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

## Problem Description

Given the `root` of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

## Constraints

- The number of nodes in the tree is in the range `[2, 10^4]`.
- 0 <= Node.val <= 10^5

## Examples

Example 1:
```
Input: root = [4,2,6,1,3]
Output: 1
```

Example 2:
```
Input: root = [1,0,48,null,null,12,49]
Output: 1
```

## Approaches

### 1. In-order Traversal to Get Sorted Sequence

**Time Complexity:** O(n) - visit each node exactly once
**Space Complexity:** O(h) - recursion stack, where h is tree height

```python
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    self.min_diff = float('inf')
    self.prev = None

    def inorder(node: Optional[TreeNode]) -> None:
        if not node:
            return

        # Visit left subtree
        inorder(node.left)

        # Process current node
        if self.prev is not None:
            self.min_diff = min(self.min_diff, node.val - self.prev)
        self.prev = node.val

        # Visit right subtree
        inorder(node.right)

    inorder(root)
    return self.min_diff
```

**Why this works:**

- BST in-order traversal produces nodes in sorted (ascending) order
- Minimum difference must be between adjacent nodes in sorted order
- Track previous node value and update minimum difference during traversal
- Use instance variables to maintain state across recursive calls

## Key Insights

- In a BST, in-order traversal gives sorted values
- Minimum absolute difference is always between consecutive sorted values
- No need to store all values; just track previous value during traversal
- This is equivalent to problem #783 (Minimum Distance Between BST Nodes)

## Common Mistakes

- Not leveraging the BST property (in-order gives sorted order)
- Storing all values and then finding minimum difference (unnecessary space)

## Related Problems

- 783 - Minimum Distance Between BST Nodes
- 98 - Validate Binary Search Tree
