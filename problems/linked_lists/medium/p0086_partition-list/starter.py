"""
LeetCode Problem #86: Partition List
Difficulty: Medium
Pattern: Linked Lists
Link: https://leetcode.com/problems/partition-list/

Problem:
--------
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Constraints:
-----------
- The number of nodes in the list is in the range [0, 200]
- -100 <= Node.val <= 100
- -200 <= x <= 200

Examples:
---------
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input: head = [2,1], x = 2
Output: [1,2]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #86: Partition List

    Approach: Two dummy lists
    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insights:
    - Create two separate lists: less and greater
    - Traverse and append to appropriate list
    - Connect less list to greater list
    - Use dummy nodes for simplicity
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 86,
    "name": "Partition List",
    "difficulty": "Medium",
    "pattern": "Linked Lists",
    "topics": ['Linked List', 'Two Pointers'],
    "url": "https://leetcode.com/problems/partition-list/",
    "companies": ['Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
}