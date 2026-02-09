"""
LeetCode Problem #128: Longest Consecutive Sequence
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Problem:
--------
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

Constraints:
-----------
- `0
- 10^9

Examples:
---------
Example 1:
```

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

```

Example 2:
```

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

Example 3:
```

Input: nums = [1,0,1,2]
Output: 3

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #128: Longest Consecutive Sequence

    Approach: Use a hash set for O(1) lookups. For each number, only start
    counting a sequence if the number is the beginning of a sequence
    (i.e., num-1 is not in the set). This ensures each element is visited
    at most twice.

    Time Complexity: O(n) - Each element is visited at most twice
    Space Complexity: O(n) - For storing elements in the set

    Key Insights:
    1. Only start counting from sequence beginnings (num-1 not in set)
    2. This optimization makes the algorithm O(n) despite nested loops
    3. Converting to set removes duplicates and enables O(1) lookup
    4. Each number is part of exactly one sequence count operation
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        pass



PROBLEM_METADATA = {
    "number": 128,
    "name": "Longest Consecutive Sequence",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Hash Table', 'Union-Find'],
    "url": "https://leetcode.com/problems/longest-consecutive-sequence/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Apple", "Bloomberg", "Uber"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}