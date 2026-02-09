# Problem 40: Combination Sum II

**Difficulty:** Medium
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/combination-sum-ii/)

## Problem Description

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations.

**Constraints:**
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

**Examples:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
```

## Approaches

### 1. Backtracking with Duplicate Skipping

**Time Complexity:** O(2^n)
**Space Complexity:** O(n)

```python
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()

    def backtrack(start: int, current: List[int], remaining: int):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Skip duplicates at same level
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current.append(candidates[i])
            backtrack(i + 1, current, remaining - candidates[i])
            current.pop()

    backtrack(0, [], target)
    return result
```

**Why this works:**

We sort the array first to bring duplicates together. Then we use backtracking with a key optimization: we skip duplicate values at the same recursion level. The condition `i > start` ensures we only skip duplicates after we've already used the first occurrence. Using `i + 1` ensures each element is used at most once.

## Key Insights

- Sort array first to group duplicates together
- Skip duplicates at same recursion level (`i > start and candidates[i] == candidates[i-1]`)
- Each element used at most once (use `i + 1` not `i`)
- The difference from Combination Sum I is no reuse and handling duplicates

## Common Mistakes

- Forgetting to sort the array first
- Using `i > 0` instead of `i > start` (skips valid duplicate usage across levels)
- Using `i` instead of `i + 1` (allows element reuse)
- Not making a copy of current list when adding to result

## Related Problems

- Combination Sum (#39)
- Subsets II (#90)
- Permutations II (#47)

## Tags

Array, Backtracking
