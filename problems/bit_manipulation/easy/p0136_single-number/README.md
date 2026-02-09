# Problem 136: Single Number

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**Link:** [LeetCode](https://leetcode.com/problems/single-number/)

## Problem Description

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one. You must implement a solution with linear runtime complexity
and use only constant extra space.

## Constraints

- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once

## Examples

Example 1:
```
Input: nums = [2,2,1]
Output: 1
```

Example 2:
```
Input: nums = [4,1,2,1,2]
Output: 4
```

## Approaches

### 1. XOR All Elements

**Time Complexity:** O(n)
**Space Complexity:** O(1)

```python
def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result
```

**Why this works:**
XOR has the property that a ^ a = 0 and a ^ 0 = a. When we XOR all elements together, pairs cancel out (become 0), and only the single element remains.

## Key Insights

1. XOR of two equal numbers is 0
2. XOR of 0 and any number is that number
3. XOR all elements to find single one
4. XOR is commutative and associative, so order doesn't matter

## Common Mistakes

- Using a hash set (uses O(n) space)
- Sorting first (uses O(n log n) time)

## Related Problems

- Single Number II
- Single Number III
- Missing Number

## Tags

Array, Bit Manipulation
