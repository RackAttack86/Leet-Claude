# Problem 720: Longest Word in Dictionary

**Difficulty:** Medium
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/longest-word-in-dictionary/)

## Problem Description

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word.

**Constraints:**
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 30
- words[i] consists of lowercase English letters

**Examples:**
```
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words. However, "apple" is lexicographically smaller.
```

## Approaches

### 1. Sorting and Set

**Time Complexity:** O(n * m) where n is words count, m is average length
**Space Complexity:** O(n * m)

```python
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Sort by length first, then lexicographically for ties
        words.sort(key=lambda x: (len(x), x))

        # Set to track valid words (words that can be built)
        valid = set([''])  # Empty string is the base case
        result = ''

        for word in words:
            # Check if the prefix (word without last char) is valid
            prefix = word[:-1]
            if prefix in valid:
                valid.add(word)
                # Update result if this word is longer
                if len(word) > len(result):
                    result = word

        return result
```

**Why this works:**
By sorting words by length first, we ensure shorter words are processed before longer ones. A word is valid if its prefix (word minus last character) is already in the valid set. Since we process shorter words first, if a word's prefix is valid, all intermediate prefixes must also be valid. The lexicographic ordering in the sort ensures that for same-length words, the lexicographically smaller one is processed first.

## Key Insights

- Sort words by length (and lexicographically for ties)
- Check if all prefixes exist using a set
- Use set for O(1) lookup
- A word is valid if its prefix (word minus last char) exists in the set
- Empty string serves as the base case for single-character words

## Common Mistakes

- Not handling the case where multiple words have the same length
- Forgetting the empty string as base case
- Not sorting lexicographically for tie-breaking

## Related Problems

- 208 - Implement Trie
- 648 - Replace Words
- 1268 - Search Suggestions System

## Tags

Array, Hash Table, String, Trie, Sorting
