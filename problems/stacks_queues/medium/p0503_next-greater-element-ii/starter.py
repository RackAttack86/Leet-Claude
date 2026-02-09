"""
LeetCode Problem #503: Next Greater Element II
Difficulty: Medium
Pattern: Stacks Queues
Link: https://leetcode.com/problems/next-greater-element-ii/

Problem:
--------
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Constraints:
-----------
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9

Examples:
---------
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""

from typing import List, Optional


class Solution:
    """
    Solution to LeetCode Problem #503: Next Greater Element II

    Approach: Monotonic stack with circular traversal
    Time Complexity: O(n)
    Space Complexity: O(n)

    Key Insights:
    - Process array twice for circular effect
    - Use monotonic decreasing stack
    - Store indices in stack
    - Update result when finding greater element
    """
    def solve(self):
        """
        [TODO: Implement solution]
        """
        pass



PROBLEM_METADATA = {
    "number": 503,
    "name": "Next Greater Element II",
    "difficulty": "Medium",
    "pattern": "Stacks Queues",
    "topics": ['Array', 'Stack', 'Monotonic Stack'],
    "url": "https://leetcode.com/problems/next-greater-element-ii/",
    "companies": ['Amazon', 'Microsoft', 'Google'],
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
}