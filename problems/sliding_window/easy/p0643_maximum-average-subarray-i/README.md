# Problem 643: Maximum Average Subarray I

**Difficulty:** Easy
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)

## Problem Description

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

### Constraints

- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

### Examples

**Example 1:**
```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
```

**Example 2:**
```
Input: nums = [5], k = 1
Output: 5.00000
```

## Approaches

### 1. Sliding Window

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def findMaxAverage(self, nums: List[int], k: int) -> float:
    # Calculate initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k
```

**Why this works:**

We use a fixed-size sliding window of size k. First, we calculate the sum of the first k elements. Then, we slide the window by adding the new element entering the window and subtracting the element leaving the window. This gives us O(1) time for each window position instead of O(k) if we recalculated the sum each time. We track the maximum sum and divide by k at the end to get the maximum average.

## Key Insights

- Fixed window size k
- Calculate initial sum of first k elements
- Slide window: add new element, remove old element
- Track maximum sum (no need to calculate average until the end)

## Common Mistakes

- Recalculating the sum for each window position (O(nk) instead of O(n))
- Forgetting to divide by k at the end
- Not handling the initial window correctly

## Related Problems

- Maximum Average Subarray II
- Minimum Size Subarray Sum

## Tags

Array, Sliding Window
