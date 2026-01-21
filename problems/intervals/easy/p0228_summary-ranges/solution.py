"""
LeetCode Problem #228: Summary Ranges
Difficulty: Easy
Pattern: Intervals
Link: https://leetcode.com/problems/summary-ranges/

Problem:
--------
You are given a sorted unique integer array `nums`.

A range `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
	
- `"a"` if `a == b`

Constraints:
-----------
- `0
- 2^31
- All the values of `nums` are unique.
- nums` is sorted in ascending order.

Examples:
---------
Example 1:
```

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

```

Example 2:
```

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #228: Summary Ranges

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 228,
    "name": "Summary Ranges",
    "difficulty": "Easy",
    "pattern": "Intervals",
    "topics": ['Array'],
    "url": "https://leetcode.com/problems/summary-ranges/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
