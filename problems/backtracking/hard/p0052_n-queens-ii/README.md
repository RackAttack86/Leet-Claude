# Problem 52: N-Queens II

**Difficulty:** Hard
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/n-queens-ii/)

## Problem Description

The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return the number of distinct solutions to the n-queens puzzle.

## Constraints

- 1 <= n <= 9

## Examples

```
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Input: n = 1
Output: 1
```

## Approaches

### 1. Backtracking with Set-based Conflict Detection

**Time Complexity:** O(N!)
**Space Complexity:** O(N)

```python
def totalNQueens(self, n: int) -> int:
    # Sets to track attacked columns and diagonals
    cols = set()           # Columns under attack
    diag1 = set()          # Main diagonals (row - col)
    diag2 = set()          # Anti-diagonals (row + col)

    def backtrack(row: int) -> int:
        # Base case: all queens placed successfully
        if row == n:
            return 1

        count = 0
        for col in range(n):
            # Check if this position is under attack
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place queen: mark column and diagonals as attacked
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # Recurse to next row
            count += backtrack(row + 1)

            # Backtrack: remove queen
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return count

    return backtrack(0)
```

**Why this works:**

We place queens row by row, using sets to track which columns and diagonals are already under attack. For each row, we try placing a queen in each column and check if it conflicts with any previously placed queen. If valid, we recurse to the next row. If we successfully place queens in all rows, we've found a valid solution.

The key optimization is using sets to track:
1. Columns already occupied
2. Main diagonals (top-left to bottom-right): characterized by (row - col)
3. Anti-diagonals (top-right to bottom-left): characterized by (row + col)

## Key Insights

- Place queens row by row - guarantees no two queens share a row
- Use sets for O(1) conflict checking instead of O(N) board scanning
- Diagonals can be uniquely identified: (row-col) for main, (row+col) for anti-diagonal
- No need to store the actual board - just count valid configurations
- Backtracking means we only explore valid partial solutions

## Common Mistakes

- Checking conflicts with O(N) board scanning instead of O(1) sets
- Incorrect diagonal formulas
- Forgetting to backtrack (remove from sets)
- Not handling n=1 edge case

## Related Problems

- N-Queens (#51) - return actual board configurations
- Sudoku Solver (#37)
- Valid Sudoku (#36)
