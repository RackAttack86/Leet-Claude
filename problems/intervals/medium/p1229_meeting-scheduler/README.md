# Problem 1229: Meeting Scheduler

**Difficulty:** Medium
**Pattern:** Intervals
**Link:** [LeetCode](https://leetcode.com/problems/meeting-scheduler/)

## Problem Description

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Find the earliest time slot that works for both people with the required duration.

Note: This is a premium problem.

## Constraints

- 1 <= slots1.length, slots2.length <= 1000
- slots1[i].length, slots2[i].length == 2
- slots1[i][0] < slots1[i][1]
- slots2[i][0] < slots2[i][1]
- 0 <= slots1[i][j], slots2[i][j], duration <= 10^9

## Examples

Example 1:
```
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
```

Example 2:
```
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
```

## Approaches

### 1. Two Pointers with Intersection Check

**Time Complexity:** O(m + n)
**Space Complexity:** O(1)

```python
def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    # Sort both lists by start time
    slots1.sort(key=lambda x: x[0])
    slots2.sort(key=lambda x: x[0])

    i, j = 0, 0

    while i < len(slots1) and j < len(slots2):
        # Find the intersection
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])

        # Check if intersection is long enough
        if end - start >= duration:
            return [start, start + duration]

        # Move the pointer with smaller end time
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1

    return []
```

**Why this works:**
- Sort both lists by start time, then use two pointers to find the first intersection with length >= duration
- The intersection of two intervals is [max(start), min(end)]
- Move the pointer with the smaller end time forward

## Key Insights

- Find intersection of intervals
- Check if intersection >= duration
- Move pointer with earlier end time
- Return first valid slot

## Common Mistakes

- Forgetting to sort the input lists
- Wrong pointer advancement logic
- Not checking if intersection length is sufficient

## Related Problems

- Interval List Intersections
- Meeting Rooms II

## Tags

Array, Two Pointers, Sorting
