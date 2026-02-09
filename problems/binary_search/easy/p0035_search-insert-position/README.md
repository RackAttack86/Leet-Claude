# Problem 35: Search Insert Position

**Difficulty:** Easy
**Pattern:** Binary Search
**Link:** [LeetCode](https://leetcode.com/problems/search-insert-position/)

## Problem Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

### Constraints
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order
- -10^4 <= target <= 10^4

### Examples
- Input: nums = [1,3,5,6], target = 5 -> Output: 2
- Input: nums = [1,3,5,6], target = 2 -> Output: 1
- Input: nums = [1,3,5,6], target = 7 -> Output: 4

## Approaches

### 1. Binary Search

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

**Why this works:**
Standard binary search implementation. When the target is not found, the left pointer indicates the correct insert position because it represents the first index where nums[left] would be greater than the target.

## Key Insights

- Standard binary search
- When not found, left pointer is insert position
- Handle edge cases at boundaries

## Common Mistakes

- Off-by-one errors in loop condition
- Returning wrong pointer when target not found

## Related Problems

- Binary Search (#704)
- First Bad Version (#278)

## Tags

Array, Binary Search
