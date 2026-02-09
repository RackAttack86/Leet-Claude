# Problem 191: Number of 1 Bits

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/number-of-1-bits/)

## Problem Description

Write a function that takes an unsigned integer and returns the number of '1' bits it has
(also known as the Hamming weight).

## Constraints

- The input must be a binary string of length 32

## Examples

Example 1:
```
Input: n = 00000000000000000000000000001011
Output: 3
```

Example 2:
```
Input: n = 00000000000000000000000010000000
Output: 1
```

## Approaches

### 1. Brian Kernighan's Algorithm

**Time Complexity:** O(k) where k is number of 1 bits
**Space Complexity:** O(1)

```python
def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        count += 1
        n &= (n - 1)
    return count
```

**Why this works:**
The expression n & (n-1) clears the rightmost set bit. By counting how many times we can do this before n becomes 0, we get the number of 1 bits.

## Key Insights

1. n & (n-1) removes the rightmost 1 bit
2. Count how many times we can do this
3. Or use built-in bit_count() in Python 3.10+
4. More efficient than checking all 32 bits when there are few 1s

## Common Mistakes

- Using a loop that always runs 32 times (less efficient)
- Not understanding the n & (n-1) trick

## Related Problems

- Reverse Bits
- Power of Two
- Counting Bits

## Tags

Bit Manipulation
