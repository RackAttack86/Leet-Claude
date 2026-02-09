# Problem 338: Counting Bits

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/counting-bits/)

## Problem Description

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

## Constraints

- 0 <= n <= 10^5

## Examples

Example 1:
```
Input: n = 2
Output: [0,1,1]
Explanation: 0 --> 0, 1 --> 1, 2 --> 10
```

Example 2:
```
Input: n = 5
Output: [0,1,1,2,1,2]
```

## Approaches

### 1. Dynamic Programming with Bit Manipulation

**Time Complexity:** O(n)
**Space Complexity:** O(1) excluding output

```python
def countBits(self, n: int) -> List[int]:
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    return result
```

**Why this works:**
For any number i, the number of 1 bits equals the number of 1 bits in i/2 (i >> 1) plus 1 if i is odd (i & 1). This is because right-shifting removes the last bit, and we add it back if it was 1.

## Key Insights

1. ans[i] = ans[i >> 1] + (i & 1)
2. Each number's count relates to i/2 (right shift by 1)
3. Alternative formula: ans[i] = ans[i & (i-1)] + 1
4. DP allows O(n) time instead of O(n log n) for counting each separately

## Common Mistakes

- Using a separate function to count bits for each number (less efficient)
- Off-by-one errors in array indexing

## Related Problems

- Number of 1 Bits
- Counting Bits

## Tags

Dynamic Programming, Bit Manipulation
