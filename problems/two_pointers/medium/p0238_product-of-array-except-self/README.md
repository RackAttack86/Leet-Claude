# Problem 238: Product of Array Except Self

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** [LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is guaranteed to fit in a 32-bit integer.

## Examples

Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

```

Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

```

## Approaches

### 1. Prefix and Suffix Products

**Time Complexity:** O(n) - Two passes through the array
**Space Complexity:** O(1) - Output array doesn't count as extra space per problem

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    # First pass: Calculate prefix products
    # answer[i] contains product of all elements to the left of i
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Second pass: Multiply by suffix products
    # suffix contains product of all elements to the right of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```

**Why this works:**
Two-pass approach using prefix and suffix products. First pass computes prefix products (product of all elements to the left). Second pass computes suffix products on-the-fly and multiplies with prefix.

## Key Insights

1. answer[i] = product of all elements left of i * product of all elements right of i
2. First pass: Build prefix products in the result array
3. Second pass: Multiply by suffix products (computed on-the-fly with running product)
4. No division used, handles zeros naturally

## Common Mistakes

- Using division (fails when array contains zeros)
- Not handling the O(1) space requirement properly
- Creating separate prefix and suffix arrays (O(n) extra space)

## Related Problems

- Trapping Rain Water (LeetCode #42)
- Maximum Product Subarray (LeetCode #152)
