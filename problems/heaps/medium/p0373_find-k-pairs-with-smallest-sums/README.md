# Problem 373: Find K Pairs with Smallest Sums

**Difficulty:** Medium
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

## Problem Description

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

## Constraints

- 1 <= nums1.length, nums2.length <= 10^5
- -10^9 <= nums1[i], nums2[i] <= 10^9
- nums1 and nums2 both are sorted in non-decreasing order
- 1 <= k <= 10^4
- k <= nums1.length * nums2.length

## Examples

Example 1:
```
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
```

Example 2:
```
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
```

## Approaches

### 1. Min Heap with Careful Exploration

**Time Complexity:** O(k log k)
**Space Complexity:** O(k)

```python
def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    if not nums1 or not nums2:
        return []

    heap = []
    for j in range(min(len(nums2), k)):
        heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))

    res = []
    while heap and len(res) < k:
        _, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])

        if i + 1 < len(nums1):
            heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))

    return res
```

**Why this works:**
We start by pushing pairs (nums1[0], nums2[j]) for all valid j. Then we pop the smallest sum pair and push the "next" pair by incrementing the index in nums1. This ensures we explore pairs in order of their sums.

## Key Insights

1. Start with (0,0) pair or first column
2. Add next candidates to heap
3. For (i,j), consider (i+1,j) and (i,j+1)
4. Use set to avoid duplicates or careful indexing

## Common Mistakes

1. Adding both (i+1,j) and (i,j+1) leading to duplicates
2. Not handling empty input arrays
3. Pushing more than necessary pairs initially

## Related Problems

- 378. Kth Smallest Element in a Sorted Matrix
- 719. Find K-th Smallest Pair Distance

## Tags

Array, Heap (Priority Queue)
