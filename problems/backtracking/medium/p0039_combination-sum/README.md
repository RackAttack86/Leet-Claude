# Problem 39: Combination Sum

**Difficulty:** Medium
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/combination-sum/)

## Problem Description

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times.

**Constraints:**
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct
- 1 <= target <= 40

**Examples:**

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

## Approaches

### 1. Backtracking with Repetition Allowed

**Time Complexity:** O(n^(T/M)) where T is target, M is minimum candidate
**Space Complexity:** O(T/M) for recursion depth

```python
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(start: int, current: List[int], remaining: int):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # Same index for reuse
            current.pop()

    backtrack(0, [], target)
    return result
```

**Why this works:**

We use backtracking to explore all possible combinations. The key insight is that we can reuse elements, so when we recurse, we pass the same index `i` (not `i+1`). We use a start index to avoid generating duplicate combinations in different orders (e.g., [2,3] and [3,2]). We stop when remaining becomes 0 (found valid combination) or negative (exceeded target).

## Key Insights

- Can reuse same element (pass same index `i` in recursion)
- Use start index to avoid duplicates in different order
- Backtrack when sum exceeds target
- Make a copy of current list when adding to result

## Common Mistakes

- Using `i+1` instead of `i` (prevents element reuse)
- Not using a start index (generates duplicate combinations)
- Not making a copy of the current list when adding to result
- Forgetting to backtrack (pop the element)

## Related Problems

- Combination Sum II (#40)
- Combination Sum III (#216)
- Subsets (#78)

## Tags

Array, Backtracking
