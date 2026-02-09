# Problem 73: Set Matrix Zeroes

**Difficulty:** Medium
**Pattern:** Bfs Dfs
**Link:** [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)

## Problem Description

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place.

## Constraints

- `m == matrix.length
- n == matrix[0].length
- 2^31

## Examples

Example 1:
```

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

```

Example 2:
```

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

```

## Approaches

### 1. First Row/Column as Markers

**Time Complexity:** O(m*n) - Two passes through the matrix
**Space Complexity:** O(1) - Use matrix itself as storage for markers

```python
def setZeroes(self, matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])

    # Check if first row or first column should be zeroed
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row and column as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark the row
                matrix[0][j] = 0  # Mark the column

    # Zero out cells based on markers (process inner matrix)
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Zero out first row if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Zero out first column if needed
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
```

**Why this works:**
Use the first row and first column as markers to track which rows/columns need to be zeroed. Use separate flags for whether the first row and first column themselves should be zeroed. This achieves O(1) space complexity.

## Key Insights

- First row and first column can serve as "marker arrays" instead of extra space
- Need separate flags for first row/column since they're used as markers
- Process: 1) Mark, 2) Zero inner cells, 3) Zero first row/column if needed
- Process inner matrix first (1 to m-1, 1 to n-1), then handle first row/column

## Common Mistakes

- Processing the first row/column before the inner matrix (corrupts markers)
- Forgetting to save the state of first row/column before using them as markers
- Using O(m+n) space for separate marker arrays when O(1) is possible

## Related Problems

- Game of Life
