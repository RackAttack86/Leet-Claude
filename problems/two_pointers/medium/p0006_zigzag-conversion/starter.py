"""
LeetCode Problem #6: Zigzag Conversion
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/zigzag-conversion/

Problem:
--------
The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```

P   A   H   N
A P L S I I G
Y   I   R

```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```

string convert(string s, int numRows);

```

Constraints:
-----------
- `1
- s` consists of English letters (lower-case and upper-case), `','` and `'.'`.

Examples:
---------
Example 1:
```

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

```

Example 2:
```

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

```

Example 3:
```

Input: s = "A", numRows = 1
Output: "A"

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #6: Zigzag Conversion

    Approach: Simulate the zigzag pattern by maintaining separate strings for each row.
    Traverse the input string character by character, appending each character to
    the appropriate row. Use a direction variable to track whether we're moving
    down or up in the zigzag pattern.

    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(n) for storing the result

    Key Insights:
    1. We don't need to build a 2D grid - just maintain n rows as strings
    2. The pattern goes: row 0, 1, 2, ..., numRows-1, numRows-2, ..., 1, 0, 1, ...
    3. Change direction when we hit row 0 or row numRows-1
    4. Edge case: if numRows == 1, return original string (no zigzag)
    """
    def convert(self, s: str, numRows: int) -> str:
        pass



PROBLEM_METADATA = {
    "number": 6,
    "name": "Zigzag Conversion",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ['String'],
    "url": "https://leetcode.com/problems/zigzag-conversion/",
    "companies": ["Amazon", "Google", "Apple", "Microsoft", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}