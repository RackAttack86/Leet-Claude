# Problem 103: Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

## Problem Description

Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- -100 <= Node.val <= 100

## Examples

Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
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

### 1. BFS with Level Tracking and Alternating Direction

**Time Complexity:** O(n) - visit each node once
**Space Complexity:** O(n) - queue can hold up to n/2 nodes at the last level

```python
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            # Add to level based on current direction
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right

    return result
```

**Why this works:**

- Use BFS to traverse level by level
- Track current level and alternate direction (left-to-right vs right-to-left)
- Use deque for efficient append from both ends

## Key Insights

- Standard BFS traversal with level grouping
- Reverse every other level OR use deque to append from left/right based on direction
- Using deque with appendleft/append is more efficient than reversing lists

## Common Mistakes

- Reversing the traversal order instead of just the output order
- Not properly alternating direction between levels

## Related Problems

- 102 - Binary Tree Level Order Traversal
- 107 - Binary Tree Level Order Traversal II
