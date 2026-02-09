# Problem 80: Remove Duplicates from Sorted Array II

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

## Examples

Example 1:
```

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

Example 2:
```

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

```

## Approaches

### 1. Two Pointers

**Time Complexity:** O(n) - single pass through array
**Space Complexity:** O(1) - in-place modification

```python
def removeDuplicates(self, nums: List[int]) -> int:
    l = 0
    for r in range(len(nums)):
        if l < 2 or nums[r] != nums[l - 2]:
            nums[l] = nums[r]
            l += 1
    return l
```

**Why this works:**
Two pointers - slow pointer (l) tracks where to place the next valid element. For each element, either we haven't placed 2 yet (l < 2), or the current element differs from the element 2 positions back.

## Key Insights

- Compare with element at l-2 (not l-1) to allow at most 2 duplicates
- First two elements are always valid (l < 2 check)
- Generalizes to k duplicates by comparing with nums[l-k]

## Common Mistakes

- Comparing with wrong index (l-1 instead of l-2)
- Forgetting the l < 2 base case
- Trying to use a counter instead of the simpler index comparison

## Related Problems

- Remove Duplicates from Sorted Array (LeetCode #26)
- Remove Element (LeetCode #27)
