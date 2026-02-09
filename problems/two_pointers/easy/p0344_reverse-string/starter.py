"""
LeetCode Problem #344: Reverse String
Difficulty: Easy
Pattern: Two Pointers
Link: https://leetcode.com/problems/reverse-string/

Problem:
--------
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
-----------
- 1 <= s.length <= 10^5
- s[i] is a printable ascii character

Examples:
---------
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #344: Reverse String

    Approach: Two Pointers (In-place swap)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Use two pointers from both ends
    - Swap characters while moving towards center
    - In-place modification with O(1) space
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pass



PROBLEM_METADATA = {
    "number": 344,
    "name": "Reverse String",
    "difficulty": "Easy",
    "pattern": "Two Pointers",
    "topics": ['Two Pointers', 'String'],
    "url": "https://leetcode.com/problems/reverse-string/",
    "companies": ['Facebook', 'Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}