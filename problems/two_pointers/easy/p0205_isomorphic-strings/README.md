# Problem 205: Isomorphic Strings

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/isomorphic-strings/)

## Problem Description

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Constraints

- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- `s` and `t` consist of any valid ascii character.

## Examples

Example 1:
```
Input: s = "egg", t = "add"
Output: true
Explanation: The strings s and t can be made identical by:
- Mapping 'e' to 'a'.
- Mapping 'g' to 'd'.
```

Example 2:
```
Input: s = "foo", t = "bar"
Output: false
Explanation: The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.
```

Example 3:
```
Input: s = "paper", t = "title"
Output: true
```

## Approaches

### 1. Two Hash Maps for Bidirectional Mapping

**Time Complexity:** O(n) where n is the length of the strings
**Space Complexity:** O(k) where k is the size of the character set

```python
def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for c1, c2 in zip(s, t):
        # Check s -> t mapping
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2

        # Check t -> s mapping
        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1

    return True
```

**Why this works:**
Need bidirectional mapping: s->t AND t->s must be consistent. Use two hash maps to track both directions. If a character in s maps to different chars in t, or vice versa, return False.

## Key Insights

- Need bidirectional mapping: s->t AND t->s must be consistent
- Use two hash maps to track both directions
- If a character in s maps to different chars in t, or vice versa, return False

## Common Mistakes

- Only checking one direction of mapping
- Not handling the case where two different characters map to the same character
- Forgetting to check if strings have the same length

## Related Problems

- Word Pattern
