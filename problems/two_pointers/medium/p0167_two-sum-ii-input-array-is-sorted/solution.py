"""
LeetCode Problem #167: Two Sum II - Input Array Is Sorted
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem:
--------
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 1 2 1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Constraints:
-----------
- `2
- 1000
- numbers` is sorted in non-decreasing order.
- 1000
- The tests are generated such that there is exactly one solution.

Examples:
---------
Example 1:
```

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

```

Example 2:
```

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

```

Example 3:
```

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #167: Two Sum II - Input Array Is Sorted

    Approach: Classic two-pointer technique. Use one pointer at the start
    and one at the end. If sum is too large, move right pointer left.
    If sum is too small, move left pointer right. The sorted property
    guarantees we will find the solution.

    Time Complexity: O(n) - Single pass with two pointers
    Space Complexity: O(1) - Only using two pointer variables

    Key Insights:
    1. Sorted array enables two-pointer approach
    2. Moving left pointer increases sum, moving right decreases it
    3. Guaranteed exactly one solution, so we will always find it
    4. Return 1-indexed positions as required by the problem
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Return 1-indexed positions
                return [left + 1, right + 1]
            elif current_sum < target:
                # Need larger sum, move left pointer right
                left += 1
            else:
                # Need smaller sum, move right pointer left
                right -= 1

        # Problem guarantees a solution exists
        return []


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 167,
    "name": "Two Sum II - Input Array Is Sorted",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Two Pointers', 'Binary Search'],
    "url": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Apple", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
