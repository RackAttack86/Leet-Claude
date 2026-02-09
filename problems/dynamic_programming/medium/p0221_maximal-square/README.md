# Problem 221: Maximal Square

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/maximal-square/)

## Problem Description

Given an `m x n` binary `matrix` filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area.

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] is '0' or '1'.

## Examples

Example 1:
```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
```

Example 2:
```
Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

Example 3:
```
Input: matrix = [["0"]]
Output: 0
```

## Approaches

### 1. Dynamic Programming with Space Optimization

**Time Complexity:** O(m * n)
**Space Complexity:** O(n)

```python
def maximalSquare(self, matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    max_side = 0

    # dp[j] represents the side length of largest square ending at current row, column j
    dp = [0] * (n + 1)

    for i in range(m):
        prev_diagonal = 0  # This stores dp[i-1][j-1]

        for j in range(1, n + 1):
            temp = dp[j]  # Save current value before updating

            if matrix[i][j - 1] == '1':
                # Take minimum of top (dp[j]), left (dp[j-1]), and top-left (prev_diagonal)
                dp[j] = min(dp[j], dp[j - 1], prev_diagonal) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0

            prev_diagonal = temp

    return max_side * max_side
```

**Why this works:**

dp[i][j] represents the side length of the largest square with bottom-right corner at (i, j). If matrix[i][j] == '1', then dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1. A square can only extend if all three neighbors can form squares, and the size is limited by the smallest neighbor.

## Key Insights

1. A square at (i,j) can only extend if all three neighbors (top, left, top-left) can form squares.
2. The size is limited by the smallest of the three neighbors.
3. This is because any larger square would require all three directions to have equally large squares.
4. We need to track the previous diagonal value when using 1D optimization.

## Common Mistakes

1. Forgetting to track the diagonal value when using space optimization
2. Returning the side length instead of the area (side * side)
3. Not handling the '0' case by resetting dp[j] to 0

## Related Problems

- Maximal Rectangle
- Largest Rectangle in Histogram
