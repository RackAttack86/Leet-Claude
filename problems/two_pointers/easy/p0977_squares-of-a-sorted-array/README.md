# Problem 977: Squares of a Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)

## Problem Description

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order

## Examples

Example 1:
```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, [16,1,0,9,100]. After sorting, [0,1,9,16,100]
```

Example 2:
```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

## Approaches

### 1. Two Pointers (from both ends)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def sortedSquares(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    l, r = 0, n - 1
    pos = n - 1

    while l <= r:
        left_sq = nums[l] * nums[l]
        right_sq = nums[r] * nums[r]

        if left_sq > right_sq:
            result[pos] = left_sq
            l += 1
        else:
            result[pos] = right_sq
            r -= 1
        pos -= 1

    return result
```

**Why this works:**
Largest squares come from either end (most negative or most positive). Use two pointers to compare absolute values. Fill result array from right to left with larger values.

## Key Insights

- Largest squares come from either end (most negative or most positive)
- Use two pointers to compare absolute values
- Fill result array from right to left with larger values

## Common Mistakes

- Squaring first then sorting (O(n log n) instead of O(n))
- Not handling negative numbers correctly
- Filling result array in wrong order

## Related Problems

- Merge Sorted Array
- Sort Colors

## Tags

Array, Two Pointers, Sorting
