# Problem 58: Length of Last Word

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/length-of-last-word/)

## Problem Description

Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

## Constraints

- 1 <= s.length <= 10^4
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

## Examples

Example 1:
```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

Example 2:
```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

Example 3:
```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

## Approaches

### 1. Reverse Traversal

**Time Complexity:** O(n) where n is the length of the string
**Space Complexity:** O(1) - only using pointers

```python
def lengthOfLastWord(self, s: str) -> int:
    # Start from the end
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count the last word
    length = 0
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length
```

**Why this works:**
Start from the end and skip trailing spaces. Count characters until we hit a space or reach the beginning. Using strip() and split() works but uses O(n) extra space.

## Key Insights

- Start from the end and skip trailing spaces
- Count characters until we hit a space or reach the beginning
- Using strip() and split() works but uses O(n) extra space

## Common Mistakes

- Not handling trailing spaces
- Not handling strings with only spaces
- Using extra space when O(1) is possible

## Related Problems

- Reverse Words in a String
