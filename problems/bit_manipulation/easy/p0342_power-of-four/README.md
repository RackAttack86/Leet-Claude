# Problem 342: Power of Four

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/power-of-four/)

## Problem Description

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x.

## Constraints

- -2^31 <= n <= 2^31 - 1

## Examples

Example 1:
```
Input: n = 16
Output: true
```

Example 2:
```
Input: n = 5
Output: false
```

Example 3:
```
Input: n = 1
Output: true
```

## Approaches

### 1. Bit Manipulation

**Time Complexity:** O(1)
**Space Complexity:** O(1)

```python
def isPowerOfFour(self, n: int) -> bool:
    # First check if power of 2, then check if 1 bit is in odd position (0, 2, 4...)
    # 0x55555555 = 01010101010101010101010101010101 in binary
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
```

**Why this works:**
Powers of 4 are powers of 2 with the single set bit at an even position (0, 2, 4, ...). First we check if it's a power of 2 using n & (n-1) == 0. Then we use the mask 0x55555555 (alternating 01 pattern) to verify the bit is at an even position.

## Key Insights

1. Must be power of 2 first (only one bit set)
2. Power of 4 has 1 bit at even position (0, 2, 4, 6, ...)
3. Use mask 0x55555555 to check even positions
4. 0x55555555 = 01010101...01010101 (32 bits)

## Common Mistakes

- Only checking if power of 2 (2 is power of 2 but not power of 4)
- Using loops instead of bit manipulation

## Related Problems

- Power of Two
- Power of Three

## Tags

Math, Bit Manipulation, Recursion
