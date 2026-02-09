"""
LeetCode Problem #5: Longest Palindromic Substring
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/longest-palindromic-substring/

Problem:
--------
Given a string s, return the longest palindromic substring in s.

Constraints:
-----------
- 1 <= s.length <= 1000
- s consist of only digits and English letters

Examples:
---------
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #5: Longest Palindromic Substring

    Approach: Expand around center or DP
    Time Complexity: O(n^2)
    Space Complexity: O(1) for expand around center, O(n^2) for DP

    Key Insights:
    - Each center can expand to form palindrome
    - Check both odd and even length palindromes
    - DP approach: dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
    - Manacher's algorithm achieves O(n) but complex
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 5,
    "name": "Longest Palindromic Substring",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ["String", "Dynamic Programming"],
    "url": "https://leetcode.com/problems/longest-palindromic-substring/",
    "companies": ["Amazon", "Microsoft", "Apple", "Google"],
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
}