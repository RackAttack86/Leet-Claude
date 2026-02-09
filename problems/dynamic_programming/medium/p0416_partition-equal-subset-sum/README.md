# Problem 416: Partition Equal Subset Sum

**Difficulty:** Medium
**Pattern:** Dynamic Programming
**Link:** [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/)

## Problem Description

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal.

### Constraints

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

### Examples

**Example 1:**
```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**
```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

## Approaches

### 1. Dynamic Programming (0/1 Knapsack)

**Time Complexity:** O(n * sum)
**Space Complexity:** O(sum)

```python
def canPartition(self, nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Iterate backwards to avoid using same number twice
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target]
```

**Why this works:**

This reduces to a subset sum problem: can we find a subset that sums to total/2? If the total sum is odd, it's impossible. Otherwise, we use 0/1 knapsack DP where dp[i] indicates whether we can form sum i. We iterate backwards to ensure each number is used at most once.

## Key Insights

1. Reduce to subset sum problem for target = sum/2
2. If sum is odd, return false immediately
3. dp[i] = can we make sum i
4. dp[i] = dp[i] or dp[i-num] for each num

## Common Mistakes

1. Forgetting to check if total sum is odd (impossible to partition)
2. Iterating forwards instead of backwards (would use same number multiple times)
3. Not initializing dp[0] = True

## Related Problems

- Partition to K Equal Sum Subsets
- Target Sum
- Last Stone Weight II

## Tags

Array, Dynamic Programming
