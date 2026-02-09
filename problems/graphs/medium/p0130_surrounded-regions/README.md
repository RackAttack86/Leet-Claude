# Problem 130: Surrounded Regions

**Difficulty:** Medium
**Pattern:** Graphs
**Link:** [LeetCode](https://leetcode.com/problems/surrounded-regions/)

## Problem Description

You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`, capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.

- Region: To form a region connect every `'O'` cell.

- Surround: The region is surrounded with `'X'` cells if you can connect the region with `'X'` cells and none of the region cells are on the edge of the `board`.

To capture a surrounded region, replace all `'O'`s with `'X'`s in-place within the original board. You do not need to return anything.

## Constraints

- `m == board.length
- n == board[i].length
- board[i][j]` is `'X'` or `'O'`.

## Examples

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]

Output: [["X"]]

## Approaches

### 1. Border DFS/BFS - Mark cells connected to border as safe

**Time Complexity:** O(m * n)
**Space Complexity:** O(m * n)

```python
def solve(self, board: List[List[str]]) -> None:
    """
    Capture all surrounded 'O' regions by converting them to 'X'.
    """
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])

    def dfs(r: int, c: int) -> None:
        """Mark cell and all connected 'O's as safe (using 'S')."""
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
            return
        board[r][c] = 'S'  # Mark as safe
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Step 1: Mark all 'O's connected to border as safe
    # Check first and last row
    for c in range(n):
        if board[0][c] == 'O':
            dfs(0, c)
        if board[m - 1][c] == 'O':
            dfs(m - 1, c)

    # Check first and last column
    for r in range(m):
        if board[r][0] == 'O':
            dfs(r, 0)
        if board[r][n - 1] == 'O':
            dfs(r, n - 1)

    # Step 2: Process all cells
    # - Convert remaining 'O's to 'X' (they were surrounded)
    # - Restore 'S' back to 'O' (they were connected to border)
    for r in range(m):
        for c in range(n):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'
```

**Why this works:**

Instead of finding surrounded regions directly, we flip the problem:
1. Find all 'O's connected to the border (these cannot be captured)
2. Mark them temporarily with a different character
3. All remaining 'O's are surrounded - convert them to 'X'
4. Restore the border-connected cells back to 'O'

## Key Insights

- 'O' cells on the border can never be captured
- Any 'O' connected to a border 'O' is also safe
- Use DFS/BFS from border cells to mark safe regions
- Remaining 'O's after marking are surrounded

## Common Mistakes

- Trying to find surrounded regions directly instead of marking safe regions
- Forgetting to check all four borders
- Not properly restoring the safe cells after marking

## Related Problems

- Number of Islands (200)
- Pacific Atlantic Water Flow (417)
- Flood Fill (733)
