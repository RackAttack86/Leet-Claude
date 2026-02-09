"""
LeetCode Problem #34: Find First and Last Position of Element in Sorted Array
Difficulty: Medium
Pattern: Binary Search
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Problem:
--------
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

Constraints:
-----------
- `0
- 10^9
- nums` is a non-decreasing array.
- 10^9

Examples:
---------
Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

```

Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

```

Example 3:
```
Input: nums = [], target = 0
Output: [-1,-1]

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #34: Find First and Last Position of Element in Sorted Array

    Approach: Two Binary Searches - Find Left and Right Boundaries
    We perform two separate binary searches:
    1. First search finds the leftmost (first) occurrence of target
    2. Second search finds the rightmost (last) occurrence of target

    For finding the first position, when we find target, we continue searching left.
    For finding the last position, when we find target, we continue searching right.

    Time Complexity: O(log n) - Two binary searches, each O(log n)
    Space Complexity: O(1) - Only using constant extra space

    Key Insights:
    1. Use binary search twice with slight modifications for left/right boundary
    2. When finding left boundary: if nums[mid] >= target, search left half
    3. When finding right boundary: if nums[mid] <= target, search right half
    4. Handle edge cases: empty array, target not found
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pass



PROBLEM_METADATA = {
    "number": 34,
    "name": "Find First and Last Position of Element in Sorted Array",
    "difficulty": "Medium",
    "pattern": "Binary Search",
    "topics": ['Array', 'Binary Search'],
    "url": "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/",
    "companies": ["Google", "Facebook", "Amazon", "Microsoft", "Bloomberg", "Apple", "LinkedIn", "Uber"],
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
}