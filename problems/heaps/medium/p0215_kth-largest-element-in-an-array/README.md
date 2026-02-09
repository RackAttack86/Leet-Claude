# Problem 215: Kth Largest Element in an Array

**Difficulty:** Medium
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## Problem Description

Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element. Can you solve it without sorting?

## Constraints

- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Examples

Example 1:
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

Example 2:
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Approaches

### 1. Min Heap of Size K

**Time Complexity:** O(n log k)
**Space Complexity:** O(k)

```python
def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    return heap[0]
```

**Why this works:**
We maintain a min heap of size k containing the k largest elements seen so far. For each new element larger than the heap minimum, we replace the minimum. At the end, the heap top is the kth largest element.

### 2. Quickselect (Alternative)

**Time Complexity:** O(n) average, O(n^2) worst case
**Space Complexity:** O(1)

**Why this works:**
Quickselect partitions the array and recursively searches only the relevant partition, similar to quicksort but only processing one side.

## Key Insights

1. Maintain min heap of k largest elements
2. Heap top is kth largest
3. Quickselect is faster but harder to implement
4. Can also sort in O(n log n)

## Common Mistakes

1. Using max heap instead of min heap (wrong direction)
2. Keeping more than k elements in heap
3. Not heapifying the initial k elements

## Related Problems

- 347. Top K Frequent Elements
- 973. K Closest Points to Origin
- 378. Kth Smallest Element in a Sorted Matrix

## Tags

Array, Heap, Quickselect, Divide and Conquer
