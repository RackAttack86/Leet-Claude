"""
LeetCode Problem #131: Palindrome Partitioning
Difficulty: Medium
Pattern: Backtracking
Link: https://leetcode.com/problems/palindrome-partitioning/

Problem:
--------
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Constraints:
-----------
- 1 <= s.length <= 16
- s contains only lowercase English letters

Examples:
---------
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #131: Palindrome Partitioning

    Approach: Backtracking with palindrome checking
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)

    Key Insights:
    - Try all possible partitions
    - Check if each substring is palindrome
    - Backtrack to build all valid partitions
    """

    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(string: str) -> bool:
            return string == string[::-1]

        def backtrack(start: int, current: List[str]):
            if start == len(s):
                result.append(current[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    current.append(substring)
                    backtrack(end, current)
                    current.pop()

        backtrack(0, [])
        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 131,
    "name": "Palindrome Partitioning",
    "difficulty": "Medium",
    "pattern": "Backtracking",
    "topics": ['String', 'Dynamic Programming', 'Backtracking'],
    "url": "https://leetcode.com/problems/palindrome-partitioning/",
    "companies": ['Amazon', 'Facebook', 'Microsoft', 'Google'],
    "time_complexity": "O(n * 2^n)",
    "space_complexity": "O(n)",
}
