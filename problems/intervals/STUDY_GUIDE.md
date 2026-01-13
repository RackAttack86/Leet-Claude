# Intervals Pattern - Study Guide

## Overview
Interval problems involve ranges with start and end points. These problems commonly appear in scheduling, meeting rooms, overlapping ranges, and merge operations. Understanding how to manipulate and reason about intervals is crucial for many real-world applications.

## Interval Representation

```python
# Common representations
interval = [start, end]  # List
interval = (start, end)  # Tuple

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
```

## Common Interval Patterns

### 1. Merge Overlapping Intervals

**Merge Intervals:**
```python
def merge(intervals):
    """Merge all overlapping intervals"""
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            # Overlapping, merge
            last[1] = max(last[1], current[1])
        else:
            # Non-overlapping, add new interval
            merged.append(current)

    return merged

# Time: O(n log n), Space: O(n)
# Example: [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
```

**Insert Interval:**
```python
def insert(intervals, newInterval):
    """Insert and merge new interval"""
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Time: O(n), Space: O(n)
```

### 2. Interval Intersection

**Interval List Intersections:**
```python
def interval_intersection(firstList, secondList):
    """Find intersection of two interval lists"""
    result = []
    i, j = 0, 0

    while i < len(firstList) and j < len(secondList):
        start1, end1 = firstList[i]
        start2, end2 = secondList[j]

        # Find intersection
        start = max(start1, start2)
        end = min(end1, end2)

        if start <= end:
            result.append([start, end])

        # Move pointer of interval that ends first
        if end1 < end2:
            i += 1
        else:
            j += 1

    return result

# Time: O(m + n), Space: O(min(m, n))
```

### 3. Interval Scheduling

**Non-Overlapping Intervals:**
```python
def erase_overlap_intervals(intervals):
    """Minimum removals to make non-overlapping"""
    if not intervals:
        return 0

    # Sort by end time (greedy choice)
    intervals.sort(key=lambda x: x[1])

    count = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            # Overlapping, need to remove
            count += 1
        else:
            # Update end time
            prev_end = intervals[i][1]

    return count

# Time: O(n log n), Space: O(1)
```

**Meeting Rooms:**
```python
def can_attend_meetings(intervals):
    """Check if person can attend all meetings"""
    if not intervals:
        return True

    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True

# Time: O(n log n), Space: O(1)
```

**Meeting Rooms II:**
```python
def min_meeting_rooms(intervals):
    """Minimum meeting rooms needed"""
    if not intervals:
        return 0

    # Separate start and end times
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    rooms = 0
    max_rooms = 0
    start_ptr = end_ptr = 0

    while start_ptr < len(starts):
        if starts[start_ptr] < ends[end_ptr]:
            # Meeting starts, need a room
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            start_ptr += 1
        else:
            # Meeting ends, free a room
            rooms -= 1
            end_ptr += 1

    return max_rooms

# Time: O(n log n), Space: O(n)


def min_meeting_rooms_heap(intervals):
    """Using min heap to track end times"""
    import heapq

    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    heap = []  # Min heap of end times

    for interval in intervals:
        # If earliest ending meeting ends before current starts
        if heap and heap[0] <= interval[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, interval[1])

    return len(heap)

# Time: O(n log n), Space: O(n)
```

### 4. Interval Coverage

**Minimum Number of Arrows to Burst Balloons:**
```python
def find_min_arrow_shots(points):
    """Minimum arrows to burst all balloons"""
    if not points:
        return 0

    # Sort by end position
    points.sort(key=lambda x: x[1])

    arrows = 1
    current_end = points[0][1]

    for i in range(1, len(points)):
        # If balloon starts after current arrow position
        if points[i][0] > current_end:
            arrows += 1
            current_end = points[i][1]

    return arrows

# Time: O(n log n), Space: O(1)
```

**Video Stitching:**
```python
def video_stitching(clips, time):
    """Minimum clips needed to cover [0, time]"""
    clips.sort()

    count = 0
    current_end = 0
    next_end = 0
    i = 0

    while current_end < time:
        # Find farthest reach from current position
        while i < len(clips) and clips[i][0] <= current_end:
            next_end = max(next_end, clips[i][1])
            i += 1

        if current_end == next_end:
            return -1  # Can't extend further

        current_end = next_end
        count += 1

    return count

# Time: O(n log n), Space: O(1)
```

### 5. Point in Intervals

**My Calendar:**
```python
class MyCalendar:
    """Book events without double booking"""
    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        for s, e in self.bookings:
            if start < e and end > s:  # Overlap condition
                return False

        self.bookings.append((start, end))
        return True

# Time: O(n) per booking, Space: O(n)


class MyCalendarOptimized:
    """Using sorted list for faster search"""
    def __init__(self):
        import bisect
        self.bookings = []

    def book(self, start, end):
        import bisect

        # Find position to insert
        idx = bisect.bisect_left(self.bookings, (start, end))

        # Check overlap with previous
        if idx > 0 and self.bookings[idx-1][1] > start:
            return False

        # Check overlap with next
        if idx < len(self.bookings) and self.bookings[idx][0] < end:
            return False

        bisect.insort(self.bookings, (start, end))
        return True

# Time: O(n) per booking (due to insert), Space: O(n)
```

### 6. Interval Partitioning

**Partition Labels:**
```python
def partition_labels(s):
    """Partition string into maximum parts"""
    # Record last occurrence of each character
    last = {char: i for i, char in enumerate(s)}

    partitions = []
    start = 0
    end = 0

    for i, char in enumerate(s):
        end = max(end, last[char])

        if i == end:
            partitions.append(end - start + 1)
            start = i + 1

    return partitions

# Time: O(n), Space: O(1)
```

### 7. Range Addition

**Range Addition:**
```python
def get_modified_array(length, updates):
    """Apply range updates efficiently"""
    result = [0] * length

    for start, end, inc in updates:
        result[start] += inc
        if end + 1 < length:
            result[end + 1] -= inc

    # Compute prefix sum
    for i in range(1, length):
        result[i] += result[i-1]

    return result

# Time: O(n + k), Space: O(1)
# where k is number of updates
```

**Car Pooling:**
```python
def car_pooling(trips, capacity):
    """Check if can complete all trips"""
    # Sort by start location
    trips.sort(key=lambda x: x[1])

    import heapq
    heap = []  # (end_location, passengers)

    current_passengers = 0

    for passengers, start, end in trips:
        # Drop off passengers who reached destination
        while heap and heap[0][0] <= start:
            current_passengers -= heapq.heappop(heap)[1]

        # Pick up new passengers
        current_passengers += passengers

        if current_passengers > capacity:
            return False

        heapq.heappush(heap, (end, passengers))

    return True

# Time: O(n log n), Space: O(n)
```

### 8. Interval Queries

**Count of Range Sum:**
```python
def count_range_sum(nums, lower, upper):
    """Count ranges with sum in [lower, upper]"""
    def merge_sort(lo, hi):
        if lo >= hi:
            return 0

        mid = (lo + hi) // 2
        count = merge_sort(lo, mid) + merge_sort(mid + 1, hi)

        # Count valid ranges
        j = k = mid + 1
        for i in range(lo, mid + 1):
            while j <= hi and prefix[j] - prefix[i] < lower:
                j += 1
            while k <= hi and prefix[k] - prefix[i] <= upper:
                k += 1
            count += k - j

        # Merge
        prefix[lo:hi+1] = sorted(prefix[lo:hi+1])
        return count

    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    return merge_sort(0, len(prefix) - 1)

# Time: O(n log n), Space: O(n)
```

## Common Techniques

### 1. Sorting Strategy

```python
# Sort by start time
intervals.sort(key=lambda x: x[0])

# Sort by end time (greedy scheduling)
intervals.sort(key=lambda x: x[1])

# Custom sort (e.g., by length)
intervals.sort(key=lambda x: x[1] - x[0])
```

### 2. Overlap Detection

```python
def overlaps(interval1, interval2):
    """Check if two intervals overlap"""
    start1, end1 = interval1
    start2, end2 = interval2

    # Overlap if: start1 < end2 AND start2 < end1
    return start1 < end2 and start2 < end1

# Alternative: No overlap if one ends before other starts
def no_overlap(interval1, interval2):
    return interval1[1] <= interval2[0] or interval2[1] <= interval1[0]
```

### 3. Two Pointer Technique

```python
def merge_intervals_technique(intervals1, intervals2):
    """Process two sorted interval lists"""
    i, j = 0, 0

    while i < len(intervals1) and j < len(intervals2):
        # Process based on start or end times
        if condition:
            i += 1
        else:
            j += 1
```

### 4. Sweep Line Algorithm

```python
def sweep_line(intervals):
    """Process events in order"""
    events = []

    for start, end in intervals:
        events.append((start, 1))   # Start event
        events.append((end, -1))    # End event

    events.sort()

    active = 0
    for time, delta in events:
        active += delta
        # Process based on active count
```

### 5. Difference Array

```python
def difference_array_technique(length, updates):
    """Efficient range updates"""
    diff = [0] * (length + 1)

    for start, end, val in updates:
        diff[start] += val
        diff[end + 1] -= val

    # Reconstruct array
    result = [0] * length
    result[0] = diff[0]
    for i in range(1, length):
        result[i] = result[i-1] + diff[i]

    return result
```

## Problem-Solving Strategy

1. **Identify Interval Type:**
   - Fixed or variable length?
   - Overlapping or non-overlapping?
   - Point queries or range queries?

2. **Choose Sorting Criterion:**
   - Start time for merging
   - End time for scheduling
   - Both for intersection

3. **Select Data Structure:**
   - Array for static intervals
   - Heap for dynamic scheduling
   - Sweep line for events

4. **Handle Edge Cases:**
   - Empty intervals
   - Single interval
   - All overlapping
   - No overlapping
   - Invalid intervals (start > end)

## Time and Space Complexity

### Common Operations:
- **Sort intervals:** O(n log n)
- **Merge intervals:** O(n log n)
- **Check overlap:** O(1)
- **Insert interval:** O(n)
- **Range query:** O(log n) with preprocessing

## Common Mistakes

1. **Wrong overlap condition**
2. **Not sorting when needed**
3. **Forgetting to handle touching intervals**
4. **Off-by-one errors with inclusive/exclusive ends**
5. **Not considering edge cases**

## Practice Tips

1. **Master overlap detection**
2. **Practice different sorting criteria**
3. **Understand greedy scheduling**
4. **Learn sweep line technique**
5. **Draw intervals on timeline**

## Related Patterns

- **Greedy:** Interval scheduling uses greedy approach
- **Sorting:** Almost always need to sort intervals
- **Two Pointers:** Used for interval intersection
- **Heap:** For dynamic interval management
