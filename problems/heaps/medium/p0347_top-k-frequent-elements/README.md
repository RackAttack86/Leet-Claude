# Problem 347: Top K Frequent Elements

**Difficulty:** Medium
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem Description

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array]
- It is guaranteed that the answer is unique

## Examples

Example 1:
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

Example 2:
```
Input: nums = [1], k = 1
Output: [1]
```

## Approaches

### 1. Hash Map + Min Heap

**Time Complexity:** O(n log k)
**Space Complexity:** O(n)

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    min_heap = []
    for num, freq in counts.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for freq, num in min_heap]
```

**Why this works:**
We count frequencies with a hash map, then maintain a min heap of size k. We push (frequency, number) pairs and pop when size exceeds k. At the end, the heap contains the k most frequent elements.

### 2. Bucket Sort (Alternative)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

**Why this works:**
Create buckets indexed by frequency. Group numbers by their frequency, then iterate from highest frequency bucket to get top k.

## Key Insights

1. Count frequencies with hash map
2. Use min heap of size k for top k
3. Bucket sort: group by frequency for O(n)
4. Heap approach is more general

## Common Mistakes

1. Using max heap instead of min heap (less efficient)
2. Forgetting to count frequencies first
3. Not handling the tie-breaking correctly

## Related Problems

- 215. Kth Largest Element in an Array
- 692. Top K Frequent Words
- 451. Sort Characters By Frequency

## Tags

Array, Hash Table, Heap, Bucket Sort
