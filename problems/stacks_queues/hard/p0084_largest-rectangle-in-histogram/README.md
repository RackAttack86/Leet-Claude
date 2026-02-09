# Problem 84: Largest Rectangle in Histogram

**Difficulty:** Hard
**Pattern:** Stacks Queues
**Link:** [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Problem Description

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

### Constraints

- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

### Examples

**Example 1:**
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

**Example 2:**
```
Input: heights = [2,4]
Output: 4
```

## Approaches

### 1. Monotonic Stack

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []  # Stack of (index, height)
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))

    # Process remaining bars in stack
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))

    return max_area
```

**Why this works:**

We maintain a monotonic increasing stack of (index, height) pairs. When we encounter a bar shorter than the top of the stack, we pop bars and calculate their areas - they can extend from their start index to the current position. The key insight is that when we pop a bar, we know its maximum width: it can extend from its original position to the current position (where we found a shorter bar). Bars remaining in the stack can extend to the end of the histogram.

## Key Insights

- Use stack to track indices
- Maintain increasing heights in stack
- Calculate area when popping
- Classic monotonic stack problem

## Common Mistakes

- Not processing remaining bars in the stack after the main loop
- Not tracking the correct start index when popping
- Using O(n^2) brute force approach

## Related Problems

- Maximal Rectangle
- Trapping Rain Water

## Tags

Array, Stack, Monotonic Stack
