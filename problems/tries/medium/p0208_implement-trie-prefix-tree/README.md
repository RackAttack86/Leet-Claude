# Problem 208: Implement Trie (Prefix Tree)

**Difficulty:** Medium
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)

## Problem Description

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.

- `void insert(String word)` Inserts the string `word` into the trie.

- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.

- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

## Constraints

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10^4` calls in total will be made to `insert`, `search`, and `startsWith`.

## Examples

Example 1:
```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

## Approaches

### 1. Tree Structure with Children Map and End Marker

**Time Complexity:** O(m) for all operations, where m is the word/prefix length
**Space Complexity:** O(n * m) where n is number of words, m is average length

```python
class TrieNode:
    """A node in the Trie structure."""

    def __init__(self):
        self.children = {}  # Maps character to TrieNode
        self.is_end = False  # Marks end of a word


class Trie:
    def __init__(self):
        """Initialize the Trie with an empty root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie. Time: O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie. Time: O(m)"""
        node = self._find_node(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        """Returns True if any word starts with the prefix. Time: O(m)"""
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        """Helper to traverse and find the node for a prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

**Why this works:**
Each node has a dictionary mapping characters to child nodes, enabling O(1) character lookup. Each node also has a boolean flag indicating if it marks the end of a word. Insert creates nodes as needed and marks the last as end. Search and startsWith both traverse the path, but search additionally checks the is_end flag. Common prefixes share the same path, which saves space.

## Key Insights

1. Each node represents a character in the path from root
2. Using dictionary for children allows O(1) character lookup
3. is_end flag distinguishes between prefix and complete word
4. Common prefixes share the same path, saving space
5. Search and startsWith differ only in checking is_end flag

## Common Mistakes

- Forgetting to mark `is_end = True` after inserting a word
- Not checking `is_end` in search method (would return True for prefixes)
- Creating a new node even when character already exists in children

## Related Problems

- 211 - Design Add and Search Words Data Structure
- 212 - Word Search II
- 1804 - Implement Trie II (Prefix Tree)
