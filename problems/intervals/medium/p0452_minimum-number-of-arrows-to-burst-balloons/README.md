# Problem 452: Minimum Number of Arrows to Burst Balloons

**Difficulty:** Medium
**Pattern:** Intervals
**Link:** [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## Problem Description

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

## Constraints

- 1 <= points.length <= 10^5
- points[i].length == 2
- -2^31 <= xstart < xend <= 2^31 - 1

## Examples

Example 1:
```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
```

Example 2:
```
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
```

## Approaches

### 1. Greedy: Sort by End

**Time Complexity:** O(n log n)
**Space Complexity:** O(1)

```python
def findMinArrowShots(self, points: List[List[int]]) -> int:
    if not points:
        return 0

    # Sort by end coordinate
    points.sort(key=lambda x: x[1])

    arrows = 1
    arrow_pos = points[0][1]  # Shoot arrow at end of first balloon

    for i in range(1, len(points)):
        # If balloon starts after current arrow position
        if points[i][0] > arrow_pos:
            # Need a new arrow
            arrows += 1
            arrow_pos = points[i][1]  # Shoot at end of this balloon

    return arrows
```

**Why this works:**
- Sort balloons by end coordinate
- Shoot an arrow at the end of the first balloon, then skip all balloons that would be burst by that arrow
- When a balloon starts after the current arrow position, we need a new arrow

## Key Insights

- Sort by end coordinate
- Shoot arrow at end of first balloon
- Skip balloons within range
- Similar to interval scheduling

## Common Mistakes

- Sorting by start instead of end
- Using wrong comparison (should be > not >=)
- Not handling the case when points is empty

## Related Problems

- Non-overlapping Intervals
- Merge Intervals

## Tags

Array, Greedy, Sorting
