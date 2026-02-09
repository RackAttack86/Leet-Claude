# Problem 212: Word Search II

**Difficulty:** Hard
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/word-search-ii/)

## Problem Description

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Constraints:**
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters
- All the strings of words are unique

**Examples:**
```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

## Approaches

### 1. Trie + DFS Backtracking

**Time Complexity:** O(M * N * 4^L) where M*N is board size, L is max word length
**Space Complexity:** O(W * L) for trie, where W is number of words

```python
class Solution:
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
```

**Why this works:**
Building a Trie from all words allows efficient prefix matching during DFS. We start DFS from each cell, following the Trie to check if the current path could lead to any word. If the current character isn't in the Trie, we prune that branch early. When we reach a node marked with '$', we've found a complete word. Using the board itself to mark visited cells (temporarily replacing with '#') avoids extra space for a visited set.

## Key Insights

- Build a Trie from all words for efficient prefix matching
- DFS from each cell on the board, guided by the Trie
- Use Trie to prune search early (if prefix not in trie, stop)
- Mark visited cells during DFS to avoid reusing same cell
- Store the complete word at end nodes for easy retrieval
- Use set for results to handle duplicates automatically

## Common Mistakes

- Not marking cells as visited during DFS (allows reusing same cell)
- Forgetting to restore cell after backtracking
- Not pruning early when prefix doesn't exist in Trie
- Using a separate visited matrix instead of modifying board in-place

## Related Problems

- 79 - Word Search
- 208 - Implement Trie
- 211 - Design Add and Search Words Data Structure

## Tags

Array, String, Backtracking, Trie, Matrix
