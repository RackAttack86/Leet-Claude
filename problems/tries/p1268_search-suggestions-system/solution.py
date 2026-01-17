"""
LeetCode Problem #1268: Search Suggestions System
Difficulty: Medium
Pattern: Tries
Link: https://leetcode.com/problems/search-suggestions-system/

Problem:
--------
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Constraints:
-----------
- 1 <= products.length <= 1000
- 1 <= products[i].length <= 3000
- 1 <= sum(products[i].length) <= 2 * 10^4
- All the strings of products are unique
- products[i] consists of lowercase English letters
- 1 <= searchWord.length <= 1000
- searchWord consists of lowercase English letters

Examples:
---------
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #1268: Search Suggestions System

    Approach: Trie or sorting with binary search
    Time Complexity: O(n * m + k) for Trie where k is searchWord length
    Space Complexity: O(n * m)

    Key Insights:
    - Sort products and use binary search
    - Or build Trie with sorted suggestions at each node
    - Return top 3 lexicographically smallest
    - Sorting approach is simpler
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 1268,
    "name": "Search Suggestions System",
    "difficulty": "Medium",
    "pattern": "Tries",
    "topics": ['Array', 'String', 'Binary Search', 'Trie', 'Sorting', 'Heap (Priority Queue)'],
    "url": "https://leetcode.com/problems/search-suggestions-system/",
    "companies": ['Amazon', 'Microsoft'],
    "time_complexity": "O(n * m + k) for Trie where k is searchWord length",
    "space_complexity": "O(n * m)",
}
