# Problem 102: Binary Tree Level Order Traversal

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## Problem Description

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

## Constraints

- The number of nodes in the tree is in the range [0, 2000]
- -1000 <= Node.val <= 1000

## Examples

Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

Example 2:
```
Input: root = [1]
Output: [[1]]
```

Example 3:
```
Input: root = []
Output: []
```

## Approaches

### 1. BFS with Queue

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_values = []

        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_values)

    return result
```

**Why this works:**

Use a queue to process nodes level by level. For each level, we know how many nodes to process (current queue size) before moving to the next level.

## Key Insights

- Use queue for BFS
- Process level by level
- Track level size before processing
- Classic BFS pattern

## Common Mistakes

- Not properly tracking level boundaries
- Forgetting to handle empty tree case
- Modifying queue while iterating

## Related Problems

- 103 - Binary Tree Zigzag Level Order Traversal
- 107 - Binary Tree Level Order Traversal II
- 637 - Average of Levels in Binary Tree

## Tags

Tree, Breadth-First Search, Binary Tree
