# Problem 427: Construct Quad Tree

**Difficulty:** Medium
**Pattern:** Trees
**Link:** [LeetCode](https://leetcode.com/problems/construct-quad-tree/)

## Problem Description

Given a `n * n` matrix `grid` of `0's` and `1's` only. We want to represent `grid` with a Quad-Tree.

Return the root of the Quad-Tree representing `grid`.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

- `val`: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the `val` to True or False when `isLeaf` is False, and both are accepted in the answer.
- `isLeaf`: True if the node is a leaf node on the tree or False if the node has four children.

We can construct a Quad-Tree from a two-dimensional area using the following steps:

- If the current grid has the same value (i.e all `1's` or all `0's`) set `isLeaf` True and set `val` to the value of the grid and set the four children to Null and stop.
- If the current grid has different values, set `isLeaf` to False and set `val` to any value and divide the current grid into four sub-grids as shown in the photo.
- Recurse for each of the children with the proper sub-grid.

## Constraints

- `n == grid.length == grid[i].length`
- `n == 2^x` where `0 <= x <= 6`

## Examples

Example 1:
```
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.
```

Example 2:
```
Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
```

## Approaches

### 1. Divide and Conquer (Recursive)

**Time Complexity:** O(n^2 * log n) - each level processes all n^2 cells
**Space Complexity:** O(log n) - recursion depth for n x n grid

```python
def construct(self, grid: List[List[int]]) -> 'Node':
    def is_uniform(row: int, col: int, size: int) -> tuple:
        """Check if subgrid is uniform and return (is_uniform, value)."""
        val = grid[row][col]
        for i in range(row, row + size):
            for j in range(col, col + size):
                if grid[i][j] != val:
                    return False, val
        return True, val

    def build(row: int, col: int, size: int) -> 'Node':
        # Check if this subgrid is uniform
        uniform, val = is_uniform(row, col, size)

        if uniform:
            # Create leaf node
            return Node(val == 1, True)

        # Not uniform - divide into 4 quadrants
        half = size // 2

        topLeft = build(row, col, half)
        topRight = build(row, col + half, half)
        bottomLeft = build(row + half, col, half)
        bottomRight = build(row + half, col + half, half)

        # Create internal node (val can be anything, using True)
        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

    n = len(grid)
    return build(0, 0, n)
```

**Why this works:**

- Check if current subgrid has uniform values
- If uniform: create leaf node with that value
- If not uniform: divide into 4 quadrants and recurse
- Build tree from bottom-up by combining quadrant results

## Key Insights

- Grid size is always 2^x, so it divides evenly
- Check uniformity first before recursing
- Quadrants: topLeft, topRight, bottomLeft, bottomRight
- Leaf node: all values same; Internal node: has 4 children

## Common Mistakes

- Not properly dividing the grid into quadrants
- Off-by-one errors in subgrid boundaries

## Related Problems

- 558 - Logical OR of Two Binary Grids Represented as Quad-Trees
