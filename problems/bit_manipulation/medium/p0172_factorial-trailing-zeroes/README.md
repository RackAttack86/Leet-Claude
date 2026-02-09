# Problem 172: Factorial Trailing Zeroes

**Difficulty:** Medium
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/factorial-trailing-zeroes/)

## Problem Description

Given an integer `n`, return the number of trailing zeroes in `n!`.

Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.

## Constraints

- `0 <= n <= 10^4`

## Examples

Example 1:
```
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```

Example 2:
```
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```

Example 3:
```
Input: n = 0
Output: 0
```

## Approaches

### 1. Count Factors of 5

**Time Complexity:** O(log5(n)) - we divide n by increasing powers of 5
**Space Complexity:** O(1) - only a counter variable used

```python
def trailingZeroes(self, n: int) -> int:
    count = 0
    power_of_5 = 5

    # Count how many times 5, 25, 125, ... divide into numbers up to n
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5

    return count
```

**Why this works:**
Trailing zeroes are created by factors of 10 in n!. Since 10 = 2 * 5, we need pairs of factors 2 and 5. In any factorial, factors of 2 are always more abundant than factors of 5. So the count of trailing zeroes equals the count of factors of 5 in n!.

## Key Insights

1. Trailing zeroes come from 10 = 2 * 5, and we always have more 2s than 5s
2. Count factors of 5, not just multiples of 5 (25 has two 5s, 125 has three, etc.)
3. Sum n/5 + n/25 + n/125 + ... until the divisor exceeds n
4. This is equivalent to repeatedly dividing n by 5 and summing the quotients
5. Example: 25! has 25/5 + 25/25 = 5 + 1 = 6 trailing zeroes

## Common Mistakes

- Only counting multiples of 5 (missing extra factors from 25, 125, etc.)
- Computing the actual factorial (causes overflow)
- Not understanding why we count 5s instead of 10s

## Related Problems

- Factorial
- Preimage Size of Factorial Zeroes Function
