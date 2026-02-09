# Problem 70: Climbing Stairs

**Difficulty:** Easy
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/climbing-stairs/)

## Problem Description

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Constraints

- 1 <= n <= 45

### Examples

**Example 1:**
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Approaches

### 1. Dynamic Programming (Fibonacci pattern)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n

    # Initialize for first two steps
    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2

    # Calculate for steps 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
```

**Why this works:**

This problem follows the Fibonacci pattern. To reach step n, you can come from step n-1 (taking 1 step) or step n-2 (taking 2 steps). Therefore, the number of ways to reach step n is the sum of ways to reach step n-1 and step n-2: `ways(n) = ways(n-1) + ways(n-2)`.

## Key Insights

1. This is actually a Fibonacci sequence problem!
2. To reach step n, you can come from step n-1 (1 step) or n-2 (2 steps)
3. Therefore: ways(n) = ways(n-1) + ways(n-2)
4. Base cases: ways(1) = 1, ways(2) = 2

## Common Mistakes

1. Not handling base cases (n = 1 and n = 2) correctly
2. Using O(n) space when O(1) is possible with two variables
3. Implementing naive recursion without memoization (leads to exponential time)

## Related Problems

- Fibonacci Number
- Min Cost Climbing Stairs
- House Robber

## Tags

Dynamic Programming, Math, Memoization
