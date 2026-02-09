"""
LeetCode Problem #745: Prefix and Suffix Search
Difficulty: Hard
Pattern: Tries
Link: https://leetcode.com/problems/prefix-and-suffix-search/

Problem:
--------
Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

Constraints:
-----------
- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 7
- 1 <= pref.length, suff.length <= 7
- words[i], pref and suff consist of lowercase English letters only
- At most 10^4 calls will be made to the function f

Examples:
---------
Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #745: Prefix and Suffix Search

    Approach: Trie with combined keys or two Tries
    Time Complexity: O(n * m^2) for constructor, O(p + s) for query
    Space Complexity: O(n * m^2)

    Key Insights:
    - Store suffix#prefix combinations in Trie
    - For word 'apple', store 'e#apple', 'le#apple', etc.
    - Or use two Tries and intersect results
    - Trade space for query speed
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 745,
    "name": "Prefix and Suffix Search",
    "difficulty": "Hard",
    "pattern": "Tries",
    "topics": ['Array', 'Hash Table', 'String', 'Design', 'Trie'],
    "url": "https://leetcode.com/problems/prefix-and-suffix-search/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(n * m^2) for constructor, O(p + s) for query",
    "space_complexity": "O(n * m^2)",
}