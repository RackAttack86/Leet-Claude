# Problem 231: Power of Two

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/power-of-two/)

## Problem Description

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.

## Constraints

- -2^31 <= n <= 2^31 - 1

## Examples

Example 1:
```
Input: n = 1
Output: true
Explanation: 2^0 = 1
```

Example 2:
```
Input: n = 16
Output: true
Explanation: 2^4 = 16
```

Example 3:
```
Input: n = 3
Output: false
```

## Approaches

### 1. Bit Manipulation Trick

**Time Complexity:** O(1)
**Space Complexity:** O(1)

```python
def isPowerOfTwo(self, n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
```

**Why this works:**
A power of 2 in binary has exactly one bit set (e.g., 8 = 1000). When we subtract 1, all bits after the set bit become 1 and the set bit becomes 0 (e.g., 7 = 0111). The AND of these two numbers is 0 only for powers of 2.

## Key Insights

1. Power of 2 has exactly one bit set in binary representation
2. Use n & (n-1) == 0 to check if only one bit is set
3. Must also check n > 0 (0 and negative numbers are not powers of 2)
4. Example: 8 & 7 = 1000 & 0111 = 0000 = 0

## Common Mistakes

- Forgetting to check n > 0
- Using a loop to divide by 2 (works but less elegant)

## Related Problems

- Power of Three
- Power of Four
- Number of 1 Bits

## Tags

Math, Bit Manipulation, Recursion
