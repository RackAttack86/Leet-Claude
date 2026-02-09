# Problem 502: IPO

**Difficulty:** Hard
**Pattern:** Heaps
**Link:** [LeetCode](https://leetcode.com/problems/ipo/)

## Problem Description

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

## Constraints

- 1 <= k <= 10^5
- 0 <= w <= 10^9
- n == profits.length == capital.length
- 1 <= n <= 10^5
- 0 <= profits[i] <= 10^4
- 0 <= capital[i] <= 10^9

## Examples

Example 1:
```
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
```

Example 2:
```
Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
```

## Approaches

### 1. Two Heaps (Min Heap for Capital, Max Heap for Profit)

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

```python
def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    # Pair projects with (capital, profit) and sort by capital
    projects = sorted(zip(capital, profits))

    # Max heap for available projects (use negative profit)
    available = []
    i = 0
    n = len(projects)

    for _ in range(k):
        # Add all affordable projects to the heap
        while i < n and projects[i][0] <= w:
            heapq.heappush(available, -projects[i][1])
            i += 1

        # If no available projects, we can't continue
        if not available:
            break

        # Pick the project with highest profit
        w += -heapq.heappop(available)

    return w
```

**Why this works:**
We sort projects by capital requirement and use a max heap for available (affordable) projects. Each iteration, we add newly affordable projects to the heap and greedily pick the one with highest profit. This maximizes capital gain at each step.

## Key Insights

1. Sort projects by capital requirement
2. Use max heap for available projects
3. Greedily pick highest profit
4. Add newly affordable projects after each pick

## Common Mistakes

1. Not sorting projects by capital first
2. Using min heap instead of max heap for profits
3. Not breaking when no projects are available

## Related Problems

- 630. Course Schedule III
- 253. Meeting Rooms II

## Tags

Array, Greedy, Sorting, Heap (Priority Queue)
