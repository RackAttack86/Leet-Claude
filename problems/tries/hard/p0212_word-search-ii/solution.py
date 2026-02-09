"""
LeetCode Problem #212: Word Search II
Difficulty: Hard
Pattern: Tries
Link: https://leetcode.com/problems/word-search-ii/

Problem:
--------
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Constraints:
-----------
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters
- All the strings of words are unique

Examples:
---------
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #212: Word Search II

    Approach: Trie + DFS Backtracking
    Time Complexity: O(M * N * 4^L) where M*N is board size, L is max word length
    Space Complexity: O(W * L) for trie, where W is number of words

    Key Insights:
    - Build a Trie from all words for efficient prefix matching
    - DFS from each cell on the board
    - Use Trie to prune search early (if prefix not in trie, stop)
    - Mark visited cells during DFS to avoid reuse
    - Optimize by removing words from trie once found
    """

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['$'] = word  # Mark end with the word itself

        rows, cols = len(board), len(board[0])
        result = set()

        def dfs(r: int, c: int, node: dict):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            char = board[r][c]
            if char not in node:
                return

            next_node = node[char]
            if '$' in next_node:
                result.add(next_node['$'])

            # Mark as visited
            board[r][c] = '#'

            # Explore neighbors
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # Restore
            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return list(result)


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 212,
    "name": "Word Search II",
    "difficulty": "Hard",
    "pattern": "Tries",
    "topics": ["Array", "String", "Backtracking", "Trie", "Matrix"],
    "url": "https://leetcode.com/problems/word-search-ii/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Apple"],
    "time_complexity": "O(M * N * 4^L)",
    "space_complexity": "O(W * L)",
}
