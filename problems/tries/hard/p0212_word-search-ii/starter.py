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
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



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