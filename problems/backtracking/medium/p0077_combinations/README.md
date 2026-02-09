# Problem 77: Combinations

**Difficulty:** Medium
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/combinations/)

## Problem Description

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

**Constraints:**
- 1 <= n <= 20
- 1 <= k <= n

**Examples:**

```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Input: n = 1, k = 1
Output: [[1]]
```

## Approaches

### 1. Backtracking

**Time Complexity:** O(C(n,k) * k) = O(n! / (k! * (n-k)!))
**Space Complexity:** O(k)

```python
def combine(self, n: int, k: int) -> List[List[int]]:
    result = []

    def backtrack(start: int, current: List[int]):
        if len(current) == k:
            result.append(current[:])
            return

        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    backtrack(1, [])
    return result
```

**Why this works:**

We use backtracking to choose k elements from 1 to n. The start index ensures we only pick elements in ascending order, which avoids duplicate combinations. When our current combination reaches size k, we add it to the result. The key insight is using `i + 1` as the next start to prevent picking the same or earlier numbers.

## Key Insights

- Choose k elements from 1 to n
- Backtrack with start index to avoid duplicates (ensures ascending order)
- Stop when combination has k elements
- Optimization: can prune when remaining elements < needed elements

## Common Mistakes

- Not using a start index (generates duplicate combinations)
- Using `start` instead of `i + 1` in recursion
- Forgetting to make a copy when adding to result
- Not handling edge case when k > n

## Related Problems

- Subsets (#78)
- Combination Sum (#39)
- Permutations (#46)

## Tags

Backtracking
