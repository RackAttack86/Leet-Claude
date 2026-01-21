"""
LeetCode Problem #219: Contains Duplicate II
Difficulty: Easy
Pattern: Sliding Window
Link: https://leetcode.com/problems/contains-duplicate-ii/

Problem:
--------
Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j)

Constraints:
-----------
- `1
- 10^9

Examples:
---------
Example 1:
```

Input: nums = [1,2,3,1], k = 3
Output: true

```

Example 2:
```

Input: nums = [1,0,1,1], k = 1
Output: true

```

Example 3:
```

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #219: Contains Duplicate II

    Approach: [TODO: Describe approach]
    Time Complexity: O(?)
    Space Complexity: O(?)

    Key Insights:
    [TODO: Add key insights]
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        [TODO: Implement]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 219,
    "name": "Contains Duplicate II",
    "difficulty": "Easy",
    "pattern": "Sliding Window",
    "topics": ['Array', 'Hash Table', 'Sliding Window'],
    "url": "https://leetcode.com/problems/contains-duplicate-ii/",
    "companies": [],
    "time_complexity": "O(?)",
    "space_complexity": "O(?)",
}
