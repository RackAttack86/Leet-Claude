# Problem 1162: As Far from Land as Possible

**Difficulty:** Medium
**Pattern:** Bfs Dfs
**Link:** [LeetCode](https://leetcode.com/problems/as-far-from-land-as-possible/)

## Problem Description

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

## Constraints

- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1

## Examples

```
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
```

## Approaches

### 1. Multi-source BFS

**Time Complexity:** O(n^2)
**Space Complexity:** O(n^2)

```python
def maxDistance(self, grid: List[List[int]]) -> int:
    n = len(grid)
    queue = deque()

    # Add all land cells to queue
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                queue.append((r, c))

    # If all land or all water
    if len(queue) == 0 or len(queue) == n * n:
        return -1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    distance = -1

    while queue:
        size = len(queue)
        distance += 1
        for _ in range(size):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # Mark as visited
                    queue.append((nr, nc))

    return distance
```

**Why this works:**
Start BFS from all land cells simultaneously. The BFS expands level by level, and the last level reached gives the maximum distance from any water cell to the nearest land. This is the same as finding the water cell that is farthest from all land cells.

## Key Insights

- Start BFS from all land cells
- Find maximum distance to any water
- BFS calculates distances correctly
- Return -1 if all land or all water

## Common Mistakes

- Not handling the case where grid is all land or all water
- Using DFS instead of BFS
- Not tracking the distance/level correctly

## Related Problems

- 01 Matrix
- Walls and Gates
- Rotting Oranges

## Tags

Array, Dynamic Programming, Breadth-First Search, Matrix
