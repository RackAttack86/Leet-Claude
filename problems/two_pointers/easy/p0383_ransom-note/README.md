# Problem 383: Ransom Note

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/ransom-note/)

## Problem Description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

## Constraints

- 1 <= ransomNote.length, magazine.length <= 10^5
- `ransomNote` and `magazine` consist of lowercase English letters.

## Examples

Example 1:
```
Input: ransomNote = "a", magazine = "b"
Output: false
```

Example 2:
```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

Example 3:
```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

## Approaches

### 1. Character Frequency Count

**Time Complexity:** O(m + n) where m and n are lengths of ransomNote and magazine
**Space Complexity:** O(1) - at most 26 lowercase letters

```python
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    magazine_count = Counter(magazine)

    for char in ransomNote:
        if magazine_count[char] <= 0:
            return False
        magazine_count[char] -= 1

    return True
```

**Why this works:**
Count character frequencies in magazine. Check if ransomNote can be constructed from those frequencies. Each magazine letter can only be used once.

## Key Insights

- Count character frequencies in magazine
- Check if ransomNote can be constructed from those frequencies
- Each magazine letter can only be used once

## Common Mistakes

- Not accounting for letter usage (using a letter more than available)
- Using set instead of counter (doesn't track count)
- Checking ransomNote against magazine incorrectly

## Related Problems

- Valid Anagram
- Stickers to Spell Word
