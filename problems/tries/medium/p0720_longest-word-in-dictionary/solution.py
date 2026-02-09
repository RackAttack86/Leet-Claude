"""
LeetCode Problem #720: Longest Word in Dictionary
Difficulty: Medium
Pattern: Tries
Link: https://leetcode.com/problems/longest-word-in-dictionary/

Problem:
--------
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word.

Constraints:
-----------
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 30
- words[i] consists of lowercase English letters

Examples:
---------
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #720: Longest Word in Dictionary

    Approach: Sorting and Set
    Time Complexity: O(n * m) where n is words count, m is average length
    Space Complexity: O(n * m)

    Key Insights:
    - Sort words by length and lexicographically
    - Check if all prefixes exist
    - Use set for O(1) lookup
    - A word is valid if its prefix (word minus last char) exists in the set
    """

    def longestWord(self, words: List[str]) -> str:
        """
        Find the longest word that can be built one character at a time.

        Args:
            words: List of words

        Returns:
            The longest word that can be built character by character
        """
        # Sort by length first, then lexicographically for ties
        words.sort(key=lambda x: (len(x), x))

        # Set to track valid words (words that can be built)
        valid = set([''])  # Empty string is the base case
        result = ''

        for word in words:
            # Check if the prefix (word without last char) is valid
            prefix = word[:-1]
            if prefix in valid:
                valid.add(word)
                # Update result if this word is longer, or same length but lexicographically smaller
                if len(word) > len(result):
                    result = word

        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 720,
    "name": "Longest Word in Dictionary",
    "difficulty": "Medium",
    "pattern": "Tries",
    "topics": ['Array', 'Hash Table', 'String', 'Trie', 'Sorting'],
    "url": "https://leetcode.com/problems/longest-word-in-dictionary/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(n * m) where n is words count, m is average length",
    "space_complexity": "O(n * m)",
}
