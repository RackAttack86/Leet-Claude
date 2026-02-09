# Problem 53: Maximum Subarray

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/maximum-subarray/)

## Problem Description

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Examples

Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

Example 2:
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

## Approaches

### 1. Kadane's Algorithm (Dynamic Programming)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def maxSubArray(self, nums: List[int]) -> int:
    # Initialize with the first element
    current_sum = nums[0]
    max_sum = nums[0]

    # Iterate through the rest of the array
    for i in range(1, len(nums)):
        # Either extend the previous subarray or start fresh
        current_sum = max(nums[i], current_sum + nums[i])
        # Update the global maximum
        max_sum = max(max_sum, current_sum)

    return max_sum
```

**Why this works:**

Kadane's algorithm uses a single pass to track the maximum sum ending at each position. At each position, we decide whether to extend the previous subarray or start fresh from the current element. The recurrence is: dp[i] = max(nums[i], dp[i-1] + nums[i]). The answer is the maximum value among all dp[i].

## Key Insights

1. If the running sum becomes negative, it's better to start fresh from current element.
2. At each position, we either extend the previous subarray or start a new one.
3. We only need to track the current sum and the global maximum, not the entire dp array.
4. This is Kadane's algorithm - a classic DP optimization.

## Common Mistakes

1. Not handling arrays with all negative numbers correctly
2. Initializing max_sum to 0 instead of the first element
3. Using O(n) space when O(1) is sufficient

## Related Problems

- Maximum Product Subarray
- Maximum Sum Circular Subarray
- Best Time to Buy and Sell Stock
