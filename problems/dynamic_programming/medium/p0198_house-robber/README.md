# Problem 198: House Robber

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/house-robber/)

## Problem Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Constraints

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

### Examples

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 2:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## Approaches

### 1. Dynamic Programming

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, 0

    for num in nums:
        current = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = current

    return prev1
```

**Why this works:**

At each house, we have two choices: rob it or skip it. If we rob the current house, we add its value to the maximum from two houses before (prev2 + num). If we skip it, we keep the maximum from the previous house (prev1). The recurrence is: dp[i] = max(dp[i-1], dp[i-2] + nums[i]).

## Key Insights

1. dp[i] = max(dp[i-1], dp[i-2] + nums[i])
2. Either rob current house or skip it
3. Can optimize to O(1) space with two variables
4. Classic DP with non-adjacent constraint

## Common Mistakes

1. Using O(n) space when O(1) is sufficient
2. Not handling edge cases (empty array, single element)
3. Confusing which variable represents what state

## Related Problems

- House Robber II (circular arrangement)
- House Robber III (binary tree)
- Delete and Earn

## Tags

Array, Dynamic Programming
