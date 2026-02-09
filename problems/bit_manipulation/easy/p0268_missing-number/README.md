# Problem 268: Missing Number

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/missing-number/)

## Problem Description

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

## Constraints

- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique

## Examples

Example 1:
```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in range [0,3]. 2 is missing.
```

Example 2:
```
Input: nums = [0,1]
Output: 2
```

Example 3:
```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

## Approaches

### 1. XOR (Bit Manipulation)

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    result = n
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```

**Why this works:**
We XOR all indices (0 to n-1) and all values in the array. Since a ^ a = 0, all matching pairs cancel out. We also XOR with n (the length). The only number without a pair is the missing number.

## Key Insights

1. XOR all indices and values together
2. Missing number remains after XOR (no pair to cancel it)
3. Alternative approach: use expected sum - actual sum
4. Sum approach: n*(n+1)/2 - sum(nums)

## Common Mistakes

- Integer overflow when using sum approach (not a problem in Python)
- Forgetting to include n in the XOR

## Related Problems

- Single Number
- Find the Duplicate Number
- First Missing Positive

## Tags

Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
