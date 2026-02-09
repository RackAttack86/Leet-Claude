# Problem 252: Meeting Rooms

**Difficulty:** Easy
**Pattern:** Intervals
**Link:** [LeetCode](https://leetcode.com/problems/meeting-rooms/)

## Problem Description

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

## Constraints

- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti < endi <= 10^6

## Examples

Example 1:
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
```

Example 2:
```
Input: intervals = [[7,10],[2,4]]
Output: true
```

## Approaches

### 1. Sort and Check Consecutive Overlaps

**Time Complexity:** O(n log n)
**Space Complexity:** O(1)

```python
def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    if not intervals:
        return True

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Check for overlaps
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True
```

**Why this works:**
- Sort intervals by start time so we can compare consecutive meetings
- Check if any consecutive intervals overlap
- Overlap occurs if the current meeting starts before the previous meeting ends (prev.end > curr.start)
- Simple one-pass after sorting to detect any conflicts

## Key Insights

- Sort intervals by start time
- Check if any consecutive intervals overlap
- Overlap if prev.end > curr.start
- Simple one-pass solution after sorting

## Common Mistakes

- Forgetting to sort the intervals first
- Using wrong comparison for overlap detection (should be start < prev_end, not <=)
- Not handling empty input

## Related Problems

- Meeting Rooms II
- Merge Intervals

## Tags

Array, Sorting
