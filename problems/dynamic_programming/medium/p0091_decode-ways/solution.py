"""
LeetCode Problem #91: Decode Ways
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/decode-ways/

Problem:
--------
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

Constraints:
-----------
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s)

Examples:
---------
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #91: Decode Ways

    Approach: Dynamic Programming
    Time Complexity: O(n)
    Space Complexity: O(1) with space optimization

    Key Insights:
    - Similar to climbing stairs with conditions
    - dp[i] depends on single digit (dp[i-1]) and two digits (dp[i-2])
    - Handle leading zeros and invalid two-digit numbers
    - Two-digit valid if 10 <= num <= 26
    """

    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2, prev1 = 1, 1

        for i in range(1, n):
            current = 0

            # Single digit
            if s[i] != '0':
                current += prev1

            # Two digits
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2

            prev2, prev1 = prev1, current

        return prev1


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 91,
    "name": "Decode Ways",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['String', 'Dynamic Programming'],
    "url": "https://leetcode.com/problems/decode-ways/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Apple'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1) with space optimization",
}
