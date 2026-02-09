# Problem 461: Hamming Distance

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/hamming-distance/)

## Problem Description

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

## Constraints

- 0 <= x, y <= 2^31 - 1

## Examples

Example 1:
```
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ^   ^
The above arrows point to positions where bits are different.
```

## Approaches

### 1. XOR and Count Bits

**Time Complexity:** O(1)
**Space Complexity:** O(1)

```python
def hammingDistance(self, x: int, y: int) -> int:
    xor = x ^ y
    count = 0
    while xor:
        count += 1
        xor &= (xor - 1)  # Brian Kernighan's algorithm
    return count
```

**Why this works:**
XOR of two numbers gives 1 at positions where bits differ. We then count the number of 1s in the XOR result using Brian Kernighan's algorithm, which clears the rightmost set bit in each iteration.

## Key Insights

1. XOR gives differing bits (1 where bits differ, 0 where same)
2. Count 1s in XOR result to get Hamming distance
3. Use Brian Kernighan's algorithm for efficient bit counting
4. n & (n-1) removes the rightmost set bit

## Common Mistakes

- Not knowing the XOR trick for finding differing bits
- Using inefficient bit counting methods

## Related Problems

- Number of 1 Bits
- Total Hamming Distance

## Tags

Bit Manipulation
