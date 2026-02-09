"""
LeetCode Problem #1647: Minimum Deletions to Make Character Frequencies Unique
Difficulty: Medium
Pattern: Greedy
Link: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

Problem:
--------
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Constraints:
-----------
- 1 <= s.length <= 10^5
- s contains only lowercase English letters

Examples:
---------
Input: s = "aab"
Output: 0
Explanation: s is already good.

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #1647: Minimum Deletions to Make Character Frequencies Unique

    Approach: Greedy with frequency set
    Time Complexity: O(n)
    Space Complexity: O(1) - only 26 letters

    Key Insights:
    - Count character frequencies
    - Use set to track used frequencies
    - Decrease frequency until unique or zero
    - Greedy approach finds minimum deletions
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 1647,
    "name": "Minimum Deletions to Make Character Frequencies Unique",
    "difficulty": "Medium",
    "pattern": "Greedy",
    "topics": ['Hash Table', 'String', 'Greedy', 'Sorting'],
    "url": "https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/",
    "companies": ['Amazon', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1) - only 26 letters",
}