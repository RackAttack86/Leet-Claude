# Problem 994: Rotting Oranges

**Difficulty:** Medium
**Pattern:** Bfs Dfs
**Link:** [LeetCode](https://leetcode.com/problems/rotting-oranges/)

## Problem Description

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2

## Examples

```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

## Approaches

### 1. Multi-source BFS

**Time Complexity:** O(m * n)
**Space Complexity:** O(m * n)

```python
def orangesRotting(self, grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Add all rotten oranges to queue and count fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    minutes = 0

    while queue:
        r, c, time = queue.popleft()
        minutes = max(minutes, time)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, time + 1))

    return minutes if fresh == 0 else -1
```

**Why this works:**
Start BFS from all rotten oranges simultaneously. Track the time/level of BFS as oranges spread. Count fresh oranges initially and decrement as they rot. If any fresh oranges remain after BFS completes, return -1.

## Key Insights

- Start BFS from all rotten oranges
- Track time/levels of BFS
- Count fresh oranges remaining
- Return -1 if fresh oranges remain

## Common Mistakes

- Forgetting to check if there are no fresh oranges initially (should return 0)
- Not tracking time correctly during BFS
- Returning the wrong value when oranges cannot all be rotted

## Related Problems

- Walls and Gates
- 01 Matrix
- Shortest Path in Binary Matrix

## Tags

Array, Breadth-First Search, Matrix
