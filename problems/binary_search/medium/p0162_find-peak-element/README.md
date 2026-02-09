# Problem 162: Find Peak Element

**Difficulty:** Medium
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/find-peak-element/)

## Problem Description

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -infinity. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

### Constraints
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i

### Examples
- Input: nums = [1,2,3,1] -> Output: 2 (3 is a peak element)
- Input: nums = [1,2,1,3,5,6,4] -> Output: 5 (6 is a peak element)

## Approaches

### 1. Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

```python
def findPeakElement(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            # Peak is on left side or at mid
            right = mid
        else:
            # Peak is on right side
            left = mid + 1

    return left
```

**Why this works:**
If the middle element is greater than its right neighbor, there must be a peak on the left side (or at mid). If the middle element is less than its right neighbor, there must be a peak on the right side (since the array ends with -infinity). This allows us to use binary search to find any peak in O(log n) time.

## Key Insights

- If mid element is increasing (nums[mid] < nums[mid+1]), peak must be on right
- If mid element is decreasing (nums[mid] > nums[mid+1]), peak must be on left or at mid
- At least one peak always exists (due to -infinity boundaries)
- We only need to find any peak, not all peaks

## Common Mistakes

- Accessing nums[mid + 1] when mid == len(nums) - 1
- Using left <= right instead of left < right
- Trying to find all peaks instead of just one

## Related Problems

- Find Minimum in Rotated Sorted Array (#153)
- Peak Index in a Mountain Array (#852)

## Tags

Array, Binary Search
