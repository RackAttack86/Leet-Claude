"""
LeetCode Problem #274: H-Index
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/h-index/

Problem:
--------
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i^th` paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

Constraints:
-----------
- `n == citations.length

Examples:
---------
Example 1:
```

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

```

Example 2:
```

Input: citations = [1,3,1]
Output: 1

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #274: H-Index

    Approach: Counting sort approach. Create a bucket array where bucket[i]
    counts papers with exactly i citations (capped at n). Then traverse
    from highest to lowest to find h-index.

    Time Complexity: O(n) - Single pass to count, single pass to find h-index
    Space Complexity: O(n) - For the counting bucket array

    Key Insights:
    1. H-index can be at most n (number of papers)
    2. Papers with citations >= n can be grouped together (count as n)
    3. Traverse buckets from high to low, accumulating paper count
    4. When accumulated count >= current index, we found h-index
    """
    def hIndex(self, citations: List[int]) -> int:
        pass



PROBLEM_METADATA = {
    "number": 274,
    "name": "H-Index",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Sorting', 'Counting Sort'],
    "url": "https://leetcode.com/problems/h-index/",
    "companies": ["Google", "Amazon", "Facebook", "Microsoft", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}