# Problem 42: Trapping Rain Water

**Difficulty:** Hard
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/trapping-rain-water/)

## Problem Description

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Constraints

- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

## Examples

Example 1:
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

Example 2:
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Approaches

### 1. Two Pointers

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def solve(self, height: List[int]) -> int:
    if len(height) < 3:
        return 0
    l, r = 0, len(height) - 1
    left_max = right_max = 0
    total = 0

    while l<r:
        if height[l] < height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                total += left_max - height[l]
            l += 1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                total += right_max - height[r]
            r -= 1
    return total
```

**Why this works:**
Water trapped at any position equals min(max_left, max_right) - current_height. Using two pointers, we always process the side with the smaller max height because we know the water level is bounded by that side.

## Key Insights

- Water trapped = min(max_left, max_right) - current_height
- Two pointers: move from side with smaller max
- Or precompute max left/right arrays (O(n) space alternative)

## Common Mistakes

- Not handling edge case when array has less than 3 elements
- Confusing which side to process (should process side with smaller max)
- Using O(n) space when O(1) is possible

## Related Problems

- Container With Most Water (LeetCode #11)
- Product of Array Except Self (LeetCode #238)
- Largest Rectangle in Histogram (LeetCode #84)

## Tags

Array, Two Pointers, Dynamic Programming, Stack
