"""
LeetCode Problem #820: Short Encoding of Words
Difficulty: Medium
Pattern: Tries
Link: https://leetcode.com/problems/short-encoding-of-words/

Problem:
--------
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].

Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

Constraints:
-----------
- 1 <= words.length <= 2000
- 1 <= words[i].length <= 7
- words[i] consists of only lowercase letters

Examples:
---------
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #820: Short Encoding of Words

    Approach: Reverse Trie or suffix checking
    Time Complexity: O(n * m)
    Space Complexity: O(n * m)

    Key Insights:
    - Build Trie in reverse (suffix tree)
    - Words that are suffixes share encoding
    - Only count leaf nodes
    - Remove words that are suffixes of others
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 820,
    "name": "Short Encoding of Words",
    "difficulty": "Medium",
    "pattern": "Tries",
    "topics": ['Array', 'Hash Table', 'String', 'Trie'],
    "url": "https://leetcode.com/problems/short-encoding-of-words/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
}