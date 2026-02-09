# Problem 129: Sum Root to Leaf Numbers

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

## Problem Description

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

## Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.
- 0 <= Node.val <= 9
- The depth of the tree will not exceed `10`.

## Examples

Example 1:
```
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path `1->2` represents the number `12`.
The root-to-leaf path `1->3` represents the number `13`.
Therefore, sum = 12 + 13 = `25`.
```

Example 2:
```
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path `4->9->5` represents the number 495.
The root-to-leaf path `4->9->1` represents the number 491.
The root-to-leaf path `4->0` represents the number 40.
Therefore, sum = 495 + 491 + 40 = `1026`.
```

## Approaches

### 1. DFS with Running Number Accumulation

**Time Complexity:** O(n) - visit each node once
**Space Complexity:** O(h) - recursion stack where h is tree height

```python
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(node: TreeNode, current_num: int) -> int:
        if not node:
            return 0

        # Build the number so far
        current_num = current_num * 10 + node.val

        # If leaf node, return the number
        if not node.left and not node.right:
            return current_num

        # Sum up left and right subtrees
        return dfs(node.left, current_num) + dfs(node.right, current_num)

    return dfs(root, 0)
```

**Why this works:**

- Traverse from root to each leaf
- Accumulate number by multiplying current value by 10 and adding new digit
- When reaching a leaf, add the accumulated number to total sum

## Key Insights

- Each digit contributes to number as: current_num * 10 + digit
- Only add to sum at leaf nodes (no children)
- Can use either recursion or iterative with stack
- Number building: 1->2->3 becomes 1, then 12, then 123

## Common Mistakes

- Adding to sum at non-leaf nodes
- Not properly building the number (forgetting to multiply by 10)

## Related Problems

- 112 - Path Sum
- 113 - Path Sum II
- 257 - Binary Tree Paths
