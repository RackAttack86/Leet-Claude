# Problem 75: Sort Colors

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/sort-colors/)

## Problem Description

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. You must solve this problem without using the library's sort function.

## Constraints

- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2

## Examples

Example 1:
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

Example 2:
```
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Approaches

### 1. Dutch National Flag (Three Pointers)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def sortColors(self, nums: List[int]) -> None:
    low, mid = 0, 0
    high = len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
```

**Why this works:**
The Dutch National Flag algorithm uses three pointers: low (boundary for 0s), mid (current element), and high (boundary for 2s). We partition the array into three sections: 0s before low, 1s between low and mid, and 2s after high.

## Key Insights

- Use three pointers: low, mid, high
- Swap 0s to front, 2s to back
- One pass solution
- When swapping with high, don't increment mid (need to check the swapped element)

## Common Mistakes

- Incrementing mid after swapping with high (the swapped element needs to be checked)
- Not using the correct boundary conditions (mid <= high, not mid < high)
- Forgetting this is an in-place operation with no return value

## Related Problems

- Sort List (LeetCode #148)
- Wiggle Sort (LeetCode #280)

## Tags

Array, Two Pointers, Sorting
