"""
LeetCode Problem #30: Substring with Concatenation of All Words
Difficulty: Hard
Pattern: Sliding Window
Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

Problem:
--------
You are given a string `s` and an array of strings `words`. All the strings of `words` are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of `words` concatenated.

- For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. `"acdbef"` is not a concatenated string because it is not the concatenation of any permutation of `words`.

Return an array of the starting indices of all the concatenated substrings in `s`. You can return the answer in any order.

Constraints:
-----------
- `1
- s` and `words[i]` consist of lowercase English letters.

Examples:
---------
Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is `"barfoo"`. It is the concatenation of `["bar","foo"]` which is a permutation of `words`.

The substring starting at 9 is `"foobar"`. It is the concatenation of `["foo","bar"]` which is a permutation of `words`.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is `"foobarthe"`. It is the concatenation of `["foo","bar","the"]`.

The substring starting at 9 is `"barthefoo"`. It is the concatenation of `["bar","the","foo"]`.

The substring starting at 12 is `"thefoobar"`. It is the concatenation of `["the","foo","bar"]`.
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #30: Substring with Concatenation of All Words

    Approach: Sliding Window with Word-Level Granularity
    - Since all words have the same length, we can treat the string as a sequence of word-sized chunks
    - Use multiple starting offsets (0 to word_len-1) to cover all possible alignments
    - For each offset, use a sliding window of exactly (num_words * word_len) characters
    - Track word frequencies using a hash map and compare with target frequencies

    Time Complexity: O(n * word_len) where n is the length of string s
        - We have word_len different starting positions
        - For each starting position, we scan through the string once
        - Each word lookup and hash map operation is O(1) amortized

    Space Complexity: O(m * word_len) where m is the number of words
        - We store word frequencies in hash maps
        - The result list can have at most n starting indices

    Key Insights:
    1. All words have the same length, which is crucial for the sliding window approach
    2. We need to try word_len different starting offsets to cover all alignments
    3. Use a sliding window that moves by one word at a time (not one character)
    4. Track "formed" count to know when window contains all required words
    5. When we have excess of a word, shrink window from the left
    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Find all starting indices of concatenated substrings containing all words.
        """
        pass



PROBLEM_METADATA = {
    "number": 30,
    "name": "Substring with Concatenation of All Words",
    "difficulty": "Hard",
    "pattern": "Sliding Window",
    "topics": ['Hash Table', 'String', 'Sliding Window'],
    "url": "https://leetcode.com/problems/substring-with-concatenation-of-all-words/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Bloomberg", "Apple"],
    "time_complexity": "O(n * word_len)",
    "space_complexity": "O(m * word_len)",
}