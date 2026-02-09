# Problem 621: Task Scheduler

**Difficulty:** Medium
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/task-scheduler/)

## Problem Description

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

Return the minimum number of intervals required to complete all tasks.

## Constraints

- 1 <= tasks.length <= 10^4
- tasks[i] is an uppercase English letter
- 0 <= n <= 100

## Examples

Example 1:
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
```

Example 2:
```
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
```

## Approaches

### 1. Greedy with Frequency Calculation

**Time Complexity:** O(n)
**Space Complexity:** O(1) - only 26 letters

```python
def leastInterval(self, tasks: List[str], n: int) -> int:
    from collections import Counter

    # Count frequency of each task
    freq = Counter(tasks)

    # Find maximum frequency
    max_freq = max(freq.values())

    # Count how many tasks have the maximum frequency
    max_count = sum(1 for f in freq.values() if f == max_freq)

    # Formula: (max_freq - 1) * (n + 1) + max_count
    # Creates (max_freq - 1) full cycles of (n + 1) slots
    # Plus the final row with max_count tasks
    result = (max_freq - 1) * (n + 1) + max_count

    # Result can't be less than total number of tasks
    # (when n is small and many different tasks fill all gaps)
    return max(result, len(tasks))
```

**Why this works:**
The most frequent task determines the minimum time. We create (max_freq - 1) full cycles with (n + 1) slots each, then add the final partial cycle with just the max frequency tasks. If there are enough different tasks to fill all gaps, the answer is simply the total number of tasks.

## Key Insights

1. Find max frequency and count of max freq tasks
2. Formula: max((max_freq - 1) * (n + 1) + count, len(tasks))
3. Schedule most frequent task first with gaps
4. Fill gaps with other tasks

## Common Mistakes

1. Not handling the case when tasks fill all gaps (return len(tasks))
2. Using simulation when math formula is simpler
3. Forgetting to count multiple tasks with max frequency

## Related Problems

- 358. Rearrange String k Distance Apart
- 767. Reorganize String

## Tags

Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
