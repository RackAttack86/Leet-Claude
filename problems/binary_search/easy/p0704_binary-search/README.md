# Problem 704: Binary Search

**Difficulty:** Easy
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/binary-search/)

## Problem Description

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

### Constraints
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique
- nums is sorted in ascending order

### Examples
- Input: nums = [-1,0,3,5,9,12], target = 9 -> Output: 4
- Input: nums = [-1,0,3,5,9,12], target = 2 -> Output: -1

## Approaches

### 1. Standard Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

```python
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Why this works:**
Classic binary search implementation. We maintain a search range [left, right] and repeatedly halve it by comparing the middle element with the target. If the middle element equals the target, we return its index. If it's smaller, we search the right half. If it's larger, we search the left half.

## Key Insights

- Classic binary search implementation
- Compare mid with target
- Adjust left or right pointer accordingly
- Template for all binary search problems

## Common Mistakes

- Off-by-one errors in loop condition (should be left <= right)
- Integer overflow when computing mid (use left + (right - left) // 2)
- Wrong boundary updates (left = mid + 1, right = mid - 1)

## Related Problems

- Search Insert Position (#35)
- First Bad Version (#278)
- Search in Rotated Sorted Array (#33)

## Tags

Array, Binary Search
