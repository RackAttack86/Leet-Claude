# Problem 820: Short Encoding of Words

**Difficulty:** Medium
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/short-encoding-of-words/)

## Problem Description

A valid encoding of an array of words is any reference string s and array of indices indices such that:

- words.length == indices.length
- The reference string s ends with the '#' character.
- For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].

Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

**Constraints:**
- 1 <= words.length <= 2000
- 1 <= words[i].length <= 7
- words[i] consists of only lowercase letters

**Examples:**
```
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring starting from indices[0] = 0 to the next '#'
words[1] = "me", the substring starting from indices[1] = 2 to the next '#'
words[2] = "bell", the substring starting from indices[2] = 5 to the next '#'

Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
```

## Approaches

### 1. Reverse Trie (Suffix Tree)

**Time Complexity:** O(n * m) where n is number of words, m is max word length
**Space Complexity:** O(n * m)

```python
class TrieNode:
    """Node in the Trie data structure."""
    def __init__(self):
        self.children = {}


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # Remove duplicates
        words = list(set(words))

        # Build a reverse Trie (inserting words in reverse)
        root = TrieNode()
        # Track the ending node and word for each word
        ending_nodes = {}

        for word in words:
            node = root
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            ending_nodes[node] = word

        # Count only leaf nodes (nodes with no children)
        # These are words that are not suffixes of any other word
        total = 0
        for node, word in ending_nodes.items():
            if not node.children:  # This is a leaf node
                total += len(word) + 1  # +1 for the '#'

        return total
```

**Why this works:**
If word A is a suffix of word B (e.g., "me" is a suffix of "time"), then A can share B's encoding. By building a reverse Trie (inserting words backwards), suffixes will share paths from the root. Words that are suffixes of other words will have their nodes as non-leaf nodes (because longer words extend the path). Only leaf nodes represent words that cannot share their encoding, so we only count those.

## Key Insights

- Build Trie in reverse order (suffix tree approach)
- Words that are suffixes of others share encoding
- Only count leaf nodes (words that are not suffixes of other words)
- Each unique word that needs encoding contributes its length + 1 (for '#')
- Remove duplicates first to avoid counting same word multiple times

## Common Mistakes

- Not reversing words when inserting into Trie
- Counting all words instead of only leaf nodes
- Forgetting to add 1 for the '#' character
- Not removing duplicate words

## Related Problems

- 208 - Implement Trie
- 648 - Replace Words
- 720 - Longest Word in Dictionary

## Tags

Array, Hash Table, String, Trie
