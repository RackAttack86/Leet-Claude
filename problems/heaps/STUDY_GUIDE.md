    # Heaps Pattern - Study Guide

## Overview
A Heap is a specialized tree-based data structure that satisfies the heap property: in a max heap, parent nodes are greater than children; in a min heap, parent nodes are smaller than children. Heaps are commonly used for priority queues, finding top K elements, and maintaining running medians.

## Heap Fundamentals

### Heap Properties
- **Complete Binary Tree**: All levels filled except possibly the last, filled left to right
- **Min Heap**: parent ≤ children
- **Max Heap**: parent ≥ children
- **Height**: O(log n) for n elements

### Python Heap (heapq)
```python
import heapq

# Min heap (default in Python)
heap = []
heapq.heappush(heap, item)      # O(log n)
min_item = heapq.heappop(heap)  # O(log n)
min_item = heap[0]              # O(1) peek
heapq.heapify(arr)              # O(n) convert list to heap

# Max heap (negate values)
max_heap = []
heapq.heappush(max_heap, -item)
max_item = -heapq.heappop(max_heap)

# Push and pop in one operation
item = heapq.heappushpop(heap, new_item)  # Push then pop
item = heapq.heapreplace(heap, new_item)  # Pop then push

# N largest/smallest
largest = heapq.nlargest(k, iterable, key=None)
smallest = heapq.nsmallest(k, iterable, key=None)
```

## Common Heap Patterns

### 1. Top K Elements

**Kth Largest Element:**
```python
def find_kth_largest(nums, k):
    """Find kth largest element"""
    import heapq

    # Use min heap of size k
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]

# Time: O(n log k), Space: O(k)
# Alternative: Use quickselect for O(n) average time
```

**Top K Frequent Elements:**
```python
def top_k_frequent(nums, k):
    """Find k most frequent elements"""
    from collections import Counter
    import heapq

    count = Counter(nums)

    # Use min heap of size k
    heap = []

    for num, freq in count.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        elif freq > heap[0][0]:
            heapq.heapreplace(heap, (freq, num))

    return [num for freq, num in heap]

# Time: O(n log k), Space: O(n)


def top_k_frequent_bucket(nums, k):
    """Using bucket sort - O(n) time"""
    from collections import Counter

    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for i in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]

# Time: O(n), Space: O(n)
```

**K Closest Points to Origin:**
```python
def k_closest(points, k):
    """Find k closest points to origin"""
    import heapq

    # Use max heap of size k (negate distance)
    heap = []

    for x, y in points:
        dist = -(x*x + y*y)  # Negate for max heap

        if len(heap) < k:
            heapq.heappush(heap, (dist, x, y))
        elif dist > heap[0][0]:
            heapq.heapreplace(heap, (dist, x, y))

    return [[x, y] for dist, x, y in heap]

# Time: O(n log k), Space: O(k)
```

### 2. Merge K Sorted Structures

**Merge K Sorted Lists:**
```python
def merge_k_lists(lists):
    """Merge k sorted linked lists"""
    import heapq

    heap = []

    # Initialize heap with first node from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    dummy = ListNode(0)
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

# Time: O(N log k) where N is total nodes, k is number of lists
# Space: O(k)
```

**Merge K Sorted Arrays:**
```python
def merge_k_arrays(arrays):
    """Merge k sorted arrays"""
    import heapq

    heap = []

    # (value, array_index, element_index)
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    result = []

    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))

    return result

# Time: O(N log k), Space: O(k)
```

### 3. Running Median / Two Heaps

**Find Median from Data Stream:**
```python
class MedianFinder:
    """Maintain running median using two heaps"""
    def __init__(self):
        import heapq
        self.small = []  # Max heap (negated)
        self.large = []  # Min heap

    def add_num(self, num):
        # Add to max heap (small)
        heapq.heappush(self.small, -num)

        # Balance: move largest from small to large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0

# Add: O(log n), Find median: O(1)
```

**Sliding Window Median:**
```python
def median_sliding_window(nums, k):
    """Find median of each sliding window"""
    import heapq
    from collections import defaultdict

    small = []  # Max heap
    large = []  # Min heap
    result = []
    removed = defaultdict(int)

    def balance():
        # Ensure small has k//2 elements, large has k - k//2
        while len(small) > k - k // 2:
            heapq.heappush(large, -heapq.heappop(small))
        while len(large) > k // 2:
            heapq.heappush(small, -heapq.heappop(large))

    def get_median():
        if k % 2:
            return -small[0]
        return (-small[0] + large[0]) / 2.0

    # Initialize first window
    for i in range(k):
        heapq.heappush(small, -nums[i])

    balance()
    result.append(get_median())

    # Process remaining windows
    for i in range(k, len(nums)):
        # Remove outgoing element
        out_num = nums[i - k]
        removed[out_num] += 1

        # Add incoming element
        if out_num <= -small[0]:
            if nums[i] <= -small[0]:
                heapq.heappush(small, -nums[i])
            else:
                heapq.heappush(large, nums[i])
        else:
            if nums[i] >= large[0]:
                heapq.heappush(large, nums[i])
            else:
                heapq.heappush(small, -nums[i])

        # Remove invalid elements from tops
        while small and removed[-small[0]] > 0:
            removed[-small[0]] -= 1
            heapq.heappop(small)

        while large and removed[large[0]] > 0:
            removed[large[0]] -= 1
            heapq.heappop(large)

        balance()
        result.append(get_median())

    return result

# Time: O(n log k), Space: O(k)
```

### 4. Scheduling / Time-Based Problems

**Meeting Rooms II (Minimum Rooms):**
```python
def min_meeting_rooms(intervals):
    """Minimum meeting rooms needed"""
    import heapq

    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    # Min heap of end times
    heap = []

    for interval in intervals:
        # If room available (earliest meeting ended)
        if heap and heap[0] <= interval[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, interval[1])

    return len(heap)

# Time: O(n log n), Space: O(n)
```

**Task Scheduler:**
```python
def least_interval(tasks, n):
    """Minimum intervals with cooldown"""
    from collections import Counter
    import heapq

    count = Counter(tasks)
    heap = [-c for c in count.values()]
    heapq.heapify(heap)

    time = 0
    queue = []  # (count, available_time)

    while heap or queue:
        time += 1

        if heap:
            count = heapq.heappop(heap) + 1
            if count < 0:
                queue.append((count, time + n))

        if queue and queue[0][1] == time:
            heapq.heappush(heap, queue.pop(0)[0])

    return time

# Time: O(n), Space: O(1) - limited by 26 letters
```

### 5. Kth Element Problems

**Kth Smallest Element in Sorted Matrix:**
```python
def kth_smallest(matrix, k):
    """Kth smallest in row and column sorted matrix"""
    import heapq

    n = len(matrix)
    heap = []

    # Initialize with first element of each row
    for r in range(min(k, n)):
        heapq.heappush(heap, (matrix[r][0], r, 0))

    result = 0
    for _ in range(k):
        result, r, c = heapq.heappop(heap)

        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

    return result

# Time: O(k log min(k, n)), Space: O(min(k, n))
```

**K Pairs with Smallest Sums:**
```python
def k_smallest_pairs(nums1, nums2, k):
    """Find k pairs with smallest sums"""
    import heapq

    if not nums1 or not nums2:
        return []

    heap = []
    result = []

    # Initialize with first element of nums1 paired with first of nums2
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])

        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result

# Time: O(k log k), Space: O(k)
```

### 6. Shortest Path with Heap (Dijkstra)

```python
def dijkstra(graph, start):
    """Single source shortest path"""
    import heapq

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    heap = [(0, start)]
    visited = set()

    while heap:
        current_dist, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Time: O((V + E) log V), Space: O(V)
```

### 7. Stream/Online Algorithms

**Kth Largest Element in Stream:**
```python
class KthLargest:
    """Maintain kth largest element in stream"""
    def __init__(self, k, nums):
        import heapq
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]

# Init: O(n log k), Add: O(log k)
```

## Advanced Heap Techniques

### Custom Comparator
```python
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)

# Usage
import heapq
heap = []
heapq.heappush(heap, PrioritizedItem(priority, data))
```

### Lazy Deletion
```python
# Mark elements as deleted, clean up later
deleted = set()

while heap and heap[0] in deleted:
    heapq.heappop(heap)

# Or use counter
from collections import defaultdict
removed_count = defaultdict(int)
```

## Problem-Solving Strategy

1. **Identify Heap Applicability:**
   - Need min/max repeatedly?
   - Top K elements?
   - Merging sorted structures?
   - Maintaining median/percentile?

2. **Choose Heap Type:**
   - Min heap for smallest elements
   - Max heap for largest elements
   - Two heaps for median

3. **Consider Alternatives:**
   - Sorting if one-time operation
   - Bucket sort for limited range
   - Quickselect for kth element (average O(n))

4. **Optimize:**
   - Fixed size heap for top K
   - Lazy deletion for removals
   - Custom comparator for complex objects

## Time and Space Complexity

### Heap Operations:
- **Insert:** O(log n)
- **Extract min/max:** O(log n)
- **Peek:** O(1)
- **Heapify:** O(n)
- **Space:** O(n)

### Common Patterns:
- **Top K:** O(n log k) time, O(k) space
- **Merge K lists:** O(N log k) time, O(k) space
- **Running median:** O(log n) per insertion

## Common Mistakes

1. **Forgetting Python uses min heap by default**
2. **Not handling ties in comparisons**
3. **Inefficient removal operations**
4. **Not considering space constraints for k**
5. **Missing heap property maintenance**

## Practice Tips

1. **Master heapq module**
2. **Practice top K problems**
3. **Understand two heap pattern for median**
4. **Learn when heap better than sorting**
5. **Practice merge k sorted structures**

## Related Patterns

- **Priority Queue:** Implemented with heap
- **Dijkstra:** Uses heap for shortest path
- **Greedy:** Often combined with heap
- **Sorting:** Heap sort uses heap
- **Streaming:** Heap maintains running statistics
