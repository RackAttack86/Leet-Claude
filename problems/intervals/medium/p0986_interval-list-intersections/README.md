# Problem 986: Interval List Intersections

**Difficulty:** Medium
**Pattern:** Intervals
**Link:** [LeetCode](https://leetcode.com/problems/interval-list-intersections/)

## Problem Description

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

## Constraints

- 0 <= firstList.length, secondList.length <= 1000
- firstList.length + secondList.length >= 1
- 0 <= starti < endi <= 10^9
- 0 <= startj < endj <= 10^9

## Examples

Example 1:
```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

Example 2:
```
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```

## Approaches

### 1. Two Pointers

**Time Complexity:** O(m + n)
**Space Complexity:** O(1) excluding output

```python
def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    result = []
    i, j = 0, 0

    while i < len(firstList) and j < len(secondList):
        # Find the overlap
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])

        # If there is an intersection
        if start <= end:
            result.append([start, end])

        # Move the pointer with smaller end time
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result
```

**Why this works:**
- Find intersection if max(starts) <= min(ends)
- Move the pointer with the smaller end time forward
- This ensures we don't miss any potential intersections

## Key Insights

- Use two pointers for both lists
- Intersection exists if max(start) <= min(end)
- Move pointer with smaller end time
- Classic merge pattern

## Common Mistakes

- Wrong pointer advancement logic
- Not checking if intersection is valid (start <= end)
- Forgetting to handle empty lists

## Related Problems

- Merge Intervals
- Meeting Scheduler

## Tags

Array, Two Pointers
