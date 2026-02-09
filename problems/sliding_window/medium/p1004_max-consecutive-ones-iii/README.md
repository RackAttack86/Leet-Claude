# Problem 1004: Max Consecutive Ones III

**Difficulty:** Medium
**Pattern:** Sliding Window
**Link:** [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)

## Problem Description

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

### Constraints

- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
- 0 <= k <= nums.length

### Examples

**Example 1:**
```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

**Example 2:**
```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
```

## Approaches

### 1. Sliding Window

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def longestOnes(self, nums: List[int], k: int) -> int:
    max_length = 0
    zero_count = 0
    left = 0

    for right in range(len(nums)):
        # Add element to window
        if nums[right] == 0:
            zero_count += 1

        # Shrink window while zeros exceed k
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update maximum length
        max_length = max(max_length, right - left + 1)

    return max_length
```

**Why this works:**

We use a sliding window that maintains at most k zeros. The window represents a valid subarray where we can flip all zeros to ones. When we have more than k zeros, we shrink the window from the left until we have at most k zeros again. The size of the window gives us the count of consecutive 1's we can achieve.

## Key Insights

- Track count of zeros in window
- Expand window with right pointer
- Contract window when zeros > k
- Window size gives consecutive 1's after flips

## Common Mistakes

- Not handling the case when k = 0 (can only find natural consecutive 1's)
- Counting 1's instead of 0's
- Updating max_length before shrinking the window

## Related Problems

- Longest Repeating Character Replacement
- Max Consecutive Ones
- Max Consecutive Ones II

## Tags

Array, Binary Search, Sliding Window, Prefix Sum
