# Problem 55: Jump Game

**Difficulty:** Medium
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/jump-game/)

## Problem Description

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.

## Constraints

- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

## Examples

Example 1:
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Example 2:
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

## Approaches

### 1. Greedy Tracking Max Reach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def canJump(self, nums: List[int]) -> bool:
    max_reach = 0
    n = len(nums)

    for i in range(n):
        # If current position is beyond max reach, we can't get here
        if i > max_reach:
            return False

        # Update the farthest position we can reach
        max_reach = max(max_reach, i + nums[i])

        # Early termination if we can already reach the end
        if max_reach >= n - 1:
            return True

    return True
```

**Why this works:**
We track the maximum reachable position as we iterate. If at any point the current index exceeds our maximum reach, we know we cannot reach that position and thus cannot reach the end.

## Key Insights

1. Track maximum reachable position
2. If current index > max reach, return false
3. Update max reach at each step
4. Simple one-pass solution

## Common Mistakes

1. Using BFS/DFS when greedy is simpler
2. Not handling the case where nums[0] = 0 and n > 1
3. Overcomplicating with DP

## Related Problems

- 45. Jump Game II
- 1306. Jump Game III
- 1345. Jump Game IV

## Tags

Array, Dynamic Programming, Greedy
