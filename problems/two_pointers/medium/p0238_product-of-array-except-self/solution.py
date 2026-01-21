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

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 238,
    "name": "Product of Array Except Self",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Prefix Sum'],
    "url": "https://leetcode.com/problems/product-of-array-except-self/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
