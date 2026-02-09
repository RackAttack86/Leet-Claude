# Problem 48: Rotate Image

**Difficulty:** Medium
**Pattern:** Bfs Dfs
**Link:** [LeetCode](https://leetcode.com/problems/rotate-image/)

## Problem Description

You are given an `n x n` 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

## Constraints

- `n == matrix.length == matrix[i].length
- 1000

## Examples

Example 1:
```

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

```

Example 2:
```

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

```

## Approaches

### 1. Transpose and Reverse

**Time Complexity:** O(n^2) - Visit each element twice (once for transpose, once for reverse)
**Space Complexity:** O(1) - In-place modification, no extra space used

```python
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Step 1: Transpose the matrix (swap across diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

**Why this works:**
Two-step transformation: First transpose the matrix (swap rows and columns), then reverse each row. This achieves 90-degree clockwise rotation in-place.

## Key Insights

- 90-degree clockwise rotation = Transpose + Reverse each row
- 90-degree counter-clockwise rotation = Transpose + Reverse each column
- Transpose swaps matrix[i][j] with matrix[j][i] for i < j
- Alternative: 4-way swap rotating elements in groups of 4 (layer by layer)

## Common Mistakes

- Forgetting to only swap upper triangular elements during transpose (to avoid double swapping)
- Confusing clockwise vs counter-clockwise rotation steps
- Not handling the in-place requirement

## Related Problems

- Spiral Matrix
- Spiral Matrix II
