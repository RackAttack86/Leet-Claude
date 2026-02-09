"""
LeetCode Problem #79: Word Search
Difficulty: Medium
Pattern: Backtracking
Link: https://leetcode.com/problems/word-search/

Problem:
--------
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Constraints:
-----------
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters

Examples:
---------
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #79: Word Search

    Approach: DFS Backtracking
    Time Complexity: O(M * N * 4^L) where L is word length
    Space Complexity: O(L)

    Key Insights:
    - DFS from each cell
    - Mark visited cells
    - Backtrack to explore all paths
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[index]:
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))

            # Backtrack
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 79,
    "name": "Word Search",
    "difficulty": "Medium",
    "pattern": "Backtracking",
    "topics": ['Array', 'Backtracking', 'Matrix'],
    "url": "https://leetcode.com/problems/word-search/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Bloomberg'],
    "time_complexity": "O(M * N * 4^L) where L is word length",
    "space_complexity": "O(L)",
}
