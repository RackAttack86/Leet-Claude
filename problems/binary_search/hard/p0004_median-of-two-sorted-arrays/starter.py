"""
LeetCode Problem #4: Median of Two Sorted Arrays
Difficulty: Hard
Pattern: Binary Search
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Problem:
--------
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

Constraints:
-----------
- `nums1.length == m
- nums2.length == n
- 10^6

Examples:
---------
Example 1:
```

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

```

Example 2:
```

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #4: Median of Two Sorted Arrays

    Approach: Binary Search on Partition
    We need to find a partition in both arrays such that:
    1. Left half contains (m+n+1)//2 elements total
    2. All elements in left half <= all elements in right half

    We binary search on the smaller array to find the correct partition.
    For partition i in nums1 and j in nums2:
    - j = (m+n+1)//2 - i
    - Valid partition: nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i]

    Time Complexity: O(log(min(m,n))) - Binary search on smaller array
    Space Complexity: O(1) - Only using constant extra space

    Key Insights:
    1. Binary search on the smaller array for efficiency
    2. Partition divides combined arrays into two halves
    3. Left partition elements must all be <= right partition elements
    4. Use infinity for out-of-bounds comparisons
    5. Median is calculated from the elements around the partition
    6. Handle odd/even total length differently for median calculation
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass



PROBLEM_METADATA = {
    "number": 4,
    "name": "Median of Two Sorted Arrays",
    "difficulty": "Hard",
    "pattern": "Binary Search",
    "topics": ['Array', 'Binary Search', 'Divide and Conquer'],
    "url": "https://leetcode.com/problems/median-of-two-sorted-arrays/",
    "companies": ["Amazon", "Google", "Microsoft", "Apple", "Facebook", "Bloomberg", "Adobe", "Goldman Sachs", "Uber"],
    "time_complexity": "O(log(min(m,n)))",
    "space_complexity": "O(1)",
}