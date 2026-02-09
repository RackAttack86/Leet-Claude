# Problem 201: Bitwise AND of Numbers Range

**Difficulty:** Medium
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

## Problem Description

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

## Constraints

- 0 <= left <= right <= 2^31 - 1

## Examples

Example 1:
```
Input: left = 5, right = 7
Output: 4
```

Example 2:
```
Input: left = 0, right = 0
Output: 0
```

Example 3:
```
Input: left = 1, right = 2147483647
Output: 0
```

## Approaches

### 1. Find Common Prefix

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

```python
def rangeBitwiseAnd(self, left: int, right: int) -> int:
    shift = 0
    # Find common prefix by right-shifting until left equals right
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1

    # Left-shift to restore the position of the common prefix
    return left << shift
```

**Why this works:**
When we AND all numbers in a range, any bit position that changes (flips from 0 to 1 or 1 to 0) within the range will result in 0 at that position. Only the common prefix bits that remain the same across all numbers will survive.

We find the common prefix by right-shifting both left and right until they are equal, then left-shift back by the same amount.

## Key Insights

1. AND of range is the common binary prefix
2. Right shift both until they're equal
3. Left shift result to restore position
4. Any bit that changes in the range becomes 0 in the result

## Common Mistakes

- Trying to iterate through all numbers (too slow for large ranges)
- Not understanding that changing bits become 0

## Related Problems

- Number of 1 Bits
- Reverse Bits

## Tags

Bit Manipulation
