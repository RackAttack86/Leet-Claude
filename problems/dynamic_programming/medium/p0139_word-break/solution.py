"""
LeetCode Problem #139: Word Break
Difficulty: Medium
Pattern: Dynamic Programming
Link: https://leetcode.com/problems/word-break/

Problem:
--------
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Constraints:
-----------
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All strings in wordDict are unique

Examples:
---------
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #139: Word Break

    Approach: Dynamic Programming
    Time Complexity: O(n^2 * m) where m is average word length
    Space Complexity: O(n)

    Key Insights:
    - dp[i] = true if s[0:i] can be segmented
    - For each position, check if any word matches ending at that position
    - Use set for O(1) word lookup
    - dp[i] = any(dp[j] and s[j:i] in wordDict)
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 139,
    "name": "Word Break",
    "difficulty": "Medium",
    "pattern": "Dynamic Programming",
    "topics": ['Array', 'Hash Table', 'String', 'Dynamic Programming', 'Trie', 'Memoization'],
    "url": "https://leetcode.com/problems/word-break/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google', 'Apple'],
    "time_complexity": "O(n^2 * m) where m is average word length",
    "space_complexity": "O(n)",
}
