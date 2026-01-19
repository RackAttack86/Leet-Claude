# Problem 16: 3Sum Closest

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/3sum-closest/)

## Problem Description

Given an integer array `nums` of length n and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

## Approaches

### 1. Sorting + Two Pointers

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

```python
def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Update closest sum if current is closer
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            # Move pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum  # Exact match

    return closest_sum
```

**Why this works:**
- Sorting allows us to use two pointers efficiently
- For each fixed element, we search for the best pair using two pointers
- We track the closest sum seen so far by comparing absolute differences
- If sum < target, we need a larger sum, so move left pointer right
- If sum > target, we need a smaller sum, so move right pointer left
- Early termination when exact match is found

## Key Insights

- Sorting is key to enabling the two-pointer approach
- We need to track the closest sum, not just find exact matches
- The problem guarantees exactly one solution exists
- Similar to 3Sum but we return a single sum value, not all triplets
- No need to handle duplicates since we're only returning one answer

## Common Mistakes

- Forgetting to sort the array first
- Not updating closest_sum correctly (should compare absolute differences)
- Not handling the case where exact match is found
- Using brute force O(n³) instead of optimized O(n²) approach

## Related Problems

- [15. 3Sum](../p0015_3sum/)
- [1. Two Sum](../../easy/p0001_two-sum/)
- [18. 4Sum](https://leetcode.com/problems/4sum/)
- [259. 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/)

## Tags

`Array` `Two Pointers` `Sorting`
