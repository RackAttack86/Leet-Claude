# Problem 918: Maximum Sum Circular Subarray

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/maximum-sum-circular-subarray/)

## Problem Description

Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray of `nums`.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A subarray may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1`, `k2 <= j` with `k1 % n == k2 % n`.

## Constraints

- n == nums.length
- 1 <= n <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4

## Examples

Example 1:
```
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
```

Example 2:
```
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
```

Example 3:
```
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
```

## Approaches

### 1. Kadane's Algorithm with Circular Consideration

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def maxSubarraySumCircular(self, nums: List[int]) -> int:
    total_sum = 0
    max_sum = nums[0]
    current_max = 0
    min_sum = nums[0]
    current_min = 0

    for num in nums:
        # Kadane's for maximum subarray
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)

        # Kadane's for minimum subarray
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)

        # Track total sum
        total_sum += num

    # If all elements are negative, max_sum is the answer
    if max_sum < 0:
        return max_sum

    # Return max of normal max subarray and wrap-around subarray
    return max(max_sum, total_sum - min_sum)
```

**Why this works:**

For a circular array, the maximum subarray is either a normal contiguous subarray (use standard Kadane's) or a "wrap-around" subarray which equals total_sum - minimum_subarray. We calculate both max and min subarrays in one pass. The answer is max(max_subarray, total_sum - min_subarray), with a special case when all elements are negative.

## Key Insights

1. A wrap-around maximum is equivalent to removing a contiguous minimum from the middle.
2. If we find the minimum subarray, the wrap-around sum = total - min_subarray.
3. We need to handle the all-negative case specially (min_subarray would be entire array).
4. We can compute max and min subarrays simultaneously using modified Kadane's.

## Common Mistakes

1. Not handling the all-negative case (would give total_sum - min_sum = 0, which is invalid)
2. Forgetting that wrap-around = total - minimum_subarray
3. Using O(n) space when O(1) is sufficient

## Related Problems

- Maximum Subarray
- Maximum Product Subarray
