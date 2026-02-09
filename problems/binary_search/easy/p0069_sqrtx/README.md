# Problem 69: Sqrt(x)

**Difficulty:** Easy
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/sqrtx/)

## Problem Description

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

## Constraints

- 0 <= x <= 2^31 - 1

## Examples

Example 1:
```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

Example 2:
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

## Approaches

### 1. Binary Search

**Time Complexity:** O(log x)
**Space Complexity:** O(1)

```python
def mySqrt(self, x: int) -> int:
    if x < 2:
        return x

    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
```

**Why this works:**
We binary search for the largest integer k such that k * k <= x. The search space is [0, x], and we narrow it down by checking if mid * mid is less than, equal to, or greater than x. Since the function f(k) = k^2 is monotonically increasing, binary search efficiently finds the boundary.

## Key Insights

- We're looking for the floor of the square root, i.e., the largest integer k where k^2 <= x
- Binary search works because the function f(k) = k^2 is monotonically increasing
- When mid^2 <= x, we save mid as a potential answer and search higher
- When mid^2 > x, we search lower
- Handle edge case: sqrt(0) = 0 and sqrt(1) = 1

## Common Mistakes

- Integer overflow when computing mid * mid (use left + (right - left) // 2)
- Not handling edge cases for 0 and 1
- Forgetting to save the result when square < x

## Related Problems

- Valid Perfect Square (#367)
- Pow(x, n) (#50)
