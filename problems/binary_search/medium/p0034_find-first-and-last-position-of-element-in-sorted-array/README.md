# Problem 34: Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Problem Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints

- `0
- 10^9
- nums` is a non-decreasing array.
- 10^9

## Examples

Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

```

Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

```

Example 3:
```
Input: nums = [], target = 0
Output: [-1,-1]

```

## Approaches

### 1. Two Binary Searches - Find Left and Right Boundaries

**Time Complexity:** O(log n) - Two binary searches, each O(log n)
**Space Complexity:** O(1) - Only using constant extra space

```python
def searchRange(self, nums: List[int], target: int) -> List[int]:
    def findFirst(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1  # Continue searching left for first occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def findLast(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1  # Continue searching right for last occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    return [findFirst(nums, target), findLast(nums, target)]
```

**Why this works:**
We perform two separate binary searches with slight modifications:
1. First search finds the leftmost (first) occurrence of target by continuing to search left when target is found
2. Second search finds the rightmost (last) occurrence of target by continuing to search right when target is found

## Key Insights

- Use binary search twice with slight modifications for left/right boundary
- When finding left boundary: if nums[mid] >= target, search left half
- When finding right boundary: if nums[mid] <= target, search right half
- Handle edge cases: empty array, target not found

## Common Mistakes

- Not continuing to search after finding the target
- Off-by-one errors when updating the search bounds
- Not handling empty array case

## Related Problems

- First Bad Version (#278)
- Search Insert Position (#35)
- Binary Search (#704)
