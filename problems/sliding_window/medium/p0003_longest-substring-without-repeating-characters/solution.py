"""
LeetCode Problem #3: Longest Substring Without Repeating Characters
Difficulty: Medium
Pattern: Sliding Window
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem:
--------
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
-----------
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

Examples:
---------
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #3: Longest Substring Without Repeating Characters

    Approach: Sliding Window with hash map
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)) where m is charset size

    Key Insights:
    - Use hash map to track character positions
    - Expand window with right pointer
    - Contract window when duplicate found
    - Track maximum window size
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Uses sliding window with a hash map to track the last seen index of each character.
        When a duplicate is found, move the left pointer past the previous occurrence.
        """
        char_index = {}  # Maps character to its last seen index
        max_length = 0
        left = 0

        for right, char in enumerate(s):
            # If character was seen and is within current window
            if char in char_index and char_index[char] >= left:
                # Move left pointer past the duplicate
                left = char_index[char] + 1

            # Update the last seen index of current character
            char_index[char] = right

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 3,
    "name": "Longest Substring Without Repeating Characters",
    "difficulty": "Medium",
    "pattern": "Sliding Window",
    "topics": ["Hash Table", "String", "Sliding Window"],
    "url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
    "companies": ["Amazon", "Google", "Microsoft", "Facebook", "Adobe", "Apple", "Bloomberg"],
    "time_complexity": "O(n)",
    "space_complexity": "O(min(m, n))",
}
