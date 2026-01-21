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

- `1
- word` and `prefix` consist only of lowercase English letters.
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

### 1. [Approach Name]

**Time Complexity:** O(?)
**Space Complexity:** O(?)

```python
# TODO: Add code snippet
```

**Why this works:**
[TODO: Explain approach]

## Key Insights

[TODO: Add key insights]

## Common Mistakes

[TODO: Add common mistakes]

## Related Problems

[TODO: Add related problems]
