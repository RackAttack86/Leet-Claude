# Problem 290: Word Pattern

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/word-pattern/)

## Problem Description

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`. Specifically:

- Each letter in `pattern` maps to exactly one unique word in `s`.
- Each unique word in `s` maps to exactly one letter in `pattern`.
- No two letters map to the same word, and no two words map to the same letter.

## Constraints

- 1 <= pattern.length <= 300
- `pattern` contains only lower-case English letters.
- 1 <= s.length <= 3000
- `s` contains only lowercase English letters and spaces `' '`.
- `s` does not contain any leading or trailing spaces.
- All the words in `s` are separated by a single space.

## Examples

Example 1:
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation: The bijection can be established as:
- 'a' maps to "dog".
- 'b' maps to "cat".
```

Example 2:
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

Example 3:
```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

## Approaches

### 1. Bidirectional Hash Map Mapping

**Time Complexity:** O(n) where n is the length of pattern/words
**Space Complexity:** O(n) for storing the mappings

```python
def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        # Check char -> word mapping
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        # Check word -> char mapping
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True
```

**Why this works:**
Similar to Isomorphic Strings, but with chars and words. Need bidirectional mapping: pattern char <-> word. First check if lengths match, then verify mappings.

## Key Insights

- Similar to Isomorphic Strings, but with chars and words
- Need bidirectional mapping: pattern char <-> word
- First check if lengths match, then verify mappings

## Common Mistakes

- Only checking one direction of mapping
- Not splitting the string by spaces first
- Not checking if the number of pattern chars equals number of words

## Related Problems

- Isomorphic Strings
