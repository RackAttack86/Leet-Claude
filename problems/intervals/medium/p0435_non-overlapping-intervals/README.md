# Problem 435: Non-overlapping Intervals

**Difficulty:** Medium
**Pattern:** Intervals
**Link:** [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)

## Problem Description

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

## Constraints

- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4

## Examples

Example 1:
```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

Example 2:
```
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
```

## Approaches

### 1. Greedy: Sort by End Time

**Time Complexity:** O(n log n)
**Space Complexity:** O(1)

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    # Sort by end time - greedy approach keeps intervals that end earliest
    intervals.sort(key=lambda x: x[1])

    count = 0  # Number of intervals to remove
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start < prev_end:
            # Overlapping - remove this interval (increment count)
            count += 1
        else:
            # Non-overlapping - keep this interval, update prev_end
            prev_end = end

    return count
```

**Why this works:**
- Sort by end time to greedily keep intervals that end earliest
- This maximizes the number of non-overlapping intervals we can keep
- Count overlapping intervals (those that start before previous end)

## Key Insights

- Sort by end time
- Greedily keep intervals with earliest end
- Count intervals that don't overlap
- Answer = total - kept (or just count removed)

## Common Mistakes

- Sorting by start time instead of end time
- Not understanding why sorting by end time is greedy optimal
- Wrong overlap detection

## Related Problems

- Merge Intervals
- Minimum Number of Arrows to Burst Balloons

## Tags

Array, Dynamic Programming, Greedy, Sorting
