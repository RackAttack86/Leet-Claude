# Problem 209: Minimum Size Subarray Sum

**Difficulty:** Medium
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Problem Description

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

### Constraints

- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

### Examples

**Example 1:**
```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**Example 2:**
```
Input: target = 4, nums = [1,4,4]
Output: 1
```

**Example 3:**
```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## Approaches

### 1. Sliding Window

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    min_length = float('inf')
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        # Expand window
        current_sum += nums[right]

        # Contract window while sum is >= target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0
```

**Why this works:**

We use a sliding window approach where we expand the window by moving the right pointer and adding elements to our current sum. When the sum becomes greater than or equal to the target, we have a valid subarray. We then try to minimize its length by contracting from the left while the sum is still valid. This works because all elements are positive, so adding more elements only increases the sum and removing elements only decreases it.

## Key Insights

- Expand window by moving right pointer
- Contract window when sum >= target
- Track minimum window size
- Each element visited at most twice (once by each pointer)

## Common Mistakes

- Returning 0 when no valid subarray exists (using infinity as initial value)
- Not continuing to contract after finding a valid subarray
- Using O(n^2) brute force when O(n) is possible

## Related Problems

- Maximum Average Subarray I
- Subarray Product Less Than K

## Tags

Array, Binary Search, Sliding Window, Prefix Sum
