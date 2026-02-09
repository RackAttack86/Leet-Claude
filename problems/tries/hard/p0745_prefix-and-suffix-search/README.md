# Problem 745: Prefix and Suffix Search

**Difficulty:** Hard
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/prefix-and-suffix-search/)

## Problem Description

Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the WordFilter class:

- `WordFilter(string[] words)` Initializes the object with the words in the dictionary.
- `f(string pref, string suff)` Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

**Constraints:**
- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 7
- 1 <= pref.length, suff.length <= 7
- words[i], pref and suff consist of lowercase English letters only
- At most 10^4 calls will be made to the function f

**Example:**
```
Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
```

## Approaches

### 1. Trie with Combined Keys (suffix#word)

**Time Complexity:** O(n * m^2) for constructor, O(p + s) for query
**Space Complexity:** O(n * m^2)

```python
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = {}

        for idx, word in enumerate(words):
            # For each word, insert all suffix#word combinations
            for i in range(len(word) + 1):
                suffix = word[i:]
                key = suffix + '#' + word
                node = self.trie
                for char in key:
                    if char not in node:
                        node[char] = {}
                    node = node[char]
                    node['idx'] = idx  # Store index at every node

    def f(self, pref: str, suff: str) -> int:
        key = suff + '#' + pref
        node = self.trie

        for char in key:
            if char not in node:
                return -1
            node = node[char]

        return node.get('idx', -1)
```

**Why this works:**
The key insight is to combine suffix and prefix search into a single Trie lookup. For each word, we insert all possible `suffix#word` combinations. For example, for "apple", we insert: "#apple", "e#apple", "le#apple", "ple#apple", "pple#apple", "apple#apple". When querying with prefix "a" and suffix "e", we look up "e#a" in the Trie, which matches "e#apple" (continuing down the path covers the prefix). We store the index at every node, and since we process words in order, later words with the same prefix/suffix combination will overwrite, giving us the largest index.

## Key Insights

- Combine suffix and prefix into a single key: `suffix#word`
- Insert all possible suffix combinations for each word
- Query becomes `suffix#prefix` lookup in Trie
- Store index at every node along the path
- Later insertions overwrite earlier ones, automatically giving largest index
- The '#' separator ensures suffix and prefix don't mix

## Common Mistakes

- Not inserting all suffix combinations (including empty suffix)
- Using wrong separator or no separator between suffix and word
- Not storing index at every node (only at leaf)
- Forgetting that query format is `suffix#prefix`

## Related Problems

- 208 - Implement Trie
- 211 - Design Add and Search Words Data Structure
- 212 - Word Search II

## Tags

Array, Hash Table, String, Design, Trie
