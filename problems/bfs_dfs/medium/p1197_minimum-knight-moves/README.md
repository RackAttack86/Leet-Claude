# Problem 1197: Minimum Knight Moves

**Difficulty:** Medium
**Pattern:** Bfs Dfs
**Link:** [LeetCode](https://leetcode.com/problems/minimum-knight-moves/)

## Problem Description

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

## Constraints

- |x| + |y| <= 300

## Examples

```
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] -> [2, 1]

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] -> [2, 1] -> [4, 2] -> [3, 4] -> [5, 5]
```

## Approaches

### 1. BFS with Symmetry Optimization

**Time Complexity:** O(max(|x|, |y|)^2)
**Space Complexity:** O(max(|x|, |y|)^2)

```python
def minKnightMoves(self, x: int, y: int) -> int:
    # Use symmetry - only need to consider first quadrant
    x, y = abs(x), abs(y)

    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]

    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while queue:
        cx, cy, steps = queue.popleft()

        if cx == x and cy == y:
            return steps

        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            # Stay in reasonable bounds (with some buffer for optimal paths)
            if (nx, ny) not in visited and -2 <= nx <= x + 2 and -2 <= ny <= y + 2:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1
```

**Why this works:**
Use BFS to find the shortest path from (0,0) to (x,y). Due to symmetry, we can work in the first quadrant by taking absolute values. Limit the search space to avoid exploring too far from the target. BFS guarantees the minimum number of moves.

## Key Insights

- Use BFS to find shortest path
- 8 possible knight moves
- Track visited positions
- Can optimize with symmetry

## Common Mistakes

- Not using symmetry optimization (searching all four quadrants)
- Unbounded search space causing TLE
- Not handling the edge case where (x,y) = (0,0)

## Related Problems

- Shortest Path in Binary Matrix
- Word Ladder

## Tags

Breadth-First Search
