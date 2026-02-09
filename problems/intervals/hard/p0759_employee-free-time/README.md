# Problem 759: Employee Free Time

**Difficulty:** Hard
**Pattern:** Intervals
**Link:** [LeetCode](https://leetcode.com/problems/employee-free-time/)

## Problem Description

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

## Constraints

- 1 <= schedule.length, schedule[i].length <= 50
- 0 <= schedule[i].start < schedule[i].end <= 10^8

## Examples

Example 1:
```
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common free time intervals would be [-inf, 1], [3, 4], [10, inf].
```

Example 2:
```
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
```

## Approaches

### 1. Merge All Intervals, Find Gaps

**Time Complexity:** O(n log n) where n is total intervals
**Space Complexity:** O(n)

```python
def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
    # Flatten all intervals
    intervals = []
    for employee in schedule:
        for interval in employee:
            intervals.append((interval.start, interval.end))

    # Sort by start time
    intervals.sort()

    # Merge intervals and find gaps
    result = []
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start > prev_end:
            # Found free time
            result.append(Interval(prev_end, start))
        prev_end = max(prev_end, end)

    return result
```

**Why this works:**
- Flatten and sort all intervals from all employees
- Merge overlapping intervals by tracking the maximum end time
- Gaps between merged intervals represent common free time

## Key Insights

- Flatten and sort all intervals
- Merge overlapping intervals
- Gaps between merged intervals are free time
- Similar to merge intervals

## Common Mistakes

- Not flattening the nested list structure properly
- Forgetting to take max of end times when merging
- Not handling the gap detection correctly

## Related Problems

- Merge Intervals
- Meeting Rooms II

## Tags

Array, Sorting, Heap (Priority Queue)
