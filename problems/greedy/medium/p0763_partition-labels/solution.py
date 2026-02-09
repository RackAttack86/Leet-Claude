"""
LeetCode Problem #763: Partition Labels
Difficulty: Medium
Pattern: Greedy
Link: https://leetcode.com/problems/partition-labels/

Problem:
--------
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Constraints:
-----------
- 1 <= s.length <= 500
- s consists of lowercase English letters

Examples:
---------
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Input: s = "eccbbbbdec"
Output: [10]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #763: Partition Labels

    Approach: Greedy with last occurrence
    Time Complexity: O(n)
    Space Complexity: O(1) - only 26 letters

    Key Insights:
    - Record last occurrence of each character
    - Expand partition end to include all occurrences
    - Create new partition when reaching partition end
    - One pass solution
    """

    def partitionLabels(self, s: str) -> List[int]:
        """
        Partition string so each letter appears in at most one part.

        Args:
            s: Input string of lowercase letters

        Returns:
            List of partition sizes
        """
        # Record last occurrence of each character
        last = {char: i for i, char in enumerate(s)}

        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            # Extend partition to include all occurrences of current char
            end = max(end, last[char])

            # When we reach the end of current partition
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 763,
    "name": "Partition Labels",
    "difficulty": "Medium",
    "pattern": "Greedy",
    "topics": ['Hash Table', 'Two Pointers', 'String', 'Greedy'],
    "url": "https://leetcode.com/problems/partition-labels/",
    "companies": ['Amazon', 'Microsoft', 'Facebook', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1) - only 26 letters",
}
