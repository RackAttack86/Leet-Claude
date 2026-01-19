# Problem 218: The Skyline Problem

**Difficulty:** Hard
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/the-skyline-problem/)

## Problem Description

A city's **skyline** is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the **skyline** formed by these buildings collectively.

The geometric information of each building is given in the array `buildings` where `buildings[i] = [lefti, righti, heighti]`:

- `lefti` is the x coordinate of the left edge of the `ith` building.
- `righti` is the x coordinate of the right edge of the `ith` building.
- `heighti` is the height of the `ith` building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height `0`.

The **skyline** should be represented as a list of "key points" **sorted by their x-coordinate** in the form `[[x1,y1],[x2,y2],...]`. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate `0` and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

**Note:** There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...,[2 3],[4 5],[7 5],[11 5],[12 7],...]` is not acceptable; the three lines of height 5 should be merged into one in the final output as such: `[...,[2 3],[4 5],[12 7],...]`

## Examples

### Example 1:
```
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
```
**Explanation:**
- Building 1 starts at x=2, height 10
- Building 2 (taller) takes over at x=3, height 15
- At x=7, building 2 ends, building 3 (height 12) becomes visible
- At x=12, building 3 ends, height drops to 0
- Building 4 starts at x=15, height 10
- At x=20, building 4 ends, building 5 (height 8) becomes visible
- At x=24, last building ends, height drops to 0

### Example 2:
```
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
```

## Constraints

- `1 <= buildings.length <= 10^4`
- `0 <= lefti < righti <= 2^31 - 1`
- `1 <= heighti <= 2^31 - 1`
- `buildings` is sorted by `lefti` in non-decreasing order.

## Approaches

### 1. Max Heap with Events

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

```python
# Process building start/end as events
# Use max heap to track active building heights
# Key point occurs when max height changes
```

**Why this works:**
- Create events for building starts (negative height) and ends (positive height)
- Sort events by x-coordinate
- Use max heap to efficiently track tallest active building
- When max height changes, record the key point

### 2. Divide and Conquer

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

**Why this works:**
- Divide buildings into halves recursively
- Solve each half independently
- Merge skylines similar to merge sort

## Key Insights

1. **Event-based thinking**: Convert 2D building rectangles into 1D events (start/end)
2. **Height tracking**: Need efficient way to track maximum height among overlapping buildings
3. **Max heap choice**: Allows O(log n) insertion and O(1) max query
4. **Handle ties carefully**: When multiple events at same x, process starts before ends (to avoid dips)
5. **Lazy deletion**: Python's heapq doesn't support efficient deletion, use lazy removal

## Common Mistakes

1. Not handling buildings that share edges properly
2. Creating duplicate points in output (consecutive same heights)
3. Not handling the case where a building completely overlaps another
4. Forgetting to add the final [x, 0] point

## Related Problems

- 56. Merge Intervals
- 253. Meeting Rooms II
- 759. Employee Free Time

## Tags

- Heap
- Divide and Conquer
- Line Sweep
- Segment Tree
- Binary Indexed Tree
