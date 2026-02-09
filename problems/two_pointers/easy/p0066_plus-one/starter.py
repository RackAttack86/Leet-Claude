"""
LeetCode Problem #66: Plus One
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/plus-one/

Problem:
--------
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i^th` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

Constraints:
-----------
- `1
- digits` does not contain any leading `0`'s.

Examples:
---------
Example 1:
```

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

```

Example 2:
```

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

```

Example 3:
```

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #66: Plus One

    Approach: Right-to-Left Carry Propagation
    Time Complexity: O(n) where n is the number of digits
    Space Complexity: O(1) in-place, or O(n) if we need to add a new digit

    Key Insights:
    - Start from the rightmost digit and add 1
    - If digit becomes 10, set it to 0 and carry 1 to the next position
    - If no carry remains, we're done
    - If we've processed all digits and still have carry, prepend 1
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increment the large integer represented by digits by one.

        Args:
            digits: Array of digits representing a large integer

        Returns:
            Array of digits representing the incremented integer
        """
        pass



PROBLEM_METADATA = {
    "number": 66,
    "name": "Plus One",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Math'],
    "url": "https://leetcode.com/problems/plus-one/",
    "companies": ['Google', 'Amazon', 'Microsoft', 'Apple'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}