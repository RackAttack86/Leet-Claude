# Problem 50: Pow(x, n)

**Difficulty:** Medium
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/powx-n/)

## Problem Description

Implement pow(x, n), which calculates `x` raised to the power `n` (i.e., `x^n`).

## Constraints

- `-100.0
- 2^31
- n` is an integer.
- Either `x` is not zero or `n > 0`.
- 10^4

## Examples

Example 1:
```

Input: x = 2.00000, n = 10
Output: 1024.00000

```

Example 2:
```

Input: x = 2.10000, n = 3
Output: 9.26100

```

Example 3:
```

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

```

## Approaches

### 1. Binary Exponentiation (Exponentiation by Squaring)

**Time Complexity:** O(log n) - We halve n at each step
**Space Complexity:** O(1) - Iterative approach uses constant space

```python
def myPow(self, x: float, n: int) -> float:
    if n == 0:
        return 1.0

    # Handle negative exponent
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    current_product = x

    while n > 0:
        # If n is odd, multiply result by current_product
        if n % 2 == 1:
            result *= current_product

        # Square the base and halve the exponent
        current_product *= current_product
        n //= 2

    return result
```

**Why this works:**
Instead of multiplying x by itself n times (O(n)), we use the property:
- x^n = (x^2)^(n/2) when n is even
- x^n = x * (x^2)^((n-1)/2) when n is odd

This allows us to halve the problem size at each step, reducing time complexity from O(n) to O(log n). For negative n, we compute 1 / x^(-n).

## Key Insights

- Use binary exponentiation to reduce from O(n) to O(log n)
- Handle negative exponent by computing 1/x^|n|
- Handle edge case where n = -2^31 (integer overflow when negating)
- When n is odd, multiply result by current x and reduce n by 1
- When n is even, square x and halve n

## Common Mistakes

- Integer overflow when negating n = -2^31
- Forgetting to handle negative exponents
- Using recursion without tail optimization (can cause stack overflow)

## Related Problems

- Sqrt(x) (#69)
- Super Pow (#372)
