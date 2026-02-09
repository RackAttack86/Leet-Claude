# Problem 54: Spiral Matrix

**Difficulty:** Medium
**Pattern:** Bfs Dfs
**Link:** [LeetCode](https://leetcode.com/problems/spiral-matrix/)

## Problem Description

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

## Constraints

- `m == matrix.length
- n == matrix[i].length
- 100

## Examples

Example 1:
```

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

```

Example 2:
```

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

```

## Approaches

### 1. Four Boundary Pointers

**Time Complexity:** O(m*n) - Visit each element exactly once
**Space Complexity:** O(1) - Excluding output array, only use constant extra space

```python
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse right along top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse down along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse left along bottom row (if still valid)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse up along left column (if still valid)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```

**Why this works:**
Use four boundary pointers (top, bottom, left, right) to track the current spiral layer. Traverse right, down, left, up in order, shrinking boundaries after each direction is completed. Continue until all elements are visited.

## Key Insights

- Maintain four boundaries and shrink them as we complete each direction
- Order of traversal: right -> down -> left -> up (repeat)
- Must check boundary conditions after traversing down and up to handle single row/column
- The spiral peels off layers from outside to inside

## Common Mistakes

- Forgetting to check if boundaries are still valid before traversing left or up
- Off-by-one errors in range calculations
- Not handling single row or single column matrices correctly

## Related Problems

- Spiral Matrix II
- Rotate Image
