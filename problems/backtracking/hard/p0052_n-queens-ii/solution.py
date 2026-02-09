"""
LeetCode Problem #52: N-Queens II
Difficulty: Hard
Pattern: Backtracking
Link: https://leetcode.com/problems/n-queens-ii/

Problem:
--------
The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return the number of distinct solutions to the n-queens puzzle.

Constraints:
-----------
- `1

Examples:
---------
Example 1:
```

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

```

Example 2:
```

Input: n = 1
Output: 1

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #52: N-Queens II

    Approach: Backtracking with Set-based Conflict Detection
    ---------------------------------------------------------
    We place queens row by row, using sets to track which columns and diagonals
    are already under attack. For each row, we try placing a queen in each column
    and check if it conflicts with any previously placed queen. If valid, we
    recurse to the next row. If we successfully place queens in all rows, we've
    found a valid solution.

    The key optimization is using sets to track:
    1. Columns already occupied
    2. Main diagonals (top-left to bottom-right): characterized by (row - col)
    3. Anti-diagonals (top-right to bottom-left): characterized by (row + col)

    Time Complexity: O(N!)
    - In the first row, we have N choices
    - In the second row, we have at most N-1 choices (one column blocked)
    - And so on... giving us approximately N! configurations to explore
    - The actual number is less due to diagonal constraints

    Space Complexity: O(N)
    - Recursion stack depth is N (one call per row)
    - Three sets each store at most N elements

    Key Insights:
    1. Place queens row by row - guarantees no two queens share a row
    2. Use sets for O(1) conflict checking instead of O(N) board scanning
    3. Diagonals can be uniquely identified: (row-col) for main, (row+col) for anti
    4. No need to store the actual board - just count valid configurations
    5. Backtracking means we only explore valid partial solutions
    """

    def totalNQueens(self, n: int) -> int:
        """
        Count the number of distinct solutions to the n-queens puzzle.

        Args:
            n: Size of the chessboard and number of queens to place

        Returns:
            Number of distinct valid configurations
        """
        # Sets to track attacked columns and diagonals
        cols = set()           # Columns under attack
        diag1 = set()          # Main diagonals (row - col)
        diag2 = set()          # Anti-diagonals (row + col)

        def backtrack(row: int) -> int:
            """
            Try to place a queen in the given row and count valid solutions.

            Args:
                row: Current row to place a queen in

            Returns:
                Number of valid solutions from this state
            """
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


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 52,
    "name": "N-Queens II",
    "difficulty": "Hard",
    "pattern": "Backtracking",
    "topics": ['Backtracking'],
    "url": "https://leetcode.com/problems/n-queens-ii/",
    "companies": ["Amazon", "Google", "Microsoft", "Bloomberg", "Facebook", "Apple", "Zenefits"],
    "time_complexity": "O(N!)",
    "space_complexity": "O(N)",
}
