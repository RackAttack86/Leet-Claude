"""
LeetCode Problem #648: Replace Words
Difficulty: Medium
Pattern: Tries
Link: https://leetcode.com/problems/replace-words/

Problem:
--------
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Constraints:
-----------
- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 100
- dictionary[i] consists of only lower-case letters
- 1 <= sentence.length <= 10^6
- sentence consists of only lower-case letters and spaces
- The number of words in sentence is in the range [1, 1000]
- The length of each word in sentence is in the range [1, 1000]
- Every two consecutive words in sentence will be separated by exactly one space
- sentence does not have leading or trailing spaces

Examples:
---------
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #648: Replace Words

    Approach: Trie
    Time Complexity: O(n + m) where n is dictionary size, m is sentence length
    Space Complexity: O(n)

    Key Insights:
    - Build Trie from dictionary roots
    - For each word, find shortest root prefix
    - Replace word with root if found
    - Trie enables efficient prefix matching
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 648,
    "name": "Replace Words",
    "difficulty": "Medium",
    "pattern": "Tries",
    "topics": ['Array', 'Hash Table', 'String', 'Trie'],
    "url": "https://leetcode.com/problems/replace-words/",
    "companies": ['Amazon', 'Google', 'Microsoft'],
    "time_complexity": "O(n + m) where n is dictionary size, m is sentence length",
    "space_complexity": "O(n)",
}
