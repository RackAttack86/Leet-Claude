"""
LeetCode Problem #1804: Implement Trie II (Prefix Tree)
Difficulty: Medium
Pattern: Tries
Link: https://leetcode.com/problems/implement-trie-ii-(prefix-tree)/

Problem:
--------
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
void erase(String word) Erases the string word from the trie.

Constraints:
-----------
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters
- At most 3 * 10^4 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase
- It is guaranteed that for any function call to erase, the string word will exist in the trie

Examples:
---------
Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output
[null, null, null, 2, 2, null, 1, 1, null, 0]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #1804: Implement Trie II (Prefix Tree)

    Approach: Trie with counters
    Time Complexity: O(m) for all operations where m is word length
    Space Complexity: O(n * m)

    Key Insights:
    - Track word count and prefix count at each node
    - Increment counters on insert
    - Decrement counters on erase
    - Return appropriate counter for queries
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 1804,
    "name": "Implement Trie II (Prefix Tree)",
    "difficulty": "Medium",
    "pattern": "Tries",
    "topics": ['Hash Table', 'String', 'Design', 'Trie'],
    "url": "https://leetcode.com/problems/implement-trie-ii-(prefix-tree)/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(m) for all operations where m is word length",
    "space_complexity": "O(n * m)",
}