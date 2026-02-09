# Problem 90: Subsets II

**Difficulty:** Medium
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/subsets-ii/)

## Problem Description

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

**Constraints:**
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

**Examples:**

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input: nums = [0]
Output: [[],[0]]
```

## Approaches

### 1. Backtracking with Duplicate Handling

**Time Complexity:** O(2^n)
**Space Complexity:** O(n)

```python
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def backtrack(start: int, current: List[int]):
        result.append(current[:])

        for i in range(start, len(nums)):
            # Skip duplicates at same level
            if i > start and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

**Why this works:**

Similar to Subsets I, but we need to handle duplicates. By sorting first, duplicates are adjacent. The key insight is to skip duplicate values at the same recursion level (`i > start`). This ensures we only use each unique value once per position while still allowing the same value to appear multiple times in a subset (from different positions in the sorted array).

## Key Insights

- Sort array first to bring duplicates together
- Skip duplicates at same recursion level (`i > start and nums[i] == nums[i-1]`)
- Include each unique subset once
- Same pattern as Combination Sum II for handling duplicates

## Common Mistakes

- Forgetting to sort the array first
- Using `i > 0` instead of `i > start` (incorrectly skips valid subsets)
- Not making a copy when adding to result
- Using a set to deduplicate (works but less efficient)

## Related Problems

- Subsets (#78) - without duplicates
- Combination Sum II (#40) - same duplicate handling pattern
- Permutations II (#47)

## Tags

Array, Backtracking, Bit Manipulation
