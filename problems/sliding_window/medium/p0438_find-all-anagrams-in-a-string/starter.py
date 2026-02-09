"""
LeetCode Problem #438: Find All Anagrams in a String
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

Problem:
--------
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints:
-----------
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters

Examples:
---------
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #438: Find All Anagrams in a String

    Approach: Sliding Window with character frequency
    Time Complexity: O(n)
    Space Complexity: O(1) - only 26 lowercase letters

    Key Insights:
    - Fixed window size = len(p)
    - Compare character frequencies
    - Slide window and update frequencies
    - Use counter or array for frequencies
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 438,
    "name": "Find All Anagrams in a String",
    "difficulty": "Medium",
    "pattern": "Sliding Window",
    "topics": ['Hash Table', 'String', 'Sliding Window'],
    "url": "https://leetcode.com/problems/find-all-anagrams-in-a-string/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1) - only 26 lowercase letters",
}