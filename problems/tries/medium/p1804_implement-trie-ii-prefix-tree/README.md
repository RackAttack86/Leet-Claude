# Problem 1804: Implement Trie II (Prefix Tree)

**Difficulty:** Medium
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/implement-trie-ii-(prefix-tree)/)

## Problem Description

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string word into the trie.
- `int countWordsEqualTo(String word)` Returns the number of instances of the string word in the trie.
- `int countWordsStartingWith(String prefix)` Returns the number of strings in the trie that have the string prefix as a prefix.
- `void erase(String word)` Erases the string word from the trie.

**Constraints:**
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters
- At most 3 * 10^4 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase
- It is guaranteed that for any function call to erase, the string word will exist in the trie

**Example:**
```
Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output
[null, null, null, 2, 2, null, 1, 1, null, 0]
```

## Approaches

### 1. Trie with Counters

**Time Complexity:** O(m) for all operations where m is word length
**Space Complexity:** O(n * m) where n is number of words, m is average length

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0      # Count of words ending at this node
        self.prefix_count = 0    # Count of words passing through this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.word_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count

    def erase(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
            node.prefix_count -= 1
        node.word_count -= 1
```

**Why this works:**
This extends the basic Trie with two counters per node: `word_count` tracks how many words end at that node, and `prefix_count` tracks how many words pass through that node. When inserting, we increment `prefix_count` at each node and `word_count` at the final node. When erasing, we decrement both counters along the path. This allows O(m) counting operations without needing to traverse subtrees.

## Key Insights

- Each node has two counters: word_count and prefix_count
- word_count tracks complete words ending at this node
- prefix_count tracks all words that pass through this node
- Insert increments both counters along the path
- Erase decrements both counters (guaranteed word exists)
- No need to actually delete nodes on erase (counters handle it)

## Common Mistakes

- Using only one counter (need separate word and prefix counts)
- Trying to delete nodes on erase (not necessary, counters suffice)
- Forgetting to increment/decrement prefix_count during insert/erase

## Related Problems

- 208 - Implement Trie
- 211 - Design Add and Search Words Data Structure
- 677 - Map Sum Pairs

## Tags

Hash Table, String, Design, Trie
