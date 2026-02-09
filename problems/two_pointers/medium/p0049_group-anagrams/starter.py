"""
LeetCode Problem #49: Group Anagrams
Difficulty: Medium
Pattern: Two Pointers
Link: https://leetcode.com/problems/group-anagrams/

Problem:
--------
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

Constraints:
-----------
- `1
- strs[i]` consists of lowercase English letters.

Examples:
---------
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

- There is no string in strs that can be rearranged to form `"bat"`.
	
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
	
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]

Output: [[""]]

Example 3:
Input: strs = ["a"]

Output: [["a"]]
"""

from typing import List, Optional
from collections import Counter, defaultdict


class Solution:
    """
    Solution to LeetCode Problem #49: Group Anagrams

    Approach: Use a hash map where the key is a canonical representation of
    each anagram group. Two strings are anagrams if they have the same sorted
    characters or the same character frequency count.

    Time Complexity: O(n * k * log(k)) where n is number of strings, k is max string length
                     Using character count as key: O(n * k)
    Space Complexity: O(n * k) for storing all strings in the hash map

    Key Insights:
    1. Anagrams have the same sorted character sequence
    2. Alternative: Use character count tuple as key (faster for long strings)
    3. defaultdict simplifies grouping logic
    4. Tuple of sorted string works as hashable key
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass



PROBLEM_METADATA = {
    "number": 49,
    "name": "Group Anagrams",
    "difficulty": "Medium",
    "pattern": "Two Pointers",
    "topics": ['Array', 'Hash Table', 'String', 'Sorting'],
    "url": "https://leetcode.com/problems/group-anagrams/",
    "companies": ["Amazon", "Google", "Facebook", "Microsoft", "Apple", "Bloomberg", "Uber"],
    "time_complexity": "O(n * k * log(k))",
    "space_complexity": "O(n * k)",
}