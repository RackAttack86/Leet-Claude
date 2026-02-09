"""
LeetCode Problem #678: Valid Parenthesis String
Difficulty: Medium
Pattern: Greedy
Link: https://leetcode.com/problems/valid-parenthesis-string/

Problem:
--------
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Constraints:
-----------
- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'

Examples:
---------
Input: s = "()"
Output: true

Input: s = "(*)"
Output: true

Input: s = "(*))"
Output: true
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #678: Valid Parenthesis String

    Approach: Greedy with range tracking
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Track range of possible open parentheses count
    - low = minimum opens, high = maximum opens
    - '*' can be (, ), or empty
    - Valid if low <= 0 and high >= 0 at end
    """

    def checkValidString(self, s: str) -> bool:
        """
        Check if string with wildcards is valid parentheses.

        Args:
            s: String containing '(', ')' and '*'

        Returns:
            True if string can be valid parentheses
        """
        # Track range of possible open parentheses counts
        low = 0   # Minimum possible open count (treat * as ) or empty)
        high = 0  # Maximum possible open count (treat * as ()

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1   # Treat as )
                high += 1  # Treat as (

            # If high becomes negative, too many )
            if high < 0:
                return False

            # low can't go below 0 (we can always choose * as empty)
            low = max(low, 0)

        # Valid if we can reach exactly 0 open parentheses
        return low == 0


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 678,
    "name": "Valid Parenthesis String",
    "difficulty": "Medium",
    "pattern": "Greedy",
    "topics": ['String', 'Dynamic Programming', 'Stack', 'Greedy'],
    "url": "https://leetcode.com/problems/valid-parenthesis-string/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}
