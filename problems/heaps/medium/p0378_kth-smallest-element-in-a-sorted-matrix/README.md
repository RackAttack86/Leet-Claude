# Problem 378: Kth Smallest Element in a Sorted Matrix

**Difficulty:** Medium
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

## Problem Description

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

## Constraints

- n == matrix.length == matrix[i].length
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order
- 1 <= k <= n^2

## Examples

Example 1:
```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
```

Example 2:
```
Input: matrix = [[-5]], k = 1
Output: -5
```

## Approaches

### 1. Min Heap

**Time Complexity:** O(k log n)
**Space Complexity:** O(n)

```python
def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    n = len(matrix)

    # (value, row, col)
    min_heap = [(matrix[0][0], 0, 0)]
    visited = {(0, 0)}

    for _ in range(k):
        val, row, col = heapq.heappop(min_heap)

        # Add right neighbor
        if col + 1 < n and (row, col + 1) not in visited:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
            visited.add((row, col + 1))

        # Add bottom neighbor
        if row + 1 < n and (row + 1, col) not in visited:
            heapq.heappush(min_heap, (matrix[row + 1][col], row + 1, col))
            visited.add((row + 1, col))

    return val
```

**Why this works:**
We start from the top-left corner (smallest element) and use BFS-like exploration with a min heap. Each time we pop the current minimum, we add its right and bottom neighbors. After k pops, we have the kth smallest.

### 2. Binary Search (Alternative)

**Time Complexity:** O(n log(max-min))
**Space Complexity:** O(1)

**Why this works:**
Binary search on value range. For each mid value, count elements <= mid. Adjust search based on count vs k.

## Key Insights

1. Heap: Start with first element of each row
2. Binary search on value range
3. Count elements <= mid to find position
4. Both approaches have merits

## Common Mistakes

1. Not tracking visited cells in heap approach
2. Incorrect binary search bounds
3. Not handling duplicates properly in counting

## Related Problems

- 373. Find K Pairs with Smallest Sums
- 668. Kth Smallest Number in Multiplication Table

## Tags

Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
