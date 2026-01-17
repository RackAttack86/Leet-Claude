"""
LeetCode Problem #881: Boats to Save People
Difficulty: Medium
Pattern: Greedy
Link: https://leetcode.com/problems/boats-to-save-people/

Problem:
--------
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Constraints:
-----------
- 1 <= people.length <= 5 * 10^4
- 1 <= people[i] <= limit <= 3 * 10^4

Examples:
---------
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #881: Boats to Save People

    Approach: Two pointers after sorting
    Time Complexity: O(n log n)
    Space Complexity: O(1)

    Key Insights:
    - Sort array
    - Use two pointers from both ends
    - Pair lightest with heaviest if possible
    - Greedy pairing minimizes boats
    """

    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass


# Metadata for tracking
PROBLEM_METADATA = {
    "number": 881,
    "name": "Boats to Save People",
    "difficulty": "Medium",
    "pattern": "Greedy",
    "topics": ['Array', 'Two Pointers', 'Greedy', 'Sorting'],
    "url": "https://leetcode.com/problems/boats-to-save-people/",
    "companies": ['Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
}
