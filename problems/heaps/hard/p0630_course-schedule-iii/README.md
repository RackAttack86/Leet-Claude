# Problem 630: Course Schedule III

**Difficulty:** Hard
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/course-schedule-iii/)

## Problem Description

There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

## Constraints

- 1 <= courses.length <= 10^4
- 1 <= durationi, lastDayi <= 10^4

## Examples

Example 1:
```
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation:
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
```

Example 2:
```
Input: courses = [[1,2]]
Output: 1
```

## Approaches

### 1. Greedy with Max Heap

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

```python
def scheduleCourse(self, courses: List[List[int]]) -> int:
    # Sort by deadline (lastDay)
    courses.sort(key=lambda x: x[1])

    # Max heap to store durations (use negative for max heap)
    heap = []
    total_time = 0

    for duration, lastDay in courses:
        # Skip courses where duration exceeds deadline
        if duration > lastDay:
            continue

        # Add this course
        heapq.heappush(heap, -duration)
        total_time += duration

        # If total time exceeds deadline, remove the longest course
        if total_time > lastDay:
            longest = -heapq.heappop(heap)
            total_time -= longest

    return len(heap)
```

**Why this works:**
We sort courses by deadline and greedily try to take each course. If adding a course exceeds its deadline, we remove the longest duration course taken so far. This swapping maintains feasibility while maximizing the count.

## Key Insights

1. Sort by end time (deadline)
2. Use max heap to track durations
3. If current course doesn't fit, replace longest
4. Greedy swapping maximizes count

## Common Mistakes

1. Not sorting by deadline first
2. Forgetting to skip courses where duration > deadline
3. Not using max heap (need to remove longest course)

## Related Problems

- 502. IPO
- 207. Course Schedule

## Tags

Array, Greedy, Heap (Priority Queue)
