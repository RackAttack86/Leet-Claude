# Problem 199: Binary Tree Right Side View

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)

## Problem Description

Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- -100 <= Node.val <= 100

## Examples

Example 1:
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

Example 2:
```
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

Example 3:
```
Input: root = [1,null,3]
Output: [1,3]
```

Example 4:
```
Input: root = []
Output: []
```

## Approaches

### 1. BFS Level Order Traversal

**Time Complexity:** O(n) - visit each node once
**Space Complexity:** O(w) - queue holds at most one level, where w is max width

```python
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # Last node in this level is visible from right side
            if i == level_size - 1:
                result.append(node.val)

            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

**Why this works:**

- Process tree level by level
- For each level, the last node seen is the rightmost (visible from right)
- Add only the last node of each level to result

## Key Insights

- Right side view = last node at each level
- BFS naturally groups nodes by level
- Alternative: DFS with right child first, tracking depth
- DFS approach: visit right first, if depth == result.length, add to result

## Common Mistakes

- Only looking at rightmost path (misses nodes that are visible from deeper left subtree)
- Not handling levels correctly

## Related Problems

- 102 - Binary Tree Level Order Traversal
- 116 - Populating Next Right Pointers in Each Node
