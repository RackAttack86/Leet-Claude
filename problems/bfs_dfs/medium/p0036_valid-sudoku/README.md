# Problem 36: Valid Sudoku

**Difficulty:** Medium
**Pattern:** Bfs Dfs
**Link:** [LeetCode](https://leetcode.com/problems/valid-sudoku/)

## Problem Description

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits `1-9` without repetition.

- Each column must contain the digits `1-9` without repetition.

- Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.

- Only the filled cells need to be validated according to the mentioned rules.

## Constraints

- `board.length == 9
- board[i].length == 9
- board[i][j]` is a digit `1-9` or `'.'`.

## Examples

Example 1:
```

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

```

Example 2:
```

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as

Example 1:
, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

```

## Approaches

### 1. Hash Set Tracking

**Time Complexity:** O(1) - Fixed 9x9 board, effectively O(81) = O(1)
**Space Complexity:** O(1) - Fixed size sets for 9 rows, 9 columns, 9 boxes

```python
def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Initialize sets for each row, column, and 3x3 box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            cell = board[i][j]

            # Skip empty cells
            if cell == '.':
                continue

            # Calculate box index
            box_idx = (i // 3) * 3 + (j // 3)

            # Check if digit already exists in row, column, or box
            if cell in rows[i] or cell in cols[j] or cell in boxes[box_idx]:
                return False

            # Add digit to the corresponding sets
            rows[i].add(cell)
            cols[j].add(cell)
            boxes[box_idx].add(cell)

    return True
```

**Why this works:**
Use hash sets to track seen digits for each row, column, and 3x3 box. Iterate through each cell once and check if the digit already exists in its corresponding row, column, or box set. If duplicate found, return False.

## Key Insights

- Each cell belongs to exactly one row, one column, and one 3x3 box
- Box index can be computed as (row // 3) * 3 + (col // 3)
- Only need to validate filled cells (digits 1-9), skip '.' cells
- Use three sets of hash sets: one for rows, columns, and boxes

## Common Mistakes

- Forgetting to skip empty cells ('.')
- Incorrectly calculating the box index
- Using O(n) space when O(1) is possible with the fixed board size

## Related Problems

- Sudoku Solver
- Valid Sudoku II
