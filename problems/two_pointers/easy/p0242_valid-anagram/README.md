# Problem 242: Valid Anagram

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/valid-anagram/)

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## Constraints

- 1 <= s.length, t.length <= 5 * 10^4
- `s` and `t` consist of lowercase English letters.

## Examples

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

Example 2:
```
Input: s = "rat", t = "car"
Output: false
```

## Approaches

### 1. Character Frequency Count

**Time Complexity:** O(n) where n is the length of the strings
**Space Complexity:** O(1) - at most 26 lowercase letters

```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return Counter(s) == Counter(t)
```

**Why this works:**
Anagrams have the same character frequencies. Use Counter or a frequency array to count characters. Compare the counts - if equal, they're anagrams.

## Key Insights

- Anagrams have the same character frequencies
- Use Counter or a frequency array to count characters
- Compare the counts - if equal, they're anagrams

## Common Mistakes

- Not checking if lengths are equal first
- Using sorting (O(n log n)) instead of counting (O(n))
- Not handling unicode characters if required

## Related Problems

- Group Anagrams
- Find All Anagrams in a String
