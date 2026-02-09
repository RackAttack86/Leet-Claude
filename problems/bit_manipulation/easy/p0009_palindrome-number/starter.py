"""
LeetCode Problem #9: Palindrome Number
Difficulty: Easy
Pattern: Bit Manipulation
Link: https://leetcode.com/problems/palindrome-number/

Problem:
--------
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

Constraints:
-----------
- `-2^31

Examples:
---------
Example 1:
```

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

Example 2:
```

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

Example 3:
```

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #9: Palindrome Number

    Approach: Reverse half of the number and compare with the first half.
    Instead of reversing the entire number (which could overflow), we only
    reverse the second half and compare it with the first half. We stop
    when the reversed number becomes >= the remaining original number.

    Time Complexity: O(log10(n)) - We process half the digits
    Space Complexity: O(1) - Only using a few integer variables

    Key Insights:
    1. Negative numbers are never palindromes (the minus sign)
    2. Numbers ending in 0 (except 0 itself) cannot be palindromes
    3. We only need to reverse half the number to check palindrome property
    4. For odd-length numbers, we can ignore the middle digit (reversed // 10)
    5. Avoids string conversion for O(1) space solution
    """
    def isPalindrome(self, x: int) -> bool:
        """
        Check if integer is a palindrome by reversing half the number.
        """
        pass



PROBLEM_METADATA = {
    "number": 9,
    "name": "Palindrome Number",
    "difficulty": "Easy",
    "pattern": "Bit Manipulation",
    "topics": ['Math'],
    "url": "https://leetcode.com/problems/palindrome-number/",
    "companies": ["Amazon", "Microsoft", "Google", "Apple", "Facebook", "Bloomberg", "Adobe", "Yahoo"],
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(1)",
}