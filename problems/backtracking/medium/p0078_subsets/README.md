# Problem 78: Subsets

**Difficulty:** Medium
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/subsets/)

## Problem Description

Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

**Constraints:**
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique

**Examples:**

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
```

## Approaches

### 1. Backtracking

**Time Complexity:** O(2^n * n)
**Space Complexity:** O(n) for recursion

```python
def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(start: int, current: List[int]):
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

**Why this works:**

Unlike combinations where we only add when we reach a target size, for subsets we add the current state at every step (including the empty set). We use a start index to ensure we only add elements in one direction, preventing duplicates. Each element has two choices: include or exclude, leading to 2^n total subsets.

## Key Insights

- Each element has two choices: include or exclude
- Backtrack with start index to avoid duplicate subsets
- Add current subset at each step (not just at the end)
- Total of 2^n subsets for n elements
- Can also solve with bit manipulation (each number from 0 to 2^n-1 represents a subset)

## Common Mistakes

- Only adding subsets at leaf nodes (should add at every step)
- Not using start index (generates duplicate subsets)
- Not making a copy when adding to result
- Forgetting the empty subset

## Related Problems

- Subsets II (#90) - with duplicates
- Combinations (#77)
- Combination Sum (#39)

## Tags

Array, Backtracking, Bit Manipulation
