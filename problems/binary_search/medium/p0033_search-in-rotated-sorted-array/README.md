# Problem 33: Search in Rotated Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Problem Description

There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index. Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not. You must write an algorithm with O(log n) runtime complexity.

### Constraints
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4

### Examples
- Input: nums = [4,5,6,7,0,1,2], target = 0 -> Output: 4
- Input: nums = [4,5,6,7,0,1,2], target = 3 -> Output: -1

## Approaches

### 1. Modified Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

```python
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

**Why this works:**
In a rotated sorted array, at least one half of the array is always sorted. We first determine which half is sorted by comparing nums[left] with nums[mid]. Then we check if the target falls within the sorted half. If yes, we search there; otherwise, we search the other half.

## Key Insights

- One half is always sorted in a rotated sorted array
- Check which half is sorted by comparing nums[left] with nums[mid]
- Determine if target is in the sorted half using range check
- Adjust search range accordingly

## Common Mistakes

- Not correctly identifying which half is sorted
- Off-by-one errors in the range comparisons
- Missing the edge case where nums[left] == nums[mid]

## Related Problems

- Find Minimum in Rotated Sorted Array (#153)
- Search in Rotated Sorted Array II (#81)
- Binary Search (#704)

## Tags

Array, Binary Search
