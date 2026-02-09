# Problem 371: Sum of Two Integers

**Difficulty:** Medium
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/sum-of-two-integers/)

## Problem Description

Given two integers a and b, return the sum of the two integers without using the operators + and -.

## Constraints

- -1000 <= a, b <= 1000

## Examples

Example 1:
```
Input: a = 1, b = 2
Output: 3
```

Example 2:
```
Input: a = 2, b = 3
Output: 5
```

## Approaches

### 1. Bit Manipulation (XOR and Carry)

**Time Complexity:** O(1)
**Space Complexity:** O(1)

```python
def getSum(self, a: int, b: int) -> int:
    # 32-bit mask to simulate 32-bit integer
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    # Keep iterating while there's a carry
    while b != 0:
        # Calculate sum without carry (XOR)
        # Calculate carry (AND shifted left)
        # Apply mask to handle Python's infinite precision
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    # If result is negative in 32-bit representation (> MAX_INT),
    # convert it back to Python's negative number representation
    return a if a <= MAX_INT else ~(a ^ MASK)
```

**Why this works:**
- XOR (^) gives the sum without considering carry (like adding without carrying)
- AND (&) followed by left shift gives the carry (positions where both bits are 1)
- We repeat until there's no carry left

In Python, we need to handle negative numbers specially since Python integers have infinite precision. We use a 32-bit mask to simulate 32-bit integer overflow behavior.

## Key Insights

1. XOR gives sum without carry
2. AND gives carry positions
3. Shift carry left and repeat until no carry
4. Python needs special handling for negative numbers due to infinite precision

## Common Mistakes

- Not handling Python's infinite precision integers
- Infinite loops with negative numbers in Python
- Forgetting to convert back to Python's negative representation

## Related Problems

- Add Two Numbers
- Add Binary

## Tags

Math, Bit Manipulation
