"""
LeetCode Problem #169: Majority Element
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/majority-element/

Problem:
--------
Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

Constraints:
-----------
- `n == nums.length
- 10^9
- The input is generated such that a majority element will exist in the array.

Examples:
---------
Example 1:
```
Input: nums = [3,2,3]
Output: 3

```

Example 2:
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #169: Majority Element

    Approach: Boyer-Moore Voting Algorithm - maintain a candidate and count.
    When count reaches 0, pick the current element as new candidate.
    Increment count for matching elements, decrement for non-matching.

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only two variables

    Key Insights:
    - Majority element appears more than n/2 times
    - Non-majority elements can at most cancel out some majority occurrences
    - After cancellation, the majority element will still have count > 0
    """

    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 169,
    "name": "Majority Element",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Hash Table', 'Divide and Conquer', 'Sorting', 'Counting'],
    "url": "https://leetcode.com/problems/majority-element/",
    "companies": [],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
