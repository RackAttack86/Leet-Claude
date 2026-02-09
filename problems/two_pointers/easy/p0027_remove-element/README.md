# Problem 27: Remove Element

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/remove-element/)

## Problem Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

## Constraints

- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

## Examples

Example 1:
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

Example 2:
```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Approaches

### 1. Two Pointers

**Time Complexity:** O(n) - single pass through array
**Space Complexity:** O(1) - in-place modification

```python
def removeElement(self, nums: List[int], val: int) -> int:
    l = r = 0
    while r < len(nums):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
        r += 1
    return l
```

**Why this works:**
Use two pointers - slow pointer (l) tracks the position for the next non-val element, fast pointer (r) scans through the array. When we find an element not equal to val, copy it to the slow pointer position and advance both. When we find val, only advance the fast pointer.

## Key Insights

- Slow pointer tracks where to place the next valid element
- Fast pointer scans through all elements
- Only copy elements that are not equal to val
- Order of remaining elements doesn't matter

## Common Mistakes

- Forgetting to advance both pointers when copying
- Returning the wrong count
- Modifying the array incorrectly

## Related Problems

- Remove Duplicates from Sorted Array
- Move Zeroes
