# Problem 190: Reverse Bits

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/reverse-bits/)

## Problem Description

Reverse bits of a given 32 bits unsigned integer.

## Constraints

- The input must be a binary string of length 32

## Examples

Example 1:
```
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
```

Example 2:
```
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
```

## Approaches

### 1. Bit Manipulation

**Time Complexity:** O(1) - Always 32 iterations
**Space Complexity:** O(1)

```python
def reverseBits(self, n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

**Why this works:**
We process each bit from right to left. For each bit, we shift the result left to make room, then add the current rightmost bit of n. We then shift n right to process the next bit.

## Key Insights

1. Process each bit from right to left
2. Shift result left and add current bit
3. Use bitwise operations for efficiency
4. Always iterate exactly 32 times for 32-bit integers

## Common Mistakes

- Not iterating exactly 32 times (missing leading zeros)
- Confusing the direction of bit shifting

## Related Problems

- Number of 1 Bits
- Reverse Integer

## Tags

Divide and Conquer, Bit Manipulation
