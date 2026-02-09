# Problem 74: Search a 2D Matrix

**Difficulty:** Medium
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/)

## Problem Description

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
	
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in `O(log(m * n))` time complexity.

## Constraints

- `m == matrix.length
- n == matrix[i].length
- 10^4

## Examples

Example 1:
```

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

```

Example 2:
```

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

```

## Approaches

### 1. Treat 2D Matrix as 1D Sorted Array

**Time Complexity:** O(log(m*n)) - Single binary search over m*n elements
**Space Complexity:** O(1) - Only using constant extra space

```python
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        # Convert 1D index to 2D coordinates
        row, col = mid // n, mid % n
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

**Why this works:**
Since each row is sorted and the first element of each row is greater than the last element of the previous row, the entire matrix can be treated as a single sorted array of length m*n. We perform standard binary search where virtual index i maps to matrix[i // n][i % n].

## Key Insights

- The 2D matrix with given properties is essentially a flattened sorted array
- Convert 1D index to 2D coordinates: row = idx // cols, col = idx % cols
- Single binary search is more efficient than two binary searches
- Handle empty matrix edge case

## Common Mistakes

- Off-by-one errors in index conversion
- Not handling empty matrix case
- Using two binary searches when one suffices

## Related Problems

- Search a 2D Matrix II (#240)
- Binary Search (#704)
