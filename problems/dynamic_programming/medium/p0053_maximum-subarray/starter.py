"""
LeetCode Problem #53: Maximum Subarray
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/maximum-subarray/

Problem:
--------
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

Constraints:
-----------
- `1
- 10^4

Examples:
---------
Example 1:
```

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

```

Example 2:
```

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

```

Example 3:
```

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #53: Maximum Subarray

    Approach: Kadane's Algorithm (Dynamic Programming)
    - Use a single pass to track the maximum sum ending at each position.
    - At each position, decide whether to extend the previous subarray or start fresh.
    - dp[i] = max(nums[i], dp[i-1] + nums[i])
    - The answer is the maximum value among all dp[i].

    Time Complexity: O(n)
    Space Complexity: O(1) - optimized to use only variables instead of array

    Key Insights:
    1. If the running sum becomes negative, it's better to start fresh from current element.
    2. At each position, we either extend the previous subarray or start a new one.
    3. We only need to track the current sum and the global maximum, not the entire dp array.
    4. This is Kadane's algorithm - a classic DP optimization.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the contiguous subarray with the largest sum using Kadane's algorithm.

        Args:
            nums: List of integers

        Returns:
            Maximum sum of any contiguous subarray
        """
        pass



PROBLEM_METADATA = {
    "number": 53,
    "name": "Maximum Subarray",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Divide and Conquer', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/maximum-subarray/",
    "companies": ["Amazon", "Microsoft", "Google", "Apple", "Facebook", "LinkedIn", "Bloomberg", "Adobe", "Uber", "ByteDance"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}