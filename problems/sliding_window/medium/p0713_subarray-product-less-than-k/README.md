# Problem 713: Subarray Product Less Than K

**Difficulty:** Medium
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/)

## Problem Description

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

### Constraints

- 1 <= nums.length <= 3 * 10^4
- 1 <= nums[i] <= 1000
- 0 <= k <= 10^6

### Examples

**Example 1:**
```
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
```

**Example 2:**
```
Input: nums = [1,2,3], k = 0
Output: 0
```

## Approaches

### 1. Sliding Window

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    count = 0
    product = 1
    left = 0

    for right in range(len(nums)):
        product *= nums[right]

        # Shrink window while product >= k
        while product >= k:
            product //= nums[left]
            left += 1

        # All subarrays ending at right with start in [left, right] are valid
        # Number of such subarrays = right - left + 1
        count += right - left + 1

    return count
```

**Why this works:**

For each position `right`, we find the smallest `left` such that the product of elements in [left, right] is less than k. All subarrays ending at `right` with starting positions from `left` to `right` are valid. The number of such subarrays is `right - left + 1`. We use the sliding window property: since all elements are positive, adding elements increases the product and removing elements decreases it.

## Key Insights

- Expand window while product < k
- Contract window when product >= k
- For window [left, right], adds (right - left + 1) subarrays
- All positive numbers simplify the problem

## Common Mistakes

- Not handling k <= 1 edge case (no valid subarrays possible)
- Miscounting the number of valid subarrays at each position
- Integer overflow (though not an issue with Python)

## Related Problems

- Subarray Sum Equals K
- Minimum Size Subarray Sum

## Tags

Array, Sliding Window
