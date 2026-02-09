"""
LeetCode Problem #20: Valid Parentheses
Difficulty: Easy
Pattern: Stacks Queues
Link: https://leetcode.com/problems/valid-parentheses/

Problem:
--------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Constraints:
-----------
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

Examples:
---------
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #20: Valid Parentheses

    Approach: Stack
    Time Complexity: O(n)
    Space Complexity: O(n)

    Key Insights:
    - Push opening brackets to stack
    - Pop and match with closing brackets
    - Stack must be empty at end
    - Classic stack application
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 20,
    "name": "Valid Parentheses",
    "difficulty": "Easy",
    "pattern": "Stacks Queues",
    "topics": ["String", "Stack"],
    "url": "https://leetcode.com/problems/valid-parentheses/",
    "companies": ["Amazon", "Microsoft", "Google", "Facebook", "Bloomberg", "Apple"],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}