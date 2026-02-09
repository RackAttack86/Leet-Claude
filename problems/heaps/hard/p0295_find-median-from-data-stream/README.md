# Problem 295: Find Median from Data Stream

**Difficulty:** Hard
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/)

## Problem Description

The median is the middle value in an ordered integer list. Design a data structure that supports adding integers and finding the median.

Implement the MedianFinder class:
- `MedianFinder()` initializes the MedianFinder object.
- `void addNum(int num)` adds the integer num to the data structure.
- `double findMedian()` returns the median of all elements so far.

## Constraints

- -10^5 <= num <= 10^5
- There will be at least one element before calling findMedian
- At most 5 * 10^4 calls will be made to addNum and findMedian

## Examples

```
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
       [[], [1], [2], [], [3], []]
Output: [null, null, null, 1.5, null, 2.0]
Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

## Approaches

### 1. Two Heaps

**Time Complexity:** O(log n) for addNum, O(1) for findMedian
**Space Complexity:** O(n)

```python
class MedianFinder:
    def __init__(self):
        # Max heap for smaller half (use negative values for max heap)
        self.small = []
        # Min heap for larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Add to max heap (small)
        heapq.heappush(self.small, -num)

        # Ensure max of small <= min of large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance heaps - small can have at most 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0
```

**Why this works:**
We split numbers into two halves: smaller half in a max heap, larger half in a min heap. The median is either the max of the smaller half (odd count) or the average of both tops (even count). Balancing ensures the heaps differ by at most 1 in size.

## Key Insights

1. Max heap stores smaller half
2. Min heap stores larger half
3. Keep heaps balanced (size diff <= 1)
4. Median is top of heap(s)

## Common Mistakes

1. Forgetting to negate values for max heap in Python
2. Not balancing heaps after each insertion
3. Wrong median calculation for odd vs even count

## Related Problems

- 480. Sliding Window Median
- 4. Median of Two Sorted Arrays

## Tags

Heap, Design, Two Pointers, Data Stream
