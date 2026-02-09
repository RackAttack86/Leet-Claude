# Problem 648: Replace Words

**Difficulty:** Medium
**Pattern:** Tries
**Link:** [LeetCode](https://leetcode.com/problems/replace-words/)

## Problem Description

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

**Constraints:**
- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 100
- dictionary[i] consists of only lower-case letters
- 1 <= sentence.length <= 10^6
- sentence consists of only lower-case letters and spaces
- The number of words in sentence is in the range [1, 1000]
- The length of each word in sentence is in the range [1, 1000]
- Every two consecutive words in sentence will be separated by exactly one space
- sentence does not have leading or trailing spaces

**Examples:**
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
```

## Approaches

### 1. Trie for Prefix Matching

**Time Complexity:** O(n + m) where n is dictionary size, m is sentence length
**Space Complexity:** O(n)

```python
class TrieNode:
    """Node in the Trie data structure."""
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build Trie from dictionary
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

        def find_root(word: str) -> str:
            """Find the shortest root for a word, or return the word itself."""
            node = root
            for i, char in enumerate(word):
                if char not in node.children:
                    # No matching root found
                    return word
                node = node.children[char]
                if node.is_end:
                    # Found a root - return it (shortest due to order of traversal)
                    return word[:i + 1]
            # Word itself might be a root or no root found
            return word

        # Process each word in the sentence
        words = sentence.split()
        result = [find_root(word) for word in words]
        return ' '.join(result)
```

**Why this works:**
The Trie stores all dictionary roots efficiently. For each word in the sentence, we traverse the Trie character by character. As soon as we encounter a node marked as `is_end`, we've found the shortest matching root (because we traverse from the start of the word). If we reach a character not in the Trie, there's no matching root, so we keep the original word.

## Key Insights

- Build Trie from dictionary roots for efficient prefix matching
- For each word, find the shortest root prefix by traversing until `is_end` is found
- Return early when a root is found (guarantees shortest match)
- Trie enables O(m) lookup where m is word length, much better than comparing against all roots

## Common Mistakes

- Not returning the shortest root (need to check `is_end` during traversal, not after)
- Forgetting to handle words with no matching root
- Not splitting/joining the sentence correctly

## Related Problems

- 208 - Implement Trie
- 211 - Design Add and Search Words Data Structure
- 720 - Longest Word in Dictionary

## Tags

Array, Hash Table, String, Trie
