# Problem 88: Merge Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/merge-sorted-array/)

## Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

## Constraints

- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

## Examples

Example 1:
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

Example 2:
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

Example 3:
```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

## Approaches

### 1. Three Pointers (from end)

**Time Complexity:** O(m + n)
**Space Complexity:** O(1) - in-place modification

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
```

**Why this works:**
Start from the end of both arrays and fill nums1 from the back. Compare the largest remaining elements from each array and place the larger one at position k. This avoids overwriting elements that haven't been processed yet.

## Key Insights

- Fill from the back to avoid overwriting unprocessed elements
- Three pointers: i for nums1, j for nums2, k for the merged position
- Only need to continue while j >= 0 (nums2 elements need to be placed)
- If i reaches -1 first, remaining nums2 elements fill the front

## Common Mistakes

- Filling from the front (overwrites unprocessed elements)
- Not handling the case when one array is exhausted
- Off-by-one errors with indices

## Related Problems

- Merge Two Sorted Lists
- Sort an Array
