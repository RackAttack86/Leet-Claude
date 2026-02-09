# Problem 1: Two Sum

**Difficulty:** Easy
**Pattern:** Two Pointers / Hash Table
**Link:** [LeetCode](https://leetcode.com/problems/two-sum/)

## Problem Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Constraints

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

## Examples

Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Approaches

### 1. Hash Map (Optimal)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}  # num -> index mapping

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # No solution found (shouldn't happen per constraints)
```

**Why this works:**
Instead of checking all pairs with nested loops (O(n^2)), use a hash map to store complements. For each number, check if its complement (target - num) exists. Trade space for time: O(n) space for O(n) time.

## Key Insights

- Instead of checking all pairs with nested loops (O(n^2)), use a hash map to store complements
- For each number, check if its complement (target - num) exists
- Trade space for time: O(n) space for O(n) time

## Common Mistakes

- Using the same element twice
- Not handling the case where complement equals the current number
- Returning indices in wrong order

## Related Problems

- 3Sum
- 4Sum
- Two Sum II - Input Array Is Sorted

## Tags

Array, Hash Table
