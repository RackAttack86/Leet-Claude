# Problem 57: Insert Interval

**Difficulty:** Medium
**Pattern:** Intervals
**Link:** [LeetCode](https://leetcode.com/problems/insert-interval/)

## Problem Description

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

## Constraints

- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by starti in ascending order
- newInterval.length == 2
- 0 <= start <= end <= 10^5

## Examples

Example 1:
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

Example 2:
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

## Approaches

### 1. Three-way Split: Before, Merge, After

**Time Complexity:** O(n)
**Space Complexity:** O(n) for output

```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    n = len(intervals)

    # Phase 1: Add all intervals that come before newInterval (no overlap)
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Phase 2: Merge all overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Phase 3: Add all remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

**Why this works:**
Three phases:
1. Add all intervals that end before newInterval starts
2. Merge all overlapping intervals with newInterval
3. Add all intervals that start after newInterval ends

## Key Insights

- Add all intervals before newInterval
- Merge overlapping intervals
- Add all intervals after newInterval
- Linear time since already sorted

## Common Mistakes

- Incorrect overlap detection conditions
- Not handling the case when newInterval should be at the beginning or end
- Forgetting to add the merged newInterval to result

## Related Problems

- Merge Intervals
- Meeting Rooms

## Tags

Array
