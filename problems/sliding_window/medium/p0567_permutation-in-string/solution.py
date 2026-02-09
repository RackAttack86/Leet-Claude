"""
LeetCode Problem #567: Permutation in String
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/permutation-in-string/

Problem:
--------
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Constraints:
-----------
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters

Examples:
---------
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba")

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #567: Permutation in String

    Approach: Sliding Window with character frequency
    Time Complexity: O(n)
    Space Complexity: O(1) - only 26 lowercase letters

    Key Insights:
    - Fixed window size = len(s1)
    - Compare character frequencies in window
    - Slide window through s2
    - Similar to finding anagrams
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if s2 contains a permutation of s1.

        Uses fixed-size sliding window of length len(s1).
        Compare character frequencies to detect permutation.
        """
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        # Count characters in s1
        s1_count = [0] * 26
        s2_count = [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        # Initialize first window
        for i in range(len1):
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == s2_count:
            return True

        # Slide window
        for i in range(len1, len2):
            # Add new character to window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove old character from window
            s2_count[ord(s2[i - len1]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True

        return False


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 567,
    "name": "Permutation in String",
    "difficulty": "Medium",
    "pattern": "Sliding Window",
    "topics": ["Hash Table", "Two Pointers", "String", "Sliding Window"],
    "url": "https://leetcode.com/problems/permutation-in-string/",
    "companies": ["Facebook", "Microsoft", "Amazon", "Google", "Oracle"],
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
}
