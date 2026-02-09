# Problem 283: Move Zeroes

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/move-zeroes/)

## Problem Description

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.

## Constraints

- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

## Examples

Example 1:
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

Example 2:
```
Input: nums = [0]
Output: [0]
```

## Approaches

### 1. Two Pointers (in-place)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            continue
        else:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
```

**Why this works:**
Keep a pointer for the next non-zero position. Swap non-zero elements forward. The slow pointer (l) tracks where the next non-zero should go, and the fast pointer (r) scans through the array.

## Key Insights

- Keep pointer for next non-zero position
- Swap non-zero elements forward
- Two passes: move non-zeros, then fill zeros (or single pass with swap)

## Common Mistakes

- Not maintaining relative order of non-zero elements
- Creating a copy of the array instead of in-place modification
- Using extra space

## Related Problems

- Remove Element

## Tags

Array, Two Pointers
