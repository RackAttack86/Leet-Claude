# Problem 45: Jump Game II

**Difficulty:** Medium
**Pattern:** Greedy
**Link:** [LeetCode](https://leetcode.com/problems/jump-game-ii/)

## Problem Description

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0]. Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where 0 <= j <= nums[i] and i + j < n. Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

## Constraints

- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1]

## Examples

Example 1:
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Example 2:
```
Input: nums = [2,3,0,1,4]
Output: 2
```

## Approaches

### 1. Greedy with Range Tracking

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def jump(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_end = 0  # End of current jump range
    farthest = 0     # Farthest we can reach

    for i in range(n - 1):  # Don't need to jump from last index
        farthest = max(farthest, i + nums[i])

        # When we reach the end of current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest

            # Early termination if we can reach the end
            if current_end >= n - 1:
                break

    return jumps
```

**Why this works:**
This is essentially a BFS-like level order traversal. We track the current jump range and the farthest position we can reach. When we reach the end of the current range, we must make a jump, and the new range extends to the farthest position found.

## Key Insights

1. Track current jump end and farthest reachable position
2. Increment jumps when reaching current end
3. Update farthest as you iterate through each position
4. BFS-like level order traversal thinking

## Common Mistakes

1. Trying to use DP when greedy is more efficient
2. Not handling single element array (return 0)
3. Jumping from the last index (not needed)

## Related Problems

- 55. Jump Game
- 1306. Jump Game III
- 1345. Jump Game IV

## Tags

Array, Dynamic Programming, Greedy
