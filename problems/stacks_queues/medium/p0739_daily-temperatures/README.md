# Problem 739: Daily Temperatures

**Difficulty:** Medium
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/daily-temperatures/)

## Problem Description

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

### Constraints

- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

### Examples

**Example 1:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## Approaches

### 1. Monotonic Stack

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stack of indices

    for i in range(n):
        # While current temp is greater than temp at stack top
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx

        stack.append(i)

    # Remaining indices in stack have no warmer day (stay 0)
    return result
```

**Why this works:**

We use a monotonic decreasing stack that stores indices of days. For each day, we check if the current temperature is warmer than the temperatures at indices in our stack. If so, we've found the next warmer day for those indices - we pop them and calculate the number of days to wait (current index - stored index). The key insight is that we're essentially finding the "next greater element" for each position.

## Key Insights

- Use monotonic decreasing stack
- Store indices in stack
- Calculate days difference when finding warmer
- Classic next greater element variant

## Common Mistakes

- Storing temperatures instead of indices (need indices to calculate days)
- Not initializing result with zeros
- Using wrong comparison (need strictly greater, not greater or equal)

## Related Problems

- Next Greater Element I
- Next Greater Element II

## Tags

Array, Stack, Monotonic Stack
