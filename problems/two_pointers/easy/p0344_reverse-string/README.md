# Problem 344: Reverse String

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/reverse-string/)

## Problem Description

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

## Constraints

- 1 <= s.length <= 10^5
- s[i] is a printable ascii character

## Examples

Example 1:
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

Example 2:
```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Approaches

### 1. Two Pointers (In-place swap)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
```

**Why this works:**
Use two pointers from both ends. Swap characters while moving towards center. This achieves in-place modification with O(1) space.

## Key Insights

- Use two pointers from both ends
- Swap characters while moving towards center
- In-place modification with O(1) space

## Common Mistakes

- Using slicing (creates a new array, not in-place)
- Not handling odd-length strings (not actually a problem, the middle element stays)
- Off-by-one errors with pointer initialization

## Related Problems

- Reverse String II
- Reverse Words in a String

## Tags

Two Pointers, String
