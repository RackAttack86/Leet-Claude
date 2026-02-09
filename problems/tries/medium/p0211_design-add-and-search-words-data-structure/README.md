# Problem 211: Design Add and Search Words Data Structure

**Difficulty:** Medium
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

## Problem Description

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.

- `void addWord(word)` Adds `word` to the data structure, it can be matched later.

- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

## Constraints

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consist of `'.'` or lowercase English letters.
- There will be at most `2` dots in `word` for `search` queries.
- At most `10^4` calls will be made to `addWord` and `search`.

## Examples

Example 1:
```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

## Approaches

### 1. Trie with DFS for Wildcard Matching

**Time Complexity:** O(m) for addWord, O(26^d * m) for search with d dots
**Space Complexity:** O(n * m) for trie storage, O(m) for recursion stack

```python
class TrieNode:
    """A node in the Trie structure."""

    def __init__(self):
        self.children = {}  # Maps character to TrieNode
        self.is_end = False  # Marks end of a word


class WordDictionary:
    def __init__(self):
        """Initialize the WordDictionary with an empty Trie."""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Add a word to the data structure. Time: O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Search for a word, where '.' can match any letter."""
        return self._search_from(word, 0, self.root)

    def _search_from(self, word: str, index: int, node: TrieNode) -> bool:
        """Recursive helper to search from a given node and index."""
        if index == len(word):
            return node.is_end

        char = word[index]

        if char == '.':
            # Wildcard: try all possible children
            for child in node.children.values():
                if self._search_from(word, index + 1, child):
                    return True
            return False
        else:
            # Regular character: follow the specific path
            if char not in node.children:
                return False
            return self._search_from(word, index + 1, node.children[char])
```

**Why this works:**
The approach uses a standard Trie structure for storing words, combined with DFS/recursion to handle the '.' wildcard. When a '.' is encountered, the algorithm explores all possible paths by trying each child node. For regular characters, it follows the specific path. This allows flexible pattern matching while maintaining efficient prefix-based storage.

## Key Insights

1. Trie provides efficient prefix-based storage and retrieval
2. The '.' wildcard requires exploring all possible paths at that position
3. DFS/recursion naturally handles the branching for wildcards
4. With at most 2 dots constraint, worst case is manageable (26^2 = 676 branches)
5. Early termination when path doesn't exist saves time

## Common Mistakes

- Not correctly handling the base case (when index equals word length)
- Forgetting to check `is_end` at the end of the word
- Not exploring all children for the '.' wildcard

## Related Problems

- 208 - Implement Trie
- 212 - Word Search II
- 79 - Word Search
