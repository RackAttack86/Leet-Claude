# Problem 112: Path Sum

**Difficulty:** Easy
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/path-sum/)

## Problem Description

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

A leaf is a node with no children.

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

## Examples

Example 1:
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
```

Example 2:
```
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
```

Example 3:
```
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
```

## Approaches

### 1. Recursive DFS with Running Sum Subtraction

**Time Complexity:** O(n) - visit each node once in worst case
**Space Complexity:** O(h) - recursion stack, where h is tree height

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    # Check if we're at a leaf node
    if not root.left and not root.right:
        return root.val == targetSum

    # Subtract current value and check children
    remaining = targetSum - root.val
    return (self.hasPathSum(root.left, remaining) or
            self.hasPathSum(root.right, remaining))
```

**Why this works:**

- Subtract current node's value from targetSum as we traverse
- At a leaf node, check if remaining targetSum equals the leaf's value
- Recursively check both left and right subtrees
- Return True if any path from root to leaf sums to targetSum

## Key Insights

- Subtract node value from targetSum instead of accumulating sum (cleaner)
- A leaf is defined as a node with NO children (both left and right are None)
- Empty tree returns False (no paths exist)
- Only check sum at leaf nodes, not internal nodes

## Common Mistakes

- Returning true at non-leaf nodes when sum matches
- Forgetting to handle empty tree case
- Not properly identifying leaf nodes

## Related Problems

- 113 - Path Sum II
- 437 - Path Sum III
- 129 - Sum Root to Leaf Numbers
