"""
LeetCode Problem #918: Maximum Sum Circular Subarray
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/maximum-sum-circular-subarray/

Problem:
--------
Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray of `nums`.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A subarray may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i

Constraints:
-----------
- `n == nums.length
- 3 * 10^4

Examples:
---------
Example 1:
```

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

```

Example 2:
```

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

```

Example 3:
```

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #918: Maximum Sum Circular Subarray

    Approach: Kadane's Algorithm with circular consideration
    - For a circular array, the maximum subarray is either:
      1. A normal contiguous subarray (use standard Kadane's)
      2. A "wrap-around" subarray = total_sum - minimum_subarray
    - Calculate both max subarray and min subarray in one pass.
    - Answer is max(max_subarray, total_sum - min_subarray)
    - Special case: if all elements are negative, return max_subarray.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    1. A wrap-around maximum is equivalent to removing a contiguous minimum from the middle.
    2. If we find the minimum subarray, the wrap-around sum = total - min_subarray.
    3. We need to handle the all-negative case specially (min_subarray would be entire array).
    4. We can compute max and min subarrays simultaneously using modified Kadane's.
    """
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Find maximum sum subarray in a circular array.

        Args:
            nums: Circular integer array

        Returns:
            Maximum sum of any non-empty subarray
        """
        pass



PROBLEM_METADATA = {
    "number": 918,
    "name": "Maximum Sum Circular Subarray",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Divide and Conquer', 'Dynamic Programming', 'Queue', 'Monotonic Queue'],
    "url": "https://leetcode.com/problems/maximum-sum-circular-subarray/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Apple", "Goldman Sachs"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}