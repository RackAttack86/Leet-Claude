"""
LeetCode Problem #238: Product of Array Except Self
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/product-of-array-except-self/

Problem:
--------
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

Constraints:
-----------
- `2
- 30
- The input is generated such that `answer[i]` is guaranteed to fit in a 32-bit integer.

Examples:
---------
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
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #238: Product of Array Except Self

    Approach: Two-pass approach using prefix and suffix products. First pass
    computes prefix products (product of all elements to the left). Second
    pass computes suffix products on-the-fly and multiplies with prefix.

    Time Complexity: O(n) - Two passes through the array
    Space Complexity: O(1) - Output array doesn't count as extra space per problem

    Key Insights:
    1. answer[i] = product of all elements left of i * product of all elements right of i
    2. First pass: Build prefix products in the result array
    3. Second pass: Multiply by suffix products (computed on-the-fly with running product)
    4. No division used, handles zeros naturally
    """

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


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 238,
    "name": "Product of Array Except Self",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Prefix Sum'],
    "url": "https://leetcode.com/problems/product-of-array-except-self/",
    "companies": ["Amazon", "Facebook", "Microsoft", "Google", "Apple", "Bloomberg", "Uber", "Adobe"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
