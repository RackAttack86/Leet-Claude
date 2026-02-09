# Problem 46: Permutations

**Difficulty:** Medium
**Pattern:** Backtracking
**Link:** [LeetCode](https://leetcode.com/problems/permutations/)

## Problem Description

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

**Constraints:**
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique

**Examples:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

## Approaches

### 1. Backtracking with Remaining Elements

**Time Complexity:** O(n! * n)
**Space Complexity:** O(n)

```python
def permute(self, nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(current: List[int], remaining: List[int]):
        if not remaining:
            result.append(current[:])
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()

    backtrack([], nums)
    return result
```

**Why this works:**

We use backtracking to build permutations by choosing elements from the remaining pool. For each position, we try each remaining element, add it to our current permutation, and recurse with the updated remaining elements. When no elements remain, we've built a complete permutation. This is a classic backtracking problem that demonstrates the core pattern.

## Key Insights

- Use backtracking to generate permutations
- Track remaining elements or use a "used" array
- Add to result when permutation is complete (no remaining elements)
- Classic backtracking problem - master this pattern!
- Alternative: swap elements in-place for O(1) extra space per recursion level

## Common Mistakes

- Not making a copy of current list when adding to result
- Forgetting to backtrack (pop the element)
- Modifying the original nums array without restoration
- Using combinations logic instead of permutations

## Related Problems

- Permutations II (#47) - with duplicates
- Subsets (#78)
- Combinations (#77)
- Next Permutation (#31)

## Tags

Array, Backtracking
