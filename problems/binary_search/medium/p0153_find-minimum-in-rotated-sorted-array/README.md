# Problem 153: Find Minimum in Rotated Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Problem Description

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the sorted rotated array nums of unique elements, return the minimum element of this array. You must write an algorithm that runs in O(log n) time.

### Constraints
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique
- nums is sorted and rotated between 1 and n times

### Examples
- Input: nums = [3,4,5,1,2] -> Output: 1
- Input: nums = [4,5,6,7,0,1,2] -> Output: 0

## Approaches

### 1. Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

```python
def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half or at mid
            right = mid

    return nums[left]
```

**Why this works:**
We compare the middle element with the rightmost element. If nums[mid] > nums[right], the rotation point (minimum) must be in the right half, so we search right. Otherwise, the minimum is in the left half or at mid, so we search left including mid. The loop continues until left == right, which is the index of the minimum element.

## Key Insights

- Compare mid with right (not left) to determine which half contains the minimum
- If mid > right, minimum is in right half (rotation point is to the right)
- If mid < right, minimum is in left half or at mid
- Minimum is at the rotation point

## Common Mistakes

- Comparing with left instead of right
- Using left <= right instead of left < right (can cause infinite loop)
- Not including mid in the search range when appropriate

## Related Problems

- Search in Rotated Sorted Array (#33)
- Find Minimum in Rotated Sorted Array II (#154)

## Tags

Array, Binary Search
