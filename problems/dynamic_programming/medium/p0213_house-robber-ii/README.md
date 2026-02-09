# Problem 213: House Robber II

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/house-robber-ii/)

## Problem Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

### Constraints

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

### Examples

**Example 1:**
```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent.
```

**Example 2:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total = 1 + 3 = 4.
```

## Approaches

### 1. Dynamic Programming (House Robber with circle)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def rob_linear(houses: List[int]) -> int:
        prev2, prev1 = 0, 0
        for num in houses:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        return prev1

    # Either exclude first house or exclude last house
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

**Why this works:**

Since houses are arranged in a circle, we cannot rob both the first and last house. We reduce this to two House Robber I problems: one excluding the first house (nums[1:n]) and one excluding the last house (nums[0:n-1]). The answer is the maximum of these two cases.

## Key Insights

1. Cannot rob both first and last house
2. Run House Robber I twice: [0:n-1] and [1:n]
3. Take maximum of both results
4. Reduces to House Robber I problem

## Common Mistakes

1. Not handling the single house case separately
2. Forgetting that the circle constraint means first and last are adjacent
3. Trying to solve with a single pass (doesn't work for circular)

## Related Problems

- House Robber
- House Robber III
- Delete and Earn

## Tags

Array, Dynamic Programming
