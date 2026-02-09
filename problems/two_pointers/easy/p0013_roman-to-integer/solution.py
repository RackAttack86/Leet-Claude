"""
LeetCode Problem #13: Roman to Integer
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/roman-to-integer/

Problem:
--------
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
	
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
	
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Constraints:
-----------
- `1
- s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is guaranteed that `s` is a valid roman numeral in the range `[1, 3999]`.

Examples:
---------
Example 1:
```

Input: s = "III"
Output: 3
Explanation: III = 3.

```

Example 2:
```

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

```

Example 3:
```

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

```
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #13: Roman to Integer

    Approach: Left-to-Right Scan with Subtraction Rule
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) - fixed size hash map

    Key Insights:
    - Map each Roman numeral to its integer value
    - If current value < next value, subtract it (e.g., IV = -1 + 5 = 4)
    - Otherwise, add the current value
    - This handles all subtraction cases (IV, IX, XL, XC, CD, CM)
    """

    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral string to an integer.

        Args:
            s: Roman numeral string

        Returns:
            Integer value of the Roman numeral
        """
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        result = 0
        for i in range(len(s)):
            # If current value is less than next value, subtract it
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                result -= roman_values[s[i]]
            else:
                result += roman_values[s[i]]

        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 13,
    "name": "Roman to Integer",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Hash Table', 'Math', 'String'],
    "url": "https://leetcode.com/problems/roman-to-integer/",
    "companies": ['Amazon', 'Microsoft', 'Apple', 'Google', 'Facebook'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
