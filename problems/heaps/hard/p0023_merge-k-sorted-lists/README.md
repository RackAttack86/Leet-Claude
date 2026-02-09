# Problem 23: Merge k Sorted Lists

**Difficulty:** Hard
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)

## Problem Description

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Constraints

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order
- The sum of lists[i].length will not exceed 10^4

## Examples

Example 1:
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

Example 2:
```
Input: lists = []
Output: []
```

## Approaches

### 1. Min Heap with K Pointers

**Time Complexity:** O(N log k) where N is total nodes
**Space Complexity:** O(k) for heap

```python
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Filter out empty lists
    if not lists:
        return None

    # Min heap: (node.val, index, node)
    # Index is used as tiebreaker since ListNode isn't comparable
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    # Dummy head to simplify building result list
    dummy = ListNode(0)
    current = dummy

    while heap:
        val, idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        # If this list has more nodes, add next one to heap
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))

    return dummy.next
```

**Why this works:**
We maintain a min heap of size k (one node from each list). We repeatedly pop the minimum, add it to our result, and push the next node from that list. This ensures O(log k) operations per node.

### 2. Divide and Conquer (Alternative)

**Time Complexity:** O(N log k)
**Space Complexity:** O(log k) for recursion

**Why this works:**
Pair up lists and merge each pair. Repeat until one list remains. Similar to merge sort.

## Key Insights

1. Use min heap to track smallest elements
2. Add head of each list to heap
3. Pop min, add next node from that list
4. More efficient than merging pairs

## Common Mistakes

1. Not handling empty lists in input
2. ListNode comparison issues (need tiebreaker index)
3. Forgetting to push next node after popping

## Related Problems

- 21. Merge Two Sorted Lists
- 264. Ugly Number II

## Tags

Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
