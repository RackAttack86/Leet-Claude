# Problem 15: 3Sum

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/3sum/)

## Problem Description

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

## Constraints

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

## Examples

Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

Example 2:
```
Input: nums = [0,1,1]
Output: []
```

## Approaches

### 1. Sort + Two Pointers

**Time Complexity:** O(n^2) - O(n log n) sorting + O(n) outer loop * O(n) two-pointer scan
**Space Complexity:** O(1) - excluding the output array, only constant extra space used

```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1
        target = -nums[i]

        while left < right:
            if nums[left] + nums[right] == target:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1

            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

    return result
```

**Why this works:**
Sort the array, then use two pointers technique. For each element, fix it as the first number and use two pointers to find pairs that sum to the negative of that number. Skip duplicates to avoid duplicate triplets.

## Key Insights

- Sorting enables efficient duplicate skipping and two-pointer technique
- Converting 3Sum to 2Sum problem by fixing one element
- Skip duplicates at all three positions (i, left, right) to avoid duplicate triplets
- Two pointers converge based on whether sum is too small or too large

## Common Mistakes

- Not sorting the array first
- Forgetting to skip duplicates at the outer loop level
- Not skipping duplicates after finding a valid triplet
- Off-by-one errors in duplicate skipping logic

## Related Problems

- Two Sum (LeetCode #1)
- 3Sum Closest (LeetCode #16)
- 4Sum (LeetCode #18)

## Tags

Array, Two Pointers, Sorting
